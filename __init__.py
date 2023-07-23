import os
from funcoes import *

def main():
  end = False
  # saving the random selected word for the game in a variable called 'palavra'
  palavra = read_txt()

  # splits the word
  letras_palavra = []
  for letra in palavra:
      letras_palavra.append(letra)

  # getting the length of the word selected
  tamanho_palavra = len(palavra)

  # creates a string with the same length of the word, but with underlines 
  palavra_underline = list('_'*tamanho_palavra)

  # set the variable erro to zero
  erro = 0

  # prints the underline word
  print('               ', ' '.join(palavra_underline))
  print('\n')

  # creates a list where the typed characters will be saved
  letras_digitadas = []

  # begin the variable 'result' to get the result for each round
  result = ''

  # begin the variable 'vitoria' to get the victory condition
  vitoria = 0

  while not end:
      # for windows
      if os.name == 'nt':
          _ = os.system('cls')

      # for mac and linux(here, os.name is 'posix')
      else:
          _ = os.system('clear')

      # ------------------------------------------

      # ini
      erros(erro)
      print('               ', ' '.join(palavra_underline))
      print('\n')
      print(f'Letras já digitadas: {letras_digitadas}')
      print(f'Quantidade de erros: {erro} / 6')
      print('\n')
      print(result)
      print('\n')
      result, letras_digitadas, erro, end, letras_palavra, palavra_underline, vitoria = tentativas(result, letras_digitadas, erro, end, letras_palavra, palavra_underline, vitoria)

      if vitoria == 1:
         print('*-'*40)
         print('\n')
         print(' '*15 + 'VOCÊ VENCEU !!!')
         print(' '*15 + f'Você acertou a palavra secreta: {palavra.upper()}')
         print('\n')
         print('*-'*40)
      elif vitoria == 2:
         print('*-'*40)
         print('\n')
         print(' '*15 + 'VOCÊ PERDEU !!!')
         print(' '*15 + f'Quantidade de erros: {erro} / 6')
         print(' '*15 + f'A palavra secreta era: {palavra.upper()}')
         print('\n')
         print('*-'*40)
         