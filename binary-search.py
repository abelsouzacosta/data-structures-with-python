# a função retorna a posição de um determinado item dentro de uma lista
# a função recebe a lista e o elemento a ser procurado, e o elemento for encontraod então devemos 
# retornar o indice do mesmo dentro do array

# a função vai usar uma técnica de pesquisa binária para encontrar o valor
def find(array, item):  
  low = 0
  high = len(array) - 1
  while low <= high:
    middle = int((low + high)/ 2) # pega o indice do meio do array
    guess = array[middle] # atribui o elemento do meio do array ao chute
    if guess == item: # se o chute for igual ao item, retorna o indice
      return middle
    if guess > item: # se o chute for maior que o item, diminui o maior indice
      high = middle - 1
    else:
      low = middle + 1 # se o chute for menor que o item, aumenta o menor indice
  return None

number = 5
list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print(f'O número {number} está na posição {find(list, number)}')