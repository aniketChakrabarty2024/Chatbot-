#QNA_SETUP

import random

# Define responses
response_bucket = {
    "hi": ["Hello!"],
    "hello": ["hi!"],
    "how are you": ["I'm good,", "Feeling great, thanks for asking!"],
    "how old are you": ["I am just typed as code few times before"],
    "about": ["I'm a python chatbot created by Aniket to enhance the past masterness of my master"],
    "master": [" In technology, \"master\" can refer to the main or primary version of something, such as a \"master copy\" of a document or a \"master branch\" in version control systems like Git, but my master is Aniket Chakrabarty who typed me in that magical way that I can resolve few questions of you"],
    "bye": ["Goodbye!"]
}

def get_response(message):
    # Convert message to lowercase
    message = message.lower()
    
    # after not getting match returning a default response
    return response_bucket.get(message, "I'm not sure how to respond to that.")

def main():
    print("Welcome to the ChatBot!")
    print("You can start chatting. Type 'bye' to exit.")
    
    while True:
        user = input("You--> ")
        if user.lower() == "bye":
            print("ChatBot: Goodbye!")
            break
        else:
            response = get_response(user)
            print("ChatBot-->", response)

if __name__ == "__main__":
    main()

