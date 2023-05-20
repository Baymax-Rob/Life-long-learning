answers = ["42", "forty two", "forty-two"]

def main():
    question = str(input("What is the meaning of life?: ").strip().lower())
    thinking(question)

def thinking(question):
    if question not in answers:
        print("No")
    else:
        print("Yes")

if __name__ == "__main__":
    main()