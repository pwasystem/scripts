import tkinter

root = tkinter.Tk()
root.title("hello")
root.geometry("800x600")

labelFrase = tkinter.Label(root,
                           text='texto',
                           font=('verdana',32),
                           fg="blue",
                           bg="red")
labelFrase.pack(padx=5,pady=5)

labelNome = tkinter.Label(root,
                          text="Digite seu nome")
labelNome.pack(padx=5,pady=5)

entryNome = tkinter.Entry(root)
entryNome.pack(padx=5,pady=5)

buttonGravar = tkinter.Button(root,
                              text = "gravar",
                              command = None)
buttonGravar.pack(padx=5,pady=5)

root.mainloop()