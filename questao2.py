numero= int(input("Informe o número procurado:"))

fibonacci=[0,1]

while fibonacci[-1] < numero:
    fibonacci.append(fibonacci[-1]+fibonacci[-2])

print(fibonacci)

if numero in fibonacci:
    print("O numero está presente na sequencia de fibonacci")
else:
    print("O numero não está presente na sequencia de fibonacci")

