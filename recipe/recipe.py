
class Recipe:
    """ Instantiate Recipe class based on cocktail config sections """

    def __init__(self, cocktail_config_dict):
        self.ingredients = cocktail_config_dict.keys()
    
    # todo: implement print method for Recipe class
    def __repr__(self):
        pass

    def contains(self, ingredient):
        """ Return if the recipe contains target ingredient """
        raise NotImplementedError

    