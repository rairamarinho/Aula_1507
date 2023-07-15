def exibir_menu():
    print("Escolha uma opção:")
    print("1 - Cadastrar Aluno(a)")
    print("2 - Remover Aluno(a)")
    print("3 - Editar Aluno(a)")
    print("4 - Listar Alunos")
    print("5 - Sair")

def cadastrar_aluno():
    print("Vai salvar esse aluno em um arquivo no formado JSON")
    # Fazer uma exception para verificar se o CPF tem 11 digitos.
    # Opcional: Para bater as paradas: Validar o email, para verificar.

while True:
    exibir_menu()
    escolha = input()
    if escolha == 1:
