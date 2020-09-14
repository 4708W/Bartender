# from cocktail import LIME_JUICE, recipe
from recipe_reader import RecipeReader


class Bartender:

    def __init__(self, recipe_reader: RecipeReader):
        self.recipe_reader = recipe_reader

    def make(self):
        """ Make cocktails based on given ingredients """
        raise NotImplementedError()

    



if __name__ == "__main__":
    
    ingredients = LIME_JUICE
    
    print("Searching ...")
    for r in recipe:
        if ingredients in recipe[r]:
            print(recipe[r])