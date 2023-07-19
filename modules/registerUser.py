from modules import database,showUsers,menu,logs,session,utils,appError

newTempTokenID = ''

def validateToken():

  # newTempTokenID = int(input('Digite o TokenID do novo usuário\nApenas Números\n4 Números (XXXX)\n>> '))

  while True:
    try:
        appError.showLastError()
        newTempTokenID = int(input('Digite o TokenID\nApenas Números\n4 Números (XXXX)\n>> '))

        if not str(newTempTokenID).isdigit() or len(str(newTempTokenID)) != 4:
          appError.add('Token Inválido!')
          # return False
        else:
          appError.clear()
          return newTempTokenID
    
    except ValueError:
        utils.clear() 
        appError.add('Entrada inválida. Digite uma sequencia números inteiros')


def getToken():
  newTempTokenID = ''

  newTempTokenID = str(validateToken())

  if(newTempTokenID in database.tokenID):
    utils.clear()
    appError.add('Esse TokenID Já existe')
    return getToken()
  else:
    appError.clear()
    return newTempTokenID  




def getUser():
  appError.showLastError()
  newTempUser = input('Digite o nome do usuário\n>> ')

  if(newTempUser.strip() == ''):
    appError.add('Nome inválido!')
    return getUser()

  else:
    appError.clear()
    return newTempUser
       



def getPass():
  appError.showLastError()
  newTempPass = input('Digite a senha do usuário\n>> ')

  if(newTempPass.strip() == ''):
    appError.add('Senha inválida!')
    return getPass()

  else:
    appError.clear()
    return newTempPass  




def addNewUser():
  newUser = getUser() 
  newPass = getPass()  
  newTokenID = getToken()


  print('USUÁRIO CADASTRADO COM SUCESSO!')
  registerUser(newUser.lower(), newPass.lower(), newTokenID.lower())




def registerUser(newUser, newPass,newTokenID):

  database.idIncrement = str(len(database.id))
  database.id.append(database.idIncrement)
  database.users.append(newUser)
  database.tokenID.append(newTokenID)
  database.password.append(newPass)
  database.roles.append(0)   


  logs.add(f'{session.sessionUsername} Cadastrou o usuário {newUser}')


  showUsers.showAllUsers() 
  menu.drawMenu()
  menu.handleUserInput()