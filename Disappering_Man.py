import random
#man in the form of a list
mlist=[" _____ \n","(0 ","0)\n","--","|","--\n"," /"," \  \n"]
Guess=0 #number of guesses
WrongGuess=[] #list of wrong guesses
Running=[] #the running status of the game
#list of movies for playing the word game
WordSangrah=["Apocalypse","Man of Steel","Dawn of Justice","The Dark Knight","Captain America","The Avengers","Doctor Strange","Suicide Squad","Black Panther","Mission Impossible","Iron Man"]
Movie=random.choice(WordSangrah).lower() #for getting random movie
Movie=list(Movie)
n=Movie.__len__()
#create a running list
for i in range(n):
    if Movie[i]!=" ":
        Running.append("__")
    else:
        Running.append("  ")
#Difficulty Level
j = int(input("Enter The Difficulty Level\n 1 For Showing One Word\n 2 For Showing Two Words\n 3 For Showing Three Words\n 4 For Showing Four Words\n 5 For Showing Five Words\n"))
while j > 0:
    recent = random.randrange(n) #choose a random alphabet
    if Running[recent] == "  ":
        recent = random.randrange(n)
    Running[recent] = Movie[recent]
    j -= 1
#Function for displaying
def show():
    print(*mlist,sep=" ")
    print("Number Of Guessess : ",Guess)
    print("Wrong Guessess :",*WrongGuess,sep=" ")
    print("Current Status : ")
    current()
    print("\n")
    print("********************************************************************")
#Function for storing the current status
def current():
    for i in Running:
        print(i,end=" ")
#For input
def inputData():
    global Guess
    word=input()
    Guess+=1
    if word in Movie:
        for i in range(n):
            if Movie[i]==word:
                if Running[i]=="__":
                    Running[i]=word
    else:
        WrongGuess.append(word)
        mlist.__delitem__(-1)
while WrongGuess.__len__() < 8 and  Running.count("__")!= 0:
    show()
    inputData()
if WrongGuess.__len__() >=8 and Running.count("__")!=0:
    print("!!!!You Lost The Game!!!!\n")
    print("Correct Answer : ", *Movie,sep=" ")
else:
    print("!!!!You Won The Game!!!!")
    