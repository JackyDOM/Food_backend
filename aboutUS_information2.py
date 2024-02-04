from flask import jsonify

# aboutUs information2
aboutUs_informationTwo = [
  {
    'id': 700,
    'image': 'https://images.pexels.com/photos/1307698/pexels-photo-1307698.jpeg?cs=srgb&dl=photo-of-cafe-interior-1307698.jpg&fm=jpg',
    'description': '''
    In our website also have a cafe restaurant that easy for you see and 
    you can read description under the image in our website to know more
    about information and about the location where it is and also more
    about it as well. you can search their name as well if you want so
    it is easy for you as well.
    ''',
  }
]

def get_aboutUs_informationTwo():
  return jsonify(aboutUs_informationTwo)