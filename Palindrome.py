word = input('Insira a palavra para checar se é um palíndromo: ')
word = str(word)
if str(word) == str(word)[::-1]:
    print(f'A palavra "{word}" é palíndromo!')
else:
    print(f'A palavra "{word}" não é um palíndromo.')
