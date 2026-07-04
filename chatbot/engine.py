from utils import clean_text

def find_answer(question, knowledge):
    question = clean_text(question)

    for item in knowledge:
        topic = clean_text(item["topic"])

        if topic in question:
            return item["answer"]

    return None