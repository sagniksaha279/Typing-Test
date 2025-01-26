from time import *
import random
from Typing_database import hard,easy,medium

def checkAccuracy(text,text_input):
    mistakes = 0
    correct_type = 0
    for i in range(len(text_input)):
        try:
            if(text[i] != text_input[i]):
                mistakes+=1
            else:
                correct_type+=1
        except:
            mistakes+=1
    accuracy = round((correct_type/len(text_input))*100,2)
    print(f"Mistakes = {mistakes}")
    print(f"Accuracy = {accuracy}%")
    
def checkTime(start_time,end_time,text_input):
    time_delay = (end_time - start_time)
    time_min = time_delay/60
    time_delay = round(time_delay,2)
    speed = round(len(text_input)/time_delay)
    speed_min = round(len(text_input)/time_min)
    print(f"Speed = {speed} wps\nSpeed = {speed_min} wpm")
    
    
#MAIN WORK
while True:
    print("                                        -------``WELCOME TO TYPING SPEED TEST``---------    ")
    hardness = input("\n\nEnter your level of test(Easy/Medium/Hard):")
    if(hardness == "Easy"):
        text = random.choice(easy)
        print("Your text is:",text)
        print("\n\n")
        start_time = time()
        text_input = input("Enter your text:")
        end_time = time()
        checkTime(start_time=start_time,end_time=end_time,text_input=text_input)
        checkAccuracy(text=text,text_input=text_input)
        con = input("Do you Want to continue(Yes/No):")
        if(con == "No"):
            break
    elif(hardness == "Medium"):
        text = random.choice(medium)
        print("Your text is:",text)
        print("\n\n")
        start_time = time()
        text_input = input("Enter your text:")
        end_time = time()
        checkTime(start_time=start_time,end_time=end_time,text_input=text_input)
        checkAccuracy(text=text,text_input=text_input)
        con = input("Do you Want to continue(Yes/No):")
        if(con == "No"):
            break
    elif(hardness == "Hard"):
        text = random.choice(hard)
        print("Your text is:",text)
        print("\n\n")
        start_time = time()
        text_input = input("Enter your text:")
        end_time = time()
        checkTime(start_time=start_time,end_time=end_time,text_input=text_input)
        checkAccuracy(text=text,text_input=text_input)
        con = input("\nDo you Want to continue(Yes/No):")
        if(con == "No"):
            break
    else:
        print("Wrong Input...Please Check")

print("\n\nThank You for using our test please come again :`)")
