from .Qwen import Qwen
from .InternLM2 import InternLM2

    
def test_Qwen(question = "如何应对压力？", mode='offline', model_path="Qwen/Qwen-1_8B-Chat"):
    llm = Qwen(mode, model_path)
    answer = llm.generate(question)
    print(answer)

    
class LLM:
    def __init__(self, mode='offline'):
        self.mode = mode
        
    def init_model(self, model_name, model_path, api_key=None, proxy_url=None, prefix_prompt='''请用少于50个字回答以下问题\n\n'''):
        if model_name == 'Qwen':
            llm = Qwen(self.mode, model_path)
        elif model_name == 'InternLM2':
            llm = InternLM2(self.mode, model_path)

        llm.prefix_prompt = prefix_prompt
        return llm
    

    def test_Qwen(self, question="如何应对压力？", model_path="Qwen/Qwen-1_8B-Chat"):
        llm = Qwen(self.mode, model_path)
        answer = llm.generate(question)
        print(answer)

        
    def InternLM2(self, question="如何应对压力？", model_path="InternLM2/InternLM2_7b"):
        llm = InternLM2(mode=self.mode, model_name_or_path=model_path)
        answer = llm.generate(question)
        print(answer)

if __name__ == '__main__':
    llm = LLM(mode='offline')
    # llm.test_Qwen()
