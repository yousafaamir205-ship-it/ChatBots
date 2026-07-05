import json
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
FILE_PATH = os.path.join(BASE_DIR, "data", "knowledge.json")


def load_knowledge():
    with open(FILE_PATH, "r", encoding="utf-8") as file:
        return json.load(file)


def save_knowledge(knowledge):
    with open(FILE_PATH, "w", encoding="utf-8") as file:
        json.dump(knowledge, file, indent=4)