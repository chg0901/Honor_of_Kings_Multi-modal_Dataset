import os
import json

# Define the directory containing the .txt files and the keyword list
directory = 'datasets/RAG_Data'
keyword_list = ["被动", "一技能", "二技能", "三技能", "英雄故事", "历史"]

# Initialize the result dictionary
result = {}

# Loop through each file in the directory
for filename in os.listdir(directory):
    if filename.endswith('.txt'):
        filepath = os.path.join(directory, filename)
        base_filename = os.path.splitext(filename)[0]  # Remove the .txt extension
        
        # Read the file line by line
        with open(filepath, 'r', encoding='utf-8') as file:
            lines = file.readlines()
            
            # Loop through each keyword in the keyword list
            for keyword in keyword_list:
                # Loop through each line in the file
                for i in range(len(lines)):
                    line = lines[i]
                    if keyword in line:
                        key = f"{base_filename}{keyword}"
                        if key not in result:
                            result[key] = []
                        if keyword in ["英雄故事", "历史"]:
                            # Add the next line if the keyword is "英雄故事" or "历史"
                            if i + 1 < len(lines):
                                next_line = lines[i + 1].strip()
                                result[key].append(next_line)
                        else:
                            # Add the current line for other keywords
                            result[key].append(line.strip())

# Convert the result dictionary to JSON format
result_json = json.dumps(result, ensure_ascii=False, indent=4)

# Save the JSON to a file
with open('datasets/RAG_Data_Metadata.json', 'w', encoding='utf-8') as json_file:
    json_file.write(result_json)

print("Processing complete.")