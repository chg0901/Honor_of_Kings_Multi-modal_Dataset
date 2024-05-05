# HoK Text 数据集

## 数据介绍

目前，此文件夹中有三个数据集，包括 [OriginalData_inChinese.xlsx](./OriginalData_inChinese.xlsx)， [processed_cn.jsonl](./processed_cn.jsonl) 和 [processed2.jsonl](./processed2_cn.jsonl) 。

数据[OriginalData_inChinese.xlsx](./OriginalData_inChinese.xlsx)

- 是生成[processed_cn.jsonl](./processed_cn.jsonl)和[processed2_cn.jsonl](./processed2_cn.jsonl)的原始数据
- 包含每个英雄详细信息的主要**文本**数据。  作为一个示例数据集，这里只上传了4个英雄的数据

数据[processed.jsonl](./processed.jsonl)和[processed2.jsonl](./processed2.jsonl)的原始数据

- 处理代码为[text_processing.py](./text_processing.py) 和 [text_processing2.py](./text_processing2.py) 是 XTuner 用于微调手机游戏《王者荣耀》英雄属性搜索的 LLM 模型的两个版本的文本数据。
  - [text_processing2.py](./text_processing2.py) 中添加了[Q] [A]标志, 这在实验中被证实作用不大.

[text_processing3.py](./text_processing3.py) 用于为每个英雄生成一个文本文件。生成的文本文件包含英雄故事，如果英雄是历史英雄，那么他或她的历史故事也会添加到文本文件中。[RAG_data](./text_data/RAG_data)为该文件运行对应每个英雄生成的text文件的文件夹。

## 如何使用

详细如何使用这两个数据集，请参考以下两个知乎链接

1. [王者荣耀问答助手[大模型实战营 结题项目][更新更多数据，计划采用RAG方法进行多模态检索搜索查询]](https://zhuanlan.zhihu.com/p/683656455)
2. [XTuner 大模型单卡低成本微调实战[大模型实战营04]【最后是王者荣耀有关的项目】](https://zhuanlan.zhihu.com/p/682241646)
