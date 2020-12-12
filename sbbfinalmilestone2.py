# Defining Score variables
x = 0
score = x

# Question One
print("What percent do women fill the positions of directors, writers, producers, executive producers, editors, and cinematographers in 2019-2020?")
answer_1 = input("a)56%\nb)34%\nc)63%\nd)21%\n:")
if answer_1.lower() == "b" or answer_1.lower() == "34%":
    print("Correct")
    x = x + 1
else:
    print("Incorrect, women fill 34% of film positions in 2019-2020.")
# Each question is formulated in the same way, where there are if and else statements that are dependent on what you enter as your answer.

# Question Two
print("Who is the first female director to win an Oscar?")
answer_2 = input("a)Greta Gerwig\nb)Sophia Coppola\nc)Kathryn Bigelow\nd)Mira Nair\n:")
if answer_2.lower() == "c" or answer_2.lower() == "Kathryn Bigelow":
    print("Correct")
    x = x + 1
else:
    print("Incorrect, in 15.9% of the top-grossing movies, 11% of the cast was a minority.")

# Question Three
print("True or False... 15.9% of the top-grossing movies consisted of casts that were 11% minorities?")
answer_3 = input(":")
if answer_3.lower() == "true" or answer_3.lower() == "t":
    print("Correct")
    x = x + 1
else:
    print("Incorrect")

# Question Four
print("Who is the highest paid, black actor in Hollywood?")
answer_4 = input("a)Samuel Jackson\nb)Morgan Freeman\nc)Eddie Murphy\nd)Denzel Washington\n:")
if answer_4.lower() == "a" or answer_4 == "Sameuel Jackson":
    print("Correct")
    x = x + 1
else:
    print("Incorrect, the highest paid, black actor is Samuel Jackson")

# Question Five
print("Memories of Murder was the first foreign film to win best picture.")
answer_5 = input(":")
if answer_5.lower() == "false" or answer_5.lower() == "f":
    print("Correct")
    x = x + 1
else:
    print("Incorrect, the first foreign film to win best picture was Parasite.")

# Question Six
print("What is the share of minority, best actor winners?")
answer_1 = input("a)3.2%\nb)15%\nc)12.2%\nd)6.8%\n:")
if answer_1.lower() == "d" or answer_1.lower() == "6.8%":
    print("Correct")
    x = x + 1
else:
    print("The share of minority, best actor winners is 6.8%.")
# Each question is formulated in the same way, where there are if and else statements that are dependent on what you enter as your answer.

# Question Seven
print("What was the hashtag that changed the Oscars?")
answer_2 = input("a)#OscarsSoWhite\nb)#HollywoodSoWhite\nc)#MeToo\nd)#BlackLivesMatter\n:")
if answer_2.lower() == "a" or answer_2.lower() == "#OscarsSoWhite":
    print("Correct")
    x = x + 1
else:
    print("Incorrect, the hashtag that went viral was #OscarsSoWhite.")

# Question Eight
print("Jordan Peele was the director that stated 'He didn't see casting a white dude as the lead'.")
answer_3 = input(":")
if answer_3.lower() == "true" or answer_3.lower() == "t":
    print("Correct")
    x = x + 1
else:
    print("Incorrect")

# Question Nine
print("Who was the first, black man to win the Oscar for best director?")
answer_4 = input("a)Spike Lee\nb)Roger Ross Williams\nc)John Singleton\nd)Barry Jenkins\n:")
if answer_4.lower() == "b" or answer_4 == "Roger Ross Williams":
    print("Correct")
    x = x + 1
else:
    print("Incorrect, Roger Ross Williams was the first, black man to win an Oscar for best director.")

# Question Ten
print("'Mother India' was the film from India to win an Oscar.")
answer_5 = input(":")
if answer_5.lower() == "false" or answer_5.lower() == "f":
    print("Correct")
    x = x + 1
else:
    print("Incorrect, 'Gandhi' was the first film from India to win an Oscar.")

#Total Score
score = float(x / 10) * 100
print(x,"out of 10, that is",score, "%")
# For the final project, I will formulate the code in the same way. I will create twenty questions, along the same lines as what I've set up above.
