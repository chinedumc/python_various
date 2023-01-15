import random
word_list = ["money", "power", "fame", "book", "apple", "broom"]

stages = [

"""
   _________
    |/        
    |              
    |                
    |                 
    |               
    |                   
    |___                 
    """,

"""
   _________
    |/   |      
    |              
    |                
    |                 
    |               
    |                   
    |___                 
    H""",

"""
   _________       
    |/   |              
    |   (_)
    |                         
    |                       
    |                         
    |                          
    |___                       
    HA""",

"""
   ________               
    |/   |                   
    |   (_)                  
    |    |                     
    |    |                    
    |                           
    |                            
    |___                    
    HAN""",


"""
   _________             
    |/   |               
    |   (_)                   
    |   /|                     
    |    |                    
    |                        
    |                          
    |___                          
    HANG""",


"""
   _________              
    |/   |                     
    |   (_)                     
    |   /|\                    
    |    |                       
    |                             
    |                            
    |___                          
    HANGM""",



"""
   ________                   
    |/   |                         
    |   (_)                      
    |   /|\                             
    |    |                          
    |   /                            
    |                                  
    |___                              
    HANGMA""",


"""
   ________
    |/   |     
    |   (_)    
    |   /|\           
    |    |        
    |   / \        
    |               
    |___           
    HANGMAN"""]

lives = 7
end_game = False

chosen_word = random.choice(word_list)
print(chosen_word)

# This: 
# display = "_" *len((chosen_word))
# display_list = [*display]
# print(display_list)

# Or this:
display = []
for _ in range(len(chosen_word)):
  display += "_"


while not end_game:
  guess = input('Guess a letter from the word\n').lower()


  # Checking if guessed letter is one of the letters of the random word chosen
  for idx in range(len(chosen_word)):
    letter = chosen_word[idx]
    if(letter == guess):
      # print("Element Exists")
      display[idx] = guess

  if guess not in chosen_word:
    lives -= 1
    if lives == 0:
      end_game = True
      print('Game Over')

  print(f"{' '.join(display)}")

  if "_" not in display:
    end_game = True
    print('You win!')
  # print(lives)
  print(stages[(len(stages)-1)-lives])