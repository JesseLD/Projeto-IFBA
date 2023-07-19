from modules import utils, session, modify, logs, database, menu, registerUser, login, appError


tempID = session.sessionID


def getProfile():
    appError.clear()
    utils.clear()
    print('Seus Dados')
    print('----------')
    print(f'ID: {session.sessionID}')
    print(f'Nome: {session.sessionUsername}')
    print(f'TokenID: {session.sessionTokenID}')
    if (session.sessionRole == 1):
        print('Cargo: Admin')
    else:
        print('Cargo: Visitante')
    print('----------')

    input('Pressione *ENTER* para continuar')
    drawOptionsMenu()


def drawProfileMenu():
    utils.clear()
    appError.showLastError()
    print('O que deseja modificar?')
    print('[1] Nome')
    print('[2] Senha')
    print('[3] TokenID')
    if (session.sessionRole == 1):
        print('[4] Cargo')
        print('[5] Tudo')
    print('[0] Sair')

    option = input('>> ')
    print('')

    if (option == '1'):
        appError.clear()
        utils.clear()
        print('Modificar nome')
        database.users[session.sessionIndex] = registerUser.getUser()
        session.forceCreateSession(session.sessionIndex)
        session.update()
        logs.add(f'{session.sessionUsername} Alterou seu próprio nome!')
        return drawOptionsMenu()

    elif (option == '2'):
        appError.clear()
        utils.clear()
        print('Modificar senha')
        database.password[session.sessionIndex] = registerUser.getPass()
        session.forceCreateSession(session.sessionIndex)
        session.update()
        logs.add(f'{session.sessionUsername} Modificou a própria senha!')
        return drawOptionsMenu()

    elif (option == '3'):
        appError.clear()
        utils.clear()
        print('Modificar Token')
        session.forceCreateSession(session.sessionIndex)
        database.tokenID[session.sessionIndex] = registerUser.getToken()
        logs.add(f'{session.sessionUsername} Modificou o próprio TokenID!')
        # erro aqui
        return drawOptionsMenu()

    if (option == '4'):
        if (session.sessionRole == 1):
            utils.clear()
            print('Modificar Cargo')
            database.roles[session.sessionIndex] = modify.getRole()
            session.forceCreateSession(session.sessionIndex)
            logs.add(f'{session.sessionUsername} Modificou o próprio Cargo!')
            session.update()
            utils.clear()
            menu.drawMenu()
            return menu.handleUserInput()
        #   return login.startAuth(tempID)
        else:
            appError.add('Sem Permissão')
            return drawProfileMenu()
        # drawOptionsMenu()

    elif (option == '5'):
        if (session.sessionRole == 1):
            utils.clear()
            print('Modificar tudo')
            modify.modifyAll(session.sessionIndex)
            session.forceCreateSession(session.sessionIndex)
            logs.add(
                f'{session.sessionUsername} Modificou seu perfil por completo!')
            return drawOptionsMenu()
        else:
            appError.add('Sem Permissão')
            return drawProfileMenu()

    elif (option == '0'):
        utils.clear()
        appError.clear()
        menu.drawMenu()
        return menu.handleUserInput()

    else:
        appError.add('Opção inválida')
        return drawProfileMenu()


def drawOptionsMenu():
    utils.clear()
    session.update()
    print('=> SISTEMA DE USUÁRIOS <=')
    print('[6] MEU PERFIL <-\n')
    userOption = input('[1] Ver Perfil\n[2] Editar Perfil\n[3] Sair\n>> ')

    if (userOption == '1'):
        return getProfile()

    elif (userOption == '2'):
        return drawProfileMenu()

    elif (userOption == '3'):
        utils.clear()
        menu.drawMenu()
        return menu.handleUserInput()

    else:
        print('Entrada inválida!')
        return drawOptionsMenu()
