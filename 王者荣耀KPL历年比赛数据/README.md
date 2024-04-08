# 王者荣耀KPL比赛数据记录

项目内的csv文件是KPL比赛从2020至2024.3月份的所有比赛数据，包括了选手，队伍，出装，BP，接下来将抽取其中一段，做字段说明。

+ 数据总量：5586

+ 每一条记录的字段：

	+ team_1：队伍一的名字

	+ team_2：队伍二的名字

	+ team_1_win：队伍一是否胜利

	+ team_2_win：队伍二是否胜利
		![image-20240331173149261](../../../typora/素材图片/image-20240331173149261.png)，此图共有5条记录，即5场比赛，展示了对应的数据

	+ battle_process：以列表的形式，用字典记录10个成员选择的英雄hero（不按照顺序，BP_process字段将会按照BP顺序展示结果），出装列表equiplist与位置position，数据举例：

		```python
		[{'team': '深圳DYG', 'hero': '王昭君', 'equiplist': ['抵抗之靴', '辉月', '痛苦面具', '凝冰之息'], 'position': '中路'}, 
		 {'team': '上海RNG.M', 'hero': '铠', 'equiplist': ['巨人之握', '抵抗之靴', '红莲斗篷', '不祥征兆', '抗魔披风', '提神水晶'], 'position': '打野'}, 
		 {'team': '深圳DYG', 'hero': '老夫子', 'equiplist': ['抵抗之靴', '不祥征兆', '速击之枪', '永夜守护', '纯净苍穹'], 'position': '发育路'},
		 {'team': '上海RNG.M', 'hero': '孙尚香', 'equiplist': ['急速战靴', '暗影战斧', '速击之枪', '宗师之力', '无尽战刃', '穿云弓'], 'position': '发育路'}, 
		 {'team': '深圳DYG', 'hero': '大乔', 'equiplist': ['极影·奔狼', '抵抗之靴', '旭日初光', '圣者法典', '咒术典籍', '大棒'], 'position': '游走'}, 
		 {'team': '上海RNG.M', 'hero': '安琪拉', 'equiplist': ['回响之杖', '秘法之靴', '博学者之怒', '云灵木', '元素杖'], 'position': '中路'}, 
		 {'team': '上海RNG.M', 'hero': '太乙真人', 'equiplist': ['近卫·奔狼', '抵抗之靴', '不祥征兆'], 'position': '游走'},
		 {'team': '深圳DYG', 'hero': '曹操', 'equiplist': ['冰痕之握', '抵抗之靴', '暗影战斧', '纯净苍穹', '暴烈之甲', '神隐斗篷'], 'position': '对抗路'}, 
		 {'team': '上海RNG.M', 'hero': '亚连', 'equiplist': ['荆棘护手', '抵抗之靴', '红莲斗篷', '末世', '血魔之怒', '雷鸣刃'], 'position': '对抗路'}, 
		 {'team': '深圳DYG', 'hero': '橘右京', 'equiplist': ['贪婪之噬', '抵抗之靴', '暗影战斧', '反伤刺甲', '破军', '陨星'], 'position': '打野'}]
		```

	+ BP_process：同样以列表的形式，用字典记录了赛场上的BP选择ban_or_pick，这里是按照顺序进行记录

		```python
		[{'team': '深圳DYG', 'ban_or_pick': 'ban', 'hero': '海诺'},
		 {'team': '上海RNG.M', 'ban_or_pick': 'ban', 'hero': '兰陵王'},
		 {'team': '深圳DYG', 'ban_or_pick': 'ban', 'hero': '镜'}, 
		 {'team': '上海RNG.M', 'ban_or_pick': 'ban', 'hero': '沈梦溪'},
		 {'team': '深圳DYG', 'ban_or_pick': 'pick', 'hero': '大乔'},
		 {'team': '上海RNG.M', 'ban_or_pick': 'pick', 'hero': '铠'}, 
		 {'team': '上海RNG.M', 'ban_or_pick': 'pick', 'hero': '太乙真人'}, 
		 {'team': '深圳DYG', 'ban_or_pick': 'pick', 'hero': '老夫子'},
		 {'team': '深圳DYG', 'ban_or_pick': 'pick', 'hero': '王昭君'}, 
		 {'team': '上海RNG.M', 'ban_or_pick': 'pick', 'hero': '孙尚香'}, 
		 {'team': '上海RNG.M', 'ban_or_pick': 'ban', 'hero': '裴擒虎'}, 
		 {'team': '深圳DYG', 'ban_or_pick': 'ban', 'hero': '海月'}, 
		 {'team': '上海RNG.M', 'ban_or_pick': 'ban', 'hero': '狂铁'},
		 {'team': '深圳DYG', 'ban_or_pick': 'ban', 'hero': '西施'}, 
		 {'team': '上海RNG.M', 'ban_or_pick': 'pick', 'hero': '亚连'}, 
		 {'team': '深圳DYG', 'ban_or_pick': 'pick', 'hero': '橘右京'}, 
		 {'team': '深圳DYG', 'ban_or_pick': 'pick', 'hero': '曹操'}, 
		 {'team': '上海RNG.M', 'ban_or_pick': 'pick', 'hero': '安琪拉'}]
		```

		