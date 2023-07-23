# read the txt file with the list of fruits available and return a random fruit from it
def read_txt():
    import random
    frutas = open('frutas.txt','r', encoding='utf-8-sig')

    # getting a random number between 1 and 42
    number = random.randint(1,42) 
    number

    # saving the 'number'th line from 'frutas.txt' in 'palavra'
    for palavra in range(number):
      palavra = frutas.readline()
    
    # cleaning the '\n' from reading the line and saving only the word in 'palavra'
    palavra = palavra.split()[0]

    # returning the 'number'th fruit from 'frutas.txt' list
    return palavra

# -----------------------------------------------------------------------------------------------------------------

# prints the structure according to the amount of errors
def erros(erro):
    erro_0 = """
      _______
      |      |
      |
      |
      |
      |
      |
   ___|___
    """
    erro_1 = """
      _______
      |      |
      |      _
      |     |_|
      |
      |
      |
   ___|___
    """

    erro_2 = ("""
      _______
      |      |
      |      _
      |     |_|
      |      |
      |      |
      |
   ___|___
    """)

    erro_3 = ("""
      _______
      |      |
      |      _
      |     |_|
      |    --|
      |      |
      |
   ___|___
    """)

    erro_4 = ("""
      _______
      |      |
      |      _
      |     |_|
      |    --|--
      |      |
      |
   ___|___
    """)

    erro_5 = ("""
      _______
      |      |
      |      _
      |     |_|
      |    --|--
      |      |
      |     /
   ___|___
    """)

    erro_6 = ("""
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
    if erro == 0:
        print(erro_0)

    # IF conditions to print the structures with the correct amount of errors made
    elif erro == 1:
        print(erro_1)
    elif erro == 2:
        print(erro_2)
    elif erro == 3:
        print(erro_3)
    elif erro == 4:
        print(erro_4)
    elif erro == 5:
        print(erro_5)
    else:
        print(erro_6)

# -------------------------------------------------------------------------------------------------------------------------

# checks the user attempt
def tentativas(result, letras_digitadas, erro, end, letras_palavra, palavra_underline, vitoria):
  letra_tentativa = input('Digite uma letra: ').lower()
  if letra_tentativa in letras_digitadas:
    result = f'Tente outra letra. A letra [{letra_tentativa}] já foi usada!'
  else:
    count = 0
    tentativa_errada = 0
    for letra in letras_palavra:
      if letra_tentativa == letra:
        palavra_underline[count] = letra_tentativa
        result = ''
      else:
        tentativa_errada += 1
      count += 1
    if (count == tentativa_errada) and (erro < 6):
      result = f'Você errou! Tente outra letra.'
      erro += 1
      erros(erro)
    letras_digitadas.append(letra_tentativa)

  if letras_palavra == palavra_underline:
    vitoria = 1
    end = True
  
  if erro == 6:
    vitoria = 2
    end = True

  return result, letras_digitadas, erro, end, letras_palavra, palavra_underline, vitoria