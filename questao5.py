texto= input("Informe a string a ser invertida:")

invertida=[]

fim=len(texto)-1

for i in range(len(texto)):
    invertida.append(texto[fim])
    fim=fim-1

invertida=''.join(invertida)

print(invertida)