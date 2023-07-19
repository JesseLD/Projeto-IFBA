#PRINTA OS ERROS DO USUARIO

errors = []

def showLastError():
    if(len(errors) > 0):
      print(f'Erro: {errors[-1]}\n')


def add(msg = 'null'):
    errors.append(msg)

def clear():
    errors.clear()