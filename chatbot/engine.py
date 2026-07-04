from utils import clean_text

def find_answer(question, knowledge):
    search_question = clean_text(question)

    for item in knowledge:
        if clean_text(item["question"]) == search_question:
            return item["answer"]

    return None