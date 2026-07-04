import difflib
from utils import clean_text

from utils import clean_text

def find_answer(question, knowledge):
    question = clean_text(question)

    topics = []

    for item in knowledge:
        topic = clean_text(item["topic"])
        topics.append(topic)

        if topic in question:
            return item["answer"]

    closest = difflib.get_close_matches(question, topics, n=1, cutoff=0.6)

    if closest:
        for item in knowledge:
            if clean_text(item["topic"]) == closest[0]:
                return f"Did you mean '{item['topic']}'?\n\n{item['answer']}"

    return None

def update_answer(topic, knowledge):
    topic = clean_text(topic)

    for item in knowledge:
        if clean_text(item["topic"]) == topic:
            print("\nCurrent Answer:")
            print(item["answer"])

            new_answer = input("\nEnter new answer: ").strip()

            item["answer"] = new_answer

            return True

    return False