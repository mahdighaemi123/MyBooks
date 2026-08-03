number = 0
while number < 5:
    number = number + 1
    
    if number == 3:
        print("Skipping the unlucky number!")
        continue  # Jumps back to line 2 (start of loop)
        
    print("Number is:", number)