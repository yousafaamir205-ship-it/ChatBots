import json

FILE_PATH = "data/knowledge.json"


def load_knowledge():
    with open(FILE_PATH, "r") as file:
        return json.load(file)


def save_knowledge(knowledge):
    with open(FILE_PATH, "w") as file:
        json.dump(knowledge, file, indent=4)


def add_knowledge(question, answer, topic):
    knowledge = load_knowledge()

    new_data = {
        "id": len(knowledge) + 1,
        "topic": topic,
        "question": question,
        "answer": answer
    }

    knowledge.append(new_data)

    save_knowledge(knowledge)