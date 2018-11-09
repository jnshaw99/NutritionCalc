import json
##Adding food to json list includig important elements
class addfood:
    def __init__(self):
        with open('foodlist.json', 'w')as outfile:
            json.dump({'Foods': []}, outfile)
    def add(self):
        addnew=input('Would you like to add a food?(y,n) ')
        if(addnew=='y'):
            with open('foodlist.json') as list:
                foodlist=json.load(list)
            foodlist['Foods'].append({input('The name: '): {
                'calories': input('Calories per 100g: '),
                'protein': input('Grams of protein per 100g: '),
                'carbs': input('Carbs per 100g: '),
                'fiber': input('Fiber per 100g: '),
                'unsaturated': input('Grams of unsaturated fat per 100g: '),
                'staturated': input('Grams of saturated fat per 100g: '),
                'vitamin a': input('Percent Daily of vitamin A per 100g: '),
                'vitamin b12': input('Percent Daily of vitamin B-12 per 100g: '),
                'vitamin b6': input('Percent Daily of vitamin B-6 per 100g: '),
                'vitamin c': input('Percent Daily of vitamin C per 100g: '),
                'iron': input('Percent Daily of iron per 100g: '),
                'magnesium': input('Percent Daily of magnesium per 100g: '),
                'potassium': input('Percent Daily of potassium per 100g: ')
            }})
            with open('foodlist.json', 'w') as outfile:
                json.dump(foodlist, outfile, indent=4)
    def adding(self):
        check=True
        while(check):
            self.add()
            if(input('Add another? (y,n) ')=='y'):
                check=True
            else:
                check=False
a=addfood()
a.adding()
            