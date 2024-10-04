print("Welcome to my computer Quiz!")

playing = input("Do you want To play? ")

if playing.lower() != "yes":
    print("Ok Thank you! ")
    quit()

print("Ok lat's play :) ")

score = 0

Answer = input("1. What does CPU stand for? ")
if Answer.lower() == "central processing unit":
    score += 1
    print("Correct!")   
else:
    print("Incorrect!")

Answer = input("2. What does RAM stand for? ")
if Answer.lower() == "random access memory":
    score += 1
    print("Correct!")   
else:
    print("Incorrect!")

Answer = input("3. What does GPU stand for? ")
if Answer.lower() == "graphics processing unit":
    score += 1
    print("Correct!")   
else:
    print("Incorrect!")

Answer = input("4. What does DS stand for? ")
if Answer.lower() == "data structure":
    score += 1
    print("Correct!")   
else:
    print("Incorrect!")

Answer = input("5. What does IU stand for? ")
if Answer.lower() == "interface unit":
    score += 1
    print("Correct!")   
else:
    print("Incorrect!")


print("You got " + str(score) + " questions correct!")
print("You got " + str((score /5)*100) + " %." )
