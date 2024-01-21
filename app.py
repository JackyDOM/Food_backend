from flask import Flask, jsonify
from flask_cors import CORS


app = Flask(__name__)
CORS(app)

# Sample data
food_provinces = [
    {
        'id': 1,
        'name': 'ខេត្ត មណ្ខលគីរី',
        'image': 'https://th.bing.com/th/id/R.bf1b728468beeb327831ec95c6413ecc?rik=jmRj7XgjSEv8Bw&pid=ImgRaw&r=0',
        'detail': [
            {
                'namey': 'ម្ហូប ស៊ុបគោ',
                'imagey': 'https://media.tacdn.com/media/attractions-splice-spp-720x480/0a/9f/8c/cc.jpg',
                'information': [
                    {
                        'images': 'https://media.tacdn.com/media/attractions-splice-spp-720x480/0a/9f/8c/cc.jpg',
                        'ingredient': '''
                        Rice: A staple in Cambodian meals.\n
                        Fish: Cambodian cuisine often includes fish, either freshwater or marine fish.\n
                        Vegetables: Various vegetables like lemongrass, galangal, kaffir lime leaves,\n
                        and different herbs are used to add flavor to dishes.\n
                        Rice Noodles: Rice noodles are commonly used in soups and stir-fried dishes.\n
                        Coconut Milk: Used in curries and desserts for a rich and creamy flavor.\n
                        Chilies: Add spice to many Cambodian dishes.\n
                        Palm Sugar: Commonly used as a sweetener in Cambodian cuisine.\n
                        Fish Sauce: A fundamental ingredient in Cambodian cooking for umami flavor.\n
                        Lime or Tamarind Juice: Used for sourness in various dishes.\n
                        Garlic and Shallots: These aromatics are often used for flavoring.'''
                    }
                ]
            },
            {
                'namey': 'ម្ហូប បាយពងទាចៀន',
                'imagey': 'https://i.pinimg.com/originals/24/a3/84/24a38408ea9ac1f40dc0f962fb28cb4f.jpg',
                'information': [
                    {
                        'images': 'https://i.pinimg.com/originals/24/a3/84/24a38408ea9ac1f40dc0f962fb28cb4f.jpg',
                        'ingredient': '''
                        Rice: A staple in Cambodian meals.\n
                        Eggs: Depend on you want.\n
                        Fish source: To make our dish good.\n
                        Vegetables: Galic leaves, white Galic, Carrot, Beans,..etc.\n
                        Meats: Chicken, Suasage, Beef, or Pork.\n
                        Pepper, Chilli, Salt, Sugar, and a little bit of water.\n
                        '''
                    }
                ]
            },
            {
                'namey': 'ម្ហូប ប្រហិតចៀនជាមួយទឹកម្ទេស',
                'imagey': 'https://i.pinimg.com/originals/55/cc/42/55cc425bf5c1a1ce8aaf3e69d30034d7.jpg',
                'information': [
                    {
                        'images': 'https://i.pinimg.com/originals/24/a3/84/24a38408ea9ac1f40dc0f962fb28cb4f.jpg',
                        'ingredient': '''
                        ប្រហិតគ្រប់មុខ ឬក៍ប្រភេទណាក័បាន,\n
                        មានទឹកម្ទេស យើងអាចធើ្វក៍បាន ឬ\n
                        ក៍យើងអាចទិញពីផ្សារក៏បានដែរ,\n
                        បន្លែមានដូចជា: ត្រសក់, ម្រះ, ការ៉ុត, ...etc.
                        '''
                    }
                ]
            },
        ],
    },
    {
        'id': 2,
        'name': 'ខេត្ត​តាកែវ',
        'image': 'https://th.bing.com/th/id/OIP.D8t9RuoiQSb8_fBNLf4DegHaE9?rs=1&pid=ImgDetMain',
        'detail': [
            {
                'namey': 'ម្ហូប បង្កងអាំង',
                'imagey': 'https://th.bing.com/th/id/OIP.8LOGrw9Okr3UcUnqkEb01QHaE8?rs=1&pid=ImgDetMain',
                'information': [
                    {
                        'images': 'https://th.bing.com/th/id/OIP.8LOGrw9Okr3UcUnqkEb01QHaE8?rs=1&pid=ImgDetMain',
                        'ingredient': '''
                        បង្កង ម្ទេស ស្ករស អំបិល ក្រូចឆ្មារ ខ្ទឹមស
                        ''',
                        'Step': '''
                        ១- បង្កងស្រស់ ៥០០ក្រាម , ម្ទេសខ្មាំង ២ស្លាបព្រាបាយ, ខ្ទឹមស ១ស្លាបព្រាបាយ,\n
                        ស្ករត្នោត ១ស្លាបព្រាកាហ្វេ, អំបិលម៉ត់ ១ស្លាបព្រាកាហ្វេ, ទឹកក្រូចឆ្មារ ២ស្លាបព្រាបាយ។
                        ២-លាងបង្កងអោយស្អាត ដោយជាមួយឈើចុងស្រួច អាំងអោយឆ្អិនល្ម​ម ទុកមួយអន្លើ
                        ៣- ធ្វើទឹកជ្រលក់ ដោយយកម្ទេសខ្មាំង នឹងខ្ទឹមស បុកលាយគ្នាអោយម៉ត់ បន្ទាប់មក ផ្សំរសជាតិ\n
                        ដោយស្ករត្នោត អំបិលម៉ត់ និងទឹកក្រូចឆ្មារ ភ្លក្សមើលអោយត្រូវមាត់ ជាការស្រេច ។
                        '''
                    }
                ]
            },
            {
                'namey': 'ម្ហូប មីឆាសាច់គោ',
                'imagey': 'https://th.bing.com/th/id/OIP.-bBggS7IUUmViEpxhOcAlAHaEK?rs=1&pid=ImgDetMain',
                'information': [
                    {
                        'images': 'https://th.bing.com/th/id/OIP.-bBggS7IUUmViEpxhOcAlAHaEK?rs=1&pid=ImgDetMain',
                        'ingredient': '''
                        - សាច់គោ ៣០០ក្រាមហាន់ស្តើងៗ
                        - មីសសៃមូល ២៥០ក្រាម
                        - ខ្ញី, ខ្ទឹមស ២ស្លាបព្រាបាយ(ចិញ្ច្រាំ)
                        - ស្លឹកខ្ទឹម ២ដើមហាន់
                        - ការ៉ុត ចិតចំណិតវែង, ផ្សិត ចិតចំណិត, សណ្តែកគួរ កាត់ ២ថ្នាំងដៃ ១មុខបន្តិច
                        - ទឹកស៊ីអ៊ីវ ២ស្លាបព្រាបាយ
                        - ប្រេងល្ង ១ស្លាបព្រាបាយ
                        - ទឹកខ្មេះ កន្លះស្លាបព្រាបាយ
                        - ស្ករស កន្លះស្លាបព្រាបាយ
                        - ម្សៅមី ១ស្លាបព្រាកាហ្វេ
                        - ប្រេងឆា ២ស្លាបព្រាបាយ
                        ''',
                        'Step': '''
                        ១. មុន​ដំ​​បូង​យក​សាច់​គោ​មក​​ប្រឡាក់​​ជា​មួយ​​ទឹក​ស៊ីអ៊ីវ ១ស្លាបព្រាបាយ និងម្សៅ​មី​ ១ស្លាបព្រាកាហ្វេ​ឲ្យ​បាន​សព្វ។
                        ២. យក​ទឹក​ កន្លះ​កូន​ចាន​មក​លាយ​ជា​មួយ ទឹកស៊ីអ៊ីវ, ប្រេងល្ង, ទឹកខ្មេះ, ស្ករស និងម្សៅមី​​ កូរ​ចូល​គ្នា​ឲ្យ​សព្វ។
                        ៣.ដាក់​ប្រេងឆា​ចូល​ក្នុង​ខ្ទះ​ទុក​ឲ្យ​ក្តៅ​ដាក់​ខ្ញី​ចូល​ឆា​​ប្រហែល​ ១នាទី ចាំ​ដាក់​សាច់​គោ​ចូលឆា​ ២-៣នា​ទី​ទៀត​ដួស​ទុក​សិន​។
                        ៤. ដាក់​ប្រេង​ឆា​ចូល​ក្នុង​ខ្ទះ​ម្តង​ទៀត​រួច​បំពងខ្ទឹម​ស​​ឲ្យ​ឈ្ងុយ ទើបដាក់​ការ៉ុត សណ្តែកគួរ​ និង\n
                        ​ផ្សិតឆា​ឲ្យ​បន្លែរាង​ស្រពាប់​ដាក់​គ្រឿង​ផ្សំ​​នៅក្នុង​កូន​ចាន​ចូល។
                        ៥. ទុក​ប្រហែល​ ២-៣នាទី​ដាក់​មី ​ឆា​ចូល​​គ្នា​បន្តិច​សិន​ចាំដាក់​សាច់​គោ​ដែល​ឆា​ម្តងរួច​ហើយ​\n
                        ឆា​ចូល​គ្នា​ទាំង​អស់​រួច​ដាក់​ស្លឹក​ខ្ទឹម​ចុងក្រោយ​ជាការ​ស្រេច៕
                        '''
                    }
                ]
            },
            {
                'namey': 'ម្ហូប លតឆាសាច់គោ',
                'imagey': 'https://th.bing.com/th/id/OIP.-U0XRJIQuKAk6COQCYVpmwHaEK?rs=1&pid=ImgDetMain',
                'information': [
                    {
                        'images': 'https://th.bing.com/th/id/OIP.-bBggS7IUUmViEpxhOcAlAHaEK?rs=1&pid=ImgDetMain',
                        'ingredient': '''
                        -សាច់គោ ២០០ក្រាម ហាន់បន្ទះស្តើងៗ
                        -ស៊ុត ១គ្រាប់ ចៀនឆ្អិន
                        -លត ១ចានគោមតូចល្មម
                        -ខាត់ណា ២ដើម ហាន់បន្ទះស្តើងៗ
                        -ផ្កាគូឆាយ ២៥ក្រាមកាត់ ២ថ្នាំងដៃ
                        -សណ្តែកបណ្តុះ ២៥ក្រាម
                        -ទឹកស៊ីអ៊ីវខាប់ ១ស្លាបព្រាបាយ
                        -ស្ករស កន្លះស្លាបព្រាកាហ្វេ
                        -ខ្ទឹមសចិញ្ច្រាំ ១ស្លាបព្រាបាយ
                        -ប្រេងឆា ២
                        -៤ស្លាបព្រាបាយ
                        ''',
                        'Step': '''
                        -ដំបូងដាក់ប្រេងឆាចូលក្នុងខ្ទះដាក់ភ្លើងឱ្យក្តៅ ដាក់ខ្ទឹមសចូលឆាឱ្យឈ្ងុយដាក់សាច់គោ\n
                        ចូលឆាត្រឡប់បន្តិចដាក់ទឹកស៊ីអ៊ីវខាប់ និងស្ករសឆាឱ្យរាងឆ្អិនល្មម។
                        -បន្ទាប់មកដាក់លតចូលឆាវាជាមួយសាច់គោបន្តិចសិន រួចហើយចាំដាក់ ខាត់ណា, ផ្កាគូឆាយ\n
                        និងសណ្តែកបណ្តុះ ឆាឱ្យបន្លែឆ្អិនតាមការចូលចិត្តរួចដួសដាក់ក្នុងចាន។បន្ទាប់មកទៀតយកស៊ុតមកដាក់ចៀនឱ្យឆ្អិន\n
                        រួចហើយដួសដាក់ពីលើចានលតឆាជាការស្រេច៕
                        ''',
                    }
                ]
            },
        ],
    },
    {
        'id': 3,
        'name': 'ខេត្ត កណ្តាល',
        'image': 'https://th.bing.com/th/id/R.50be05010cd5bda403018a15846f0314?rik=lfYtBGFACzTe5A&riu=http%3a%2f%2fwww.soprita.com%2fwp-content%2fuploads%2f2021%2f04%2f1680-840-Kandal-01.png&ehk=RkhYJh9QKUhNCKlocTUwKHbGSFAhD0VJ7ZUur1lz%2f14%3d&risl=&pid=ImgRaw&r=0',
        'detail': [
            {
                'namey': 'ម្ហូប កណ្តុរអាំង',
                'imagey': 'https://th.bing.com/th/id/OIP.NMpNvJNZ5sm8_KkI7L2A-AHaEK?rs=1&pid=ImgDetMain',
                'information': [
                    {
                        'images': 'https://th.bing.com/th/id/OIP.NMpNvJNZ5sm8_KkI7L2A-AHaEK?rs=1&pid=ImgDetMain',
                        'ingredient': '''
                        ១. យើងមានកណ្តុរអាស្រ័យទៅលើចំនួនយើងហូប\n
                        ២. បន្ទាប់មកយើងមានគ្រឿងផ្សំដូចជា: ម្រេច អំបិល គល់ស្លឹកគ្រៃ ស្ករស ស្លឹកក្រូចជាដើម និងកូចឆ្មារ។
                        ''',
                        'Step': '''
                        ១. យើងត្រូវសម្អាតកណ្តុរអោយស្អាត ហើយយើងត្រូវបង្កាត់ភ្លើង\n
                        ដើម្បីអាំងកណ្តុរដែលយើងបានធើ្វ។
                        ២. ចំពោះទឹកជ្រលក់យើងមានម្រេច បន្ទាប់មកច្របាត់ក្រូចឆ្មាចូលជាការស្រេច។
                        '''
                    }
                ]
            },
            {
                'namey': 'ម្ហូប សាច់គោអាំង',
                'imagey': 'https://th.bing.com/th/id/OIP.NLBxclVsqDInfp170YDreQHaFa?rs=1&pid=ImgDetMain',
                'information': [
                    {
                        'images': 'https://th.bing.com/th/id/OIP.NLBxclVsqDInfp170YDreQHaFa?rs=1&pid=ImgDetMain',
                        'ingredient': '''
                        - សាច់គោល្អ ឬសាច់ជាប់ខ្លាញ់ តាមចំណង់អ្នកបរិភោគ\n
                        -​ម្ទេសក្រហម ( សម្រាប់អ្នកមិនចេះហិរមិនបាច់ដាក់ក៏បាន )\n 
                        - គល់ស្លឹកគ្រៃ\n
                        - រំដេង\n
                        - ខ្ជាយ \n
                        - សំបកក្រូចសើច\n
                        - ខ្ទឹមស\n
                        - ខ្ទឹមក្រហម\n
                        - សណ្តែកដីលីង\n
                        - ស្ករស ឬ ស្ករត្នោត\n
                        - គ្រឿងការី\n
                        - សាច់ដូងទុំ\n
                        - អំបិល ទឹកត្រី\n
                        - ម៉្សៅស៊ុប\n
                        - ល្ហុងចាស់\n
                        - ត្រសក់\n
                        - ការ៉ុត\n
                        - ទឹកខ្មេះ\n
                        ''',
                        'Step': '''
                        - យកសាច់គោហាន់ជាបន្ទះស្តើងៗល្មមហើយទុកមួយអន្លើរសិន
                        - យកគ្រឿង គល់ស្លឹកគ្រៃ រំដេង ខ្ជាយ សំបកក្រូចសើច ខ្ទឹមស ខ្ទឹមក្រហម\n
                        គ្រឿងការី អំបិល បុកចូលគ្នាអោយម៉ដ្ឋ -យកសាច់ដូងទុំពូតយកទឹកដើម
                        - យកសណ្តែកដីលីងបុកតែកុំអោយល្អិតពេក
                        - យកគ្រឿងដែលបុកហើយ និងសណ្តែកដី ដាក់លាយចូលគ្នាហើយថែមម៉្សៅស៊ុប\n
                        ទឹកត្រី អោយល្មមទើបយកសាច់គោមកប្រលាក់ជាមួយគ្រឿងអោយសព្វរួចយកមកដោតឈើចង្កាក់ហើយដាក់អាំងជាការស្រេច ។

                        *វិធីធ្វើជ្រក់
                        -  យកល្ហុង ការ៉ុត ត្រសក់មកឈូសជាសសៃ ហើយដាក់ស្ករ អំបិល ទឹកខ្មេះ ផ្អាប់វារវាងប្រាំម៉ោងទើបអាចទទួលទានបាន ។
                        '''
                    }
                ]
            },
             {
                'namey': 'ម្ហូប បាយឆា',
                'imagey': 'https://hilltopcambodia.com/wp-content/uploads/2020/09/MONDULKIRI-FRIED-RICE.jpeg',
                'information': [
                    {
                        'images': 'https://hilltopcambodia.com/wp-content/uploads/2020/09/MONDULKIRI-FRIED-RICE.jpeg',
                        'ingredient': '''
                        - បង្គាបកសំបកវះយកអាចម៍ខ្នងចេញ\n
                        - មឹកកាត់វាកង់ៗ\n
                        - ខ្ទឹមសចិញ្ច្រាំ\n
                        - ទឹកប្រេងខ្ចង\n
                        - ទឹកត្រី & ប៊ីចេង & ស្ករស\n
                        - ពងទា ឬពងមាន់\n
                        - បាយស\n
                        - អាចដាក់បន្លែក៏បានដូចជា សណ្តែកគួរហាន់កង់ខ្លីៗ ការ៉ុតហាន់ដុំតូចៗ ពោត……\n
                        ''',
                        'Step': '''
                        1. ដាក់ខ្ទះ ដាក់ប្រេងឆាពេលខ្ទះក្តៅដោយបើកភ្លើងតិចៗ ដាក់ខ្ទឹមស គ្រឿងសមុទ្រ ឆា២-៣ត្រឡប់\n
                        ដាក់ទឹកប្រេងខ្ចង ទឹកត្រីបន្តិចបានហើយ ស្ករស ប៊ីចេង (ឆាវាចូលគ្នា)។
                        2. ដាក់ពងទាចូល( កុំទាន់អាលឆាចាំអោយពងទាឆ្អិនបន្តិចចាំឆាដើម្បីអោយពងទារៀងដុំបន្តិច)។
                        3. ដាក់បន្លែ (ឆា២-៣ត្រឡប់) ដាក់បាយសចូល ឆាវាចូលគ្នាអោយបាយរៀងក្រៀមស្ងួតបន្តិច\n
                        រួចភ្លក់មើល ហើយរោយស្លឹកខ្ទឹមពីលើជាការស្រេច។
                        '''
                    }
                ]
            },
        ],
    },
    {
        'id': 4,
        'name': 'ខេត្ត កំពត',
        'image': 'https://th.bing.com/th/id/OIP.yfA7tJ8J1UfjV_gvI4uWjAHaFj?rs=1&pid=ImgDetMain',
        'detail': [
            {
                'namey': 'ម្ហូប មឹកអាំង',
                'imagey': 'https://th.bing.com/th/id/OIP.dNanhn4piykyfcmPisrXbAHaEK?rs=1&pid=ImgDetMain',
                'information': [
                    {
                        'images': 'https://th.bing.com/th/id/OIP.dNanhn4piykyfcmPisrXbAHaEK?rs=1&pid=ImgDetMain',
                        'ingredient': '''
                        1-មឹកធំ 1ក្បាល\n
                        2-ទឹកស៊ីអ៊ីវជប៉ុន(shoyu) 4ស្លាបព្រាបាយ\n
                        3-ទឹកស៊ីអ៊ីវខាប់ 2ស្លាបព្រាបាយ\n
                        4-ទឹកមីរិន(Milin sausce) 2ស្លាបព្រាបាយ\n 
                        5-ស្ករស 1ស្លាបព្រាបាយកន្លះ\n
                        ''',
                        'Step': '''
                        1-លាងមឹកឲ្យស្អាត​ខ្វះយកគ្រឿងក្នុងចេញ\n
                        2-ផ្សំទឹកស៊ីអ៊ីវ-ទឹកស៊ីអ៊ីវខាប់-មីរិន-ស្ករស កូរឲ្យរលាយចូលគ្នាទុកមួយឡែក\n 
                        3-យកមឹកមកត្រាំជាមួយទឹកស៊ីអ៊ីវផ្សំ ផ្អាប់ទុក10-15នាទី\n
                        4-យកមឹកមកអាំងដោយលាបទឹកស៊ីអ៊ីវផ្សំឲ្យបានញឹកញាប់រហូតឆ្អិនល្អ\n 
                        5-រៀបមឹកដាក់ចាន រួចយកទឹកស៊ីអ៊ីវផ្សំនៅសល់ទៅចំអិនដាក់ស្ករថែម​ រួចយកទៅស្រោចពីលើមឹកជាការស្រេច។\n
                        ''',
                    }
                ]
            },
            {
                'namey': 'ម្ហូប ក្តាមឆា',
                'imagey': 'https://i.pinimg.com/originals/df/d5/f8/dfd5f87e6df96826c9758efcc5b67c3d.jpg',
                'information': [
                    {
                        'images': 'https://i.pinimg.com/originals/df/d5/f8/dfd5f87e6df96826c9758efcc5b67c3d.jpg',
                        'ingredient': '''
                        - ក្ដាម​ថ្ម 2ក្បាល\n
                        - ទឹម​ក្រហម 3មើម\n
                        - ម្សៅ​ឆា 1ស្លាបព្រាកាហ្វេ\n
                        - ទឹក​ដោះ​គោសុទ្ធ 4ពែងរង្វាល់ ប្រហែលកន្លះចានចង្កឹះ\n
                        - ស៊ុត​មាន់ 1\n
                        - ទឹក​ស៊ុប 1ចានចង្កឹះ ឬប្រើទឹកដោះគោជំនួសក៏បាន\n
                        - ទឹក​ការី​ខាប់\n
                        - ម្ទេស​ម៉ដ្ឋ 1លស្លាបព្រាកាហ្វេ\n
                        - ខ្ទឹម​បារាំង 1ផ្លែ\n
                        - ការ៉ុត 1មើម\n
                        - ប៉េងប៉ោះ 2ផ្លែ\n
                        - ស្ករ 1ស្លាបព្រាបាយ\n
                        - អំបិល 1ស្លាបព្រាកាហ្វេ\n
                        - ម្សៅស៊ុប 1ស្លាបព្រាកាហ្វេ\n
                        - ប្រេងខ្យង 1ស្លាបព្រាបាយ\n
                        ''',
                        'Step': '''
                        1. យក​ក្ដាម​ថ្ម​មក កាត់​ដង្កៀបហើយដំអោយបែក និង​កាត់សាច់ជាដុំៗ ។ រួច​ប្រឡាក់​ជាមួយ​ម្សៅ​ឆា\n
                        2. និង​អំបិល បន្ទាប់​មក​ដាក់​​បំពង​នៅ​ក្នុង​ឆ្នាំ​ខ្ទះ​ដែល​មាន​ប្រេងកំពុងពុះ ដោយ​ដាក់​ភ្លើង​ឲ្យ​ក្ដៅ​ខ្លាំង​ ប្រែទៅប្រែមក រួច​ស្រង់​ចេញ។\n
                        3. ដាក់​ខ្ទឹម​ស ម្ទេស​ម៉ដ្ឋ ខ្ទឹម​ក្រហម និង​ទឹក​ការី​ចូល​ទៅ​ក្នុង​ខ្ទះថ្មីមួយ ដើម្បី​បំពង​ឲ្យ​បាន​ឈ្ងុយ\n
                        4. រួច​ចាក់​ទឹក​ស៊ុប និង​សាច់​ក្ដាម​ចូល​រំងាស់ ដាក់គ្រឿងផ្សំចូល។ ភ្លក្សរសជាតិតាមចំនូលចិត្តរួច រំងាស់បន្តិចដើម្បីឲ្យ​ដាច់​ទឹក\n
                        5. ចុង​ក្រោយ​បង្អស់ ចាក់​ទឹក​ដោះ​គោ​សុទ្ធ​ចូល បន្ទាប់​មក​ចាក់ពងមាន់​ចូលទៀត ឆាប្រហែល2នាទីរួចរោយស្លឹកខ្ទឹមឬជីវ៉ាន់ស៊ុយក៏បាន\n
                        6. មុខម្ហូបមួយមុខនេះរួចរាល់ហើយ សូមទទួលទានដោយរីករាយ\n
                        ''',
                    }
                ]
            },
            {
                'namey': 'ម្ហូប គ្រឿងសមុទ្រក្រឡុក',
                'imagey': 'https://th.bing.com/th/id/OIP.vxN4mFTgrnIsMAiHCgYtoQHaEK?rs=1&pid=ImgDetMain',
                'information': [
                    {
                        'images': 'https://th.bing.com/th/id/OIP.vxN4mFTgrnIsMAiHCgYtoQHaEK?rs=1&pid=ImgDetMain',
                        'ingredient': '''
                        - គ្រឿងសមុទ្រគ្រប់ប្រភេទតាមចំនូលចិត្ត ក្តាម មឹក បង្គា លាស ងាវ បង្កងប៉ាក\n
                        - ហតដក\n
                        - ម្ទេសស្រស់ ម្ទេសក្រៀម\n
                        - ម្ទេសកូរ៉េ មានម្ទេសទឹក ម្ទេសហុយ\n
                        - ពោត ឬបន្លែផ្សេងទៀតតាមចំនូលចិត្ត\n
                        - ស្ករ អំបិល ទឹកត្រី ម្សៅស៊ុប ប្រេងខ្យង\n
                        - ទឹកដោះគោឆៅ\n
                        ''',
                        'Step': '''
                        1. បន្លែនឹងសាច់ត្រូវលាងអោយស្អាតជាមុនសិន ពោតត្រូ​វចំហុយអោយឆ្អិន\n
                        2. ខ្ទឹមបុកលាយជាមួយម្ទេសស្រស់អោយម៉ត់\n
                        3. ដាក់ខ្ទះអោយក្តៅ រួចហើយបំពង់ខ្ទឹមបុកអោយឆ្ងុយទើបដាក់ម្ទេសកូរ៉េទាំង2មុខចូល\n 
                        4. ម្ទេសហុយ1ស្លាបព្រាបាយ ម្ទេសទឹក2ស្លាបព្រាបាយ ឬលើសនេះតាមចំនូលចិត្ត\n
                        5. រួចដាក់ស្ករ ទឹកត្រី អំបិល ម្សៅស៊ុប ប្រេងខ្យង នឹងទឹកដោះគោឆៅចូល កូរអោយសព្វរួចភ្លក្សរសជាតិ\n
                        តាមការចូលចិត្តទើបដាក់ពោត ហតដក នឹងគ្រឿងសមុទ្រគ្រប់មុខចូល\n
                        6. រួចរាល់ហើយ បើសិនជាចូលចិត្តមី អាចដាក់ស្ពាហ្គាទីចូលទៀតក៏បាន\n
                        '''
                    }
                ]
            },
        ]
    },
    {
        'id': 5,
        'name': 'ខេត្ត សៀមរាប',
        'image': 'https://th.bing.com/th/id/OIP.OcvIfYmnX_tVMrqAaMSYjwHaE_?rs=1&pid=ImgDetMain',
        'detail': [
            {
                'namey': 'ម្ហូប អាម៉ុក',
                'imagey': 'https://image.cookly.me/images/Siem-Reap-Food-Amok.cover.jpg',
                'information': [
                    {
                        'images': 'https://image.cookly.me/images/Siem-Reap-Food-Amok.cover.jpg',
                        'ingredient': '''
                        - ខ្យង 1 គីឡូក្រាម\n
                        - សាច់ជ្រូកបីជាន់ 1 ខាំ\n
                        - សណ្ដែកដី ម្ទេសឆ្អើរ ខ្ទិះដូង\n
                        - គ្រឿងបុក (រំដេង រមៀត ស្លឹកគ្រៃហាន់)\n
                        - កាពិ\n
                        - ប្រេងខ្យង\n
                        - គ្រាប់ជម្ពូឆាយកខ្ទិះ\n
                        - ស្លឹកកន្ទួត\n
                        - ស្លឹកក្រូចសើច\n
                        - ពង់មាន់\n
                        ''',
                        'Step': '''
                        1. យកសាច់ខ្យងចេញពី សំបករបស់វា ប៉ុន្តែត្រូវរក្សាសំបកទាំងនោះទុក កុំចោល។\n
                        2. ចិញ្ច្រាំសាច់ជ្រូក និងហាន់សាច់ខ្យងជាចំណិតតូចៗ។\n
                        3. បន្ទាប់មកយកសាច់ជ្រូកចិញ្ច្រាំនិងសាច់ខ្យងហាន់រួចនោះទៅឆាចូលគ្នាជាមួយនឹងគ្រឿងបុក, ម្ទេសឆ្អើរ, និងកាពិ រហូតដល់ឆ្អិនល្អ។\n
                        4. ជំហានបន្ទាប់ ត្រូវយកស្លឹកកន្ទួតទៅទ្រាប់សាច់ដែលឆាជាមួយគ្រឿងអម្បាញ់មិញ\n
                        5. រួចហើយយកទៅញាត់ចូលក្នុងសំបកខ្យងដែលរក្សាទុកនោះ។\n
                        6. ជំហានបន្ទាប់ ត្រូវចាក់ទឹកខ្ទិះដែលឆាបញ្ចូលគ្នាជាមួយពងមាន់ ម្ទេស និងស្លឹក ក្រូចសើច ទៅស្រោចពីលើខ្យង\n 
                        7. ដែលមានញាត់សាច់ទ្រាប់ស្លឹកកន្ទួតនោះ រួចហើយយកវាទៅចំហុយ ប្រហែលជា១៥នាទីទៀត ទើបរួចរាល់៕\n
                        ''',
                    }
                ]  
            },
            {
                'namey': 'ម្ហូប ការីខ្មែរ',
                'imagey': 'https://th.bing.com/th/id/OIP.Y9aE-WKX8CeN_QOkRGDSlgHaE7?rs=1&pid=ImgDetMain',
                'information': [
                    {
                        'images': 'https://th.bing.com/th/id/OIP.Y9aE-WKX8CeN_QOkRGDSlgHaE7?rs=1&pid=ImgDetMain',
                        'ingredient': '''
                        - មាន់ធំ 1ក្បាល ឆ្អឹងជំនីជ្រូក 1គីឡូ\n
                        - គ្រឿងបុក(ស្លឹកគ្រៃ រមៀត ខ្ជាយ រំដេង ខ្ទឹមស ខ្ទឹមក្រហម សម្បកក្រូចសើច) 1ត្បាល់ ប្រហែល1ចានចង្កឹះ\n
                        - គ្រឿងការីគ្រប់មុខ(ផ្កាចាន់ ឈើអែម ម្សៅការី ប្រេងគ្រាប់ការីក្រហម) មួយមុខបន្តិចៗ\n
                        - ម្ទេសឆ្អើរចិញ្ច្រាំ ប្រហែលកន្លះចានចង្កឹះ\n
                        - ស្លឹកក្រូចសើច 5-6សន្លឹក\n
                        - កាពិឆៅ 1ស្លាបព្រាបាយ\n
                        - ខ្ទិះដូងដើម 300g ឬប្រើដូង1ផ្លែ ឬមួយចំហៀងតាមចំនូលចិត្ត\n
                        - បន្លែការីគ្រប់មុខ(ដំឡូងបារាំង ឬដំឡូងជ្វា ខ្ទឹមបារាំង សណ្តែកកួរ ត្រប់វែង)មួយមុខបន្តិច\n
                        - សណ្តែកដីលីង (មិនដាក់ក៏បាន)\n
                        - អំបិល កន្លះស្លាបព្រាបាយ\n
                        - ទឹកត្រី 3ស្លាបព្រាបាយ\n
                        - ស្ករត្នោត4-5 ស្លាបព្រាបាយ\n
                        - ប្រេងខ្យង 2-3ស្លាបព្រាកាហ្វេ\n
                        - ម្សៅស៊ុប 1ស្លាបព្រាបាយ\n
                        - ទឹកធម្មតា 2លីត្រ ឬប្រើខ្ទិះដូងចុងជំនួសក៏បាន\n
                        ''',
                        'Step': '''
                        1. សាច់និងបន្លែលាងទឹកអោយស្អាត។ សាច់កាប់ជាដុំៗ ចំណែកបន្លែវិញកុំហាន់តូចពេក\n 
                        ព្រោះវានឹងរលួយអស់ តំឡូងកាប់ធំៗល្មម រួចទុកមួយឡែកសិន\n
                        2. ចំពោះដូងបងប្អូនប្រើមួយផ្លែក៏បានបើសិនជាចូលចិត្តញ៉ាំសម្លបែបចាស់គ្រឿង តែបើដាក់ខ្ទិះច្រើនឆ្ងាញ់ខ្លាំងណាស់។\n 
                        ដូង1ពូតយកទឹកតែ2ទេ ខ្ទិះដើមយកខ្ទិះសុទ្ធ​។ រូចហើយច្របាច់ខ្ទិះបន្ទាប់ដាក់ទឹកប្រហែល2លីត្រ។\n
                        ច្របាច់2-3ដងក៏បានដើម្បីអោយអស់ខ្ទិះ (កុំភ្លេចត្រូវប្រទឹកក្តោអ៊ុនៗ)\n
                        3. ផ្កាចាន់នឹងឈើឯមត្រូវលីងអោយឈ្ងុយជាមុនសិន\n
                        4. ដាំឆ្នាំងឲ្យក្តៅ ចាក់ខ្ទិះដូងដើមចូល កូរវាអោយឈ្ងុយហើយឡើងប្រេង ទើបដាក់កាពិមួយស្លាបព្រាបាយចូល\n 
                        កូរវាអោយរលាយសព្វសាច់ជាមួយខ្ទិះដូង រួចដាក់ស្ករត្នោតចូល។ កូរអោយស្ករត្នោតឡើងក្រហមជើងអង្ក្រង\n
                        5. បន្ទាប់មកត្រូវចាក់គ្រឿងបុក ស្លឹកក្រូចសើច គ្រឿងការីនឹងផ្កាចាន់ដែលយើងលីងហើយចូល គូរវាអោយសព្វបើស្ងួតឆ្នាំង\n
                        ពេកថែមខ្ទិះចុងចូលបន្តិច កុំអោយវាខ្លោច។ កូរវាអោយពុះហើយឈ្ងុយ\n
                        6. ដាក់គ្រឿងផ្សំចូលមានដូចជា ទឹកត្រី ម្សៅស៊ុប ប្រេងខ្យង នឹងអំបិល កូរអោយសព្វហើយមានក្លិនឈ្ងុយ\n
                        7. ភ្លក្សរសជាតិតាមចំនូលចិត្ត តែសម្លការីត្រូវប្រើគ្រឿងអោយចាស់ទើបឆ្ងាញ់\n
                        8. ទើបចាក់សាច់ចូលតាមក្រោយ កូរសាច់អោយសព្វជាមួយគ្រឿង រំងាស់ប្រហែល 15-20នាទីសិន\n 
                        ទើបចាក់ខ្ទិះដូងទីពីរចូលអោយល្មមលិចសាច់ (ថែមទឹកម្តងពីរដង)។ មើលតែសាច់ល្មមផុយហើយទើបយើងចាក់តំឡូងជ្វានឹងតំឡូងបារាំងចូល\n
                        9. រំងាស់តំឡូងប្រហែល 5នាទីសិន មុនដាក់ខ្ទឹមបារាំង សណ្តែកគួរ នឹងត្រប់ចូល រំងាស់ថែម5នាទីទៀតជាការស្រេច\n
                        10. ស្លដាក់គ្រឿងអោយចាស់ហើយញ៉ាំជាមួយនំបញ្ចុកឬនំប៉័ងកាន់តែឆ្ងាញ់\n
                        ''',
                    }
                ]
            },
            {
                'namey': 'ម្ហូប នំបញ្ចុកខ្មែរ',
                'imagey': 'https://www.thidaskitchen.com/wp-content/uploads/2022/12/Nom-Banh-Chok.jpg',
                'information': [
                    {
                        'images': 'https://www.thidaskitchen.com/wp-content/uploads/2022/12/Nom-Banh-Chok.jpg',
                        'ingredient': '''
                        - ត្រីផ្ទក់ 1គីឡូ\n
                        - នំបញ្ចុក\n
                        - គល់ស្លឹកគ្រៃ ស្លឹកគ្រៃ រមៀត ខ្ចាយ រំដេង ស្លឹកក្រូចសើច ខ្ទឹមស ខ្ទឹមក្រហម\n
                        - ប្រហុក\n
                        - ស្ករ អំបិល ទឹកត្រី ម្សៅស៊ុប\n
                        - បន្លែគ្រប់មុខ តាមចំនូលចិត្ត\n
                        - ម្ទេសស្រស់ឬម្ទេសហុយ\n
                        ''',
                        'Step': '''
                        1. លាងត្រី នឹងបន្លែអោយស្អាតរួចទុកមួយឡែកសិន\n
                        2. ដាក់ដាំទឺកកន្លះឆ្នាំងដើម្បីស្ងោរត្រី ក្នុងទឹកត្រូវបង់ស្លឹកគ្រៃ 3-4សន្លឹក(បត់ចងវាអោយខ្លីហើយញីវាអោយចេញក្លិនឈ្ងុយ)\n 
                        ដាក់អំបិលនឹងស្ករបន្តិចផង ដើម្បីអោយសាច់ត្រីមានជាតិ\n
                        3. ដាក់ត្រីស្ងោរអោយឆ្អិន រួចស្រង់មកបេះយកតែសាច់\n
                        4. បុកគ្រឿងមានដូចជា គល់ស្លឹកគ្រៃ រមៀត ខ្ចាយ រំដេង ស្លឹកក្រូចសើច ខ្ទឹមស ខ្ទឹមក្រហម អោយម៉ត់\n
                        5. បន្ទាប់មកដាក់សាច់ត្រីដែលបេះហើយចូល\n
                        6. បុកសាច់ត្រីអោយម៉ត់ជាមួយគ្រឿង\n
                        7. យកទឹកដែលសល់ពីស្ងោរត្រីមកដាំអោយពុះម្តងទៀត (ថែមទឹកអោយល្មមសមជាមួយនំបញ្ចុក)\n
                        8. ពេលទឹកពុះដាក់ជ្រុំប្រហុក (ដាក់ប្រហុកអោយច្រើនបន្តិចទើបឆ្ងាញ់ខ្លាំងៗ)\n
                        9. ចុងក្រោយដាក់សាច់ត្រីដែលបុកជាមួយគ្រឿងចូល\n
                        10. ភ្លក្សរសជាតិតាមចំនូលចិត្ត រួចបិទភ្លើង (មិនចាំបាច់ទុកអោយពុះយូទេ)\n
                        11. បន្លែល្ហុង ត្រយ៉ូងចេក ត្រសក់ ស្លឹកល្ងៀង ផ្កាស្នោរ មិនគួរចោលទេ ដាក់បន្លែកាន់តែច្រើនកាន់តែឆ្ងាញ់\n
                        ''',
                    }
                ]
            },
        ]
    },
    {
        'id': 6,
        'name': 'ខេត្ត ស្វាយរៀង',
        'image': 'https://www.aboutcambodiatravel.com/uploads/images/content_image/Svay%20Rieng/Svay%20Rieng-ACT%20Cambodia%20Tours.jpg',
        'detail': [
            {
                'namey': 'ម្ហូប បុកល្ហុងគ្រឿងសមុទ្រ',
                'imagey': 'https://i.ytimg.com/vi/jibv2v8Y5NY/maxresdefault.jpg',
                'information': [
                    {
                        'images': 'https://i.ytimg.com/vi/jibv2v8Y5NY/maxresdefault.jpg',
                        'ingredient': 'WOW'
                    }
                ]  
            },
            {
                'namey': 'ម្ហូប ជ្រក់ជើងមាន់',
                'imagey': 'https://i.ytimg.com/vi/4RYpMfvK1S0/maxresdefault.jpg',
                'information': [
                    {
                        'images': 'https://i.ytimg.com/vi/4RYpMfvK1S0/maxresdefault.jpg',
                        'ingredient': 'WOW'
                    }
                ]  
            },
            {
                'namey': 'ម្ហូប ជ្រក់ជើងទា',
                'imagey': 'https://images.khmer24.co/22-08-02/235642---1659415332-41292179-b.jpg',
                'information': [
                    {
                        'images': 'https://images.khmer24.co/22-08-02/235642---1659415332-41292179-b.jpg',
                        'ingredient': 'WOW'
                    }
                ]  
            },
        ]
    },
    {
        'id': 7,
        'name': 'ខេត្ត ព្រៃវែង',
        'image': 'https://th.bing.com/th/id/R.8dc11aaa362bb45cdb179db6e6b96c69?rik=IeSVOfBSsVNi2A&riu=http%3a%2f%2fcambodia.thajsko.com%2fwp-content%2fuploads%2fPrey-Veng-01.jpg&ehk=0OkoZNssftcBhyuW2hvC3%2bOGOsqrIjDKpyMRKIWjdcA%3d&risl=&pid=ImgRaw&r=0',
        'detail': [
            {
                'namey': 'ម្ហូប គោដុត',
                'imagey': 'https://i.ytimg.com/vi/rU2kBIg4G_E/maxresdefault.jpg',
                'information': [
                    {
                        'images': 'https://i.ytimg.com/vi/rU2kBIg4G_E/maxresdefault.jpg',
                        'ingredient': 'WOW'
                    }
                ]  
            },
            {
                'namey': 'ម្ហូប កង្កែបបោក',
                'imagey': 'https://i.ytimg.com/vi/pVyG9ecRsdg/maxresdefault.jpg',
                'information': [
                    {
                        'images': 'https://i.ytimg.com/vi/pVyG9ecRsdg/maxresdefault.jpg',
                        'ingredient': 'WOW'
                    }
                ]  
            },
            {
                'namey': 'ម្ហូប មាន់ដុត',
                'imagey': 'https://i.ytimg.com/vi/ReEGyYimDQU/maxresdefault.jpg',
                'information': [
                    {
                        'images': 'https://i.ytimg.com/vi/ReEGyYimDQU/maxresdefault.jpg',
                        'ingredient': 'WOW'
                    }
                ] 
            },
        ]
    },
    {
        'id': 8,
        'name': 'ខេត្ត ក្រចេះ',
        'image': 'https://www.travel4history.com/wp-content/uploads/2020/01/Kratie-travel-guide-kampi.jpg',
        'detail': [
            {
                'namey': 'ម្ហូប ទាដុត',
                'imagey': 'https://images.deliveryhero.io/image/fd-kh/LH/bxk5-hero.jpg',
                'information': [
                    {
                        'images': 'https://images.deliveryhero.io/image/fd-kh/LH/bxk5-hero.jpg',
                        'ingredient': 'WOW'
                    }
                ] 
            },
            {
                'namey': 'ម្ហូប ខជើងជ្រូក',
                'imagey': 'https://i.ytimg.com/vi/x5x8Xjg3ZTw/maxresdefault.jpg',
                'information': [
                    {
                        'images': 'https://i.ytimg.com/vi/x5x8Xjg3ZTw/maxresdefault.jpg',
                        'ingredient': 'WOW'
                    }
                ] 
            },
            {
                'namey': 'ម្ហូប ស៊ុបមាន់ខ្មៅ',
                'imagey': 'https://i.pinimg.com/originals/2f/25/73/2f2573a95ba22504864b81187e960e00.jpg',
                'information': [
                    {
                        'images': 'https://i.pinimg.com/originals/2f/25/73/2f2573a95ba22504864b81187e960e00.jpg',
                        'ingredient': 'WOW'
                    }
                ] 
            },
        ]
    },
    {
        'id': 9,
        'name': 'ខេត្ត កំពង់ស្ពឺ',
        'image': 'https://i.ytimg.com/vi/1KopaSG9v_g/maxresdefault.jpg',
        'detail': [
            {
                'namey': 'ម្ហូប ញាំស្ពៅ',
                'imagey': 'https://i.ytimg.com/vi/AFB3VGXhPjU/maxresdefault.jpg',
                'information': [
                    {
                        'images': 'https://i.ytimg.com/vi/AFB3VGXhPjU/maxresdefault.jpg',
                        'ingredient': 'WOW'
                    }
                ] 
            },
            {
                'namey': 'ម្ហូប សម្លរកកូរ',
                'imagey': 'https://i.ytimg.com/vi/gyXkTNSBAG0/maxresdefault.jpg',
                'information': [
                    {
                        'images': 'https://i.ytimg.com/vi/gyXkTNSBAG0/maxresdefault.jpg',
                        'ingredient': 'WOW'
                    }
                ] 
            },
            {
                'namey': 'ម្ហូប សម្លរម្ជួរយួន',
                'imagey': 'https://th.bing.com/th/id/OIP.eLANz7XESVhf-V2TEXopiAHaEK?rs=1&pid=ImgDetMain',
                'information': [
                    {
                        'images': 'https://th.bing.com/th/id/OIP.eLANz7XESVhf-V2TEXopiAHaEK?rs=1&pid=ImgDetMain',
                        'ingredient': 'WOW'
                    }
                ] 
            },
        ]
    },
    {
        'id': 10,
        'name': 'ខេត្ត កំពងចាម',
        'image': 'https://thumbs.dreamstime.com/b/preah-soramrit-kosamak-kirirom-national-park-mountain-oamrei-phong-village-commune-phnom-sruoch-district-kilometers-118549110.jpg',
        'detail': [
            {
                'namey': 'ម្ហូប បុកមី',
                'imagey': 'https://i.ytimg.com/vi/Dct2agFefUM/maxresdefault.jpg',
                'information': [
                    {
                        'images': 'https://i.ytimg.com/vi/Dct2agFefUM/maxresdefault.jpg',
                        'ingredient': 'WOW'
                    }
                ] 
            },
            {
                'namey': 'ម្ហូប ឆាក្តៅទា',
                'imagey': 'https://th.bing.com/th/id/OIP.hfXuuTYeAoI4aIO5mrjjEgHaEK?rs=1&pid=ImgDetMain',
                'information': [
                    {
                        'images': 'https://th.bing.com/th/id/OIP.hfXuuTYeAoI4aIO5mrjjEgHaEK?rs=1&pid=ImgDetMain',
                        'ingredient': 'WOW'
                    }
                ] 
            },
            {
                'namey': 'ម្ហូប ឆាក្តៅអន្ទង់',
                'imagey': 'https://i.ytimg.com/vi/QqLkDlxFJPc/maxresdefault.jpg',
                'information': [
                    {
                        'images': 'https://i.ytimg.com/vi/QqLkDlxFJPc/maxresdefault.jpg',
                        'ingredient': 'WOW'
                    }
                ] 
            },
        ]
    }
]

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
        'image': 'https://www.prettywildworld.com/wp-content/uploads/2018/08/points-of-interest-where-to-go-and-places-to-visit-in-cambodia-featured.jpg'
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

@app.route('/api/food_provinces', methods=['GET'])
def get_food_provinces():
    return jsonify(food_provinces)

@app.route('/api/banner_provinces', methods=['GET'])
def get_banner_provinces():
    return jsonify(banner_provinces)

if __name__ == '__main__':
    app.run(debug=True)
