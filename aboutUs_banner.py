from flask import jsonify

# aboutUs banner
aboutUs_banners = [
  {
    'id': 500,
    'name': 'About Us',
    'image': 'https://lirp.cdn-website.com/469c397a/dms3rep/multi/opt/shutterstock_1500952496-8df0d1b9-1920w.jpg'
  },
  {
    'id': 501,
    'name': 'Cafe Shop',
    'image': 'https://i.pinimg.com/originals/b7/cc/f8/b7ccf85e3aceb11d7dc35c2c98077570.jpg'
  },
  {
    'id': 502,
    'name': 'Hotel',
    'image': 'https://cdn.dribbble.com/users/6550057/screenshots/14740066/hotel_4x.jpg'
  }
]

def get_aboutUs_information():
  return jsonify(aboutUs_banners)