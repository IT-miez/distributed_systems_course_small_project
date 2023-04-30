from flask import Flask, jsonify
import random



images = [
    {"id": 1, "url": "https://picsum.photos/id/100/200/300"},
    {"id": 2, "url": "https://picsum.photos/id/200/200/300"},
    {"id": 3, "url": "https://picsum.photos/id/300/200/300"},
    {"id": 4, "url": "https://picsum.photos/id/400/200/300"},
    {"id": 5, "url": "https://picsum.photos/id/500/200/300"}
]

# Flask setup
app = Flask(__name__)

@app.route('/images')
def get_images():
    # Random number between 0 and the lenght of the images-array
    imageNumber = random.randint(0,4)
    chosenElement = images[imageNumber]
    print(chosenElement["url"])
    # Return the URL of the random image
    return jsonify(chosenElement["url"])

if __name__ == '__main__':
    app.run(host='localhost', port=6000, debug=True)
