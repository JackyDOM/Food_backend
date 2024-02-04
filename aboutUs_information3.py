from flask import jsonify

# aboutUs information3
aboutUs_infofrmationThree = [
  {
    'id': 800,
    'image': 'https://th.bing.com/th/id/R.10790e90e41c325a167eb776a835a7f7?rik=p1Uz0DxRjA97Bg&pid=ImgRaw&r=0',
    'description': '''
    In our website also have a hotel as well so you can view it and also can
    read the description about it as well. you can search their hotel name as well
    as you want and you can know more about it like location and rating that
    everyone rate about it.
    ''',
  }
]

def get_aboutUs_informationThree():
  return jsonify(aboutUs_infofrmationThree)