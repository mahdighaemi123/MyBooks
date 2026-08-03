# Infinite loop seeking magic phrase
while True: 
    text = input("Say the magic word: ")
    
    if text == "Abra Kadabra":
        print("Spell broken! You are free.")
        break  # The loop ends right here!
        
    print("Wrong word! Try again.")