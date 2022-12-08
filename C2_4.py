#Code for my C2 aspect of my first coding summative assessment
#Finished after 9 refinements
#Christopher Jagdeo
#Upper Canada College
#Game based on Jabari Jumps
#Text based game




Splash = """
                                                                    
██     ██ ███████ ██       ██████  ██████  ███    ███ ███████     ████████  ██████      ███    ███ ██    ██      ██████   █████  ███    ███ ███████ ██                                          
██     ██ ██      ██      ██      ██    ██ ████  ████ ██             ██    ██    ██     ████  ████  ██  ██      ██       ██   ██ ████  ████ ██      ██                                          
██  █  ██ █████   ██      ██      ██    ██ ██ ████ ██ █████          ██    ██    ██     ██ ████ ██   ████       ██   ███ ███████ ██ ████ ██ █████   ██                                          
██ ███ ██ ██      ██      ██      ██    ██ ██  ██  ██ ██             ██    ██    ██     ██  ██  ██    ██        ██    ██ ██   ██ ██  ██  ██ ██                                                  
 ███ ███  ███████ ███████  ██████  ██████  ██      ██ ███████        ██     ██████      ██      ██    ██         ██████  ██   ██ ██      ██ ███████ ██                                          
                                                                                                                                                                                                
                                                                                                                                                                                                
                                                                                                                                                                                                
                                                                                                                                                                                                
                                                                                                                                                                                                
                                                                                                                                                                                                
                                                                                                                                                                                                
                                                                                                                                                                                                
                                                                                                                                                                                                
██ ████████     ██ ███████     ██████   █████  ███████ ███████ ██████       ██████  ███    ██          ██  █████  ██████   █████  ██████  ██          ██ ██    ██ ███    ███ ██████  ███████ ██ 
██    ██        ██ ██          ██   ██ ██   ██ ██      ██      ██   ██     ██    ██ ████   ██          ██ ██   ██ ██   ██ ██   ██ ██   ██ ██          ██ ██    ██ ████  ████ ██   ██ ██      ██ 
██    ██        ██ ███████     ██████  ███████ ███████ █████   ██   ██     ██    ██ ██ ██  ██          ██ ███████ ██████  ███████ ██████  ██          ██ ██    ██ ██ ████ ██ ██████  ███████ ██ 
██    ██        ██      ██     ██   ██ ██   ██      ██ ██      ██   ██     ██    ██ ██  ██ ██     ██   ██ ██   ██ ██   ██ ██   ██ ██   ██ ██     ██   ██ ██    ██ ██  ██  ██ ██           ██    
██    ██        ██ ███████     ██████  ██   ██ ███████ ███████ ██████       ██████  ██   ████      █████  ██   ██ ██████  ██   ██ ██   ██ ██      █████   ██████  ██      ██ ██      ███████ ██ 
                                                                                                                                                                                                
                                                                                                                                                                                                

"""

print(Splash)

#This displays this piece of splash art, and shows the user the art. It is the first thing that the user will see as it introduces them to the game.

#It is the only thing displayed before the tutorial and its prelude.


#____________________________________________________________________________________________________________________________________________________________________________________________________________________
#This line seperates the different pieces of code and helps make the code more readable. However, it should not be interpreted by the computer, so a # is used.

def question11():

#This defines question 11; the following information is what makes up question 11

   global willingness_to_help

#This global command makes the term "willingness_to_help" visible to the whole code, which is important to the code running properly as the variable is continually used.

   print("1. Yes!")
   print("2. No \n")

#These are the options in question 11 that the user has to pick from

   print("\n Now you know how easy it is for someone to feel a little better, and how important an accomplishment can be on someone's wellbeing.")
   print("Now that you know this, will you help someone achieve something awesome today? \n")

#These are the prompts helping the user answer the question

   willingness_to_help = int(input("Please select an option from the choices above \n"))

#This introduces the variable, and also gives a way for the user to answer the question using the input command.

   if willingness_to_help == 1:

#These are the details and information that happens after the first input, hence the if statement. The == sign is user here to faciliate the comparison.

      print("You understand alot about health and well being! Now, I feel confident telling you... \n")

      Splash2 = """



__   _______ _   _   _    _ _____ _   _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
\ \ / /  _  | | | | | |  | |_   _| \ | | | | | | | | | | | | | | | | |
 \ V /| | | | | | | | |  | | | | |  \| | | | | | | | | | | | | | | | |
  \ / | | | | | | | | |/\| | | | | . ` | | | | | | | | | | | | | | | |
  | | \ \_/ / |_| | \  /\  /_| |_| |\  |_|_|_|_|_|_|_|_|_|_|_|_|_|_|_|
  \_/  \___/ \___/   \/  \/ \___/\_| \_(_|_|_|_|_|_|_|_|_|_|_|_|_|_|_)
                                                                      
                                                                      


      """

      print(Splash2)

#These commands allow for the spalsh art to be printed, and it is used at the end of the game.
#It is used after so the user can clearly see they won, and feel a great sense of accomplishment

   elif willingness_to_help == 2:

#These are the details for the second possible input, hence the elif statement. The == sign is user here to faciliate the comparison.


      print("I disagree, and I don't think that this is the right mindset and attitude to have. Please try again, and stay positive! \n")

      question11()

#This calls the question again if the user gets the answer wrong, so they can try again.

   else:

#The following information is for any input that is not listed, and not valid, hence the else statement.

      print("That is not a valid choice. Please try again \n")

      question11()

#This calls the question again if the user gets an unvalid answer, so they can try again.



def question10():

   global adventure_emotion5

   print("1. Happy")
   print("2. Sad \n")
 
   print("\n After all this, how do you feel?")

   adventure_emotion5 = int(input("Please select one of the options above."))


   if adventure_emotion5 == 1:

      print("That's great, I would feel this way too if I did something like that!")

   elif adventure_emotion5 == 2:

      print("I disagree. After you have done something that you have wanted to do for so long, I don't think you would be sad. Please try again.")

      question10()

   else:

      print("That is not a valid choice. Please try again.")

      question10()


def dive_details():

#This defines this term, hence abridging all the information, and making it more concise when it is time to run the program, making it less confusing.

#This give the user information and details, that is why the following information is only in print statements, and there are no input statements.

   print("\n You float weightlessly through the air for what seemse like hours. The blue pit coming closer to your eyes with every passing second.")
   print(" SPPPPPPISH is the sound your body makes as you make a large splash in the pool.")
   print("As soon as your head reaches the surface of the pool, you begin to search for your family. After what seems like forever, you finally see them.")
   print("They are all laughing and smiling and cheering you on. Your dad has the biggest smile on his face. \n")




def adventure_board_information():

   print(" \n You walk up the board with enthusiasm! You think to yourself that you are ready to do your dive!")
   print("You reach the top of the board, and you look down at the blue pit that is the pool. It seems that the baord is in the sky, and the pool on the ground.")
   print("But the distance does not scare you anymore, and you feel ready. Your toes curl at the edge of the diving board. You take a sharp deep breath.")
   print("And then YOU JUMP! \n")



def question9():

   global adventure_emotion4

   print("1. Look at your family, even though you have a scared expression on your face.")
   print("2. Try and look unphased, and just keep climbing up the ladder.")
   print("3. Do nothing. \n")

   print("\n With your renewed sense of confidence, you walk to the ladder of the tall diving board.")
   print("You climb the first few rungs of the ladder, but suddenly, the uncertain feelings from before come back, and you feel a little scared.")
   print("What do you think you should do? \n")

   adventure_emotion4 = int(input("Please select an option from the choices above. \n"))

   if adventure_emotion4 == 1:

      print("I personally agree, I think that it is ok to look to your family to help you out.")
      print("Your family looks back at you, and they give you a warm smile. Again, your confidence returns and you feel better! \n")

   elif (adventure_emotion4 == 2 or adventure_emotion4 == 3):

      print("I disagree, and I think you can do something better in this situation. Please try again. \n")

      question9()

   else:

      print("That is not a valid choice. Please try again.")

      question9()




def question8():

   global adventure_emotion3

   print("1. Happy")
   print("2. Scared \n")

   print(" \n Your whole family and you arrive at the pool. You walk out onto the warm concrete, and feel the smooth texture under your bare feet.")
   print("You look up, and see how big and tall the diving board is. How do you feel? \n")

   adventure_emotion3 = int(input("Please select an option from the choices above. \n"))

   if adventure_emotion3 == 1:
      print("Awesome, you are ready to do this! \n")

   elif adventure_emotion3 == 2:
      print("You look over at your dad, and he gives you an encouraging nod and smile. After that, you feel better and calmer! \n")

   else:
      print("That is not a valid choice. Please try again. \n")
      question8()


def question7():

   global adventure_diving_place2

   print(" 1. The indoor pool inside your house, with the shorter diving board.")
   print(" 2. The town pool outside your house with the slightly higher diving board. \n")

   print(" \n Your dad asks you where you want to give him his present by doing your dive. Where do you want to do it? \n")

   adventure_diving_place2 = int(input("Please select an option from the choices above. \n"))

   if adventure_diving_place2 == 1:

      print(" \nI think that your decision makes sense, given it is your first dive. But I disagree.")
      print("You have already dived off the indoor diving boards, and I think you should try something new!")
      print("So please try again, and pick where you want to dive. \n")
      
      question7()

   elif adventure_diving_place2 == 2:

      print(" \n I agree, and I think that is the right decision! \n")

   else:

      print(" \n That is not a valid choice, please try again. \n")

      question7()




def question6():

   global mood1

   print("1. Happy")
   print("2. Sad")
   print("3. Scared")
   print("4. Nervous \n")

   print(" \n After you wish your dad a very happy birthday and tell him of the present you intend to give him.")
   print("He laughs a happy laugh as he remembers last year. But he quickly assures you that you do not have to give him a present, especially that one.")
   print("But you have been practicing your swimming for so long, and you know you can do the dive. So you tell your dad to wait and see, as you are going to dive!")
   print("He happily tells you that you can give him his present in half an hour, and that is when he will take the family and you to whatever pool you want.")
   print("Suddenly, the fact that you have to dive finally dawns on you, and you feel a bit odd. How do you feel knowing you will do your first big dive. \n")
   

   mood1 = int(input("Please select one of the options listed above."))

   if mood1 == 1:

      print(" \n That's great. It is good to have a positive and optimistic attitude before you do something you are nervous about!")
      print("But some people may not deal with this stress and little bit of nerves as well as you are.")
      print("Unfortunately, there are a lot of people in the world who don't have a great well-being")
      print("I think that if you do your dive today for your dad, you will feel even happier! So try and do this! \n")

   elif (mood1 == 2 or mood1 == 3 or mood1 == 4):

#This or statement allows for the same response to be given after multiple inputs hence making the code more efficent.

      print(" \n I am so sorry about that, but it makes some sense given the weird situation you are in.")
      print("Unfortuantely, there are alot of people in the world who don't have a great well-being, and their situation is even tougher.")
      print("I think if you do the thing that is making your situation a little difficult, you will be relieved from all the pressure.")
      print("I think if you do the dive, you will be 1000x happier! So try and do this! \n")

   else:

      print("Sorry that is not a valid choice. Please try again.")

      question6()

#______________________________________________________________________________________________________________________________________________________________________________________________

def adventure_comprehension():

   print("\n After 5 long years, you have finally mastered swimming! Your backstroke and frontstroke is incredible! You can even do a pretty good canonball.")
   print("On your dad's birthday last year, you told him that you were going to do a dive off the big board for his next birthday present!")
   print("However, right now you are feeling a little under pressure, as tommorow is your dad's birthday, and you are still a little scared of diving.")
   print("\n You wake up a day later. You run to your dad and wish your dad a very happy birthday.")
   print("You tell him that like you promised last year, you are going to dive for your first time today. This is where your adventure starts!")


def question5():

   global backstory_comprehension1

   print ("1. Yes")
   print("2. No \n")

   #I am incorporating this \n command into my code oftenly. This is to aid with the readability of the instructions and responses to the user.
   #I do not want all the information cramped together, and by putting information on new lines with this command, it is easier to comprehend.

   print("Do you understand the main story behind the book Jabari Jumps? \n")

   backstory_comprehension1 = int(input("Please select an options from the choices above."))

   if backstory_comprehension1 == 1:

      print("\n Great! Here is the imporatant backstory and details for your adventure. \n")

   elif backstory_comprehension1 == 2:

      print("\n That's unfotunate, but it is not a problem! Let me give you a brief summary of the story.")
      print("Young Jabari is full of energy, and after finishing his swimming lessons, he wants to do a dive into the pool. His dad takes him to the pool.")
      print("There, he suffers some minor setbacks as he begins to realize how tough the dive into the pool will be.")
      print("However, after everything, he finishes his dive, and is filled with happiness. Now, you are ready for the backstory of the adventure. \n")

   else:

      print(" \n Sorry, but that is not a valid choice. Please pick the number corresponding to your number. Plese try again. \n")

      question5()


#These are all the defintions for the information that occurs in the backstory
#___________________________________________________________________________________________________________________________________________________________________________________________

def tutorial_information():

   global tutorial_information

   print("Before we start the adventure, let's first do a small tutorial.") 
   print("This tutorial will help you understand the types of questions you will see in the game, and how to answer them.")
   print("This tutorial will also introduce you to the themes of the adventure! Let's get started! \n")

def question4():

   global tutorial_after_dive

   print("1. Run to your mom and let her congratulate you, and also thank her for the pool and diving board and letting your dream come true.")
   print("2. Immeadiatly dive again.")
   print("3. Just swim around. \n")  

   print("After you finish your dive. You are swelled with a sense of pride. What do you do immeadiatly after. \n")
 
   tutorial_after_dive = int(input("Please select an option from the choices above. \n"))


   if (tutorial_after_dive == 2 or tutorial_after_dive == 3):
      print(" \n Sorry, but this answer was wrong. This type of question and theme is important, so please try again. \n")
      question4()

   elif tutorial_after_dive == 1:
      print(" \n Great job. Well done getting the right answer. Now you are ready to read and understand the backstory for the story and game. \n")
      

   else:

      print(" \n Sorry but that is not a valid choice. You know how to do it! So please try again.")

      question4()


def question3():

   global tutorial_diving_board

   print("1. The high and tall diving board")
   print("2. The lower and short diving board \n")


   print("You walk down the stairs, and turn left. Suddenly, in front of you, the shimmering blue water becomes visible to your eyes.")
   print("You are breathtaken at your beautiful new indoor pool! You run down to the ladders, and you look up at the 2 diving boards.")   
   print("You have been dreaming about having your first dive for so long. And now, your time has finally come.")
   print("But, it is only your first dive, and you lack experience. Your mom watches you from the corner of the pool, and she wants you to stay safe. \n")

   print("Where do you think you should dive off for your first dive? \n")

   tutorial_diving_board = int(input("Please select an option from the choices above.\n"))

   if tutorial_diving_board == 1:

      print("\n Intresting choice, but I disagree. I don't think that your first dive should be off the higher diving board with the longer fall. Please try again.\n")
      question3()
   #This calls question 3 again after the user originally got the wrong answer, and it allows them to retry the question, as the concept is important to the game.

   elif tutorial_diving_board == 2:

      print(" \n I agree! I think that you first dive should be a little easier. Congratulations on the right answer. \n")
     

   else:
      print(" \n That is not a valid choice. Please try again.\n")
      question3()
   #This allows the user to retry the question if they select a non valid answer.



def question2():

   global pool_activities 

   print("1. Swimming")
   print("2. Diving")
   print("3. Sleeping")
   print("4. Playing games \n ")

   print("What can you not do in a pool? \n")

   pool_activities = int(input("Please select an option from the choices above. \n"))

   #This defines question 2 of the game 

   #The following lines are responses to all the potential answers from the question called above.

   if (pool_activities == 1 or pool_activities == 2 or pool_activities == 4):

      print (" \n Sorry, but unfortunately this answer is wrong. Please try again and stay positive!") 
      print("But as long as you know how to answer these questions, you are ready for the full tutorial! \n")
      
      question2()

      
   elif pool_activities == 3: 


      print (" \n Well done! That is the correct answer! You are ready for the full tutorial! \n")


   #This calls the third question after the user submits any vaild answer.

   else:

      print(" \n That is not a valid choice. Remember to pick a number :) Please try again.\n")

      question2()

   #This calls the second question again for the user to retry the question. This will help the user learn the style to answer the question.



def question1():

   global diving_place1
#This command makes everything in this definition visible to the program.


#question1 is a variable that represents the first question of the tutorial, and the program displays the following when it is called.

   print("1. Car")
   print("2. Stack of books")
   print("3. Trampoline")
   print("4. Diving board \n")
              
   print("Where do divers dive off of to go into the pool? \n")

   diving_place1 = int(input("Please select an option from the list above. \n"))
   
#This defines question 1, and basically tells the program what the first question is

 #The following lines are responses to all the potential answers from the question called above.


   if (diving_place1 == 1 or diving_place1 == 2 or diving_place1 == 3):

#The or statements are used here, and they streamline the code if there are recurring actions after specific responses, like in this example.

      print(" \n Sorry, but this answer is wrong. However, this is not a big problem.")
      print("It is good that you understand that to answer a question you need to select an option and then input the number for the option.")
      print("In the mean time, please try again. \n")
      
      question1() 
   
   elif diving_place1 == 4:

        print("Great job! Way to go, you got the right answer. Well done, and it is great that you understand how to answer these questions. \n")


   else:

      print(" \n Sorry, unfortunatly that is not a valid choice.")
      print("What you need to do to asnwer these types of questions is look at the options, and pick the option you think is right in your mind.")
      print("Then, look at the number that is associated with that option, and input that.")
      print("For example, if you think the option Diving board is right, then look at the number beside diving board, which is 4.")
      print("Then simply type in 4, then press enter.")
      print("Let's try another example! \n")

#These are all the definitions for the events in the tutorial

#____________________________________________________________________________________________________________________________________________________________________________________________


def tutorial():
   tutorial_information()
   question1()
   question2()
   question3()
   question4()

#This calls all these pieces of information and questions in the tutorial.
   

def backstory():
   question5()
   adventure_comprehension()

#This calls all these pieces of information and questions in the backstory.

def adventure():
   question6()
   question7()
   question8()
   question9()
   adventure_board_information()
   dive_details()
   question10()
   question11()

#This calls all these peices of information and questions in the adventure.

#These defintions are all before the start of the game

########################################################################### This is where the main game begins ####################################################################################


tutorial()
backstory() 
adventure()

#In the game, all these definitions are called, so subsequently all the information in the tutorial, backstory, and adventure are called.

input("When you are finished, please press ENTER to leave the game.")

#This gives the user an easy way to leave the game, leaving them the possibility to replay the game.



