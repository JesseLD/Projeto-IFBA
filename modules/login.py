from modules import database,menu,session,utils,logs,appError
access = '0'
tries = 1


utils.clear()

def startAuth(id):
  appError.clear()

  if(id > len(database.id)):
    session.update()
    return startAuth()
  
  else:
    session.createSession(
      database.id[id],
      database.users[id],
      database.tokenID[id],
      database.roles[id]
    )
    session.update()
    logs.add(f'{session.sessionUsername} Logou!')
    menu.drawMenu()
    return menu.handleUserInput()


def login():
    userTokenID = input('Digite o TokenID do usuário\n>> ')
    
    if(userTokenID.lower() in database.tokenID):
      userPassword = input('Digite a senha\n>> ')
      utils.clear()
      tempID = database.users.index(userTokenID)

      if(userPassword.lower() == database.password[tempID]):
        startAuth(tempID)
        return True
      
      else:
        appError.add('Senha Errada!')

    else:
       appError.add('Usuário Inválido')

    
def loginPanel():

  while True:
    utils.clear()
    print('=> FAÇA LOGIN PARA ACESSAR TODOS OS RECURSOS')
    appError.showLastError()
    access = input('[1] FAZER LOGIN\n[0] SAIR DO SISTEMA\n>> ')

    utils.clear()
    if(access == '1'):
      if(login()):
            # print('Logado!')
            return True
      else: 
        global tries
        if(tries <= 0):
          print('Máximo de tentativas alcançadas')
          print('Tente mais tarde!')
          break
        else:
          tries -= 1
    
    elif(access == '0'):
      print('Saindo...')
      break
    else:
      print('Entrada Inválida!')
