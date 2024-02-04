from flask import Flask, jsonify
from flask_cors import CORS
from food_province import get_food_provinces
from banner_food import get_banner_food
from cafe import get_cafe_information
from hotel import get_hotel_information
from aboutUs_banner import get_aboutUs_information
from aboutUS_information1 import get_aboutUs_informationOne
from aboutUS_information2 import get_aboutUs_informationTwo
from aboutUs_information3 import get_aboutUs_informationThree



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

@app.route('/api/hotel_information', methods=['GET'])
def hotel_information_route():
    return get_hotel_information()

@app.route('/api/aboutUs_bannery', methods=['GET'])
def aboutUs_bannery_route():
    return get_aboutUs_information()

@app.route('/api/aboutUs_information1', methods=['GET'])
def aboutUs_information1_route():
    return get_aboutUs_informationOne()

@app.route('/api/aboutUs_information2', methods=['GET'])
def aboutUs_information2_route():
    return get_aboutUs_informationTwo()

@app.route('/api/aboutUs_information3', methods=['GET'])
def aboutUs_information3_route():
    return get_aboutUs_informationThree()

if __name__ == '__main__':
    app.run(debug=True)
