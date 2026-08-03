score = 0
with open("quiz.txt", "r") as file:
    for line in file:
        data = line.strip().split(",")
        question = data[0]
        correct_answer = data[1]
        
        user_ans = input(f"{question} ")
        if user_ans == correct_answer:
            score += 1
 
print(f"Final Score: {score}")
