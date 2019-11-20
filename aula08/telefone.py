# Complete este programa como pedido no guião da aula.

def listContacts(dic):
    """Print the contents of the dictionary as a table, one item per row."""
    print("{:>12s} : {}".format("Numero", "Nome"))
    for num in dic:
        print("{:>12s} : {}".format(num, dic[num]))

def numberToName(contacts, number):
    """Returns the name associated to the given phone number,
    or the same number, if not in the contacts."""
    if number not in contacts:
        print("Não há correspondencia:",number)
    else:
        print("Este número pertence a",contacts[number])

def filterPartName(contacts, partName):
    """Returns a new dict with the contacts whose names contain partName."""
    verifica = False
    for i in contacts.keys():
        if partName.capitalize() in contacts[i]:
            print("O número",i,"é da",contacts[i])
            verifica = True
    if verifica == False:
        print("Não há correspondencia:", partName)

def menu():
    """Shows the menu and gets user option."""
    print()
    print("(L)istar contactos")
    print("(A)dicionar contacto")
    print("(R)emover contacto")
    print("Procurar (N)úmero")
    print("Procurar (P)arte do nome")
    print("(T)erminar")
    op = input("opção? ").upper()   # converts to uppercase...
    return op

def adicionar_contactos(dicionario):
	numero = str(input("Número: "))
	nome = str(input("Nome: "))
	dicionario[numero] = nome

def remover_contactos(dicionario):
	numero = str(input("Número: "))
	if numero not in dicionario:
		print("Não existe")
	else:
		del dicionario[numero]

#MAIN:

# The list of contacts (it's actually a dictionary!):
contactos = {"234370200": "Universidade de Aveiro",
    "727392822": "Cristiano Aveiro",
    "387719992": "Maria Matos",
    "887555987": "Marta Maia",
    "876111333": "Carlos Martins",
    "433162999": "Ana Bacalhau"
    }

op = ""
while op != "T":
    op = menu()
    if op == "T":
        print("Fim")
    elif op == "L":
        print("Contactos:")
        listContacts(contactos)
    elif op == "A":
        adicionar_contactos(contactos)
    elif op == "R":
        remover_contactos(contactos)
    elif op == "N":
        number = input("Qual é o número que pretende procurar? ")
        numberToName(contactos, number)
    elif op == "P":
        partName = input("Qual é o nome que pretended procurar? ")
        filterPartName(contactos, partName)
    else:
        print("Não implementado!")