from engine import find_answer

from database import load_knowledge, save_knowledge
knowledge = load_knowledge()

print("Knowledge loaded successfully!")
print(f"Number of records: {len(knowledge)}")
while True:
    question = input("Ask me: ")
    if question.lower() == "exit":
        print("Goodbye!")
        break


    answer = find_answer(question, knowledge)

    if answer:
        print(answer)
        
        
        print("FOUND ANSWER")
    else:
        print("Sorry, no answer.")
        choice = input("Would you like to teach me? (yes/no): ").strip().lower()
        if choice == "yes":
            answer = input("Please tell me the answer: ").strip()
            topic = input("Please enter the topic: ").strip()

            new_data = {
                "id": len(knowledge) + 1,
                "topic": topic,
                "question": question,
                "answer": answer
        }

            knowledge.append(new_data)

            save_knowledge(knowledge)

            print("Thank you! I learned something new.")
