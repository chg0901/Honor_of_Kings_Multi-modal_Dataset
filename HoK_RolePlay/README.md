# Honor of Kings - RolePlay

![img](妲己Images/时之奇旅.jpg)

## 背景

王者荣耀是一款MOBA类国产游戏，王者荣耀中英雄众多，每个英雄都有自己鲜明的故事背景、性格特征、技能招式等，因此王者荣耀的有关数据包含了丰富的文本和语音，适合创建角色扮演聊天机器人。

| 分路       | 代表英雄 | 经典台词                               | 故事背景                                                     | 被动技能                                                     |
| ---------- | -------- | -------------------------------------- | ------------------------------------------------------------ | :----------------------------------------------------------- |
| **发育路** | 黄忠     | 正义或许会迟到，但绝不会忘记砸到你头顶 | 黄忠，字汉升，东汉末年的猛将之一。早年追随刘表，刘表死后，成为长沙太守韩玄的部将 ... ... | 黄忠普攻时可以提高6-12点攻击和0.75%-1.5%暴击率，持续1.5秒，此效果最多可叠加5层。黄忠处于炮台形态时享受双倍增益效果，黄忠在进入或退出炮台形态时，刷新身上留存的增益效果持续时间并将增益系数替换成当前形态的倍数。 |
| **中路**   | 妲己     | 请尽情吩咐妲己，主人\n来和妲己玩耍吧   | 纣王身边妲己实际上是狐狸精。她蛊惑纣王干下了种种祸害百姓、残害忠良的倒行逆施，最终断送了商朝的天下 ... ... | 妲己技能命中敌人会减少目标30~72点法术防御，持续3秒，最多叠加3层 |
| **打野**   | 赵云     | 心怀不惧，才能翱翔于天际               | 三国时的蜀汉名将。常山真定人，字子龙。东汉末年大乱，群雄并起之时，起兵归于公孙瓒。公孙瓒败亡，投奔刘备，时刘备未成气候 ... ... | 赵云每损失3%最大生命就会获得1%减伤                           |
| **对抗路** | 老夫子   | 老夫年少时，也曾像他们一样，征战四方   | 历史原型为儒家学派创始人孔子，他广收门徒，周游列国，号称三千弟子，传播其学说 ... ... | 老夫子普通攻击命中会增加1点训诫值，最多叠加5点，叠满后会获得强化自身，持续5秒；强化时老夫子会增加60点移动速度和25%攻击速度，同时普通攻击将会附带60点真实伤害，每次攻击能够减少1秒圣人训诫和举一反三的冷却时间 |
| **游走**   | 庄周     | 蝴蝶是我，我就是蝴蝶                   | 庄周，一般人称庄子。是战国时的思想家，跟老子一道，为道家的代表人物之一，后世老庄并称。其学说崇尚自然，推崇自由 ... ... | 在自然梦境中，庄周解除并免疫所有控制效果，获得15%减伤，并增加15%移速，持续2秒。庄周每6秒进入一次自然梦境 |

## 目标

基于xtuner微调🌟**InternLM2**打造一个王者荣耀领域的角色扮演聊天机器人（以妲己为例），同时结合🌟**ASR**技术实现语音输入、🌟**TTS**技术实现声音克隆和语音输出、🌟**数字人**技术实现视频输出。

将特定游戏角色的形象带入大语言模型，在实现①知识输出的同时，也实现②角色扮演行为：

> 1. **角色扮演**：使模型表现得像《王者荣耀》游戏里的英雄角色妲己
>    - 了解妲己的角色背景和英雄故事
>    - 使用像妲己的性格特点、语气、方式和词汇来回复问题
>    - 如果问题与游戏内容有关，尽量重复使用游戏中妲己的原始台词。
> 2. **知识输出**：使模型表现得像《王者荣耀》游戏专家
>    - 知道关于《王者荣耀》中所有英雄的知识，包括被动、技能1/2/3/4、角色背景、英雄故事

## 期望结果

- 用户进行王者荣耀领域相关的提问，模型根据知识储备做出回答
- 模型在作出回答时同时结合妲己的语气口吻
- 模型模拟妲己的声音，同步以音频形式输出回答内容

## demo

| 文字/语音对话 |              数字人回答               |
| :-----------: | :-----------------------------------: |
|    你好呀     | <video src="assets/demo.mp4"></video> |

## 行动

### 数据收集

王者荣耀数据的收集，来源于**兄弟项目**[Honor_of_Kings_Multi-modal_Dataset](https://github.com/chg0901/Honor_of_Kings_Multi-modal_Dataset/)，欢迎大家前去star~

```bash
|-- Honor-of-Kings_RolePlay/
    |-- README.md
    |-- 王者荣耀英雄名单.txt
    |-- RAG_Data/
        |-- 上官婉儿.txt
        |-- 不知火舞.txt
        |-- 东皇太一.txt
        ... ...
    |-- 妲己Images/
        |-- 仙境爱丽丝.jpg
        |-- 女仆咖啡.jpg
        |-- 时之奇旅.jpg
        ... ...
    |-- 妲己Texts/
        |-- 妲己介绍.txt
        |-- 妲己介绍.xlsx
        |-- 妲己台词.txt
        |-- 妲己性格特点.txt
        |-- 妲己英雄故事.txt
        |-- 妲己角色背景.txt
    |-- 妲己Voices/
        |-- 109_妲己__魅力之狐.txt
        |-- 109_妲己__魅力之狐/
            |-- 109_妲己_妲己,一直爱主人,因为被设定成这样..wav
            |-- 109_妲己_妲己,陪你玩.wav
            ... ...
```

### 数据生成

### 微调

### ASR

### TTS

### 数字人

## 使用指南

Clone the repo

```bash
git clone https://github.com/YongXie66/Honor-of-Kings_RolePlay.git
```

install the environment

```bash
conda create -n hok-roleplay python=3.10
conda activate hok-roleplay

pip install torch==2.0.1 torchvision==0.15.2 torchaudio==2.0.2 --index-url https://download.pytorch.org/whl/cu118

pip install -r requirements.txt

conda install -q ffmpeg
```

download models

```bash
# LLM 下载
>>>from openxlab.model import download
>>>download(model_repo=LLM_path,output='./InternLM2/InternLM2_7b')
# or
apt install git
apt install git-lfs
git clone https://code.openxlab.org.cn/shenfeilang/Honor-of-Kings_RolePlay.git InternLM2/InternLM2_7b/

# gpt_sovits, sadtalker 模型下载
>>>download(model_repo=vivid_path, output='./DaJi_RolePlay')

# 模型位置移动
mv ./DaJi_RolePlay/GPT_SoVITS/pretrained_models/* ./GPT_SoVITS/pretrained_models/
mv ./DaJi_RolePlay/checkpoints/* ./checkpoints
mv ./DaJi_RolePlay/gfpgan/* ./gfpgan/
```

WEBUI

```bash
python webui.py
```



## 项目成员

|      | 成员                                        | 贡献（更新中...） |
| ---- | ------------------------------------------- | ----------------- |
| 主创 | [谢勇](https://github.com/YongXie66/)       |                   |
| 主创 | [程宏](https://github.com/chg0901)          |                   |
| 共创 | [Wong Tack Hwa](https://github.com/tackhwa) |                   |
| 共创 | [沈飞](https://github.com/shenfeilang)      |                   |

