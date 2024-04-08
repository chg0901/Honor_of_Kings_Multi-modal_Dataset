# HoK Text Dataset

## Data Introduction

Currently, there are three files including [OriginalData_inChinese.xlsx](./OriginalData_inChinese.xlsx), [processed.jsonl](./processed.jsonl) and [processed2.jsonl](./processed2.jsonl) dataset in this folder.

Data [OriginalData_inChinese.xlsx](./OriginalData_inChinese.xlsx)

- is the original data for generating [processed.jsonl](./processed.jsonl) and [processed2.jsonl](./processed2.jsonl)
- contains the main **text** data of details of each heros. As an example dataset, I just upload the data of 4 heros (`安琪拉`, `艾琳`, `阿古朵` and `阿轲`)

Data [processed.jsonl](./processed.jsonl) and [processed2.jsonl](./processed2.jsonl)

- processing codes: [text_processing.py](./text_processing.py) and [text_processing3.py](./text_processing3.py)
- are two version of text data used for XTuner to fine-tune a LLM model for the hero property searching of mobile smart phone game, Honor of Kings

## How to Use

Details to how to use these two dataset, please refer to the following two ZhiHu Links

1. [王者荣耀问答助手[大模型实战营 结题项目][更新更多数据，计划采用RAG方法进行多模态检索搜索查询]](https://zhuanlan.zhihu.com/p/683656455)
2. [XTuner 大模型单卡低成本微调实战[大模型实战营04]【最后是王者荣耀有关的项目】](https://zhuanlan.zhihu.com/p/682241646)
