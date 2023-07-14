import random
import time

OPERATORS = ['+', '-', '*']
MIN_OPERAND = 3
MAX_OPERAND = 12
TOTAL_PROBLEMS = 10
TIME_LIMIT = 5  # Time limit per problem in seconds

def generate_problem():
    left = random.randint(MIN_OPERAND, MAX_OPERAND)
    right = random.randint(MIN_OPERAND, MAX_OPERAND)
    operator = random.choice(OPERATORS) #Choose random operator from OPERATORS list

    expr = str(left) + ' ' + operator + ' ' + str(right)
    answer = eval(expr)
    return expr, answer

wrong = 0
input("Press enter to start!")
print("----------------------")

start_time = time.time() 

for i in range(TOTAL_PROBLEMS):
    expr, answer = generate_problem()
    print("Problem #" + str(i+1) + ": " + expr + ' = ')

    start = time.time()
    while True:
        guess = input("Your answer: ")
        if time.time() - start > TIME_LIMIT:
            print("Time's up!")
            wrong += 1
            break
        try:
            if int(guess) == answer:
                print("Correct!")
                break
            else:
                print("Incorrect! Try again.")
                wrong += 1
        except ValueError:
            print("Invalid input! Try again.")

end_time = time.time()
total_time = end_time - start_time

print("----------------------")
print("Well done! You finished in", total_time , "seconds")
accuracy = (TOTAL_PROBLEMS - wrong) / TOTAL_PROBLEMS * 100
print("Your score:", accuracy, "%")
