from flask import jsonify

# Banner
banner_provinces = [
    {
        'id': 101,
        'name': 'CeraVe Product',
        'image': 'https://th.bing.com/th/id/OIP.J3GPow8KJaz-J9NL1P_mogHaEM?rs=1&pid=ImgDetMain'
    },
    {
        'id': 102,
        'name': 'The Ordinary Product',
        'image': 'https://static.vecteezy.com/system/resources/previews/000/962/811/original/cosmetic-advertising-banner-with-3d-bottle-set-vector.jpg'
    },
    {
        'id': 103,
        'name': 'La Roche-Posay Product',
        'image': 'https://th.bing.com/th/id/OIP.cezBsMjwB691xflD7qyYxQHaC9?rs=1&pid=ImgDetMain',
    },
    {
        'id': 104,
        'name': 'Neutrogena Product',
        'image': 'https://th.bing.com/th/id/OIP.VClSI_L_bjMRBiwSP-FK3AHaEO?rs=1&pid=ImgDetMain',
    },
    {
        'id': 105,
        'name': 'Drunk Elephant Product',
        'image': 'https://th.bing.com/th/id/OIP.1_BcGt_nlQb4A9bgSEKDzgHaEO?w=740&h=423&rs=1&pid=ImgDetMain'
    },
    {
        'id': 106,
        'name': 'Glossier Product',
        'image': 'https://th.bing.com/th/id/OIP.Bxi-_O7OQV2dZrYIcyx5WQHaE8?w=1380&h=920&rs=1&pid=ImgDetMain'
    }
]

def get_banner_food():
  return jsonify(banner_provinces)