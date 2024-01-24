from flask import jsonify

# Cafe
cafe_information = [
  {
    'id': 100,
    'name': 'Crane Café',
    'image': 'https://b.zmtcdn.com/data/reviews_photos/00b/626b1c51074f50aa643551774a3ed00b.jpg',
    'detail': [
      {
        'images': 'https://b.zmtcdn.com/data/reviews_photos/00b/626b1c51074f50aa643551774a3ed00b.jpg',
        'description': '''
        Crane Café - Crane Cafe is a small club and a quiet place suitable for resting and relaxing and to talk 
        about movies, art, culture, religion or whatever you want to discuss, this cafe is famous for serving 
        great coffee and other delicious hot drinks, in addition to a range of delicious dishes 
        such as Tom Yam soup and curry noodles And chicken sandwich, along with many amazing desserts.
        Place address: Krong Siem Reap, Cambodia
        ''',
      }
    ]
  },
  {
    'id': 200,
    'name': 'Vintage Bar',
    'image': 'https://th.bing.com/th/id/OIP.WjVvUDNUYvvlrbsoR0lVygHaE1?rs=1&pid=ImgDetMain',
    'detail': [
      {
        'images': 'https://th.bing.com/th/id/OIP.WjVvUDNUYvvlrbsoR0lVygHaE1?rs=1&pid=ImgDetMain',
        'description': '''
        Vintage Bar - The Vintage Café is located in the wonderful city of Battambang, 
        and it is characterized by its friendly staff, great service, and affordable prices 
        for everyone. It serves some distinguished wines such as traditional organic palm wine, 
        French and international wines, in addition to some vegetarian appetizers, pâté pastries, 
        cheese and meat dishes, and has a comfortable atmosphere suitable for enjoying with friends .
        Place address: #84 Rd No 2.5, Krong Battambang, Cambodia
        ''',
      }
    ]
  },
  {
    'id': 300,
    'name': 'Fresh Fruit Factory',
    'image': 'https://th.bing.com/th/id/R.817a74f80ebf0eb1f5c443337ac6d72e?rik=oS8GbPHRQS9L0g&riu=http%3a%2f%2fcdn.4travel.jp%2fimg%2ftcs%2ft%2ftips%2fpict%2fsrc%2f148%2f246%2fsrc_14824627.jpg&ehk=PItAHRIRwiBtLFfyHpGZZ%2baHXrTbZN0mDVWIJfCF%2fos%3d&risl=&pid=ImgRaw&r=0',
    'detail': [
      {
        'images': 'https://th.bing.com/th/id/R.817a74f80ebf0eb1f5c443337ac6d72e?rik=oS8GbPHRQS9L0g&riu=http%3a%2f%2fcdn.4travel.jp%2fimg%2ftcs%2ft%2ftips%2fpict%2fsrc%2f148%2f246%2fsrc_14824627.jpg&ehk=PItAHRIRwiBtLFfyHpGZZ%2baHXrTbZN0mDVWIJfCF%2fos%3d&risl=&pid=ImgRaw&r=0',
        'description': '''
        Fresh Fruit Factory Restaurant - The Fresh Fruit Factory restaurant is famous 
        for serving delicious fruit food made from fresh and safe ingredients in a healthy kitchen. 
        It is distinguished by its friendly staff, great service and quiet sessions that are ideal 
        for spending some quality time with friends. It is a contemporary international cafe suitable 
        for vegetarians, and provides a group of distinctive dishes such as Caesar salad and toast and 
        carbonara and pineapple salad.
        Place address: 155 ផ្លូវ តាភុល ក្រុងសៀមរាប, Krong Siem Reap 17254, Cambodia
        ''',
      }
    ]
  },
  {
    'id': 400,
    'name': 'Little Casablanca Café & Bar',
    'image': 'https://www.moroccoclassictours.com/wp-content/uploads/2020/03/Rick%E2%80%99s-Cafe-in-Casablanca-2.jpg',
    'detail': [
      {
        'images': 'https://www.moroccoclassictours.com/wp-content/uploads/2020/03/Rick%E2%80%99s-Cafe-in-Casablanca-2.jpg',
        'description': '''
        Little Casablanca Café & Bar - Sit, relax and enjoy the distinctive flavors 
        of East and West at Little Casablanca Café, which provides a comfortable and 
        calm atmosphere with a beautiful design inspired by Casablanca, and savor what is 
        cooked in their kitchen of Asian and international cuisine mixed with local flavors 
        and ingredients, and examples of its dishes are spicy chicken with basil and chicken curry, 
        as well It provides many refreshing juices.
        Place address: Sok San Rd, Krong Siem Reap, Cambodia
        ''',
      }
    ]
  },
  {
    'id': 500,
    'name': 'Footprint Café',
    'image': 'https://i0.wp.com/thefoodbunny.com/wp-content/uploads/2018/06/20180622_084140.jpg?resize=780%2C439&ssl=1',
    'detail': [
      {
        'image': 'https://i0.wp.com/thefoodbunny.com/wp-content/uploads/2018/06/20180622_084140.jpg?resize=780%2C439&ssl=1',
        'description': '''
        Footprint Café - The popular, non-profit Footprint Café located on vibrant 
        26th Street supports educational projects and community initiatives in Siem Reap. 
        Its menu includes an eclectic range of breakfast dishes, a special selection of Cambodian 
        favorites, along with many delicious desserts, and provides a quiet and comfortable space 
        to sit with Hundreds of books to browse or buy.
        Place address: Postal Code 17254, Street 26, Wat Bo Village, Krong Siem Reap, Cambodia
        ''',
      }
    ]
  },
  {
    'id': 600,
    'name': 'Romcheik 5 Artspace & Café',
    'image': 'https://th.bing.com/th/id/OIP.CGOUZRratm6msAK-o9cyywHaFD?rs=1&pid=ImgDetMain'
  },
  {
    'id': 700,
    'name': 'Pages Café',
    'image': 'https://res.cloudinary.com/tf-lab/image/upload/w_600,h_337,c_fill,g_auto:subject,q_auto,f_auto/restaurant/3f3c76ef-8872-47b1-b336-fd90ddc8ad22/b70325f7-85ad-4f48-b2b3-9204f4b1c43f.jpg'
  },
  {
    'id': 800,
    'name': 'Pou Restaurant and Bar',
    'image': 'https://th.bing.com/th/id/OIP.JCuArF4rNs3kKISIyg2fWgHaE8?rs=1&pid=ImgDetMain'
  },
  {
    'id': 900,
    'name': 'Enocafe Coffee and Italian Restaurant',
    'image': 'https://th.bing.com/th/id/R.8f5c9a9f4c8ecd99ab8e2f33daff51ad?rik=9Xo6DZ7filQFtQ&pid=ImgRaw&r=0'
  }
]

def get_cafe_information():
  return jsonify(cafe_information)