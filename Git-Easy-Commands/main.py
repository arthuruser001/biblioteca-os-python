import os
import branchmanager

print('Bem-vindo ao Git Easy Commands!')
codigo_input = input('Digite 1 para acessar a área de gereciamento de branches.')
if (codigo_input == '1'):
    print('Bem vindo ao gerenciador de branches!')
    print('Digite 1 para criar um novo branch.')
    print('Digite 2 para deletar um branch.')
    print('Digite 3 para mudar de branch.')
    print('Digite 4 para listar as branches. (Dentro do Dispositivo)')
    print('Digite 5 para listar as branches. (Somente as branches remotas)')
    print('Digite 6 para listar as branches. (Todas as branches)')
    print('Digite 7 para renomear a branch atual.')
    opcao = input('Escolha uma opção: ')
    if (opcao == '1'):
        branchmanager.NewBranch()
    elif (opcao == '2'):
        branchmanager.DeleteBranch()
    elif (opcao == '3'):
        branchmanager.SwitchBranch()
    elif (opcao == '4'):
        branchmanager.ListLocalBranches()
    elif (opcao =='5'):
        branchmanager.ListRemoteBranches()
    elif (opcao == '6'):
        branchmanager.ListAllBranches()
    elif (opcao == '7'):
        branchmanager.RenameBranch()
    else:
        print('Opção inválida!')

