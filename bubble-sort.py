# Importa a biblioteca do matplot.
import matplotlib.pyplot as plt 
# Criamos a variável lista e a ordenamos em ordem crescente com o script abaixo.
# Número de elementos da lista.
N = 20
# Indica que a lista possui todos esses elementos.
lista = [11,18,3,1,16,12,6,19,5,0,14,4,17,9,13,7,10,15,2,8] 
# Escreve a lista original.
print("Lista original:", lista)
# Cria uma figura (gráfico) vazia.
plt.figure()
# Desenha um gráfico de pontos pretos com a lista no eixo y e os índices no eixo x.
plt.plot(range(0, N, 1), lista, "ok")
# Permite colocar título nos gráficos e nos eixos (x, y).
plt.title ("Estado inicial")
plt.xlabel("Indices")
plt.ylabel("Valores")
# Salva a figura criada dentro da pasta fig, nomeando-a como bubble-inicio.png.
plt.savefig("fig/bubble-inicio.png")
# Conclui o comando.
plt.close()
# Variável para indicar a troca.  
A = 1
# Variável para indicar a iteração.
B = 1
# Indica que o valor de i começa do 0 e vai até 18, de um em um.
for i in range(0, N-1, 1):
# Indica que o valor de j começa em 1, variando com os valores de i, até 19, de um em um.
    for j in range(i+1, N, 1):
        plt.figure()
        plt.plot(range(0, N, 1), lista, "ok")
        # Plota pontos vermelhos com os valores de i no eixo x e o correspondente na lista i no eixo y.
        plt.plot(i, lista[i], "or")
        # Plota pontos azuis com os valores de i no eixo x e o correspondente na lista i no eixo y.
        plt.plot(j, lista[j], "ob")
        plt.title ("Iteração")
        plt.xlabel("Indices")
        plt.ylabel("Valores")
        # Salva o gráfico dentro da pasta fig e nomeia a figura de acordo com a variação da iteração.
        plt.savefig("fig/bubble-it-{}.png".format(A))
        A = A+1
        plt.close()
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
            # Salva o gráfico dentro da pasta fig e nomeia a figura de acordo com a variação da troca.
            plt.savefig("fig/bubble-troca-{}.png".format(B))
            B = B+1
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
