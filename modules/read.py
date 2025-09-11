import json

data = []
def load(name):
    global data
    with open(name,encoding='utf-8') as file:
        data = json.load(file)