import openai
import json
import pyfiglet


# Defining a small function for printing styled text to console
def fig_print(text, font):
    fig_output = pyfiglet.figlet_format(text, font=font)
    print(fig_output)


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
fig_print("Open AI Chat:", "slant")
print("Enter a prompt to begin your AI chat. "
      "To finish the chat, enter 'end'.\n\nThe selected model is: " + selected_model + "\n\n" + ("-" * 71) + "\n")

# Kicking off the chat session
first_input = input("User:\n")

# Defining the messages variable which will carry the conversation values
messages = [{"role": "user", "content": first_input}]

# Looping recursive statement
while True:
    # Creating a response object based on the messages
    response = openai.ChatCompletion.create(model=selected_model, messages=messages)

    # Appending the message dict to the messages list
    messages.append(response["choices"][0]["message"])

    # Getting the response as a string
    response_string = response["choices"][0]["message"]["content"]

    # Removing leading newlines prefixed by openai
    response_string_lstrip = response_string.lstrip('\n')

    # Printing that response, removing leading newlines that are always added
    print("\n" + selected_model + ":\n" + response_string_lstrip)

    # Requesting user response
    user_response = input("\nUser:\n")

    # Setting the break condition
    if user_response == "end":
        break
    else:
        # Formatting the response in the required dict format
        user_response_dict = {"role": "user", "content": user_response}

        # Appending the new response to the rolling messages value, then looping
        messages.append(user_response_dict)

# TODO Add support for muilti-line input, will likely have to be outside of command line. Currently pasting in anything multi-line causes issues