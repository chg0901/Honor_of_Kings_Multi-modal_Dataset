from langchain.embeddings.huggingface import HuggingFaceEmbeddings
from rag.metadata_retriever import MetadataRetriever
from langchain_community.vectorstores import Chroma
from rag.langchain_internlm2 import InternLM_LLM
from langchain.prompts import PromptTemplate
from langchain.chains import RetrievalQA
import os

os.environ['HF_ENDPOINT'] = 'https://hf-mirror.com'

def load_chain(model,tokenizer):
    # 加载问答链
    # 定义 Embeddings
    embeddings = HuggingFaceEmbeddings(model_name="BAAI/bge-small-zh-v1.5")

    # 向量数据库持久化路径
    persist_directory = './datasets/rag_chroma_db'

    # 加载数据库
    vectordb = Chroma(
        persist_directory=persist_directory,  # 允许我们将persist_directory目录保存到磁盘上
        embedding_function=embeddings
    )

    retriever_chroma=vectordb.as_retriever(search_kwargs={"k": 1})
    retriever=MetadataRetriever(base_retriever=retriever_chroma)


    # 加载自定义 LLM
    llm = InternLM_LLM(model,tokenizer)


    # 定义一个 Prompt Template
    template = """使用以下上下文来回答最后的问题。如果你不知道答案，就说你不知道，不要试图编造答
    案。请提供详细而清晰的回答。尽量详细回答问题，并尽量避免简单带过问题。可参考的上下文：
    ```
    {context}
    ```
    问题: ```{question}```
    有用的回答:"""

    QA_CHAIN_PROMPT = PromptTemplate(input_variables=["context", "question"], template=template)

    # 运行 chain
    qa_chain = RetrievalQA.from_chain_type(llm=llm, retriever=retriever, chain_type_kwargs={"prompt": QA_CHAIN_PROMPT})

    return qa_chain