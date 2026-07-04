
import os

print("Running:", os.path.abspath(__file__))
from engine import find_answer
from database import load_knowledge, save_knowledge

knowledge = load_knowledge()

print("Knowledge loaded successfully!")
print(f"Number of records: {len(knowledge)}")

while True:
    question = input("Ask me: ").strip()

    # Exit command
    if question.lower() == "exit":
        print("Goodbye!")
        break

    # Show all topics
    if question.lower()in ["topics", "type"]:
        print(">>> ENTERED TOPICS BLOCK <<<")

    for item in knowledge:
        print(item["topic"])

    continue
    # Search for answer
    answer = find_answer(question, knowledge)

    if answer:
        print(answer)

    else:
        print("Sorry, no answer.")

        choice = input("Would you like to teach me? (yes/no): ").strip().lower()

        if choice == "yes":
            user_answer = input("Please tell me the answer: ").strip()
            topic = input("Please enter the topic: ").strip()

            new_data = {
                "id": len(knowledge) + 1,
                "topic": topic,
                "question": question,
                "answer": user_answer
            }

            knowledge.append(new_data)
            save_knowledge(knowledge)

            print("Thank you! I learned something new.")