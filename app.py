from flask import Flask, jsonify
from flask_cors import CORS


app = Flask(__name__)
CORS(app)

# Sample data
food_provinces = [
    {
        'id': 1,
        'name': 'Province 1',
        'category': 'Category 1',
        'description': 'Description 1',
        'image': 'https://wallpaperaccess.com/full/4723250.jpg'
    },
    # Add more provinces as needed
]

@app.route('/api/food_provinces', methods=['GET'])
def get_food_provinces():
    return jsonify(food_provinces)

if __name__ == '__main__':
    app.run(debug=True)
