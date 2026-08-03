# The "magic" way: Tuple Unpacking
score_record = ("Aria", 100)

# Python smartly puts "Aria" into 'name' and 100 into 'score'
name, score = score_record 

print(name + " scored " + str(score))