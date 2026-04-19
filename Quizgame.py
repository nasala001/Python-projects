#python quiz game
questions=("how many elements are in the periodic table",
           "what is the national colour of nepal",
           "what is the most abundant gas in earth's atmosphere",
           "which planet in the solar system is the hottest?",
           "which animal lays the largest eggs")
options = (("A. 89","B.90","C.78","D.118"),
           ("A.red","B.orange","C.green","D.blue"),
           ("A.hydrogen","B.nitrogen","C.oxygen","D.carbondioxide"),
           ("A.mars","B.venus","C.mercury","D.earth"),
           ("A.human","B.ostrich","C.crow","D.blue whale"))

answers=("D","A","B","B","B")
guesses=[]
score=0
question_number=0
for question in questions:
    print("------------------")
    print(questions)
    for option in options[question_number]:
        print(option)

    guess=input("enter(A,B,C,D):")
    guesses.append(guess)
    if guess==answers[question_number]:
        score+=1
        print("Correct!")
    else:
        print("incorrect")
        print(f"{answers[question_number]} was correct")
        question_number+=1

print("---------------")
print("    RESULTS     ")
print("----------------")
print("answers:")




