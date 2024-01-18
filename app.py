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

# Banner
banner_provinces = [
    {
        'id': 101,
        'image': 'https://www.fodors.com/wp-content/uploads/2019/07/25UltimateCambodia__HERO_shutterstock_653520022.jpg'
    },
    {
        'id': 102,
        'image': 'https://th.bing.com/th/id/R.44fecfc5175df2d4b56c6fe38fcb954c?rik=LnFPyFYX4ngNgQ&pid=ImgRaw&r=0'
    }
]

@app.route('/api/food_provinces', methods=['GET'])
def get_food_provinces():
    return jsonify(food_provinces)

@app.route('/api/banner_provinces', methods=['GET'])
def get_banner_provinces():
    return jsonify(banner_provinces)

if __name__ == '__main__':
    app.run(debug=True)
