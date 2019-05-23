class GameDone(Exception): pass
print ('Bienvenido a Ta-Te-Tí')
#Listas que conforman el board
board0=[' ','1','2','3']
boarda=['A',' ',' ',' ']
boardb=['B',' ',' ',' ']
boardc=['C',' ',' ',' ']
def board():
    #Funcion que muestra el board
    print('                        \n',board0,'\n',boarda,'\n',boardb,'\n',boardc)

def turno_x(x):
    #Comprueba si el jugador que ingreso antes no gano ya el juego y de ser así interrumpe el loop
    if boarda[1] == boarda[2] == boarda[3] == 'O' or boardb[1] == boardb[2] == boardb[3] == 'O' or boardc[1] == boardc[2] == boardc[3] == 'O' or boarda[1] == boardb[1] == boardc[1] == 'O' or boarda[2] == boardb[2] == boardc[2] == 'O' or boarda[3] == boardb[3] == boardc[3] == 'O' or boarda[1] == boardb[2] == boardc[3] == 'O' or boardc[1] == boardb[2] == boarda[3] == 'O':
        print('El jugador O es el ganador')
        raise GameDone
    else:
        pass
    #Comienza el turno del jugador O
    print('Es el turno del jugador X')
    print('Ingrese la casilla que desee seleccionar del siguiente modo:A1, B2, C3\n')
    x = input('>> ')
    #Dependiendo del ingreso del jugador cambia la casilla en la lista correspondiente
    if x[0]=='A'and boarda[int(x[1])]!='O' and boarda[int(x[1])]!='X':
        boarda[int(x[1])]='X'
        print('\n'*100)
        board()
        turno_o(0)
        #Al haber cambiado la casilla el programa salta a la funcion del turno del otro jugador creando un loop
    elif x[0]=='B'and boardb[int(x[1])]!='O' and boardb[int(x[1])]!='X':
        boardb[int(x[1])]='X'
        print('\n'*100)
        board()
        turno_o(0)
    elif x[0]=='C'and boardc[int(x[1])]!='O' and boardc[int(x[1])]!='X':
        boardc[int(x[1])]='X'
        print('\n'*100)
        board()
        turno_o(0)
    else:
        print('Ingreso incorrecto')
        turno_x(0)

def turno_o(o):
    #Comprueba si el jugador que ingreso antes no gano ya el juego y de ser así interrumpe el loop
    if boarda[1] == boarda[2] == boarda[3] == 'X' or boardb[1] == boardb[2] == boardb[3] == 'X' or boardc[1] == boardc[2] == boardc[3] == 'X' or boarda[1] == boardb[1] == boardc[1] == 'X' or boarda[2] == boardb[2] == boardc[2] == 'X' or boarda[3] == boardb[3] == boardc[3] == 'X' or boarda[1] == boardb[2] == boardc[3] == 'X' or boarda[3] == boardb[2] == boardc[1] == 'X':
        print('El jugador X es el ganador')
        raise GameDone
    else:
        pass
    #Comienza el turno del jugador O
    print('Es el turno del jugador O')
    print('Ingrese la casilla que desee seleccionar del siguiente modo:A1, B2, C3 etc.\n')
    o = input('>> ')
    #Dependiendo del ingreso del jugador cambia la casilla en la lista correspondiente
    if o[0]=='A' and boarda[int(o[1])]!='O' and boarda[int(o[1])]!='X':
            boarda[int(o[1])]='O'
            print('\n'*100)
            board()
            turno_x(0)
            #Al haber cambiado la casilla el programa salta a la funcion del turno del otro jugador creando un loop
    elif o[0]=='B'and boardb[int(o[1])]!='O' and boardb[int(o[1])]!='X':
            boardb[int(o[1])]='O'
            print('\n'*100)
            board()
            turno_x(0)
    elif o[0]=='C'and boardc[int(o[1])]!='O' and boardc[int(o[1])]!='X':
            boardc[int(o[1])]='O'
            print('\n'*100)
            board()
            turno_x(0)
    else:
            print('Ingreso incorrecto')
            turno_o(0)
#Main, comienza el turno de un jugador para despues crearse el loop solo interrumpido cuando un jugador gana
try:
    while True:
        board()
        turno_x(0)
except GameDone:
    pass
