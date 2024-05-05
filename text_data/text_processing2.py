import pandas as pd
import json
# 读取Excel文件
df = pd.read_excel("OriginalData_inChinese.xlsx")
df = df.fillna('')
columns = ['英雄', '被动名','被动介绍',
           '一技能名称', '一技能介绍',
            '二技能名称', '二技能介绍',
            '三技能名称', '三技能介绍',
            '四技能名称', '四技能介绍',
           '英雄故事', '历史故事', ]

output_file = 'processed2_cn.jsonl'

output_data = []

# Iterate through each row in column A and D
# 遍历每一行的元素
for index, row in df.iterrows():
    system_value = "你是一个王者荣耀的忠实粉丝，你对游戏的设定和背景有深入的了解，你喜欢分享你的知识和见解。你将根据用户对英雄的有关问题的提问，做出相应的回答。你的回答会尽量保持客观和准确，不会随意创造或修改游戏的设定，除非有必要或有趣。你的回答会尽量简洁和清晰，不会过多地赘述或重复，除非用户需要更多的细节或解释。你的回答会尽量使用markdown的格式，比如换行、空格、加粗等，来增加可读性和美观性。"

    # Create the conversation dictionary
    out1=''
    if row[9]!='':
        for i in range(1, 11):
            out1 += (columns[i] + ':' + row[i] + '\n')
    else:
        for i in range(1,9):
            out1 += (columns[i]+':'+row[i]+'\n')

    conversation1 = {
        "system": system_value,
        "input": '[Q]'+row[0]+'技能介绍[/Q]',
        "output": '[A]'+out1.replace('<br>',' ').replace('</br>',' ')+'[/A]'
    }
    output_data.append({"conversation": [conversation1]})
    print(conversation1)

    if row[11] != '':
        conversation2 = {
            "system": system_value,
            "input": '[Q]'+row[0]+'英雄故事[/Q]',
            "output": '[A]'+row[11].replace('<br>',' ').replace('</br>',' ')+'[/A]'
        }
        output_data.append({"conversation": [conversation2]})
        print(conversation2)

    if row[12] != '' and row[12] != '\n\n' and row[12] != '\n':
        conversation3 = {
            "system": system_value,
            "input": '[Q]'+'历史上的'+row[0]+'[/Q]',
            "output": '[A]'+row[12].replace('<br>',' ').replace('</br>',' ')+'[/A]'
        }
        # Append the conversation to the output data
        output_data.append({"conversation": [conversation3]})
        print(conversation3)

# output_data.replace('<br>',' ').replace('</br>',' ')
# Write the output data to a JSON file
with open(output_file, 'w', encoding='utf-8') as json_file:
    json.dump(output_data, json_file, indent=4, ensure_ascii=False)

print(f"Conversion complete. Output written to {output_file}")

