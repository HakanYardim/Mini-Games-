import string
print("=== Hangman === ")
print()

def Hangman(word):
    counter = 8
    wordLength = len(word)
    currentPrediction = "_" * wordLength
    print("This word has " + str(wordLength) + " letters.")
    print("Current prediction is " + currentPrediction)
    print("You start with " + str(counter) + " remaining guesses.")
    print("---------------------------------------------")
    print()
    guessLetter = ""
    while (currentPrediction != word and counter>0):
      enteredLetters = []
      alphabet = list(string.ascii_lowercase)
      for guess in range(len(alphabet)):
        guessLetter = input("Enter your letter as a guess: ").lower()
        if(guessLetter not in alphabet or len(guessLetter) != 1):
            print("Input not acceptable!")
            print("Please enter a letter from the alphabet.")
            print("You still have " + str(counter) + " remaining guesses.")
        elif(guessLetter in enteredLetters):
            print("This letter has been entered before.")
            print("Please enter another letter.")
        elif (guessLetter in word):
            foundIndexNumbers = []
            for count,value in enumerate(word, start=0):      
              if(value==guessLetter):
                  foundIndexNumbers.append(count)  
            numGuessedLetters = len(foundIndexNumbers)
            print("There is " + str(numGuessedLetters) + " " + guessLetter + "'s" + " in this word")    
            for i in foundIndexNumbers:
                currentPrediction = currentPrediction[:i] + guessLetter + currentPrediction[i+1:] 
            print("Based on that your current prediction is: " + currentPrediction)
            enteredLetters.append(guessLetter)
        elif (guessLetter not in word):
            print(guessLetter + " not found in the word")
            counter -= 1
            print("You have " + str(counter) + " remaining guesses.")
            print("Your current prediction is:" + currentPrediction)
            enteredLetters.append(guessLetter)
        print()
        print("Already tried letters: " + str(enteredLetters))
        print("---------------------------------------------")
        print()
        if (counter == 0):
            print("You have no remaining guesses.")
            print("The word was: " + word)
            print("But your current prediction was " + currentPrediction)
            print("You COULDN'T GUESS IT RIGHT!!")
            raise SystemExit()
        if(currentPrediction == word and counter>0):
            print("You GUESSED IT RIGHT !!")
            print("It took " + str(guess) + " tries")
            raise SystemExit()
          
Hangman("")




