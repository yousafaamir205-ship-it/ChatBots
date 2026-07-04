import json

def load_knowledge():
    with open("data/knowledge.json", "r") as file:
        return json.load(file)

def save_knowledge(knowledge):
    with open("data/knowledge.json", "w") as file:
        json.dump(knowledge, file, indent=4)