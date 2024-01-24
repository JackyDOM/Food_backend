from flask import Flask, jsonify
from flask_cors import CORS
from food_province import get_food_provinces
from banner_food import get_banner_food
from cafe import get_cafe_information


app = Flask(__name__)
CORS(app)

@app.route('/api/food_provinces', methods=['GET'])
def food_provinces_route():
    return get_food_provinces() 


@app.route('/api/banner_provinces', methods=['GET'])
def banner_food_route():
    return get_banner_food()

@app.route('/api/cafe_information', methods=['GET'])
def cafe_information_route():
    return get_cafe_information()

if __name__ == '__main__':
    app.run(debug=True)
