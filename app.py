from flask import Flask, jsonify
from flask_cors import CORS
from food_province import get_food_provinces
from banner_food import get_banner_food


app = Flask(__name__)
CORS(app)

@app.route('/api/food_provinces', methods=['GET'])
def food_provinces_route():
    return get_food_provinces() 


@app.route('/api/banner_provinces', methods=['GET'])
def banner_food_route():
    return get_banner_food()

if __name__ == '__main__':
    app.run(debug=True)
