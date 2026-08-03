def check_palindrome(word):
    # Check if word equals its reverse
    if word == word[::-1]:
        print("Magic Word! (It is a palindrome)")
    else:
        print("Normal Word.")
  
user_word = input("Enter a word: ")
check_palindrome(user_word)