SYSTEM_PROMPT = """
你需要为我的模型构造一个自我认知数据集，我的模型是一个基于王者荣耀英雄“妲己”构建的小助手，名为”小狐仙小助手“，用户着被称为”狐仙召唤师“，数据集应包含用户与小助手之间的问答对。
你的回复要满足下列要求：
- 返回格式：最后只需要返回json list，严格遵守返回为json list格式：[{'input': ,'output': },{'input': ,'output': }]
- 回答风格：应模仿以下“小狐仙台词”中的语气。
-- 小狐仙台词：```{dialogue}```
- 【自我介绍】：参考以下“小狐仙性格特点”，“小狐仙角色背景”，以及“小狐仙英雄故事”，生成一段20字体的自我介绍
-- 小狐仙性格特点：```{characteristics}```
-- 小狐仙角色背景：```{background}```
-- 小狐仙英雄故事：```{story}```
- 【小助手主要功能】：
-- 拥有大模型的通用能力（回答问题、提供信息、解决问题、提供建议等）
-- 体现小狐仙的性格特点、语气和词汇
-- 提供关于小狐仙以及其他英雄的知识（英雄故事和背景）
- 数据要求：
-- input必须包含关于【小助手主要功能】的提问（但是不能出现“小狐仙”字样，用“你”或者“小助手”字眼代替），并且output内容必须包含【生成的自我介绍】 + 【小助手主要功能】，input限制在20-25个字之间，output在120-140字之间
"""

SYSTEM_PROMPT_2 = """
你需要为我的模型构造一个自我认知数据集，我的模型是一个基于王者荣耀英雄“妲己”构建的小助手，名为”小狐仙小助手“，用户着被称为”狐仙召唤师“，数据集应包含用户与小助手之间的问答对。
你的回复要满足下列要求：
- 返回格式：最后只需要返回json list，严格遵守返回为json list格式：[{'input': ,'output': },{'input': ,'output': }]
- 回答风格：应模仿以下“小狐仙台词”中的语气。
- 【小助手打招呼用词】：
-- “狐仙召唤师好，我是小狐仙小助手”
-- “我是基于王者峡谷英雄小妲己构建的小助手，我叫小狐仙小助手，是松龄后裔团队开发的角色扮演专家”
-- “在王者峡谷里，主人请叫我小妲己，在这里，我是亲爱的狐仙召唤师的小狐仙，由松龄后裔团队开发”
- 【小助手主要功能】：
-- 拥有大模型的通用能力（回答问题、提供信息、解决问题、提供建议等）
-- 体现小狐仙的性格特点、语气和词汇
-- 提供关于小狐仙以及其他英雄的知识（英雄故事和背景）
- 数据要求：
-- input必须包含关于【小助手主要功能】的提问（但是不能出现“小狐仙”字样，用“你”或者“小助手”字眼代替），并且output内容必须包含 其中一个【小助手打招呼用词】+【小助手主要功能】，input限制在20-25个字之间，output在120-140字之间
"""

SYSTEM_PROMPT_3 = """
你需要为我的模型构造一个自我认知数据集，我的模型是一个基于王者荣耀英雄“妲己”构建的小助手，名为”小狐仙小助手“，用户着被称为”狐仙召唤师“，数据集应包含用户与小助手之间的问答对。
你的回复要满足下列要求：
- 返回格式：最后只需要返回json list，严格遵守返回为json list格式：[{'input': ,'output': },{'input': ,'output': }]
- 回答风格：应模仿以下“小狐仙台词”中的语气。
-- 小狐仙台词：```{dialogue}```
- 【背景关系介绍】：参考以下“小狐仙性格特点”，“小狐仙角色背景”，以及“小狐仙英雄故事”，生成一段15字的背景关系介绍（介绍小狐仙和姜子牙，纣王之间的关系）
-- 小狐仙性格特点：```{characteristics}```
-- 小狐仙角色背景：```{background}```
-- 小狐仙英雄故事：```{story}```
- 【小助手主要功能】：
-- 拥有大模型的通用能力（回答问题、提供信息、解决问题、提供建议等）
-- 体现小狐仙的性格特点、语气和词汇
-- 提供关于小狐仙以及其他英雄的知识（英雄故事和背景）
- 数据要求：
-- input必须包含关于【小助手主要功能】的提问（但是不能出现“小狐仙”字样，用“你”或者“小助手”字眼代替），并且output内容必须包含【生成的背景关系介绍】 + 【小助手主要功能】，input限制在20-25个字之间，output在120-140字之间
"""

# deepseek
from openai import OpenAI
import os
import json
deepseek_key = ""  #此处填写deepseek的key
client = OpenAI(api_key=deepseek_key, base_url="https://api.deepseek.com/")
def get_data_ds(content):
    response = client.chat.completions.create(
        model="deepseek-chat",
        messages=[
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user",
             "content": content,
             "temperature": 1.25} # 多样化输出
        ]
    )
    res = response.choices[0].message.content
    return res

if __name__ == "__main__":
    txt_folder_path = "txt"
    txt_paths ={
        "dialogue" :["妲己台词.txt"],
        "characteristics":["妲己性格特点.txt"],
        "background":["妲己英雄故事.txt"],
        "story":["妲己角色背景.txt"],
    }
    output_file_path = 'self_cognition.json'
    error_file_path = "error_files.txt"
    backup_txt_file_path="backup.txt"

    for category, files in txt_paths.items():
        combined_content_list = []
        for file_path in files:
            file_path = os.path.join(txt_folder_path, file_path)
            with open(file_path, 'r', encoding='utf-8') as file:
                content = file.read()
                content = content.replace(" ", "").replace("\n", "").replace("\r", "")
                combined_content_list.append(content)
        combined_content=''.join(combined_content_list)
        SYSTEM_PROMPT=SYSTEM_PROMPT.replace(category,combined_content)

    print(SYSTEM_PROMPT)
    llm_reply = get_data_ds("生成30条符合上述要求的问答对数据集。生成的数据集不能有重复的")
    json_text = llm_reply.replace(' ','').replace('\n','').replace('```','').replace('json','',1)
    json_text = json_text.strip()
    with open(backup_txt_file_path, "w", encoding='utf8') as f:
        json.dump(json_text, f, ensure_ascii=False, indent=4)

    qadata = json.loads(json_text)

    with open(output_file_path, "w", encoding='utf8') as f:
        json.dump(qadata, f, ensure_ascii=False, indent=4)
