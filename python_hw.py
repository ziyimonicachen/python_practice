import json
import pip._vendor.requests as requests

class CatBreeds:
    def __init__(self):
        self.result = json.loads(requests.get('https://catfact.ninja/breeds').text)

    def get_nth_breed(self, n):
        return self.result[n]

cat = CatBreeds()
print(cat.get_nth_breed(1))