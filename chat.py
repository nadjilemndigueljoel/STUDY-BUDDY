from assistant import get_ai_response
from memory import load_memory, save_memory


def run_chat():
    print("Welcome to Study-Buddy!")
    print("Your AI study assistant is ready.")

    messages = load_memory()

    while True:
        user_input = input("\nYou: ").strip()

        if not user_input:
            continue

        if user_input.lower() in {"exit", "quit"}:
            print("Goodbye!")
            save_memory(messages)
            break

        messages.append({"role": "user", "content": user_input})

        try:
            response = get_ai_response(messages)
        except Exception as error:
            messages.pop()
            print(f"\nError: {error}")
            continue

        answer = response.get("answer", "")
        topic = response.get("topic", "")
        next_question = response.get("next_question", "")

        messages.append({"role": "assistant", "content": answer})
        save_memory(messages)

        print(f"\nStudy Buddy: {answer}")
        if topic:
            print(f"Topic: {topic}")
        if next_question:
            print(f"Next question: {next_question}")


if __name__ == "__main__":
    run_chat()