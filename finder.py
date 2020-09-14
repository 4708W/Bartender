from cocktail import LIME_JUICE, recipe

if __name__ == "__main__":
    
    ingredients = LIME_JUICE
    
    print("Searching ...")
    for r in recipe:
        if ingredients in recipe[r]:
            print(recipe[r])