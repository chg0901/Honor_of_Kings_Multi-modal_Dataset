# 王者荣耀多模态RAG项目

基于王者荣耀（中国最受欢迎的智能手机游戏之一）数据集的多模态RAG项目

## 来自王者荣耀的多模态数据集

[HoK_multi-modal_toy_data 阅读文档 (**英文**)](./HoK_multi-modal_toy_data/readme_EN.md)

[HoK_multi-modal_toy_data 阅读文档 (**中文**)](./HoK_multi-modal_toy_data/readme.md)

[**兄弟项目**：王者荣耀 对局策略推荐小助手-LLM](https://github.com/YuWangyin/-LLM)

### 数据调整（含兄弟项目数据引入）

```bash
.
|   README.md
|   README_CN.md
|   tree.txt
|   tree_simple.txt
|
+---王者荣耀KPL历年比赛数据              # 新增
|       README.md
|       WZRY.csv
|
+---王者荣耀攻略                        # 新增
|       WZtrick.jsonl 
|
+---crawler_data                       # 新增
|       image_0.jpg
|       image_1.jpg
......
|       pvp_picture_picture1.jpg
......
|       text_content.csv
|     
+---HoK_multi-modal_toy_data
|   |   readme.md
|   |   readme_EN.md
|   |
|   +---英雄Q版头像
|   |
|   +---英雄档案图片
|   |       
|   +---英雄海报
|   |
|   \---英雄语音和对应台词
|       |   readme.md
|       |
|       +---安琪拉
|       |   |   142_安琪拉__乘龙·聚宝船.txt
|       |   |   142_安琪拉__心灵骇客.txt
|       |   |   142_安琪拉__时之奇旅.txt
|       |   |   142_安琪拉__暗夜萝莉.txt
|       |   |   142_安琪拉__追逃游戏.txt
|       |   |   142_安琪拉__魔法小厨娘.txt
|       |   |   readme.md
|       |   |
|       |   +---142_安琪拉__乘龙·聚宝船
...................
|       |   |       142_安琪拉_西望灵洲选自广东通志.mp3
|       |   |       142_安琪拉_问尔能奈浪涛何.mp3
|       |   |       142_安琪拉_顺风得利,祀海祈祥.mp3
|       |   |       142_安琪拉_须知黄金未是宝,机勇情义胜珠珍改编自王梵.mp3
|       |   |       142_安琪拉_驾海相迎.mp3
|       |   |
|       |   +---142_安琪拉__心灵骇客
|       |   |
|       |   +---142_安琪拉__时之奇旅
|       |   |
|       |   +---142_安琪拉__暗夜萝莉
|       |   |
|       |   +---142_安琪拉__追逃游戏
|       |   |
|       |   \---142_安琪拉__魔法小厨娘
|       |
|       +---艾琳
|       |
|       +---阿古朵
|       |
|       \---阿轲
|
\---text_data
        OriginalData_inChinese.xlsx
        processed.jsonl
        processed2.jsonl
        README.md
        README_CN.md
        text_processing.py
        text_processing3.py

```

### 简单文件结构

```bash
│   王者荣耀故事英雄与技能-toy.xlsx
├───英雄Q版头像
├───英雄档案图片
├───英雄海报
├───英雄皮肤
│   ├───安琪拉
│   ├───艾琳
│   ├───阿古朵
│   └───阿轲
└───英雄语音和对应台词
    ├───安琪拉
    │   ├───142_安琪拉__乘龙·聚宝船
    │   ├───142_安琪拉__心灵骇客   
    │   ├───142_安琪拉__时之奇旅
    │   ├───142_安琪拉__暗夜萝莉
    │   ├───142_安琪拉__追逃游戏
    │   └───142_安琪拉__魔法小厨娘
    ├───艾琳
    │   ├───155_艾琳__奇遇舞章
    │   ├───155_艾琳__精灵之舞
    │   └───155_艾琳__觅芳踪
    ├───阿古朵
    │   ├───533_阿古朵__山林之子
    │   ├───533_阿古朵__江河有灵
    │   └───533_阿古朵__顽趣
    └───阿轲
        ├───116_阿轲__信念之刃
        ├───116_阿轲__暗夜猫娘
        ├───116_阿轲__节奏热浪
        └───116_阿轲__迷踪丽影
```

## 王者荣耀文本数据
[文本数据](https://github.com/chg0901/Honor_of_Kings_Multi-modal_Dataset/tree/main/text_data)  

## 加入InternLM·Puyu大模型实战营第二阶段，让我们一起开发这个项目。

我们非常期待新成员的加入。您可以扫描二维码参与最新的课程，在那里我们可以一起学习和交流想法。

<div align="center">
<img src="https://github.com/chg0901/Honor_of_Kings_Multi-modal_Dataset/assets/8240984/9f15fa5c-fa4d-4e91-80e9-3419e43df182" width="40%"/>
</div>

## 未来计划

我将尝试使用这些数据通过**InternLM**使用**LLM finetuning**和**RAG**技术进行玩耍

## 更多中文信息

关于这个数据集和未来项目的详细信息，请参考以下两个知乎链接

1. [王者荣耀问答助手[大模型实战营 结题项目][更新更多数据，计划采用RAG方法进行多模态检索搜索查询]](https://zhuanlan.zhihu.com/p/683656455)  
2. [XTuner 大模型单卡低成本微调实战[大模型实战营04]【最后是王者荣耀有关的项目】](https://zhuanlan.zhihu.com/p/682241646)  
