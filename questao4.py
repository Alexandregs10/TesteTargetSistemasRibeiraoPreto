# 4) Descubra a lógica e complete o próximo elemento:
# a) 1, 3, 5, 7, ___
# b) 2, 4, 8, 16, 32, 64, ____
# c) 0, 1, 4, 9, 16, 25, 36, ____
# d) 4, 16, 36, 64, ____
# e) 1, 1, 2, 3, 5, 8, ____
# f) 2,10, 12, 16, 17, 18, 19, ____

#Respostas
a = 1, 3, 5, 7, 9
b = 2, 4, 8, 16, 32, 64, 128
c =  0, 1, 4, 9, 16, 25, 36, 49
d = 4, 16, 36, 64, 100
e = 1, 1, 2, 3, 5, 8, 13
f = 2, 10, 12, 16, 17, 18, 19, 20    

def proximo_impar(sequencia):
    ultimo_numero = sequencia[-1]
    return ultimo_numero + 2

def proximo_geometrico(sequencia):
    razao = sequencia[1] / sequencia[0]
    return sequencia[-1] * razao

def proximo_quadrado(sequencia):
    ultimo_indice = int(sequencia[-1]**0.5)
    return (ultimo_indice + 1)**2

def proximo_quadrado_par(sequencia):
    ultimo_indice = int(sequencia[-1]**0.5)
    proximo_par = ultimo_indice + 2
    return proximo_par**2

def proximo_fibonacci(sequencia):
    return sequencia[-1] + sequencia[-2]

def proximo_incremental(sequencia):
    return sequencia[-1] + 1

sequencia_a = [1, 3, 5, 7]
sequencia_b = [2, 4, 8, 16, 32, 64]
sequencia_c = [0, 1, 4, 9, 16, 25, 36]
sequencia_d = [4, 16, 36, 64]
sequencia_e = [1, 1, 2, 3, 5, 8]
sequencia_f = [2, 10, 12, 16, 17, 18, 19]

proximo_elemento_a = proximo_impar(sequencia_a)
proximo_elemento_b = int(proximo_geometrico(sequencia_b))
proximo_elemento_c = proximo_quadrado(sequencia_c)
proximo_elemento_d = proximo_quadrado_par(sequencia_d)
proximo_elemento_e = proximo_fibonacci(sequencia_e)
proximo_elemento_f = proximo_incremental(sequencia_f)

print(f"Próximo elemento da sequência a): {proximo_elemento_a}")
print(f"Próximo elemento da sequência b): {proximo_elemento_b}")
print(f"Próximo elemento da sequência c): {proximo_elemento_c}")
print(f"Próximo elemento da sequência d): {proximo_elemento_d}")
print(f"Próximo elemento da sequência e): {proximo_elemento_e}")
print(f"Próximo elemento da sequência f): {proximo_elemento_f}")
