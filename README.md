# openai-dialogue-generator

Interactive dialogue generator built using the OpenAI API via their python library. 

Easily usable by anyone with their own API key, just change the values in the 'secrets_placeholder.json' and change the file name to 'secrets.json'.

## How it works
A step-by-step command line interface guides you through the process of generating character and starting a dialogue between them.

You describe the characters, and their names are generated by the AI. 

From there, you can leave it to the AI to choose a topic of discussion - or direct it to have the characters talk about something specific.

After each response from the AI, you can continue generating the dialogue with or without additional prompts.

When you are done, you can conveniently output the dialogue to a text file - see the example saved in the root folder.

![Dialogue generator example gif](https://i.imgur.com/VrWYYI1.gif)

## Other Notes
- Used models can be swapped in the code by changing the 'selected_model' variable
- Prompts are divided into building blocks which can be easily adjusted in the code to fine-tune the AI output
