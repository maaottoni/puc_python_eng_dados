agenda={}
while True:
    cpf = input('Qual o CPF?:')
    if cpf == '':
        break
    nome = str(input('Qual o nome: '))
    idade = int(input('Qual a idade?:'))
    tel = int(input('Qual o telefone do contato:?'))
    agenda[cpf] = (nome, idade, tel)

print("Agenda" + agenda)
