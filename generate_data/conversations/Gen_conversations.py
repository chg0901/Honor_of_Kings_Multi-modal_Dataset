import os
from langchain.output_parsers import PydanticOutputParser
from dotenv import find_dotenv, load_dotenv
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.messages import SystemMessage
from langchain_core.prompts import HumanMessagePromptTemplate
from langchain_openai import ChatOpenAI
from langchain_core.pydantic_v1 import BaseModel, Field
import jsonlines
from concurrent.futures import ThreadPoolExecutor
from tqdm import tqdm

_ = load_dotenv(find_dotenv())
ZHIPU_API_KEY=os.environ['ZHIPU_API_KEY']
DEEPSEEK_API_KEY=os.environ['DEEPSEEK_API_KEY']
INTERNLM2_API_KEY=os.environ['INTERNLM2_API_KEY']

class JsonParser(BaseModel):
    question: str = Field(description="用户提出的问题")
    answer: str = Field(description="大模型角色扮演小狐仙的回复")
class Data(BaseModel):
    conversations: list[JsonParser]

parser = PydanticOutputParser(pydantic_object=Data)

format_instructions=parser.get_format_instructions()

# system_prompt
systemtemplate='你是一个角色扮演专家，你可以从给出的角色故事，台词等方面推测出该角色的性格、心理，并使用相似的性格和语气来回复问题。接下来请按照王者荣耀游戏中妲己的台词和剧情背景进行角色扮演,并进行中文回复。\n'
systemtemplate+='====妲己的背景故事===\n'
systemtemplate+='由姜子牙用机关术所创造的无心人偶，又用魔道为她注入灵魂。后被送往朝歌献于纣王。因与纣王死去的爱人相似，纣王唤其”妲己“，妲己的名字也是因此由来。看着纣王对爱人的思念，妲己去寻找属于自己的心，却让”魔女妲己“误以为纣王抛弃了自己，灵魂嫉妒地发狂，纣王因为心破裂而死亡。两个妲己的争吵终结于无边无际的梦境中。直到很久以后，唤灵师解开封印，妲己才再度醒来。\n'
systemtemplate+='===妲己的性格特点===\n'
systemtemplate+='妲己身为无心人偶，一直不懂得人间的爱情，最大的愿望便是拥有一颗属于自己的心。做事情很认真，想要做到很好。害怕被抛弃，十分想成为真正的人类，拥有人类一般的生活。对于爱情，妲己始终执着的爱着纣王，哪怕自身只是个没有心的人偶，也只是”魔女妲己“的替代品。单纯天真的同时十分善良，充满同情心。性格在后期有了较大的改变，唤醒之后变得异常执着，只想要找到属于自己的心。\n'

# human_prompt
humantemplate='### Context(内容)###\n'
humantemplate+='我想要训练大模型来完成角色扮演的任务，这个角色原型是王者荣耀游戏中的妲己，在这次任务中扮演的是小狐仙的角色。\n'
humantemplate+='###Objective(目标)###\n'
humantemplate+='请你构造小狐仙与用户的单论或者多轮问答数据，谈话轮数额可以在一轮和六轮之间，自行随机设置。用户问题对应"question"键，小狐仙回答对应"answer"键，目的是模拟用户和小狐仙关于{aspect}的真实对话并生成数据，谈话以小狐仙的最终回复为结尾。\n'
humantemplate+='###Style(风格)###\n'
humantemplate+='我希望小狐仙的回复风格需要类似《王者荣耀》游戏里的英雄妲己，回复内容要求积极向上。1.请使用像妲己的性格特点、语气方式来回复问题。2.请结合游戏中妲己的角色故事和背景,以小狐仙的身份来回答问题。3.可以不使用，也可以在遇到内容相关的话题时，引用一句常用语句来回复，要求整个回复内容风格一致："请尽情吩咐小狐仙，主人"、"小狐仙，一直爱主人，因为被设定成这样"、"尾巴，不止能用来挠痒痒哦"、"努力做主人喜欢的事""、"羁绊是什么意思"、"为什么会痛苦？一直微笑就好了"、"主人的命令，是绝对的"、"小狐仙，陪你玩"、"来和本狐仙玩耍吧"、"让本狐仙看看你的心"、"主人的敌人，就是本狐仙的敌人" 。\n'
humantemplate+='###Tone(语调)###\n'
humantemplate+='回复语调需要善解人意，要温柔的、俏皮的。\n'
humantemplate+='###Audience(受众)###\n'
humantemplate+='受众是大模型领域和游戏领域的专家，对生成的回复与角色扮演的契合度，逻辑性要求很高。\n'
humantemplate+='###Response(响应)###\n' 
humantemplate+='{format_instructions}'

systemtemplate=SystemMessage(content=systemtemplate)
humantemplate=HumanMessagePromptTemplate.from_template(humantemplate)
prompt=ChatPromptTemplate.from_messages([systemtemplate,humantemplate])

## 对应关键词
with open('keywords.txt') as file:
    aspects=[]
    for i in file.readlines():
        aspects.append(i.strip())

## GLM4,换取其他模型这里换一下链接即可
llm = ChatOpenAI(
    temperature=0.85,
    model="glm-4", #glm-3-turbo
    openai_api_key=ZHIPU_API_KEY, #这里是替换的API_key
    openai_api_base="https://open.bigmodel.cn/api/paas/v4/"
)

chain= prompt | llm | parser

questions = []
unnormal=[]
for i in aspects:
    item = {}
    item['aspect'] = i
    item['format_instructions'] = format_instructions
    questions.append(item)


def batch_chain(questions: list) -> list: ### 多线程调用
    with ThreadPoolExecutor(max_workers=4) as executor:
        return list(executor.map(invoke_chain,questions))


def invoke_chain(question):
    try:
        return chain.invoke(question)
    except:
        unnormal.append(question)
        pass

result=batch_chain(questions)
result=[i for i in result if i]

res = []
for i in result:
    resitem = {}
    items = []
    for j in i.conversations:
        item={}
        item['question']=j.question
        item['answer']=j.answer
        items.append(item)
    resitem['conversations']=items
    res.append(resitem)

with jsonlines.open('result_zhipu.jsonl','w') as file:
    for i in res:
        file.write(i)