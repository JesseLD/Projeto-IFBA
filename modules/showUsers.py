from modules import database,menu,utils,login,session

biggestName = 0


def printUsers():
  print('Usuários Cadastrados')
  
  global biggestName
  for i in range(0, len(database.users)):
    if(len(database.users[i]) > biggestName):
      biggestName = len(database.users[i])
  
  for i in range(0, len(database.users)):
    roleName = 'Visitante'

    if(database.roles[i] == 1): roleName = 'Admin'
    print(f'ID: {database.id[i]:<4} | Nome: {database.users[i].capitalize():<{biggestName}} | Cargo: {roleName:<10} | TokenID: {database.tokenID[i]}')

  print('---------------------')
  print('\n\n')

  

def showAllUsers():
  utils.clear()
  print('Usuários Cadastrados')
  
  global biggestName
  for i in range(0, len(database.users)):
    if(len(database.users[i]) > biggestName):
      biggestName = len(database.users[i])
  
  for i in range(0, len(database.users)):
    roleName = 'Visitante'

    if(database.roles[i] == 1): roleName = 'Admin'
    print(f'ID: {database.id[i]:<4} | Nome: {database.users[i].capitalize():<{biggestName}} | Cargo: {roleName:<10} | TokenID: {database.tokenID[i]}')


  print('---------------------')
  print('\n\n')


  input('Pressione *ENTER* para continuar')
  utils.clear() 

  tempIndex = database.users.index(session.sessionUsername)

  return login.startAuth(tempIndex)

