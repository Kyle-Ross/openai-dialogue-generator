import openai
import json
import pyfiglet
import random


# Defining a small function for printing styled text to console
def fig_print(text, font):
    fig_output = pyfiglet.figlet_format(text, font=font)
    print(fig_output)


# Defining the seperator line length
sep_line = "-" * 71

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

# Printing flavour text to console
fig_print("Open AI Dialogue Generator:", "slant")
print("Follow the prompts to start generating a dialogue between two defined characters. "
      "To finish the chat, enter 'end'.\n\nThe selected model is: " + selected_model + "\n\n" + sep_line + "\n")

# Define the first character
character_a_description = input("Describe the first character:\n")

# Define the second character
character_b_description = input("\nDescribe the second character:\n")

# Defining the prompt to get character names
name_prompt = "1 name idea for a character with the description (name only): "

# Prompt for the AI to provide the name of the first character
character_a_message = name_prompt + character_a_description
character_a_name_input = [{"role": "user", "content": character_a_message}]

# Prompt for the AI to provide the name of the second character
character_b_message = name_prompt + character_b_description
character_b_name_input = [{"role": "user", "content": character_b_message}]

# Prompting ChatGPT for the name of the first character and then saving that as a variable with newlines removed
name_a_response = openai.ChatCompletion.create(model=selected_model, messages=character_a_name_input)
name_a_string_raw = name_a_response["choices"][0]["message"]["content"]
name_a_string_clean = name_a_string_raw.replace("\n", "")

# Prompting ChatGPT for the name of the second character and then saving that as a variable with newlines removed
name_b_response = openai.ChatCompletion.create(model=selected_model, messages=character_b_name_input)
name_b_string_raw = name_b_response["choices"][0]["message"]["content"]
name_b_string_clean = name_b_string_raw.replace("\n", "")

# Creating a description of the characters including their names, to pass to prompts
the_situation = """There are two characters.

1st character's name: %s
1st character's description: %s

2nd character's name: %s
2nd character's description: %s

They are having a conversation.""" % (name_a_string_clean,
                                      character_a_description,
                                      name_b_string_clean,
                                      character_b_description)

# Print the situation set-up to console
print("\n" + sep_line + "\n\n" + the_situation + "\n\n" + sep_line + "\n")

# Set up prompts for certain choices below
situation_a_random = "Act as the 1st character. I will be the 2nd character. Do not provide a response. " \
                     "Begin a conversation. Initially, focus on a topic. " \
                     "This topic can be anything at all, decide randomly. " \
                     "Don't break character for the rest of this chat session. " \
                     "Provide only a single response."

situation_a_related = "Act as the 1st character. I will be the 2nd character. Do not provide a response. " \
                      "Begin a conversation. Initially, focus on a topic. " \
                      "This topic should be related to your character and their potential interests. " \
                      "Don't break character for the rest of this chat session. " \
                      "Provide only a single response."

situation_b_random = "Act as the 2nd character. I will be the 1st character. Do not provide a response. " \
                     "Begin a conversation. Initially, focus on a topic. " \
                     "This topic can be anything at all, decide randomly. " \
                     "Don't break character for the rest of this chat session. " \
                     "Provide only a single response."

situation_b_related = "Act as the 2nd character. I will be the 1st character. Do not provide a response. " \
                      "egin a conversation. Initially, focus on a topic. This topic should be related " \
                      "to your character and their potential interests. " \
                      "Don't break character for the rest of this chat session. " \
                      "Provide only a single response." \

# Defining the variable which to contain the selected conversation start type
conversation_choice = 1

# Defining the variable to contain the chosen character in certain prompts
character_choice = 1

# Options for beginning the dialogue, where variables are defined to drive other logic
while True:
    print("How would you like to the conversation to play out?")
    print("1. Let the AI decide everything")
    print("2. Define the topic of conversation")
    print("3. Start the conversation as one of the characters, then let the AI decide")
    print("4. Act as one of the characters for the whole dialogue")
    choice = input("\nEnter a number (1-4):\n")

    # Handle the user's selection
    if choice == "1":  # Let the AI decide everything
        # Randomly determining how the AI should decide on a topic
        if random.random() < 0.5:  # Topic is completely random
            if random.random() < 0.5:   # Character a starts
                situation_variation = situation_a_random
                character_choice = 1
            else:  # Character b starts
                situation_variation = situation_a_random
                character_choice = 2
        else:  # Topic is related to the character somehow
            if random.random() < 0.5:  # Character a starts
                situation_variation = situation_a_related
                character_choice = 1
            else:  # Character b starts
                situation_variation = situation_b_related
                character_choice = 2
        conversation_choice = 1
    elif choice == "2":  # Define the topic of conversation
        user_defined_topic = input("\nWhat should the topic of conversation be?:\n")
        situation_variation = "should be " + user_defined_topic
        conversation_choice = 2
    elif choice == "3":  # Start the conversation as one of the characters, then let the AI decide
        while True:
            print("\nWhich character should start the conversation?:")
            print("1. Character 1: " + "'" + name_a_string_clean + "'")
            print("2. Character 2: " + "'" + name_b_string_clean + "'")
            choice = input("\nEnter 1 or 2: ")
            if choice == "1":
                character_choice = 1
                break
            elif choice == "2":
                character_choice = 2
                break
            else:
                print("Invalid input. Please choose 1 or 2.\n")
        conversation_choice = 3
    elif choice == "4":  # Act as one of the characters for the whole dialogue
        conversation_choice = 4
    # What happens if they input the wrong number at the start
    else:
        print("Invalid selection. Please enter a number between 1 and 4.\n")
        continue

    # Exit the loop if the user made a valid selection
    break

# Printing a seperator line
print("\n" + sep_line + "\n")


# Function to get the response object based on a selected model and messages dict
def get_response(model, messages):
    response_in_func = openai.ChatCompletion.create(model=model, messages=messages)
    return response_in_func


# Function to return the message dict from the response object
def get_message_dict(response_obj):
    messages_dict_in_func = response_obj["choices"][0]["message"]
    return messages_dict_in_func


# Function to return the message content from the response object, with leading newlines removed
def get_message_content(response_obj):
    messages_content_in_func = response_obj["choices"][0]["message"]["content"]
    messages_content_in_func_lstrip = messages_content_in_func.lstrip('\n')
    return messages_content_in_func_lstrip


# Defining dictionaries to contain messages in the perspective of each character
messages_a_perspective = []  # Target format is {"role": "user", "content": "Placeholder"}, ...
messages_b_perspective = []  # Target format is {"role": "user", "content": "Placeholder"}, ...


# Starting the chat off depending on the choices above - but not yet looping
if conversation_choice == 1:  # Let the AI decide everything

    if character_choice == 1:  # i.e. character a
        # Combine the set-up elements
        combined_situation = the_situation + "\n\n" + situation_variation
        # Append the set-up for a into the a messages dictionary
        messages_a_perspective.append({"role": "user", "content": combined_situation})
        # Get the a response
        response_a = get_response(selected_model, messages_a_perspective)
        # Get the response as a dict
        message_dict_as_a = get_message_dict(response_a)
        # Append that dict to the messages for the a perspective
        messages_a_perspective.append(message_dict_as_a)
        # Get just the content of that message as a string
        message_a_content = get_message_content(response_a)
        # Creating the prompt for the b perspective
        situation_b_perspective = "".join([the_situation,
                                           "\n\n",
                                           "Act as the 2nd character. Pretend that I am the 1st character. ",
                                           "Don't break character for the rest of the chat session.\n\n",
                                           "I say: ",
                                           "'", message_a_content, "'",
                                           "\n\nHow do you respond? Only include your in character responses. ",
                                           "Do not provide a response."])
        # Append the set-up for b into the b messages dictionary
        messages_b_perspective.append({"role": "user", "content": situation_b_perspective})
        # Get the b response
        response_b = get_response(selected_model, messages_a_perspective)
        # Get the response as b dict
        message_dict_as_b = get_message_dict(response_b)
        # Append that dict to the messages for the b perspective
        messages_b_perspective.append(message_dict_as_b)

    if character_choice == 2:  # i.e. character a
        # Combine the set-up elements
        combined_situation = the_situation + "\n\n" + situation_variation
        # Append the set-up for b into the b messages dictionary
        messages_b_perspective.append({"role": "user", "content": combined_situation})
        # Get the b response
        response_b = get_response(selected_model, messages_b_perspective)
        # Get the response as a dict
        message_dict_as_b = get_message_dict(response_b)
        # Append that dict to the messages for the a perspective
        messages_b_perspective.append(message_dict_as_b)
        # Get just the content of that message as b string
        message_b_content = get_message_content(response_b)
        # Creating the prompt for the a perspective
        situation_a_perspective = "".join([the_situation,
                                           "\n\n",
                                           "Act as the 1st character. Pretend that I am the 2nd character. ",
                                           "Don't break character for the rest of the chat session.\n\n",
                                           "I say: ",
                                           "'", message_b_content, "'",
                                           "\n\nHow do you respond? Only include your in character responses. ",
                                           "Do not provide a response."])
        # Append the set-up for a into the a messages dictionary
        messages_a_perspective.append({"role": "user", "content": situation_a_perspective})
        # Get the a response
        response_a = get_response(selected_model, messages_a_perspective)
        # Get the response as a dict
        message_dict_as_a = get_message_dict(response_a)
        # Append that dict to the messages for the a perspective
        messages_a_perspective.append(message_dict_as_a)

print(messages_a_perspective)
print(messages_b_perspective)


if conversation_choice == 2:  # Define the topic of conversation
    print("do this")

if conversation_choice == 3:  # Start the conversation as one of the characters, then let the AI decide
    print("do this")

if conversation_choice == 4:  # Act as one of the characters for the whole dialogue
    print("do this")