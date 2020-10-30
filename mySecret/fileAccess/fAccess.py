import os


def openAndWrite(path: str, content=''):
    path = str(path)
    content = str(content)
    with open(path, 'w') as writer:
        writer.write(content)
        print('Conteudo escrito com sucesso')


def openAndAppend(path: str, content=''):
    path = str(path)
    content = str(content)
    with open(path, 'a') as appender:
        appender.write(content)
        print('conteudo escrito com sucesso')


def openAndRead(path: str):
    path = str(path)
    try:
        with open(path, 'r') as reader:
            content = reader.read()
            return content
    except FileNotFoundError:
        print('Verifique o path, ou arquivo nao existe')


def removeFile(path: str, message='Arquivo removido com sucesso', errMessage=''):
    path = str(path)
    if os.path.exists(path):
        os.remove(path)
        print(message)
        return
    print(f'{errMessage}')
