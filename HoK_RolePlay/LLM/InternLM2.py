import os
import torch
import requests
from transformers import AutoModelForCausalLM, AutoTokenizer
os.environ['CUDA_LAUNCH_BLOCKING'] = '1'

class InternLM2:
    def __init__(self, mode='offline', model_path="InternLM2/InternLM2_7b", prefix_prompt = '''请用少于50个字回答以下问题\n\n'''):

        self.prefix_prompt = prefix_prompt
        self.mode = mode
        self.model, self.tokenizer = self.init_model(model_path)
        self.model = self.model.eval()
        self.history = []
    
    def init_model(self, path = "InternLM2/InternLM2_7b"):
        model = AutoModelForCausalLM.from_pretrained(path, 
                                                     device_map="auto", 
                                                     torch_dtype="auto",
                                                     trust_remote_code=True).eval()
        tokenizer = AutoTokenizer.from_pretrained(path, trust_remote_code=True)

        return model, tokenizer   
    
    def generate(self, question, system_prompt="You are a helpful assistant."):
        response, history = self.model.chat(self.tokenizer, self.prefix_prompt + question, history=[])

        return response
        
    def chat(self, system_prompt, message, history):
        response, self.history = self.model.chat(self.tokenizer, message, history=self.history)
        # history.append((message, response))

        return response, self.history
    
    def clear_history(self):
        # 清空历史记录
        self.history = []
    
def test():
    llm = InternLM2(mode='offline', model_path="InternLM2/InternLM2_7b")
    # llm = Qwen2(mode='offline', model_path="Qwen/Qwen2-0.5B")
    answer = llm.generate("如何应对压力？")
    print(answer)

if __name__ == '__main__':
    test()
