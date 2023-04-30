from flask import Flask, jsonify
import random

app = Flask(__name__)

quotes = [
    {"id": 1, "text": "Be the change you wish to see in the world.", "author": "Mahatma Gandhi"},
    {"id": 2, "text": "In three words I can sum up everything I've learned about life: it goes on.", "author": "Robert Frost"},
    {"id": 3, "text": "No one can make you feel inferior without your consent.", "author": "Eleanor Roosevelt"},
    {"id": 4, "text": "It does not matter how slowly you go as long as you do not stop.", "author": "Confucius"},
    {"id": 5, "text": "You only live once, but if you do it right, once is enough.", "author": "Mae West"}
]

@app.route('/quotes')
def get_quotes():
    # Random number between 0 and the lenght of the images-array
    quoteNumber = random.randint(0,4)
    chosenElement = quotes[quoteNumber]
    quoteWithFormat = chosenElement["author"]+": "+chosenElement["text"]
    print(chosenElement["author"]+": "+chosenElement["text"])
    # Return Author name next to the quote as a "formatted" string
    return jsonify(quoteWithFormat)

if __name__ == '__main__':
    app.run(host='localhost', port=5000, debug=True)
