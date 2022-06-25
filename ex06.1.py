#Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e todos as informações sobre ela
n =input('Digite algo:')
print('O tipo primitivo é', type(n))
print('É um número?', n.isnumeric())
print('É um número e uma letra?', n.isalnum())
print('É uma letra?', n.isalpha())
print('Possui letras maiúsculas?', n.isupper())