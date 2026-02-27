import os

def NewBranch():
    name = str(input('Digite o nome do novo branch: '))
    confirm = ''
    while(confirm != 's' and confirm != 'n'):
        confirm = str(input('Você tem certeza que deseja criar um novo branch chamado {}? (y ou n)'.format(name)))
        if(confirm == 's'):
            print('Criando branch...')
            os.system('git branch {}'.format(name))
            print('Branch criado (Por enquanto não temos verificação de erro).')
        elif(confirm == 'n'):
            print('Fechando aplicação...')
            exit()
        else:
            print('Valor de confirmação inválido, por favor digite s ou n.')
    print('Fechando aplicação...')

def DeleteBranch():
    name = str(input('Digite o nome do branch que deseja deletar: '))
    confirm = ''
    while(confirm != 's' and confirm != 'n'):
        confirm = str(input('Você tem certeza que deseja deletar o branch {}? (y ou n)'.format(name)))
        if(confirm == 's'):
            print('Deletando branch...')
            os.system('git branch -d {}'.format(name))
            print('Branch deletado (Por enquanto não temos verificação de erro).')
        elif(confirm == 'n'):
            print('Fechando aplicação...')
            exit()
        else:
            print('Valor de confirmação inválido, por favor digite s ou n.')
    print('Fechando aplicação...')

def SwitchBranch():
    name = str(input('Digite o nome do branch que deseja mudar: '))
    confirm = ''
    while(confirm != 's' and confirm != 'n'):
        confirm = str(input('Você tem certeza que deseja mudar para o branch {}? (y ou n)'.format(name)))
        if(confirm == 's'):
            print('Mudando de branch...')
            os.system('git checkout {}'.format(name))
            print('Branch mudado (Por enquanto não temos verificação de erro).')
        elif(confirm == 'n'):
            print('Fechando aplicação...')
            exit()
        else:
            print('Valor de confirmação inválido, por favor digite s ou n.')
    print('Fechando aplicação...')

def ListLocalBranches():
    print('Listando branches locais...')
    os.system('git branch')

def ListAllBranches():
    print("Listando branches locais e remotos...")
    os.system('git branch -a')

def ListRemoteBranches():
    print('Listando branches remotos...')
    os.system('git branch -r')


        

