import random

def guess_reddle():
    riddle = [
        {"question": "Did Snow white ate poisonous carrot?(Y/N)", "answer":"N"},
        {"question": "Is sashimi Chinese food?(Y/N)", "answer": "N"},
        {"question": "How many people are on each team in a basketball game:", "answer": "5"},
        {"question": "Do polar bears eat penguins?(Y/N)", "answer": "N"},
        {"question": "Can I go to Tampere on 30-02-2024?(Y/N)", "answer": "N"},
        {"question": "Are pandas good at sport?(Y/N)", "answer": "N"}
    ]


    attample = 5
    while attample > 0:
        reddle = random.choice(riddle)
        question = reddle["question"]
        answer = reddle["answer"]
        guess = print(f"GUESS: {question}\nyou have{attample} chances")
        userAnswer = input("Answer: ")
        if userAnswer == answer:
            print("BINGO!,You've got new petrol!")
            return True
        else:
            attample -= 1
            if attample > 0:
                print(f"Again!")
            else:
                print("Wrong!\nBut you got new petrol because you are so cute!")
                return True

guess_reddle()