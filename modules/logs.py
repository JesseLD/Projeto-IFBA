from modules import utils,menu

logsList = []

def add(message = 'Log Vazio'):
    # if((not message) or (message == '')):
    #     logs.append(f'Log Inválido {utils.dateSuffix()}')

    logsList.append(f'{message} {utils.dateSuffix()}')

def show():
  utils.clear()
  print('Todos os logs\n')
  for i in range(0,len(logsList)):
      print(f'{logsList[i]}')

  print('\n')
  input('Pressione *ENTER* para continuar')
  utils.clear() 
  logMenu()


def clearLogs():
  utils.clear() 
  logsList.clear()
  print('Logs limpos\n')

  input('Pressione *ENTER* para continuar')
  utils.clear() 
  logMenu()



def logMenu():
  print('=> SISTEMA DE USUÁRIOS <=')
  print('[5] LOGS DO SISTEMA <-\n')
  userInput = input('[1] Mostrar Logs\n[2] Limpar Logs\n[3] Sair\n>> ')
  if(userInput == '1'):
      show()
  elif(userInput == '2'):
      clearLogs()
  elif(userInput == '3'):
      utils.clear() 
      menu.drawMenu()
      menu.handleUserInput()
  else:
      utils.clear()
      print('Entrada inválida')
      logMenu()
    