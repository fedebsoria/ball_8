import random

answer_number = 0

def generate_random_answer():
    r_number = random.randint(1, 9)
    return r_number

def ask_name():
    name = input("Enter your name and ask a question. I'll see your faith...\n")
    return name

def enter_question():
    question = input("Make me a question, don't fear the future.\n")
    while len(question) <= 0:
        question = input("Make a question. I can wait and live forever, but you can't.\n")
        return question
    return question

def answer(number):
    response = ""
    if number == 9:
        response ="Yes.\n"
    elif number == 8:
        response ="No.\n"
    elif number == 7:
        response ="I won't count on it.\n"
    elif number == 6:
        response ="It will be true and it will change your life.\n"
    elif number == 5:
        response ="I can't answer that, but the ghost in your back can.\n"
    elif number == 4:
        response ="Go for it, it will be great.\n"
    elif number == 3:
        response ="Sure, why not. If you want a better answer look for a real AI or use a OUIJA.\n"
    elif number == 2:
        response ="No way I'll answer that. I'm not THAT disgusting.\n"
    elif number == 1:
        response ="Yes, that will make you happy.\n"
    return response

def answer_precise_questions(question):
    result_question = False
    if "lottery" in question:
        print("I do not gamble, but you do, so... I don't know... {} maybe?\n".format(str(random.randint(1111, 9999))))
        result_question = True
    return result_question

def grettings(name):
    print("Pleased to meet you {}, feel welcome.\n If you want to leave say GOOD BYE.\n".format(name))

def main():
    name = ask_name()
    grettings(name)
    while True:
        answer_number = generate_random_answer()
        question = enter_question()
        result_question = answer_precise_questions(question)

        if question == "bye" or question == "GOOD BYE" or question == "good bye":
            break

        if result_question != True:
            script_answer = answer(answer_number)
            print(script_answer)

    print("Good Bye")



    


if __name__ == "__main__":
    main()
    #test