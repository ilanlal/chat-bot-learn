from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer

# Create a chatbot instance
chatbot = ChatBot('MyChatBot')

# Create and set up a new trainer
trainer = ChatterBotCorpusTrainer(chatbot)

# Train the chatbot on English language data
trainer.train('chatterbot.corpus.english')

# Function to get chatbot responses
def get_bot_response(message):
    return str(chatbot.get_response(message))

if __name__ == '__main__':
    app.run()
