import openai
import keys

openai.api_key = keys.OPENAI_API_KEY
def generate_text(user_input):
    resp = openai.Completion.create(
        model='gpt-3.5-turbo',
        messages = {'role': 'user', 'text': user_input}
        )
    
    return resp['choices'][0]['text'].strip()


if __name__ == '__main__':
    print("Howdy! My name is Conv and I am ready for your requests! Enter 'quit' to exit.")
    user_input = input("You: ")
    while user_input != 'quit':
        print("Conv:", generate_text(user_input))
        user_input = input("You: ")