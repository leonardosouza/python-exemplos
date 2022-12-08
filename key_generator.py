tamanho = int(input('Tamanho senha: '))
valores = string.ascii_lowercase + string.digits
senha = ''
for i in range(tamanho):
  senha += choice(valores)

print(senha)