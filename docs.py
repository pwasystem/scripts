import os

def cls():
	os.system("cls" if os.name == "nt" else "clear")

def docCriar():
    cls()
    nome = ""
    while nome == "" :
    	nome = input("Digite o nome do arquivo: ")
    conteudo = input("Digite o conteudo do arquivo: ")
    arquivo = open("docs/" + nome +".txt" ,"w")
    arquivo.write(conteudo)
    arquivo.close()
    input("\n\nO arquivo " + nome +" foi criado com sucesso.\n\nPressione enter para voltar a tela inicial.")

def docListar() :
	cls()
	indice = 1
	arquivos = [""]
	print("Selecione um arquivo ou uma opção da lista abaixo e tecle enter:\n\n\t 0 . Voltar")
	for item in os.listdir("docs/"):
		arquivos.insert(indice, item)
		print("\t", indice, ". " + item.replace(".txt",""))
		indice += 1
	selecao = input("\n")
	try :
		arquivo = arquivos[int(selecao)]
	except :
		input("Arquivo inexistente.\n\nPressione enter para voltar.")
		docListar()
	else:
		if arquivo != "" :
			nome = arquivo.replace(".txt",'')
			try :
				docAcao = int(input("\nEscolha uma opção e pressione enter:\n\n\t0 - Voltar\n\t1 - Ver arquivo " + nome + "\n\t2 - Editar arquivo " + nome + "\n\t3 - apagar arquivo " +nome+ "\n"))
			except :
				docAcao = 0
			else :
				if docAcao == 1:
					docVer(arquivo)
				elif docAcao == 2:
					docEditar(arquivo)
				elif docAcao == 3:
					docApagar(arquivo)
				else :
					docListar()

def docApagar(nome) :
	if os.path.exists("docs/" + nome) :
		os.remove("docs/" + nome)
	input("O arquivo " + nome + " foi apagado com sucesso.\n\nPressione enter para voltar a tela inicial.")

def docEditar(nome):
	conteudo = input("Insira o novo conteudo para o arquivo: ")
	arquivo = open("docs/" + nome,"w")
	arquivo.write(conteudo)
	arquivo.close()
	input("Arquivo " + nome + " editado com sucesso.\n\nPressione enter para voltar ao início.")

def docVer(nome):
	cls()
	arquivo = open("docs/" + nome)
	conteudo = arquivo.read()
	print("Arquivo " + nome + "\n\n" + conteudo)
	input("\n\nPressione enter para voltar ao inicio.")

def menu():
	cls()
	print("Gerenciador de arquivos\n\n\t1 . Listar arquivos\n\t2 . Criar arquivo\n\t3 . Sair")
	try :
		acao = int(input("\nEscolha uma ação:"))
	except :
	    acao = 0
	else :
	 	if acao == 2 :
	 		docCriar()
	 	elif acao == 1 :
	 		docListar()
	 	elif acao == 3 :
	 		global ativo
	 		ativo = 0
	 	else :
	 		input("Ação invalida, pressione enter para voltar.")

ativo = 1

def run():
	while ativo == 1 :
		menu()

run()