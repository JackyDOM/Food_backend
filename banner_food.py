from flask import jsonify

# Banner
banner_provinces = [
    {
        'id': 101,
        'name': 'ទេសភាពភ្នំ',
        'image': 'https://th.bing.com/th/id/OIP.sD8hMXWXjpQwNjnshKC6IAHaE7?rs=1&pid=ImgDetMain'
    },
    {
        'id': 102,
        'name': 'កន្លែងដើរលេង',
        'image': 'https://www.studentuniverse.com/blog/wp-content/uploads/2014/04/Most-Beautiful-Places-to-Travel-Featured-Image.jpg'
    },
    {
        'id': 103,
        'name': 'ទឹកជ្រោះ',
        'image': 'https://d13jio720g7qcs.cloudfront.net/images/destinations/848_477/561f7b8593e09.jpg',
    },
    {
        'id': 104,
        'name': 'ភោជនីដ្ខាន',
        'image': 'https://res.cloudinary.com/djcyhbk2e/image/upload/f_auto,q_35,w_1200/v1/gvv/prod/djkgwshfi64a2rh0nm8w',
    },
    {
        'id': 105,
        'name': 'សណ្ខារគារ',
        'image': 'https://th.bing.com/th/id/OIP.ZqW5-jDyB0Itgq9D3BByYwHaEU?rs=1&pid=ImgDetMain'
    },
    {
        'id': 106,
        'name': 'ហាងកាហ្វេ',
        'image': 'https://southeastasiaglobe.com/wp-content/uploads/2017/01/Store-Environments.jpg'
    }
]

def get_banner_food():
  return jsonify(banner_provinces)