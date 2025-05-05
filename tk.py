# import tkinter as tk
from tkinter import *

#Janela
root = Tk()
root.title("Aula Tk")



# Botão

btnFechar = Button(root, text="Fechar", command=root.destroy).grid(row=100, columnspan=2, stick=E)
# btnFechar.pack()

#Rótulos
labNome = Label(root, text="Nome").grid(row=1)
labConteudo = Label(root, text="Conteudo").grid(row=2)

#entradas
entNome = Entry(root).grid(row=1,column=1)
entConteudo = Entry(root).grid(row=2,column=1)

#botao de verificacao
var1 = IntVar()
var2 = IntVar()
Checkbutton(root,text="opt 1",variable=var1).grid(row=3, stick=W)
Checkbutton(root,text="opt 2",variable=var2).grid(row=4, stick=W)
#var3 = Checkbutton(root,text="opt 3").grid(row=5, stick=W)

#botao de opcao
var4 = IntVar()
Radiobutton(root, text="Selecao 1", variable=var4, value=1).grid(row=5, stick=W)
Radiobutton(root, text="Selecao 2", variable=var4, value=2).grid(row=6, stick=W)


#barra
scrollbar = Scrollbar(root, orient=VERTICAL)
#scrollbar.grid(side=RIGHT, fill=Y)

#caixa de listagem
lb = Listbox(root, yscrollcommand=scrollbar.set)
for line in range(20) :
	lb.insert(END,"opt " + str(line))
#lb.insert(2,'opt 2')

scrollbar.config(command=lb.yview)

lb.grid(row=7,stick=(N,S,E,W))
scrollbar.grid(row=7,column=1, stick=(N,S,W))


#menu
menu = Menu(root)
root.config(menu=menu)

filemenu = Menu(menu)
menu.add_cascade(label="Arquivo",menu=filemenu)
filemenu.add_command(label="Novo")
filemenu.add_command(label="Abrir")
filemenu.add_separator()
filemenu.add_command(label="Sair", command=root.quit)

helpmenu = Menu(menu)
menu.add_cascade(label="Ajuda",menu=helpmenu)
helpmenu.add_command(label="Sobre")
helpmenu.add_command(label="Ajuda")


root.mainloop()