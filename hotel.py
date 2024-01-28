from flask import jsonify

# Hotel
hotel_information = [
  {
    'id': 200,
    'name': 'Raffles Hotel Le Royal - Phnom Penh',
    'image': 'https://www.rafflesphnompenh.com/wp-content/uploads/sites/232/2021/06/Raffles-Hotel-Le-Royal-Morning-Facade-Shot-2021-2100x1100.jpg',
    'detail': [
      {
        'image': 'https://www.rafflesphnompenh.com/wp-content/uploads/sites/232/2021/06/Raffles-Hotel-Le-Royal-Morning-Facade-Shot-2021-2100x1100.jpg',
        'description': '''
        Blending luxury with an old-world charm, Raffles Hotel Le Royal features accommodation 
        with a private balcony offering pool or garden views. Guests can take a dip in the outdoor 
        lap pool and enjoy meals at one of the 2 dining options or have a drink at the bar. Free WiFi 
        is available in all rooms.Located in the heart of Phnom Penh, Chaktomuk Conference Hall 
        2 is 3 km away from Raffles Hotel Le Royal, while it is just a 20-minute drive from Phnom Penh 
        International Airport. Royal Palace and the National Museum are 2 km away.Spacious air-conditioned 
        rooms at Raffles are equipped with a TV with cable channels and a minibar. En suite bathrooms 
        include a hairdryer, bathrobes and free toiletries.Guests can approach the 24-hour front 
        desk for use of meeting rooms and banquet facilities. Other facilities include a business 
        centre and a tour desk. Raffles Hotel Le Royal also provides a toll-free Global Events 
        and Meetings Solutions service.Restaurant Le Royal serves up modern French and Khmer dishes, 
        while Le Phnom 1929 features all-day dining with buffet and a la carte options. 
        Drinks and light snacks are served at Writers Bar, Elephant Bar and Poolside Terrace. 
        24-hour room service is also available.Couples particularly like the location — they 
        rated it 9.5 for a two-person trip.
        ''',
      }
    ]
  },
  {
    'id': 201,
    'name': 'Sofitel Angkor Phokeethra Golf & Spa Resort - Siem Reap',
    'image': 'https://pix3.agoda.net/hotelimages/3685/-1/a694e08e21d178d19d9c369e9c142a15.jpg',
    'detail': [
      {
        'image': 'https://pix3.agoda.net/hotelimages/3685/-1/a694e08e21d178d19d9c369e9c142a15.jpg',
        'description': '''
        Sofitel Angkor Phokeethra Golf & Spa Resort is set among tranquil landscaped gardens on 
        the tree-lined Charles de Gaulle Avenue. It is just 10 minutes drive to Angkor Wat.Rooms 
        enjoy a blend of French and Khmer design and decor. Each is equipped with a tea and coffee 
        maker, satellite TV and air conditioning. Bathrooms have a bathtub, toiletries and bathrobes. 
        Room service is available 24 hours a day.Sofitel Angkor Phokeethra Golf & Spa Resort 
        offers guests a wide variety of dining options, including French and international cuisines.
        The outdoor pool with swim-up bar is an ideal place for relaxing. There is an indulgent spa 
        centre with a hot tub and massage treatments. It also has an 18-hole Country Golf Club.
        Sofitel Angkor Phokeethra Golf & Spa Resort is located less than 15 minutes drive to 
        Siem Reap bustling centre, Pub Street and the Old French Quarter.  The Siem Reap Angkor 
        International Airport is also located around 55 minutes drive away.Couples 
        particularly like the location — they rated it 9.4 for a two-person trip.
        ''',
      }
    ]
  },
  {
    'id': 202,
    'name': 'Amansara - Siem Reap',
    'image': 'https://th.bing.com/th/id/OIP.wxM7F8v2_SupE65dq9Z-3gHaEw?rs=1&pid=ImgDetMain',
    'detail': [
      {
        'image': 'https://th.bing.com/th/id/OIP.wxM7F8v2_SupE65dq9Z-3gHaEw?rs=1&pid=ImgDetMain',
        'description': '''
        The 5-star Amansara resort, in Angkor, Cambodia, is a former Royal residence, 
        now a spacious and tranquil sanctuary in central Siem Reap. The resort is located only
        10 mins away from the Unesco World Heritage Site of Angkor Archaelogical Park. Customised 
        guided itineraries and Amanbala boat excursions are also an option how to get to know the 
        surroundings. The Aman Spa located in the resort offers Khmer healing traditions and yoga, 
        movement and meditation and spiritually enriching activities such as forest bathing, walking 
        meditation and Buddhist water blessing are also provided. Amansara resort also celebrates 
        the pure, fresh flavours of traditional Khmer cuisine with a daily changing menu shaped 
        by Siem Reap's seasonal market produce.
        ''',
      }
    ]
  },
  {
    'id': 203,
    'name': 'Belmond La Résidence dAngkor - Siem Reap',
    'image': 'https://secure.s.forbestravelguide.com/img/properties/belmond-la-residence-dangkor/extra-large/belmond-la-residence-dangkor-restaurant.jpg',
    'detail': [
      {
        'image': 'https://secure.s.forbestravelguide.com/img/properties/belmond-la-residence-dangkor/extra-large/belmond-la-residence-dangkor-restaurant.jpg',
        'description': '''
        Address: River Road, Siem Reap, Cambodia.
        It's strategically situated near the Angkor Wat temple complex, 
        one of the most famous archaeological sites in Southeast Asia.
        The hotel offers luxurious rooms and suites with modern amenities.
        Rooms may include features such as private balconies, traditional Khmer-inspired 
        decor, and views of lush gardens or the river.
        Belmond La Résidence d'Angkor typically provides a range of dining options, 
        including on-site restaurants serving Khmer and international cuisine.
        The hotel often emphasizes high-quality dining experiences with a focus on local flavors.
        The hotel may offer spa and wellness facilities for guests seeking relaxation.
        Other amenities might include a swimming pool, fitness center, and possibly event spaces 
        for conferences or special occasions.
        Some luxury hotels in Siem Reap, including Belmond La Résidence d'Angkor, may provide 
        cultural programs or experiences to help guests explore the local traditions and heritage.
        The hotel might offer transportation services, including transfers to and from the Siem Reap 
        International Airport.
        ''',

      }
    ]
  },
  {
    'id': 204,
    'name': 'Park Hyatt Siem Reap - Siem Reap',
    'image': 'https://assets.hyatt.com/content/dam/hyatt/hyattdam/images/2016/12/21/1432/Park-Hyatt-Siem-Reap-P024-Exterior-Shot.jpg/Park-Hyatt-Siem-Reap-P024-Exterior-Shot.16x9.adapt.1920.1080.jpg',
    'detail': [
      {
        'image': 'https://assets.hyatt.com/content/dam/hyatt/hyattdam/images/2016/12/21/1432/Park-Hyatt-Siem-Reap-P024-Exterior-Shot.jpg/Park-Hyatt-Siem-Reap-P024-Exterior-Shot.16x9.adapt.1920.1080.jpg',
        'description': '''
        Nestled within private gardens, the luxurious 5-star Park Hyatt Siem Reap offers 
        modern guestrooms with free WiFi. Featuring the largest collection of modern and 
        traditional Cambodian Art, the hotel has indoor and outdoor pools and 3 dining options.
        Located on Sivutha Boulevard, Park Hyatt Siem Reap is a minutes walk away from the 
        French Colonial Quarters, the Old Market and Pub streets. The Angkor National Museum 
        is a 2-minute tuk-tuk (rickshaw) ride away. It takes 15 minutes by car to reach the UNESCO 
        World Heritage Site of Angkor Wat and Siem Reap International Airport.
        Offering views of downtown Siem Reap or the hotel courtyard, each air-conditioned room 
        features Khmer-inspired contemporary art, custom furniture and summery decor. Rooms 
        include a flat-screen satellite TV with DVD player, Nespresso coffee and welcome fruits 
        that are replenished daily. A private bathroom features Italian marble and dual vanities.
        Well-manicured gardens and private plunge pools dot the property, which also boasts 
        a 24-hour fitness centre and spa offering massage services. Other recreation facilities 
        include a hot tub and steam room. Custom made tours can be arranged with the concierge.
        ''',
      }
    ]
  },
  {
    'id': 205,
    'name': 'Sokha Beach Resort - Sihanoukville',
    'image': 'https://cf.bstatic.com/images/hotel/max1024x768/960/96085585.jpg',
    'detail': [
      {
        'image': 'https://cf.bstatic.com/images/hotel/max1024x768/960/96085585.jpg',
        'description': '''
        You're eligible for a Genius discount at Sokha Beach Resort! To save 
        at this property, all you have to do is sign in.
        Sokha Beach Resort is a beachfront resort located in Sihanoukville, 
        Southern Cambodia. With easy access to the 1.5 km long white sand beach, the resort 
        also features landscaped gardens, swimming pools, multiple choices of restaurants, spa 
        facilities as well as poolside swim up bars. Complimentary WiFi is available in the public 
        areas. Staff is able to converse in Chinese, Vietnamese, Russian, Khmer and English.
        All rooms feature a private balcony and are fitted with wooden flooring, individual air 
        conditioning and hot water system. Other amenities included in the rooms are a kettle, a 
        personal safety deposit box, a flat-screen cable TV, minibar, slippers and an en suite bathroom 
        with toothbrushes, separate bathtubs and shower cubicles.
        The resort features 2 large swimming pools with an adjoining kids pool, poolside swim up 
        bars such as the “Pool Bar” and “Dolphin Bar”. Guests can also visit kiosk bars located along 
        the beach area. Beachfront dining options are also available via “The Deck Tapas Bar”, “Lemongrass”, 
        "Champa Cafe" and "China House", which offer a wide selection of local Khmer, Asian and Western cuisines.
        Jasmine Spa also offers guests relaxing massages in private treatment rooms, which include double 
        and triple massage bed combinations for couples, families and friends. Guests can also select 
        to have their massages at the outdoor kiosks on the terrace, while overlooking the sea view. 
        Guests can also enjoy the complimentary steam, sauna, hot tub, the fitness centre, or even the Kids Club.
        Located within 30 minutes driving distance from Sihanoukville International Airport, 5 minutes 
        to the coastal town centre, and a 4-hour drive from Phnom Penh International Airport, 
        Sokha Beach Resort offers two-way airport transfers depending on destinations and upon availability.
        Couples particularly like the location — they rated it 8.4 for a two-person trip.
        ''',
      }
    ]
  },
  {
    'id': 206,
    'name': 'Independence Hotel Resort & Spa - Sihanoukville',
    'image': 'https://pix10.agoda.net/hotelImages/894/89449/89449_16091623000046562684.jpg?ca=6&ce=1&s=1024x768',
    'detail': [
      {
        'image': 'https://pix10.agoda.net/hotelImages/894/89449/89449_16091623000046562684.jpg?ca=6&ce=1&s=1024x768',
        'description': '''
        Located on a private beach in Sihanoukville, this 4-star hotel offers a peaceful retreat with 
        its tropical gardens and sea-facing accommodation. It houses an outdoor pool and a fitness centre. 
        Free WiFi is available throughout the property.
        Spacious rooms at Independence Hotel offer either a rainforest or ocean view and include a cable 
        TV and modern bathroom with a hairdryer. Tea/coffee making facilities and a minibar are included.
        Independence is about a 30-minute drive from Ream National Park and Kbal Chhay Waterfalls. Sihanoukville 
        International Airport is approximately a 20-minute drive away.
        The Coral Restaurant serves á la carte meals and a buffet spread of international dishes. 
        The Sunset Terrace offers fresh seafood while the History Bar & Lounge features a variety of 
        beverages and snacks.
        Guests can use the business centre or make travel arrangements at the tour desk. 
        Other facilities at Independence include water sports and the Jouvence Spa.
        Couples particularly like the location — they rated it 8.1 for a two-person trip.
        ''',
      }
    ]
  },
  {
    'id': 207,
    'name': 'Shinta Mani Shack - Siem Reap',
    'image': 'https://s-ec.bstatic.com/images/hotel/max1024x768/107/107274458.jpg',
    'detail': [
      {
        'image': 'https://s-ec.bstatic.com/images/hotel/max1024x768/107/107274458.jpg',
        'description': '''
        Address: Junction of Oum Khun and 14th Street, Siem Reap, Cambodia.
        It is centrally located in Siem Reap, providing convenient access to 
        the Angkor Wat temple complex.
        Shinta Mani Shack offers stylish and comfortable accommodations with a 
        focus on contemporary design.
        The hotel's rooms and suites may feature modern amenities and elegant furnishings.
        The hotel likely has dining options, and it may offer a mix of local and international cuisine.
        Some boutique hotels in Siem Reap, like Shinta Mani Shack, often emphasize personalized and 
        high-quality dining experiences.
        Facilities may include a swimming pool, spa, and fitness center.
        The hotel might provide additional services such as guided tours, transportation arrangements, 
        and concierge services.
        Shinta Mani Foundation, associated with Shinta Mani Shack, is known for its philanthropic 
        efforts in supporting education, 
        healthcare, and small business opportunities in Cambodia.
        ''',
      }
    ]
  },
  {
    'id': 208,
    'name': 'Anantara Angkor Resort - Siem Reap',
    'image': 'https://secure.s.forbestravelguide.com/img/properties/anantara-angkor-resort/extra-large/anantara-angkor-resort-pool-wide.jpg',
    'detail': [
      {
        'image': 'https://secure.s.forbestravelguide.com/img/properties/anantara-angkor-resort/extra-large/anantara-angkor-resort-pool-wide.jpg',
        'description': '''
        Anantara Angkor Resort is an award-winning luxury hotel with spacious suites with butler service 
        and free WiFi. Featuring gardens set amidst fountains, it offers a fitness centre and an outdoor pool.
        Situated close to the Cambodian Cultural Village and the temples of Angkor, Anantara Angkor Resort 
        is a 10-minute drive from Siem Reap International Airport.
        Fitted with parquet floors, rooms at  Anantara Angkor Resort feature a lounge area with day beds. 
        Private bathrooms are equipped with marble baths. Each room is also equipped with a flat-screen 
        TV and minibar.
        Both local and Western dishes are available at the hotel. Chi Restaurant & Bar offers two 
        wine cellars and progressive menu. L Lounge features a variety of drinks and cigars. For book-lovers, 
        Sastra is well-stocked with both fiction and non-fiction reads. 24-hour room service is also provided.
        Massages and body treatments can be enjoyed at Anantara Spa or in the King Suite. Guests can also 
        take a dip in the hot tub or relax at the sauna. Alternatively, they can arrange for an acupuncture 
        session or make travel arrangements at the reception.
        ''',
      }
    ]
  },
  {
    'id': 209,
    'name': 'Rosewood Phnom Penh - Phnom Penh',
    'images': 'https://th.bing.com/th/id/R.e868987f88765c0394c5e90e6a356fca?rik=mZNCEl3PIphjkw&pid=ImgRaw&r=0',
    'detail': [
      {
        'images': 'https://th.bing.com/th/id/R.e868987f88765c0394c5e90e6a356fca?rik=mZNCEl3PIphjkw&pid=ImgRaw&r=0',
        'description': '''
        Located in Phnom Penh, adjacent to Vattanac Capital Mall, Rosewood Phnom Penh features 
        175 rooms and suites, 4 on-site restaurants, a lounge and the skybar, Sora. Located around 
        500 m from Wat Phnom, the hotel is also 901 m away from Riverfront Park. The accommodations 
        offers a 24-hour front desk and currency exchange for guests.
        At the hotel, each room is equipped with a wardrobe, a flat-screen TV and a private bathroom. 
        Rosewood Phnom Penh provides some units with river views, and all rooms are fitted with a coffee machine.
        Buffet and à la carte breakfast options are available daily at the accommodations. 
        There are four in-house restaurants, which serve a variety of Cambodian, French, Chinese 
        and Western dishes.
        Sisowath Quay is a 17-minute walk from Rosewood Phnom Penh, while Royal Palace 
        Phnom Penh is 1.1 mi from the property. The nearest airport is Phnom Penh International 
        Airport, 5 mi from the hotel.
        Couples particularly like the location — they rated it 9.5 for a two-person trip.
        ''',
      }
    ]
  }
]

def get_hotel_information():
  return jsonify(hotel_information)