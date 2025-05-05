import tkinter as tk
from tkinter import messagebox

diretorio ="docs"

def doxCriar() :
#	dox = open(diretorio + "/" +entryNome.get(),"w")
#	dox.write(entryConteudo.get())
#	dox.close()
	entryNome.delete(0,"end")
	entryConteudo.delete(0,"end")
	messagebox.showinfo("Criar arquivo","Arquivo criado com sucesso.")


root = tk.Tk()
root.title("hello")
root.geometry("800x600")

labelFrase = tk.Label(root, text='Gerenciador de arquivos', font=('verdana',14))
labelFrase.pack(padx=5,pady=5)

labelNome = tk.Label(root, text="Digite um nome para o novo arquivo:")
labelNome.pack(padx=5,pady=5)

entryNome = tk.Entry(root)
entryNome.pack(padx=5,pady=5)

labelConteudo = tk.Label(root, text="Digite o conteúdo do novo arquivo:")
labelConteudo.pack(padx=5,pady=5)

entryConteudo = tk.Entry(root)
entryConteudo.pack(padx=5,pady=5)

buttonGravar = tk.Button(root,
                              text = "Criar",
                              command = doxCriar)
buttonGravar.pack(padx=5,pady=5)

root.mainloop()