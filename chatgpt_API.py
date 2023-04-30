import openai
import os
from flask import Flask, request
from dotenv import load_dotenv



# OpenAI credentials through .env file
my_openai_key = os.getenv("OPEN_AI_PASSCODE")
openai.api_key = my_openai_key
load_dotenv()


# Flask setup
app = Flask(__name__)

@app.route('/prompt', methods=['POST'])
def index():
    # User input from JSON body
    input_text = request.json['input_text']

    # OpenAI request
    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=input_text,
        max_tokens=50,
        n=1,
        stop=None,
        temperature=0.5,
    )

    # Extract the generated response from the API response
    output_text = response.choices[0].text.strip()

    return {"result": output_text}

    

if __name__ == '__main__':
    app.run(host='localhost', port=7000, debug=True)
