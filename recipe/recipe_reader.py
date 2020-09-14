import json

from recipe import Recipe


# todo: singleton
class RecipeReader:

    def __init__(self):
        self.config = None

    def find(self, cocktail_name):
        pass

    def _read_config(self):
        with open("config/cocktail.json") as f:
            self.config = json.load(f)
    

if __name__ == "__main__":
    r = RecipeReader()
    r._read_config()
    print(r.config)
