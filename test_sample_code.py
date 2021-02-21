import json
from json import JSONDecoder,JSONEncoder
import pickle
import chardet

class _23:
    def __init__(self,x):
        self.x = x

obj = _23(23)
with open("./client_data/sample","wb") as file:
    _byte = pickle.dump(obj, file)
with open("./client_data/sample","rb") as file:
    obj = pickle.load(file)
print(obj)