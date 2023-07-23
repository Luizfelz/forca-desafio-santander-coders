# import all the functions from 'functions.py'
from functions import *

# main function
def main():
  end = False
  # saving the random selected word for the game in a variable called 'word'
  word = read_txt()

  # splits the word
  letters_word = []
  for letter in word:
      letters_word.append(letter)

  # getting the length of the word selected
  len_word = len(word)

  # creates a string with the same length of the word, but with underlines 
  word_underline = list('_'*len_word) 

  # set the variable error to zero
  error = 0

  # creates a list where the typed characters will be saved
  typed_letters = []

  # begin the variable 'result' to get the result for each round
  result = ''

  # begin the variable 'victory' to get the victory condition
  victory = 0

  while not end:
      # clear the prompt
      clear_prompt()

      # start the drawing 
      errors(error)

      # prints the secret word with underlines
      print('               ', ' '.join(word_underline))
      print('\n')
      
      # shows the characters already typed
      print(f'Typed characters: {typed_letters}')
      
      # shows the total amount of errors
      print(f'Errors: {error} / 6')
      print('\n')
      
      # shows an informative message to the user: if he typed a wrong character or repeated a character
      print(result)
      print('\n')

      # calls the function that verifies the attempt
      result, typed_letters, error, end, letters_word, word_underline, victory = trys(result, typed_letters, error, end, letters_word, word_underline, victory)

      #shows the final message to the user when the game finishes: 1 to WIN or 2 to LOST
      if victory == 1:
         clear_prompt()
         errors(error)
         print('*-'*40)
         print('\n')
         print(' '*15 + 'YOU WIN !!!')
         print(' '*15 + f'You got the word right: {word.upper()}')
         print('\n')
         print('*-'*40)
      
      elif victory == 2:
         clear_prompt()
         errors(error)
         print('*-'*40)
         print('\n')
         print(' '*15 + 'YOU LOST !!!')
         print(' '*15 + f'Errors: {error} / 6')
         print(' '*15 + f'The secret word was: {word.upper()}')
         print('\n')
         print('*-'*40)
         