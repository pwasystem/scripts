import tkinter as tk
from tkinter import ttk, messagebox

pets = []
next_pet_id = 1

root = tk.Tk()
root.title("Sistema de Cadastro de Pets")
root.geometry("800x500")

frame_form = ttk.LabelFrame(root,text="Formulário de Pet")
frame_form.pack(padx=10, pady=5, fill="x")

ttk.Label(frame_form, text="Tutor:").grid(row=0, column=0, padx=5, pady=5, sticky="e")
entry_tutor = ttk.Entry(frame_form, width=40)
entry_tutor.grid(row=0, column=1, padx=5, pady=5)

ttk.Label(frame_form, text="Nome:").grid(row=1, column=0,padx=5, pady=5, sticky="e")
entry_nome = ttk.Entry(frame_form, width=40)
entry_nome.grid(row=1, column=1, padx=5, pady=5)

ttk.Label(frame_form, text="Espécie:").grid(row=2, column=0,padx=5, pady=5, sticky="e")
entry_especie = ttk.Entry(frame_form, width=40)
entry_especie.grid(row=2, column=1, padx=5, pady=5)

ttk.Label(frame_form, text="Raça:").grid(row=3, column=0,padx=5, pady=5, sticky="e")
entry_raca = ttk.Entry(frame_form, width=40)
entry_raca.grid(row=3, column=1, padx=5, pady=5)

ttk.Label(frame_form, text="Idade:").grid(row=4, column=0,padx=5, pady=5, sticky="e")
entry_idade = ttk.Entry(frame_form, width=40)
entry_idade.grid(row=4, column=1, padx=5, pady=5)

frame_botoes = ttk.LabelFrame(root)
frame_botoes.pack(pady=5)

btn_adicionar = ttk.Button(frame_botoes, text="adicionar", command=None)
btn_adicionar.grid(row=0, column=0, padx=5)

btn_editar = ttk.Button(frame_botoes, text="editar", command=None)
btn_editar.grid(row=0, column=1, padx=5)

btn_remover = ttk.Button(frame_botoes, text="remover", command=None)
btn_remover.grid(row=0, column=2, padx=5)

btn_limpar = ttk.Button(frame_botoes, text="Limpar",command=None)
btn_limpar.grid(row=0, column=3, padx=5)

frame_tabela = ttk.LabelFrame(root)
frame_tabela.pack(pady=5,padx=10,fill="both",expand=True)

tree = ttk.Treeview(frame_tabela, column = ('ID','Tutor','Nome','Espécie', 'Raça', 'Idade'), show='headings')
tree.heading('ID', text='ID')
tree.heading('Tutor', text='Tutor')
tree.heading('Nome', text='Nome')
tree.heading('Espécie', text='Espécie')
tree.heading('Raça', text='Raça')
tree.heading('Idade', text='Idade')

root.mainloop()