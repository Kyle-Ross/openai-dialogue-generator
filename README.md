# openai-bot-bazaar

## About
Various scripts utilising the OpenAI API via their python library. Quick and easy ways to use your paid API key, including ways usually reserved for the far more expensive ChatGPT Plus subscription.

Easily usable by anyone with their own API key, just change the values in the 'secrets_placeholder.json' and change the file name to 'secrets.json'.

## single_prompt_and_response
Basic script that allows you to get a single response from ChatGPT based on a string value. No command line interface.

## rolling_chat
Emulates the chat functionality of the OpenAI Web UI in the console, allowing you to have a rolling conversation with the AI where it remembers the conversation.

Key Differences to the web UI:
- Use your much faster API key
- Can use different language models
- Conversations are not saved

![rolling_chat example gif](https://i.imgur.com/pjuCkKm.gif)

## dialogue_generator
Command line interface for generating characters and dialogue between them with OpenAI.