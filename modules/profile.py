from modules import utils,session,modify,logs,database,menu,registerUser,login


tempID = session.sessionID

def getProfile():

  utils.clear()
  print('Seus Dados')
  print('----------')
  print(f'ID: {session.sessionID}')  
  print(f'Nome: {session.sessionUsername}')  
  print(f'TokenID: {session.sessionTokenID}')  
  if(session.sessionRole == 1):
    print('Cargo: Admin') 
  else:
    print('Cargo: Visitante') 
  print('----------')

  input('Pressione *ENTER* para continuar')
  drawOptionsMenu()


def drawProfileMenu():
  utils.clear()

  print('[1] Nome')
  print('[2] Senha')
  print('[3] TokenID')
  if(session.sessionRole == 1):
    print('[4] Cargo')
    print('[5] Tudo')    
  print('[0] Sair')


  option = input('>> ')
  print('')

  if(option == '1'):
      utils.clear()
      print('Modificar nome')
      database.users[tempID] = registerUser.getUser()
      session.update()
      logs.add(f'{session.sessionUsername} Alterou seu próprio nome!')
      return drawOptionsMenu()

  elif(option == '2'):
      utils.clear()
      print('Modificar senha')
      database.password[tempID] = registerUser.getPass()
      session.update()
      logs.add(f'{session.sessionUsername} Modificou a própria senha!')
      return drawOptionsMenu()

  elif(option == '3'):
      utils.clear()
      print('Modificar Token')
      database.tokenID[tempID] = registerUser.getToken()
      logs.add(f'{session.sessionUsername} Modificou o próprio TokenID!')
      #erro aqui
      return drawOptionsMenu()

  if(session.sessionRole == 1):
    if(option == '4'):
        utils.clear()
        print('Modificar Cargo')
        database.roles[tempID] = modify.getRole()     
        logs.add(f'{session.sessionUsername} Modificou o próprio Cargo!') 
        session.update()
        utils.clear()
        return login.startAuth(tempID)
        # drawOptionsMenu()

    elif(option == '5'):
        utils.clear()
        print('Modificar tudo')
        modify.modifyAll(tempID) 
        logs.add(f'{session.sessionUsername} Modificou seu perfil por completo!')
        return drawOptionsMenu()

  elif(option == '0'):
     utils.clear()
     menu.drawMenu()
     return menu.handleUserInput()
           
  else:
      print('Opção inválida')    
      return drawProfileMenu()



      
  
def drawOptionsMenu():
  utils.clear()
  session.update()
  userOption = input('[1] Ver Perfil\n[2] Editar Perfil\n[3] Sair\n>> ')

  if(userOption == '1'):
    return getProfile()

  elif(userOption == '2'):
    return drawProfileMenu()

  elif(userOption == '3'):
    utils.clear()
    menu.drawMenu()
    return menu.handleUserInput()
  
  else:
     print('Entrada inválida!')
     return drawOptionsMenu()