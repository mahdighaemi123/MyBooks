import datetime
 
text = input("Write your memory: ")
current_time = str(datetime.datetime.now())
 
with open("diary.txt", "a") as file:
    file.write(f"\nDate: {current_time}\n")
    file.write(f"{text}\n")
    print("Memory saved.")
