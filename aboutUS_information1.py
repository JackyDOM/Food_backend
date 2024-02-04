from flask import jsonify

# aboutUS information1
aboutUS_informationOne = [
  {
    'id': 600,
    'image': 'https://th.bing.com/th/id/OIP.XwpGr0cjBYjE73iYMn9VvwHaE5?rs=1&pid=ImgDetMain',
    'description': '''
    In Our website, we have a food depend on provinces in Cambodia's country,
    you can click on it and see their food and ingredient and the step of
    how to cook it?. In our website we also have a name as well so it easy for
    you to know and take note about it.
    ''',
  }
]

def get_aboutUs_informationOne():
  return jsonify(aboutUS_informationOne)