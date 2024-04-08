# Multi-modal RAG Project with Dataset from Honor of Kings

A Multi-modal RAG Project with Dataset from Honor of Kings, one of the most popular smart phone games in China

[**We NEED you** ](https://github.com/InternLM/Tutorial/discussions/594) in discussion of [InternLM](https://github.com/InternLM/InternLM) , which is [**《王者荣耀》多模态问答助手 【RAG】【AGENT】【RolePlay】【Deploy】【MultiModal】)** in Chinese](https://github.com/InternLM/Tutorial/discussions/594)

## Multi-modal Dataset from Honor of Kings

[HoK_multi-modal_toy_data readme_EN (**English**)](./HoK_multi-modal_toy_data/readme_EN.md)

[HoK_multi-modal_toy_data readme (**中文**)](./HoK_multi-modal_toy_data/readme.md)

[**HoK-BP-LLM**: Our Team's second repo](https://github.com/YuWangyin/-LLM)

### More Data From [HoK-BP-LLM](https://github.com/YuWangyin/-LLM)

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

### Simple File Structures

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

## Text data of Honor of Kings
[text_data](https://github.com/chg0901/Honor_of_Kings_Multi-modal_Dataset/tree/main/text_data)

## Join the second phase of the InternLM·Puyu Large Model Practical Camp and let's develop this project together.

We are excited to welcome new members. You can scan the QR code to participate in the latest course, where we can learn and exchange ideas together.

<div align="center">
<img src="https://github.com/chg0901/Honor_of_Kings_Multi-modal_Dataset/assets/8240984/9f15fa5c-fa4d-4e91-80e9-3419e43df182" width="40%"/>
</div>


## Future Plans

I will try to use this data to play with **InternLM** using **LLM finetuning** and **RAG** techs 

## More infomations in Chinese

Details to about this dataset and future projects, please refer to the following two ZhiHu Links

1. [王者荣耀问答助手[大模型实战营 结题项目][更新更多数据，计划采用RAG方法进行多模态检索搜索查询]](https://zhuanlan.zhihu.com/p/683656455)
2. [XTuner 大模型单卡低成本微调实战[大模型实战营04]【最后是王者荣耀有关的项目】](https://zhuanlan.zhihu.com/p/682241646)
