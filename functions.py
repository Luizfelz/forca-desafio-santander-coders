# clear the prompt
def clear_prompt():
    import os

    # for windows
    if os.name == 'nt':
      _ = os.system('cls')

    # for mac and linux(here, os.name is 'posix')
    else:
      _ = os.system('clear')

# -----------------------------------------------------------------------------------------------------------------

# read the txt file with the list of fruits available and return a random fruit from it
def read_txt():
    import random
    fruits = open('frutas.txt','r', encoding='utf-8-sig')

    # getting a random number between 1 and 42
    number = random.randint(1,42) 

    # saving the 'number'th line from 'frutas.txt' in 'word'
    for word in range(number):
      word = fruits.readline()
    
    # cleaning the '\n' from reading the line and saving only the word in 'word'
    word = word.split()[0]

    # closes the file
    fruits.close()

    # returning the 'number'th fruit from 'frutas.txt' list
    return word

# -----------------------------------------------------------------------------------------------------------------

# prints the structure according to the amount of errors
def errors(error):
    error_0 = """
      _______
      |      |
      |
      |
      |
      |
      |
   ___|___
    """
    error_1 = """
      _______
      |      |
      |      _
      |     |_|
      |
      |
      |
   ___|___
    """

    error_2 = ("""
      _______
      |      |
      |      _
      |     |_|
      |      |
      |      |
      |
   ___|___
    """)

    error_3 = ("""
      _______
      |      |
      |      _
      |     |_|
      |    --|
      |      |
      |
   ___|___
    """)

    error_4 = ("""
      _______
      |      |
      |      _
      |     |_|
      |    --|--
      |      |
      |
   ___|___
    """)

    error_5 = ("""
      _______
      |      |
      |      _
      |     |_|
      |    --|--
      |      |
      |     /
   ___|___
    """)

    error_6 = ("""
      _______
      |      |
      |      _
      |     |_|
      |    --|--
      |      |
      |     / \\
   ___|___
    """)

    # printing the main structure of the Forca, with zero errors
    if error == 0:
        print(error_0)

    # IF conditions to print the structures with the correct amount of errors made
    elif error == 1:
        print(error_1)
    elif error == 2:
        print(error_2)
    elif error == 3:
        print(error_3)
    elif error == 4:
        print(error_4)
    elif error == 5:
        print(error_5)
    else:
        print(error_6)

# -------------------------------------------------------------------------------------------------------------------------

# checks the user attempt
def trys(result, typed_letters, error, end, letters_word, word_underline, victory):
  # saves the letter typed by the user
  letter_try = input('Type a letter: ').lower()

  # checks if the typed is already in the list with all the typed letters. If TRUE, it returns a message stating that
  if letter_try in typed_letters:
    result = f'Try another letter. The letter [{letter_try}] has already been used!'
  
  else:
    # error quantity checker 
    count = 0

    # error counter
    wrong_try = 0

    # checks letter by letter in the secret word. If the typed letter is equal to a letter in the secret word, it substitute 
    # the underline for the correct letter
    for letra in letters_word:
      if letter_try == letra:
        word_underline[count] = letter_try
        result = ''
      
      # if the letter is not in the secret word, it cunts 1 error and state it to the user
      else:
        wrong_try += 1
      count += 1
    
    # checks if the user typed a wrong letter and state it to the user, as long as the total amount of error is below the 
    # maximum allowed (=6)
    if (count == wrong_try) and (error < 6):
      result = f'You missed! Try another letter.'
      error += 1
      errors(error)
    typed_letters.append(letter_try)
  
  # checks if all the letters in the secret word have already been discoverd. If so, it ends the game and state it to the user
  if letters_word == word_underline:
    victory = 1
    end = True
  
  # checks the amount of errors commited by the user. If it is equal to the maximum error allowed (=6), it ends the game and
  # state it tho the user
  if error == 6:
    victory = 2
    end = True

  return result, typed_letters, error, end, letters_word, word_underline, victory
