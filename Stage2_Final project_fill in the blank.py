print("Stage2_Final project by Saranya Ruiz-Esparza")


# Quizes and answers of 3 paragraphs
paragraph_easy = ("An apple can taste very nice. Try a bite or a ___1___." " If it is ___2___ or it is green."
           " It will ___3___ good, if it is ___4___." " My grandma says an apple a day, always keeps the doctor ___5___. ")
answers_easy = ["slice","red","taste","clean","away"]

# Quiz and answes about programming facts
paragraph_medium = ("The first computer ___1___ is Ada Lovelace."
             "The first computer was actual a ___2___ called the Jacquard loom,"
             " an automated, ___3___ loom,which didn't use any electricity."
             "The first high-level programming ___4____ was Fortran invented in ___5___ by John Backus from IBM")
answers_medium = ["programmer","loom","machanical","language","1954"]

# Quiz and answers about Python(programming language) facts
paragraph_hard = ("Python is ___1___ by"" Guido Van Rossum and first released in ___2___."
           "Python is a ___3___ -level language with its own specific rules and format."
           "Python can be easily used for small, large, online and offline project."
           "The best option for ___4___ Python are web development, simple ___5____ and data annalysis.")
answers_hard = ["created","1991","high","utilizing","scripting"]

spaces = ["___1___", "___2___", "___3___", "___4___", "___5___"]

player_name = raw_input("What is your name?")

""" Asking player's name and welcome to play game
Input: player's name.
Output: greeting player and stating their name.

"""


print "Hi!"+player_name+".Welcome to Fill in the blanks quiz."


print("You have 5 chances per quiz")

def difficulty_level():
 
    """ Player choose a level of a game to play
    Input: choices of levels with its level of questions and answers.
    Output: selected level that comes with its question and answers.
    
    """
    while True:
        difficulty = raw_input("Please select a quiz difficulty by typing it in: Possible choices include Easy, Medium and Hard:  ")
        if difficulty == "Easy":
            print "You choose " + difficulty + ". Start to play game: "
            return paragraph_easy, answers_easy
        elif difficulty == "Medium":
            print "You choose " + difficulty + ". Start to play game: "
            return paragraph_medium, answers_medium
        elif difficulty == "Hard":
            print "You choose " + difficulty + ". Start to play game: "
            return paragraph_hard, answers_hard
        print "This is not a valid category"
paragraph, answers = difficulty_level()


def play_game(paragraph, answers, spaces): 
    
    """ Function to get the game to play
    Input: selected paragraph, list of answers, list of spaces.
    output: game responds correctly with right or wrong answers and let player have 5 chances for a game.
    
    """
    print paragraph
    count = 0
    attempts = 0
    max_attempts = 5
    space_index = 0
    while count < len(spaces):
        user_input = raw_input("What is the answer for this blank" + spaces[space_index] + ": ")
        if user_input.lower() == answers[count]:
            paragraph = paragraph.replace(spaces[count], answers[count]) # .replace for replacing a correct answer in a right blank
            print "Correct"
            print paragraph
            count += 1
            space_index += 1
         
        else:
            print "Incorrect, try again."
            attempts < max_attempts # player can keep playing game, if it doesn't reach 5 incorrect answers yet
            attempts += 1

        if attempts == max_attempts:
            print " You used up all your chances. Game Over!" # this sentence shows when already give 5 incorrect answers in one game.
            break # to stop the loop when game is over

play_game(paragraph, answers, spaces)



