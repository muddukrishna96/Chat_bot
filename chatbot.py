# -*- coding: utf-8 -*-
"""
Created on Mon Jul 31 23:11:38 2023

@author: mgalaval
"""

from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer

# Create a new chatbot instance
chatbot = ChatBot('MyChatBot')

# Create a new instance of a ChatterBotCorpusTrainer
trainer = ChatterBotCorpusTrainer(chatbot)

# Train the chatbot on the English language corpus data
trainer.train('chatterbot.corpus.english')

# Main loop for the chatbot
while True:
    user_input = input('You: ')
    if user_input.lower() == 'exit':
        print('ChatBot: Goodbye!')
        break
    response = chatbot.get_response(user_input)
    print('ChatBot:', response)
