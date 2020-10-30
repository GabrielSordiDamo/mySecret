import os


def isKeyOnEnvDict(key, message=None):
    '''True if is on dict false otherwise '''
    try:
        os.environ[key]
        print(message if message else f'A chave {key} ja se encontra nas suas variaveis de ambiente, \
                {key}: {os.getenv(key)}')
    except KeyError:
        return False

    return True


def isContentOverridable():
    overridable = None
    while overridable != 1 and overridable != 0:
        overridable = int(input(
            'Deseja sobrescrever o conteudo? (1) - sim (0) - nao: '))
    return bool(overridable)


def updateEnvVar(key, value: str):
    value = str(value)
    if isKeyOnEnvDict(key, f'Atualizando o valor de {key}'):
        os.environ[key] = value
        print(f'Variavel ({key}) de ambiente teve seu valor atualizado')
        return
    print('Variavel nao encontrada, criando variavel')
    createEnvVar(key, value)
    return


def createEnvVar(key, value: str):
    value = str(value)
    if isKeyOnEnvDict(key):
        if isContentOverridable():
            pass
        else:
            print('A variavel nao foi sobrescrita')
            return
    try:
        os.putenv(key)
    except Exception:
        print('Ops algo deu errado')
    else:
        print(
            f'variavel de ambiente {key} : {os.environ[key]} criada',
            'com sucesso')


def deleteEnvVar(key):
    if isKeyOnEnvDict(key, 'Variavel de ambiente encontrada'):
        try:
            del os.environ[key.upper()]
        except Exception:
            print('Ops algo deu errado')
        else:
            print(
                f'variavel {key} foi deletada com sucesso')


def envToBool(key: str):
    key = str(key)
    if os.environ[key]:
        return True
    else:
        return False
