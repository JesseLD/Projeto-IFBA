from modules import login,registerUser,showUsers,delete,modify,session,utils,logs,profile

utils.clear()

def drawMenu():
  print('\n')
  print('=> SISTEMA DE USUÁRIOS <=')
  session.update()
  session.drawNameAndRole()


  if(session.sessionRole == 1): 
    print('[1] MOSTRAR USUÁRIOS CADASTRADOS\n[2] CADASTRO DE USUÁRIO\n[3] DELETAR USUÁRIO\n[4] MODIFICAR USUÁRIO\n[5] LOGS DO SISTEMA')
  
  
  print('[6] MEU PERFIL')  
  print('[0] LOGOUT')


  
def handleUserInput():
  userInput = input('Selecione uma opção\n>> ')

  if(userInput == '1'):
    utils.clear()
    print('=> SISTEMA DE USUÁRIOS <=')
    print('[2] MOSTRAR USUÁRIOS CADASTRADOS<-')
    return showUsers.showAllUsers()
  
  elif(userInput == '2'):
    utils.clear()
    print('=> SISTEMA DE USUÁRIOS <=')
    print('[1] CADASTRO DE USUÁRIO <-')
    return registerUser.addNewUser()

  elif(userInput == '3'):
    utils.clear()
    print('[3] DELETAR USUÁRIO <-')
    return delete.deleteUser()

  elif(userInput == '4'):
    utils.clear()
    print('=> SISTEMA DE USUÁRIOS <=')
    print('[4] MODIFICAR USUÁRIO <-')
    return modify.modifyUser()     

  elif(userInput == '5'):
    utils.clear()
    return logs.logMenu()  

  elif(userInput == '6'):
    utils.clear()     
    print('=> SISTEMA DE USUÁRIOS <=')
    print('[6] MEU PERFIL <-\n')
    return profile.drawOptionsMenu()


  elif(userInput == '0'):
    utils.clear()
    logs.add(f'{session.sessionUsername} Saiu!')
    session.resetValues()
    print('Saindo...')  
    return login.loginPanel()     
      
  else:
    print('*ENTRADA INVÁLIDA :-\ \n')
    drawMenu()
    return handleUserInput()
