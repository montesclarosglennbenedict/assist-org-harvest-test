
import os
import ast
import json

folder_path = './uci'

# Ensure the folder path is valid
if not os.path.exists(folder_path):
    print(f"The folder path '{folder_path}' does not exist.")
else:
    # Loop through all files in the folder
    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)
        
        # Check if the file is a JSON file
        if file_path.endswith('.json'):
            try:
                # Open and load the JSON file
                with open(file_path, 'r') as json_file:
                    data = json.load(json_file)
                    
                    # Check if the "articulations" key exists in the JSON
                    try:
                        articulations_value = data['result']['articulations']
                        try:
                            output_file_path = "./uci-dump/"+filename
                            with open(output_file_path, 'w') as file:
                                file.write(articulations_value)
                        except:
                            with open(output_file_path, 'w') as file:
                                file.write("None")
                    except:
                        print('bleh')
            except json.JSONDecodeError as e:
                print(f"Error decoding JSON in file '{filename}': {e}")
            except Exception as e:
                print(f"Error processing file '{filename}': {e}")
