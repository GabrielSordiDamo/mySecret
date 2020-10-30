import os
import dotenv
import fileAccess.fAccess as fAccess
import envVariables.eVars as eVars
import securing.crypto as crypto


dotenv.load_dotenv(dotenv_path='.env')


def isFirstRun():
    if not os.environ['KEY_OF_THE_SECRET']:
        return True
    return False


def gatherKeyAndSecret():
    print(f'{os.environ["username"]} PRONTO PARA GUARDAR SEUS SEGREDOS?')
    print('Digite seus segredos eles serao criptografados\nUma chave privada sera gerada para voce')

    unencryptedSecret = input('Por favor digite seu segredo:')
    encryptMessage, _, getKey = crypto.generateEncrypterAndDecrypter()
    encryptedSecret = encryptMessage(unencryptedSecret)
    encryptionKey = getKey()

    generateExtraFile = None
    while generateExtraFile != 1 and generateExtraFile != 0:
        print(f'{os.environ["USERNAME"]}  sua senha sera salva',
              '\nDentro do arquivo .env.',
              '\n Voce deseja gerar um arquivo texto extra',
              '\n com a chave?')
        generateExtraFile = int(input('(1) Sim, (0) Nao: '))
    fAccess.openAndWrite(
        f'{os.environ["USERNAME"]}_SECRETS_KEY', encryptionKey) if generateExtraFile else None

    os.environ['KEY_OF_THE_SECRET'] = f'{encryptionKey}'
    eVars.updateEnvVar('KEY_OF_THE_SECRET', encryptionKey)
    eVars.updateEnvVar('OWNER_OF_KEY', f'{os.environ["USERNAME"]}')

    fAccess.openAndWrite(f'{os.environ["USERNAME"]}_SECRET', encryptedSecret)

    print('A versao criptografada do seu segredo foi guardada',
          f'\nNa pasta {os.environ["USERNAME"]}_SECRET', '\nPARA O PROGRAMA FUNCINAR CORRETAMENTE, POR FAVOR', '\tNAO MOVA OS ARQUIVOS DE DIRETORIO')

    dotenv.set_key('.env', 'KEY_OF_THE_SECRET', f'{encryptionKey}')
    dotenv.set_key('.env', 'OWNER_OF_KEY', os.environ["USERNAME"])
    print('Variaveis de ambiente resetadas')


def notFirstRun():
    if os.environ['USERNAME'] == dotenv.get_key('.env', 'OWNER_OF_KEY'):
        print(
            f'{os.environ["USERNAME"]}, verifiquei que voce e o portador do segredo')
        print('Por favor selecine uma opcao')
        option = None
        while option not in [1, 2, 3, 4]:
            print('1 - Apagar os arquivos criados por esse programa',
                  'e resetar as variaveis de ambiente ')
            print('2 - Descriptar e mostar o segredo')
            print('3 - Modificar o segredo')
            print('4 - Sair do programa')
            option = int(input())
        if option == 1:
            fAccess.removeFile(
                f'{os.environ["USERNAME"]}_SECRET', 'Arquivo do segredo removido com sucesso')
            fAccess.removeFile(
                f'{os.environ["USERNAME"]}_SECRETS_KEY', 'Arquivo de chave removido com sucesso')
            dotenv.set_key('.env', 'KEY_OF_THE_SECRET', '')
            dotenv.set_key('.env', 'OWNER_OF_KEY', '')
            print('Variavies de ambiente resetadas com sucesso')
        elif option == 2 or option == 3:
            encryptMessage, decryptMessage, getKey = crypto.generateEncrypterAndDecrypter(
                os.environ['KEY_OF_THE_SECRET'])
            decryptedSecret = decryptMessage(
                fAccess.openAndRead(f'{os.environ["USERNAME"]}_SECRET'))
            print(f'Seu segredo e: \n {decryptedSecret}')
            if option == 3:
                newSecret = input('Digite o novo segredo: ')
                encryptSecret = encryptMessage(newSecret)
                fAccess.openAndWrite(
                    f'{os.environ["USERNAME"]}_SECRET', encryptSecret)
                print('Segredo atualizado')
        else:
            exit(0)
    else:
        print('Verifiquei que nao foi voce que criou o segredo',
              '\nAte mais!')


def main():
    if isFirstRun():
        gatherKeyAndSecret()
    else:
        notFirstRun()


main()
