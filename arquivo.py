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
	docs = [""]
	print("Arquivos disponíveis:\n")
	for item in os.listdir("docs/"):
		docs.insert(indice, item)
		print(indice, ". " + item.replace(".txt",""))
		indice += 1
	docAcao = int(input("\nEscolha uma opção:\n\n\t1 - ver arquivo\n\t2 - editar arquivo\n\t3 - apagar arquivo\n\nOu pressione enter para voltar a tela inicial."))
	if docAcao == 1:
		doc = int(input("Digite o número do arquivo que você deseja ver e pressione enter:"))
		try :
			docVer(docs[doc])
		except IndexError:
			input("Arquivo inexistente.\n\nPressione enter para voltar.")
	elif docAcao == 2:
		doc = int(input("Digite o número do arquivo que você deseja editar e pressione enter:"))
		try :
			docEditar(docs[doc])
		except IndexError:
			input("Arquivo inexistente.\n\nPressione enter para voltar.")
	elif docAcao == 3:
		doc = int(input("Digite o número do arquivo que você deseja apagar e pressione enter:"))
		try :
			docApagar(docs[doc])
		except IndexError :
			input("Arquivo inexistente.\n\nPressione enter para voltar.")

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
	print("Gerenciador de arquivos\n1 . Listar arquivos\n2 . Criar arquivo\n3 . Sair")
	acao = int(input("Escolha uma ação:"))
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