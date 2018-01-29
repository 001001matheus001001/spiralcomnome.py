#SpiralMyName.py - exibe espiral colorida com o nome do usuário
#script feito por Matheus Silva
#29/01/2018 hs 01:15
#Dependencias Python3 é python3-tk 
#obs: não tenho formação em programação então descupe-me por algum
#Defeito devido a erros. "Tudo se aproveita nada se perde" !

import turtle   #importa os graficos da tartaruga
t = turtle.Pen()
turtle.bgcolor("black")
colors =["red", "yellow", "blue", "green"]

# Pede o nome do usuário usando a janela pop-up do turtle para
# entrada de texto
your_name = turtle.textinput("Entre com seu nome:", "qual é seu nome ?")

#desenha um espiral na tela usando o nome, escrevendo-o 100 vezes

for x in range(100):
    t.pencolor(colors[x%4])        #circula pelas quatro linhas
    t.penup()         #não desenha as linhas normais da espiral
    t.forward(x*4)           #apenas move a tartaruga pela tela
    t.pendown()                  #escreve o nome cada vez maior
    t.write(your_name, font = ("Arial", int( (x + 4) / 4), "bold") )
    t.left(92)
