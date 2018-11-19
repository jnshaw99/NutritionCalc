import json

class recipe:
    name=""
    ingredients=[[], []]
    calories=0.0
    protein=0.0
    carbs=0.0
    fiber=0.0
    saturated=0.0
    unsaturated=0.0
    vit_a=0.0
    vit_b12=0.0
    vit_b6=0.0
    vit_c=0.0
    iron=0.0
    potassium=0.0
    magnesium=0.0
    def __init__(self,name):
        self.name=name
    def add_food(self,food,amount):
        self.ingredients[0].append(food)
        self.ingredients[1].append(amount)
        self.protein+=(amount*.01)*self.get_content(food,'protein')
        self.calories+=(amount*.01)*self.get_content(food,'calories')
        self.fiber+=(amount*.01)*self.get_content(food,'fiber')
        self.carbs+=(amount*.01)*self.get_content(food,'carbs')
        self.iron+=(amount*.01)*self.get_content(food,'iron')
        self.magnesium+=(amount*.01)*self.get_content(food,'magnesium')
        self.potassium+=(amount*.01)*self.get_content(food,'potassium')
        self.saturated+=(amount*.01)*self.get_content(food,'saturated')
        self.unsaturated+=(amount*.01)*self.get_content(food,'unsaturated')
        self.vit_a+=(amount*.01)*self.get_content(food,'vitamin a')
        self.vit_b12+=(amount*.01)*self.get_content(food,'vitamin b12')
        self.vit_b6+=(amount*.01)*self.get_content(food,'vitamin b6')
        self.vit_c+=(amount*.01)*self.get_content(food,'vitamin c')
    def get_content(self,name,spec):
        json_val={}
        try:
            json_val=json.load(open('foodlist.json'))
        except:
            print('files fails to open')
        for vals in json_val['Foods']:
            return float((vals[name][spec]))
    def get_calories(self):
        return self.calories
