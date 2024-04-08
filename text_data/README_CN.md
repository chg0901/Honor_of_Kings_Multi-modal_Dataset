# HoK Text 数据集

## 数据介绍

目前，此文件夹中有三个数据集，包括 [OriginalData_inChinese.xlsx](./OriginalData_inChinese.xlsx)， [processed.jsonl](./processed.jsonl) 和 [processed2.jsonl](./processed2.jsonl) 。

数据[OriginalData_inChinese.xlsx](./OriginalData_inChinese.xlsx)

- 是生成[processed.jsonl](./processed.jsonl)和[processed2.jsonl](./processed2.jsonl)的原始数据
- 包含每个英雄详细信息的主要**文本**数据。  作为一个示例数据集，这里只上传了4个英雄的数据

数据[processed.jsonl](./processed.jsonl)和[processed2.jsonl](./processed2.jsonl)的原始数据

- 处理代码为[text_processing. py](./text_processing.py) 和 [text_processing3.py](./text_processing3.py) 
- 是 XTuner 用于微调手机游戏《王者荣耀》英雄属性搜索的 LLM 模型的两个版本的文本数据。

## 如何使用

详细如何使用这两个数据集，请参考以下两个知乎链接

1. [王者荣耀问答助手[大模型实战营 结题项目][更新更多数据，计划采用RAG方法进行多模态检索搜索查询]](https://zhuanlan.zhihu.com/p/683656455)
2. [XTuner 大模型单卡低成本微调实战[大模型实战营04]【最后是王者荣耀有关的项目】](https://zhuanlan.zhihu.com/p/682241646)
