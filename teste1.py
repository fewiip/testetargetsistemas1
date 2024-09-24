import json

lista = [1,2,2,2,3]

jsonteste = '{"janeiro": 2333, "fevereiro": 2444}'
lista2 = json.loads(jsonteste)

print(lista2["janeiro"])
#print(lista2[1])
print(len(lista2))

def adicionaValorLista(lista, valor):
    lista.append(valor)

def media(lista):
    return sum(lista) / len(lista)

def imprimeLista(lista):
    for i in range(len(lista)):
        print(str(lista[i]))
        i = i + 1

def numeroDeDias(lista):
    a = 0

    for i in range(len(lista)):
        if (lista[i] < media(lista)) :
            a = a+1
            #print("o valor " +str(lista[i])+ " é menor que a media " + str(media(lista)))
        
        i = i +1 

    return a

adicionaValorLista(lista,4)

#print( str( lista[len(lista) - 1]))

#imprime o menor valor da lista 
print("o menor valor do dia: ", min(lista) )

#o maior valor da lista 
print("o maior valor do dia:", max(lista) )

print("a media mensal foi", media(lista))

print("o numero de dias menor que a media foi: " ,  str(numeroDeDias(lista)) )