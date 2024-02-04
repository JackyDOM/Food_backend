from flask import jsonify

# aboutUS information1
aboutUS_informationOne = [
  {
    'id': 600,
    'imaged': 'https://th.bing.com/th/id/OIP.XwpGr0cjBYjE73iYMn9VvwHaE5?rs=1&pid=ImgDetMain',
    'descriptiony': '''
    In Our website, we have a food depend on provinces in Cambodia's country,
    you can click on it and see their food and ingredient and the step of
    how to cook it?. In our website we also have a name as well so it easy for
    you to know and take note about it.
    ''',
  },
  {
    'id': 600,
    'imaged': 'https://images.pexels.com/photos/1307698/pexels-photo-1307698.jpeg?cs=srgb&dl=photo-of-cafe-interior-1307698.jpg&fm=jpg',
    'descriptiony': '''
    In our website also have a cafe restaurant that easy for you see and 
    you can read description under the image in our website to know more
    about information and about the location where it is and also more
    about it as well. you can search their name as well if you want so
    it is easy for you as well.
    ''',
  },
  {
    'id': 602,
    'imaged': 'https://th.bing.com/th/id/R.10790e90e41c325a167eb776a835a7f7?rik=p1Uz0DxRjA97Bg&pid=ImgRaw&r=0',
    'descriptiony': '''
    In our website also have a hotel as well so you can view it and also can
    read the description about it as well. you can search their hotel name as well
    as you want and you can know more about it like location and rating that
    everyone rate about it.
    ''',
  },
  
]

def get_aboutUs_informationOne():
  return jsonify(aboutUS_informationOne)