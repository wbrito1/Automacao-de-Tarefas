# Bibliotecas

import pyautogui
import time
import pandas as pd

# Passo 1: Abrir o sistema da empresa
# Passo 2: Fazer Login
# Passo 3: Importar a base da dados dos produtos
# Passo 4: Cadastrar um produto
# Passo 5: Repetir o passo 4 até acabar todos os produtos

#Pausa o tempo entre uma linha e outra
pyautogui.PAUSE = 1

link_sistema = "https://dlp.hashtagtreinamentos.com/python/intensivao/login"
pyautogui.press("win")

pyautogui.write("chrome")

pyautogui.press("enter")

pyautogui.write(link_sistema)

pyautogui.press("enter")

time.sleep(3)

pyautogui.click(x=946, y=613)

pyautogui.write("projetospython2409@gmail.com")

pyautogui.press("tab")

pyautogui.write("123456")

pyautogui.press("tab")

pyautogui.press("enter")

tabela = pd.read_csv("produtos.csv")
print(tabela)

time.sleep(3)
for linha in tabela.index:
    pyautogui.click(x=900, y=441)
    
    codigo = str(tabela.loc[linha, "codigo"])
    pyautogui.write(codigo)
    pyautogui.press("tab")

    marca = str(tabela.loc[linha, "marca"])
    pyautogui.write(marca)
    pyautogui.press("tab")

    tipo = str(tabela.loc[linha, "tipo"])
    pyautogui.write(tipo)
    pyautogui.press("tab")

    categoria = str(tabela.loc[linha, "categoria"])
    pyautogui.write(categoria)
    pyautogui.press("tab")

    preco_unitario = str(tabela.loc[linha, "preco_unitario"])
    pyautogui.write(preco_unitario)
    pyautogui.press("tab")

    custo = str(tabela.loc[linha, "custo"])
    pyautogui.write(custo)
    pyautogui.press("tab")
    
    obs = str(tabela.loc[linha, "obs"])
    if obs != "nan":
        pyautogui.write(obs)

    pyautogui.click(x=1160, y=1436)
    
    pyautogui.scroll(5000)