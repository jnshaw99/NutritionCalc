import json
from recipe import recipe

class getdata:
    def __init__(self):
        print('Initialize...')
    def add_food_to(self,recipe,food,amount):
        recipe.add_food(food,amount)

r=recipe("test")
a=getdata()
a.add_food_to(r,'Rice,White',200)
print("200g White Rice "+str(r.get_calories()))