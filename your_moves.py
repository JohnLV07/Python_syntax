#Task 1: fix and make sure the code below is correct 
# Objective is to undestand the importance od the indentation in Python, especially with if statements.


weather = "sunny"
if weather == "sunny":
    print("Wear sunglasses!")
else:
    print("take an umbrella!")



# Task 2: Ask the user how they feel today. If they say "happy", print "That's great to hear!", and if they say "sad", print "I hope your day gets better!". Ensure your if statement is properly indented

mood_user = input("How do you feel today? ")
sad_mood = "Hope your day gets better"
happy_mood = "thats's good to hear!"
if mood_user == "happy":
    print(happy_mood)
elif mood_user == "sad":
    print(sad_mood)

