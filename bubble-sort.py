# Criamos a variável lista e a ordenamos em ordem crescente com o script abaixo.
# Número de elementos da lista.
N = 20
# Indica que a lista possui todos esses elementos.
lista = [11,18,3,1,16,12,6,19,5,0,14,4,17,9,13,7,10,15,2,8] 
print("Lista original:", lista)

import matplotlib.pyplot as plt
plt.figure()
plt.plot(range(0, N, 1), lista, "ok")
plt.title ("Estado inicial")
plt.xlabel("Indices")
plt.ylabel("Valores")
plt.savefig("fig/bubble-inicio.png")
plt.close()
A = 1
# Indica que o valor de i começa do 0 e vai até 18, de um em um.
for i in range(0, N-1, 1):
# Indica que o valor de j começa em 1, variando com os valores de i, até 19, de um em um.
    for j in range(i+1, N, 1):
# Condiciona que: se a lista i for maior que a lista j, ele deve executar a mudança abaixo.
        if lista[i] > lista[j]: 
# Coloca a lista i num aquivo temporario, chamado temp.
            temp = lista[i] 
# Coloca a lista j no lugar da lista i.
            lista[i] = lista[j] 
# Coloca o arquivo temporario na lista j.
            lista[j] = temp
            plt.figure()
            plt.plot(range(0, N, 1), lista, "ok")
            plt.title ("Troca")
            plt.xlabel("Indices")
            plt.ylabel("Valores")
            plt.savefig("fig/bubble-troca-{}.png".format(A))
            A = A+1
            plt.close()
# Escreve no terminal a lista ordenada.			
print("Lista em ordem crescente:", lista)

plt.figure()
plt.plot(range(0, N, 1), lista, "ok")
plt.title ("Estado final")
plt.xlabel("Indices")
plt.ylabel("Valores")
plt.savefig("fig/bubble-fim.png")
plt.close()

# Indica a lista no intervalo de 14 a 19.
lista[N-5:N]
# Imprime a lista no intervalo de 14 a 19.
print("Cinco maiores valores:", lista[N-5:N])
# Indica a lista no intervalo de 0 a 4.
lista[0:5]
# Imprime a lista no intervalo de 0 a 4.
print("Cinco menores valores:", lista[0:5])					
