from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
chatbot = ChatBot('MyBot')
conversation = [
    'Hello',
    'Hi there!',
    'What is your name?',
    "My name is MyBot. What can I do for you?",
    'How are you?',
    'I am doing great!',
    'That is good to hear',
    'Thank you',
    'You are welcome.',
    'Bye',
    'Goodbye!'
]

trainer = ListTrainer(chatbot)
trainer.train(conversation)
while True:
    try:
        user_input = input("You: ")
        response = chatbot.get_response(user_input)
        print("Bot: ", response)

    except KeyboardInterrupt:
        print("Goodbye!")
        break
