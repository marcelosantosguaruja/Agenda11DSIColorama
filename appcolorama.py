# ********************************************
# ** Listas e Funções com uso de biblioteca **
# ** Colorindo o programa com colorama      **
# ********************************************

# importando comandos de systema para limpar tela
import os
os.system("cls")

from colorama import Fore, Style, init

# Inicializa a biblioteca Colorama
init(autoreset=True)

# Criação da Lista de produtos
produtos = ["Pizzas", "Bebidas", "Sobremesas"]

# Função para exibir os produtos
def mostrar_produtos(lista):
    print(Fore.BLUE +"Loja Aberta - Lista de Produtos Disponíveis")
    for produto in lista:
        print(Fore.RED + produto)

# Chamada da função
mostrar_produtos(produtos)