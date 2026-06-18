import sys

question_answer_set = {
    "What does CPU stand for? ": "central processing unit",
    "What does GPU stand for? ": "graphics processing unit",
    "What does RAM stand for? ": "random access memory",
    "What does PSU stand for? ": "power supply unit"
}

def whether_to_continue():
    ask = input("Do you want to continue? ")
    if ask.strip().lower() != "yes":
        sys.exit()

def main() -> None:
    print("Welcome to my computer quiz!")

    playing = input("Do you want to play? ")
    if playing.strip().lower() != "yes":
        sys.exit()

    print("Okay! Let's play :)")
    score = 0

    for index, (key, value) in enumerate(question_answer_set.items()):
        serial_no = f"{index+1}/{len(question_answer_set)}"
        answer = input(f"{serial_no} - {key}")
        if answer.strip().lower() == f"{value}":
            print('Correct!')
            score += 1
        else:
            print("Incorrect!")
            whether_to_continue()

    print("You got " + str(score) + " questions correct!")
    print("You got " + str((score / 4) * 100) + "%.")


if __name__ == "__main__":
    main()