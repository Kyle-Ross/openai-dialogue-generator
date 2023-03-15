import openai
import json

# Defining the json file path containing API information
json_secrets = "secrets.json"

# Open JSON file
with open(json_secrets) as file:
    json_data = json.load(file)

# Define API values, and setting to openai attributes
openai.api_key = json_data["openai_api_key"]
openai.organization = json_data["openai_org_id"]

# Define model to be used
selected_model = "gpt-3.5-turbo"

# Define the prompt
prompt = "Give me 3 ideas for a the name of a spooky potato villain"

# Including that into that ChatCompletion syntax
messages = [{"role": "user", "content": prompt}]

# Creating a response object based on a prompt
chat_completion = openai.ChatCompletion.create(model=selected_model, messages=messages)

# Getting the output
output = chat_completion.choices[0].message.content

# Trimming leading newlines from output
output_lstrip = output.lstrip('\n')

# Printing the output
print(output_lstrip)
