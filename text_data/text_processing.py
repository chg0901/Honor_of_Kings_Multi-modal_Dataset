import pandas as pd
import json
# 读取Excel文件
df = pd.read_excel("王者荣耀故事英雄与技能4.xlsx")
df = df.fillna('')
columns = ['英雄', '被动名','被动介绍',
           '一技能名称', '一技能介绍',
            '二技能名称', '二技能介绍',
            '三技能名称', '三技能介绍',
            '四技能名称', '四技能介绍',
           '英雄故事', '历史故事', ]

output_file = 'processed.jsonl'

output_data = []

# Iterate through each row in column A and D
# 遍历每一行的元素
for index, row in df.iterrows():
    system_value = "你是一个资深的王者荣耀骨灰级玩家, 你对每个英雄的背景故事, 技能都了如指掌, 你将根据用户对英雄的有关问题的提问, 做出相应的回答, 回答会尽量的根据王者荣耀设定回答而非创造或者修改.."

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
        "input": row[0]+'技能介绍',
        "output": out1.replace('<br>',' ').replace('</br>',' ')
    }
    output_data.append({"conversation": [conversation1]})
    print(conversation1)

    if row[11] != '':
        conversation2 = {
            "system": system_value,
            "input": row[0]+'英雄故事',
            "output": row[11].replace('<br>',' ').replace('</br>',' ')
        }
        output_data.append({"conversation": [conversation2]})
        print(conversation2)

    if row[12] != '' and row[12] != '\n\n' and row[12] != '\n':
        conversation3 = {
            "system": system_value,
            "input": '历史上的'+row[0],
            "output": row[12].replace('<br>',' ').replace('</br>',' ')
        }
        # Append the conversation to the output data
        output_data.append({"conversation": [conversation3]})
        print(conversation3)

# output_data.replace('<br>',' ').replace('</br>',' ')
# Write the output data to a JSON file
with open(output_file, 'w', encoding='utf-8') as json_file:
    json.dump(output_data, json_file, indent=4)

print(f"Conversion complete. Output written to {output_file}")

