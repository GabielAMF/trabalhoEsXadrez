start_table = [["BT","BH","BB","BK","BQ","BB","BH","BT"],
               ["BP","BP","BP","BP","BP","BP","BP","BP"],
               ["0","0","0","0","0","0","0","0"],
               ["0","0","0","0","0","0","0","0"],
               ["0","0","0","0","0","0","0","0"],
               ["0","0","0","0","0","0","0","0"],
               ["WP","WP","WP","WP","WP","WP","WP","WP"],
               ["WT","WH","WB","WQ","WK","WB","WH","WT"]
               ]
cemiterio_B = []
cemiterio_W = []
def check_colision():
    return False
def check_move_pawn(x0,y0,tabuleiro):
    piece = tabuleiro[x0][y0]
    player = piece[0]

    possible_move = []
    if player == "B":


        if tabuleiro[x0+1][y0] == "0":

            possible_move.append([x0+1,y0])
            if x0 == 1 and tabuleiro[x0+2][y0] == "0":
                possible_move.append([x0+2,y0])
        if y0 > 0:
            player_inimigo = tabuleiro[x0+1][y0-1]
            if player_inimigo[0] == "W":
                possible_move.append([x0+1,y0-1])
        if y0 < 7 :
            player_inimigo = tabuleiro[x0+1][y0+1]
            if player_inimigo[0] == "W":
                possible_move.append([x0+1,y0+1])
    if player == "W":
        if tabuleiro[x0-1][y0] == "0":
            possible_move.append([x0-1,y0])
            if y0 == 6 and tabuleiro[x0-2][y0] =="0":
                possible_move.append([x0-2,y0])
        if y0 > 0:
            player_inimigo = tabuleiro[x0-1][y0-1]
            if player_inimigo[0] == "B":
                possible_move.append([x0-1,y0-1])
        if y0 < 7:
            player_inimigo = tabuleiro[x0-1][y0+1]
            if player_inimigo[0] == "B":
                possible_move.append([x0-1,y0+1])
    return possible_move

def check_border(x0,y0):
    if x0 > 7 or x0 < 0 or y0 > 7 or y0 <0 :
        return False
    return True

def check_move_horse(x0,y0,tabuleiro):
    piece = tabuleiro[x0][y0]
    player = piece[0]
    possible_move = []
    if player == "B":
        if check_border(x0+2,y0+1) and tabuleiro[x0+2][y0+1][0] != "B":
            possible_move.append([x0+2,y0+1])
        if check_border(x0+2,y0-1) and tabuleiro[x0+2][y0-1][0] != "B":
            possible_move.append([x0+2,y0-1])
        if check_border(x0+1,y0+2) and tabuleiro[x0+1][y0+2][0] != "B":
            possible_move.append([x0+1,y0+2])
        if check_border(x0+1,y0-2) and tabuleiro[x0+1][y0-2][0] != "B":
            possible_move.append([x0+1,y0-2])
        if check_border(x0-1,y0+2) and tabuleiro[x0-1][y0+2][0] != "B":
            possible_move.append([x0-1,y0+2])
        if check_border(x0-1,y0-2) and tabuleiro[x0-1][y0-2][0] != "B":
            possible_move.append([x0-1,y0-2])
        if check_border(x0-2,y0+1) and tabuleiro[x0-2][y0+1][0] != "B":
            possible_move.append([x0-2,y0+1])
        if check_border(x0-2,y0-1) and tabuleiro[x0-2][y0-1][0] != "B":
            possible_move.append([x0-2,y0-1])
    if player == "W":
        if check_border(x0+2,y0+1) and tabuleiro[x0+2][y0+1][0] != "W":
            possible_move.append([x0+2,y0+1])
        if check_border(x0+2,y0-1) and tabuleiro[x0+2][y0-1][0] != "W":
            possible_move.append([x0+2,y0-1])
        if check_border(x0+1,y0+2) and tabuleiro[x0+1][y0+2][0] != "W":
            possible_move.append([x0+1,y0+2])
        if check_border(x0+1,y0-2) and tabuleiro[x0+1][y0-2][0] != "W":
            possible_move.append([x0+1,y0-2])
        if check_border(x0-1,y0+2) and tabuleiro[x0-1][y0+2][0] != "W":
            possible_move.append([x0-1,y0+2])
        if check_border(x0-1,y0-2) and tabuleiro[x0-1][y0-2][0] != "W":
            possible_move.append([x0-1,y0-2])
        if check_border(x0-2,y0+1) and tabuleiro[x0-2][y0+1][0] != "W":
            possible_move.append([x0-2,y0+1])
        if check_border(x0-2,y0-1) and tabuleiro[x0-2][y0-1][0] != "W":
            possible_move.append([x0-2,y0-1])
    return possible_move
def check_move_king(x0,y0,tabuleiro):
    piece = tabuleiro[x0][y0]
    player = piece[0]
    possible_move = []
    if player == "B":
        if check_border(x0+1,y0) and tabuleiro[x0+1][y0][0] != "B":
            possible_move.append([x0+1,y0])
        if check_border(x0-1,y0) and tabuleiro[x0-1][y0][0] != "B":
            possible_move.append([x0-1,y0])
        if check_border(x0+1,y0+1) and tabuleiro[x0+1][y0+1][0] != "B":
            possible_move.append([x0+1,y0+1])
        if check_border(x0+1,y0-1) and tabuleiro[x0+1][y0-1][0] != "B":
            possible_move.append([x0+1,y0-1])
        if check_border(x0,y0+1) and tabuleiro[x0][y0+1][0] != "B":
            possible_move.append([x0,y0+1])
        if check_border(x0,y0-1) and tabuleiro[x0][y0-1][0] != "B":
            possible_move.append([x0,y0-1])
        if check_border(x0-1,y0+1) and tabuleiro[x0-1][y0+1][0] != "B":
            possible_move.append([x0-1,y0+1])
        if check_border(x0-1,y0-1) and tabuleiro[x0-1][y0-1][0] != "B":
            possible_move.append([x0-1,y0-1])
    if player == "W":
        if check_border(x0+1,y0) and tabuleiro[x0+1][y0][0] != "W":
            possible_move.append([x0+1,y0])
        if check_border(x0-1,y0) and tabuleiro[x0-1][y0][0] != "W":
            possible_move.append([x0-1,y0])
        if check_border(x0+1,y0+1) and tabuleiro[x0+1][y0+1][0] != "W":
            possible_move.append([x0+1,y0+1])
        if check_border(x0+1,y0-1) and tabuleiro[x0+1][y0-1][0] != "W":
            possible_move.append([x0+1,y0-1])
        if check_border(x0,y0+1) and tabuleiro[x0][y0+1][0] != "W":
            possible_move.append([x0,y0+1])
        if check_border(x0,y0-1) and tabuleiro[x0][y0-1][0] != "W":
            possible_move.append([x0,y0-1])
        if check_border(x0-1,y0+1) and tabuleiro[x0-1][y0+1][0] != "W":
            possible_move.append([x0-1,y0+1])
        if check_border(x0-1,y0-1) and tabuleiro[x0-1][y0-1][0] != "W":
            possible_move.append([x0-1,y0-1])
    return possible_move

def check_move_tower(x0,y0,tabuleiro):
    piece = tabuleiro[x0][y0]
    player = piece[0]
    print(player)
    possible_move = []
    possible_X = [0,1,2,3,4,5,6,7]
    possible_Y = [0, 1, 2, 3, 4, 5, 6, 7]
    possible_X.remove(x0)
    possible_Y.remove(y0)
    temp_x = x0

    if player == "B":
        temp_x = x0 +1
        while temp_x <= 7:
            if tabuleiro[temp_x][y0] == "0":
                possible_move.append([temp_x,y0])
                #print(possible_move)
            if tabuleiro[temp_x][y0][0] == "B":
                break
            if tabuleiro[temp_x][y0][0] == "W":
                possible_move.append([temp_x,y0])
                break
            temp_x += 1


        temp_x = x0 -1

        while temp_x >= 0 :
            if tabuleiro[temp_x][y0] == "0":
                possible_move.append([temp_x,y0])
            if tabuleiro[temp_x][y0][0] == "B":
                break
            if tabuleiro[temp_x][y0][0] == "W":
                possible_move.append([temp_x,y0])
                break
            temp_x -= 1

        #temp_x = x0
        temp_y = y0 +1

        while temp_y <= 7 :
            if tabuleiro[x0][temp_y] == "0":
                possible_move.append([x0,temp_y])
            if tabuleiro[x0][temp_y][0] == "B":
                break
            if tabuleiro[x0][temp_y][0] == "W":
                possible_move.append([x0,temp_y])
                break
            temp_y += 1

        temp_y = y0 -1
        while temp_y >= 0:
            if tabuleiro[x0][temp_y] == "0":
                possible_move.append([x0,temp_y])
            if tabuleiro[x0][temp_y][0] == "B":
                break
            if tabuleiro[x0][temp_y][0] == "W":
                possible_move.append([x0,temp_y])
                break
            temp_y -= 1

    if player == "W":
        temp_x = x0+1
        while temp_x < 7:
            if tabuleiro[temp_x][y0] == "0":
                possible_move.append([temp_x,y0])
            if tabuleiro[temp_x][y0][0] == "W":
                break
            if tabuleiro[temp_x][y0][0] == "B":
                possible_move.append([temp_x,y0])
                break
            temp_x += 1
        temp_x = x0 -1
        while temp_x > 0:
            if tabuleiro[temp_x][y0] == "0":
                possible_move.append([temp_x,y0])
            if tabuleiro[temp_x][y0][0] == "W":
                break
            if tabuleiro[temp_x][y0][0] == "B":
                possible_move.append([temp_x,y0])
                break
            temp_x -= 1
        # temp_x = x0
        temp_y = y0+1
        while temp_y < 7:
            if tabuleiro[x0][temp_y] == "0":
                possible_move.append([x0,temp_y])
            if tabuleiro[x0][temp_y][0] == "W":
                break
            if tabuleiro[x0][temp_y][0] == "B":
                possible_move.append([x0,temp_y])
                break
            temp_y += 1
        temp_y = y0-1
        while temp_y > 0:
            if tabuleiro[x0][temp_y] == "0":
                possible_move.append([x0,temp_y])
            if tabuleiro[x0][temp_y][0] == "W":
                break
            if tabuleiro[x0][temp_y][0] == "B":
                possible_move.append([x0,temp_y])
                break
            temp_y -= 1
    return possible_move

def check_move_bishop(x0,y0,tabuleiro):
    piece = tabuleiro[x0][y0]
    player = piece[0]
    print(player)
    possible_move = []
    if player == "B":
        sum_factor = 1
        while check_border(x0+sum_factor,y0+sum_factor):
            if tabuleiro[x0+sum_factor][y0+sum_factor] == "0":
                possible_move.append([x0+sum_factor,y0+sum_factor])
            if tabuleiro[x0+sum_factor][y0+sum_factor][0] == "B":
                break
            if tabuleiro[x0 + sum_factor][y0 + sum_factor][0] == "W":
                possible_move.append([x0+sum_factor,y0+sum_factor])
                break
            sum_factor+=1
        sum_factor = 1
        while check_border(x0-sum_factor,y0-sum_factor):
            if tabuleiro[x0-sum_factor][y0-sum_factor] == "0":
                possible_move.append([x0-sum_factor,y0-sum_factor])
            if tabuleiro[x0-sum_factor][y0-sum_factor][0] == "B":
                break
            if tabuleiro[x0 - sum_factor][y0 - sum_factor][0] == "W":
                possible_move.append([x0-sum_factor,y0-sum_factor])
                break
            sum_factor+=1

        sum_factor = 1

        while check_border(x0+sum_factor,y0-sum_factor):
            if tabuleiro[x0+sum_factor][y0-sum_factor] == "0":
                possible_move.append([x0+sum_factor,y0-sum_factor])
            if tabuleiro[x0+sum_factor][y0-sum_factor][0] == "B":
                break
            if tabuleiro[x0 + sum_factor][y0 - sum_factor][0] == "W":
                possible_move.append([x0+sum_factor,y0-sum_factor])
                break
            sum_factor+=1
        sum_factor = 1

        while check_border(x0 - sum_factor, y0 + sum_factor):
            if tabuleiro[x0 - sum_factor][y0 + sum_factor] == "0":
                possible_move.append([x0 - sum_factor, y0 + sum_factor])
            if tabuleiro[x0 - sum_factor][y0 + sum_factor][0] == "B":
                break
            if tabuleiro[x0 - sum_factor][y0 + sum_factor][0] == "W":
                possible_move.append([x0 - sum_factor, y0 + sum_factor])
                break
            sum_factor += 1
    if player == "W":
        sum_factor = 1
        while check_border(x0+sum_factor,y0+sum_factor):
            if tabuleiro[x0+sum_factor][y0+sum_factor] == "0":
                possible_move.append([x0+sum_factor,y0+sum_factor])
            if tabuleiro[x0+sum_factor][y0+sum_factor][0] == "W":
                break
            if tabuleiro[x0 + sum_factor][y0 + sum_factor][0] == "B":
                possible_move.append([x0+sum_factor,y0+sum_factor])
                break
            sum_factor+=1
        sum_factor = 1
        while check_border(x0-sum_factor,y0-sum_factor):
            if tabuleiro[x0-sum_factor][y0-sum_factor] == "0":
                possible_move.append([x0-sum_factor,y0-sum_factor])
            if tabuleiro[x0-sum_factor][y0-sum_factor][0] == "W":
                break
            if tabuleiro[x0 - sum_factor][y0 - sum_factor][0] == "B":
                possible_move.append([x0-sum_factor,y0-sum_factor])
                break
            sum_factor+=1

        sum_factor = 1

        while check_border(x0+sum_factor,y0-sum_factor):
            if tabuleiro[x0+sum_factor][y0-sum_factor] == "0":
                possible_move.append([x0+sum_factor,y0-sum_factor])
            if tabuleiro[x0+sum_factor][y0-sum_factor][0] == "W":
                break
            if tabuleiro[x0 + sum_factor][y0 - sum_factor][0] == "B":
                possible_move.append([x0+sum_factor,y0-sum_factor])
                break
            sum_factor+=1
        sum_factor = 1

        while check_border(x0 - sum_factor, y0 + sum_factor):
            if tabuleiro[x0 - sum_factor][y0 + sum_factor] == "0":
                possible_move.append([x0 - sum_factor, y0 + sum_factor])
            if tabuleiro[x0 - sum_factor][y0 + sum_factor][0] == "W":
                break
            if tabuleiro[x0 - sum_factor][y0 + sum_factor][0] == "B":
                possible_move.append([x0 - sum_factor, y0 + sum_factor])
                break
            sum_factor += 1
    return possible_move

def check_move_queen(x0,y0,tabuleiro):
    piece = tabuleiro[x0][y0]
    player = piece[0]
    print(player)
    possible_move = []
    if player == "B":
        temp_x = x0 +1
        while temp_x <= 7:
            if tabuleiro[temp_x][y0] == "0":
                possible_move.append([temp_x,y0])
                #print(possible_move)
            if tabuleiro[temp_x][y0][0] == "B":
                break
            if tabuleiro[temp_x][y0][0] == "W":
                possible_move.append([temp_x,y0])
                break
            temp_x += 1


        temp_x = x0 -1

        while temp_x >= 0 :
            if tabuleiro[temp_x][y0] == "0":
                possible_move.append([temp_x,y0])
            if tabuleiro[temp_x][y0][0] == "B":
                break
            if tabuleiro[temp_x][y0][0] == "W":
                possible_move.append([temp_x,y0])
                break
            temp_x -= 1

        #temp_x = x0
        temp_y = y0 +1

        while temp_y <= 7 :
            if tabuleiro[x0][temp_y] == "0":
                possible_move.append([x0,temp_y])
            if tabuleiro[x0][temp_y][0] == "B":
                break
            if tabuleiro[x0][temp_y][0] == "W":
                possible_move.append([x0,temp_y])
                break
            temp_y += 1

        temp_y = y0 -1
        while temp_y >= 0:
            if tabuleiro[x0][temp_y] == "0":
                possible_move.append([x0,temp_y])
            if tabuleiro[x0][temp_y][0] == "B":
                break
            if tabuleiro[x0][temp_y][0] == "W":
                possible_move.append([x0,temp_y])
                break
            temp_y -= 1
        sum_factor = 1
        while check_border(x0 + sum_factor, y0 + sum_factor):
            if tabuleiro[x0 + sum_factor][y0 + sum_factor] == "0":
                possible_move.append([x0 + sum_factor, y0 + sum_factor])
            if tabuleiro[x0 + sum_factor][y0 + sum_factor][0] == "B":
                break
            if tabuleiro[x0 + sum_factor][y0 + sum_factor][0] == "W":
                possible_move.append([x0 + sum_factor, y0 + sum_factor])
                break
            sum_factor += 1
        sum_factor = 1
        while check_border(x0 - sum_factor, y0 - sum_factor):
            if tabuleiro[x0 - sum_factor][y0 - sum_factor] == "0":
                possible_move.append([x0 - sum_factor, y0 - sum_factor])
            if tabuleiro[x0 - sum_factor][y0 - sum_factor][0] == "B":
                break
            if tabuleiro[x0 - sum_factor][y0 - sum_factor][0] == "W":
                possible_move.append([x0 - sum_factor, y0 - sum_factor])
                break
            sum_factor += 1

        sum_factor = 1

        while check_border(x0 + sum_factor, y0 - sum_factor):
            if tabuleiro[x0 + sum_factor][y0 - sum_factor] == "0":
                possible_move.append([x0 + sum_factor, y0 - sum_factor])
            if tabuleiro[x0 + sum_factor][y0 - sum_factor][0] == "B":
                break
            if tabuleiro[x0 + sum_factor][y0 - sum_factor][0] == "W":
                possible_move.append([x0 + sum_factor, y0 - sum_factor])
                break
            sum_factor += 1
        sum_factor = 1

        while check_border(x0 - sum_factor, y0 + sum_factor):
            if tabuleiro[x0 - sum_factor][y0 + sum_factor] == "0":
                possible_move.append([x0 - sum_factor, y0 + sum_factor])
            if tabuleiro[x0 - sum_factor][y0 + sum_factor][0] == "B":
                break
            if tabuleiro[x0 - sum_factor][y0 + sum_factor][0] == "W":
                possible_move.append([x0 - sum_factor, y0 + sum_factor])
                break
    if player == "W":
        temp_x = x0 + 1
        while temp_x < 7:
            if tabuleiro[temp_x][y0] == "0":
                possible_move.append([temp_x, y0])
            if tabuleiro[temp_x][y0][0] == "W":
                break
            if tabuleiro[temp_x][y0][0] == "B":
                possible_move.append([temp_x, y0])
                break
            temp_x += 1
        temp_x = x0 - 1
        while temp_x > 0:
            if tabuleiro[temp_x][y0] == "0":
                possible_move.append([temp_x, y0])
            if tabuleiro[temp_x][y0][0] == "W":
                break
            if tabuleiro[temp_x][y0][0] == "B":
                possible_move.append([temp_x, y0])
                break
            temp_x -= 1
        # temp_x = x0
        temp_y = y0 + 1
        while temp_y < 7:
            if tabuleiro[x0][temp_y] == "0":
                possible_move.append([x0, temp_y])
            if tabuleiro[x0][temp_y][0] == "W":
                break
            if tabuleiro[x0][temp_y][0] == "B":
                possible_move.append([x0, temp_y])
                break
            temp_y += 1
        temp_y = y0 - 1
        while temp_y > 0:
            if tabuleiro[x0][temp_y] == "0":
                possible_move.append([x0, temp_y])
            if tabuleiro[x0][temp_y][0] == "W":
                break
            if tabuleiro[x0][temp_y][0] == "B":
                possible_move.append([x0, temp_y])
                break
            temp_y -= 1
        sum_factor = 1
        while check_border(x0 + sum_factor, y0 + sum_factor):
            if tabuleiro[x0 + sum_factor][y0 + sum_factor] == "0":
                possible_move.append([x0 + sum_factor, y0 + sum_factor])
            if tabuleiro[x0 + sum_factor][y0 + sum_factor][0] == "W":
                break
            if tabuleiro[x0 + sum_factor][y0 + sum_factor][0] == "B":
                possible_move.append([x0 + sum_factor, y0 + sum_factor])
                break
            sum_factor += 1
        sum_factor = 1
        while check_border(x0 - sum_factor, y0 - sum_factor):
            if tabuleiro[x0 - sum_factor][y0 - sum_factor] == "0":
                possible_move.append([x0 - sum_factor, y0 - sum_factor])
            if tabuleiro[x0 - sum_factor][y0 - sum_factor][0] == "W":
                break
            if tabuleiro[x0 - sum_factor][y0 - sum_factor][0] == "B":
                possible_move.append([x0 - sum_factor, y0 - sum_factor])
                break
            sum_factor += 1

        sum_factor = 1

        while check_border(x0 + sum_factor, y0 - sum_factor):
            if tabuleiro[x0 + sum_factor][y0 - sum_factor] == "0":
                possible_move.append([x0 + sum_factor, y0 - sum_factor])
            if tabuleiro[x0 + sum_factor][y0 - sum_factor][0] == "W":
                break
            if tabuleiro[x0 + sum_factor][y0 - sum_factor][0] == "B":
                possible_move.append([x0 + sum_factor, y0 - sum_factor])
                break
            sum_factor += 1
        sum_factor = 1

        while check_border(x0 - sum_factor, y0 + sum_factor):
            if tabuleiro[x0 - sum_factor][y0 + sum_factor] == "0":
                possible_move.append([x0 - sum_factor, y0 + sum_factor])
            if tabuleiro[x0 - sum_factor][y0 + sum_factor][0] == "W":
                break
            if tabuleiro[x0 - sum_factor][y0 + sum_factor][0] == "B":
                possible_move.append([x0 - sum_factor, y0 + sum_factor])
                break
            sum_factor += 1
    return possible_move

def move(x0,y0,xf,yf,tabuleiro):
    global cemiterio_B
    global cemiterio_W
    player = tabuleiro[x0][y0][0]

    if tabuleiro[xf][yf][0] == "W"   and player == "B":
        print("Comeu uma peça")
        cemiterio_B.append(tabuleiro[xf][yf])
    if tabuleiro[xf][yf][0] == "B" and player == "W":
        print("Comeu uma peça")
        cemiterio_W.append(tabuleiro[xf][yf])
    tabuleiro[xf][yf] = tabuleiro[x0][y0]
    tabuleiro[x0][y0] = "0"
    return tabuleiro

def checar_cheque(lista_jogadas,tabuleiro):
    return True


#print(start_table[0][0][0])
#start_table[3][3] = "WK"
#start_table[2][2] = "BQ"
#for line in start_table:
#    print(line)
#print(check_move_king(3,3,start_table))

#print(check_move_queen(2,2,start_table))

#print(check_move_pawn(1,1,start_table))
#print(check_move_pawn(1,1,start_table))
#print(check_move_horse(1,1,start_table))

exit = 0




for line in start_table:
    print(line)

while exit ==0:
    escolha_peca = input("Escolha a casa de sua jogada(separada por espaço)")
    escolha_peca= escolha_peca.split()
    x0 = int(escolha_peca[0])
    y0 = int(escolha_peca[1])
    tipo_de_peca = start_table[x0][y0][1]
    if tipo_de_peca == "P":
        movimentos_possiveis = check_move_pawn(x0,y0,start_table)

        #movimentos_validos = checar_cheque(movimentos_possiveis,start_table)
        if len(movimentos_possiveis):
            print("Os movimentos válidos são: ", movimentos_possiveis)
            print("Escolha uma jogada de 0 a",len(movimentos_possiveis)-1)
            jogada = int(input())
            start_table =  move(x0,y0,movimentos_possiveis[jogada][0],movimentos_possiveis[jogada][1],start_table)
        else:
            print("Sem jogadas possíveis nessa peça")
    if tipo_de_peca == "T":
        movimentos_possiveis = check_move_tower(x0,y0,start_table)

        #movimentos_validos = checar_cheque(movimentos_possiveis,start_table)
        if len(movimentos_possiveis):
            print("Os movimentos válidos são: ", movimentos_possiveis)
            print("Escolha uma jogada de 0 a",len(movimentos_possiveis)-1)
            jogada = int(input())
            start_table = move(x0,y0,movimentos_possiveis[jogada][0],movimentos_possiveis[jogada][1],start_table)
        else:
            print("Sem jogadas possíveis nessa peça")
    if tipo_de_peca == "H":
        movimentos_possiveis = check_move_horse(x0,y0,start_table)

        #movimentos_validos = checar_cheque(movimentos_possiveis,start_table)
        if len(movimentos_possiveis):
            print("Os movimentos válidos são: ", movimentos_possiveis)
            print("Escolha uma jogada de 0 a",len(movimentos_possiveis)-1)
            jogada = int(input())
            start_table = move(x0,y0,movimentos_possiveis[jogada][0],movimentos_possiveis[jogada][1],start_table)
        else:
            print("Sem jogadas possíveis nessa peça")
    if tipo_de_peca == "B":
        movimentos_possiveis = check_move_bishop(x0,y0,start_table)

        #movimentos_validos = checar_cheque(movimentos_possiveis,start_table)
        if len(movimentos_possiveis):
            print("Os movimentos válidos são: ", movimentos_possiveis)
            print("Escolha uma jogada de 0 a",len(movimentos_possiveis)-1)
            jogada = int(input())
            start_table = move(x0,y0,movimentos_possiveis[jogada][0],movimentos_possiveis[jogada][1],start_table)
        else:
            print("Sem jogadas possíveis nessa peça")
    if tipo_de_peca == "Q":
        movimentos_possiveis = check_move_queen(x0,y0,start_table)

        #movimentos_validos = checar_cheque(movimentos_possiveis,start_table)
        if len(movimentos_possiveis):
            print("Os movimentos válidos são: ", movimentos_possiveis)
            print("Escolha uma jogada de 0 a",len(movimentos_possiveis)-1)
            jogada = int(input())
            start_table = move(x0,y0,movimentos_possiveis[jogada][0],movimentos_possiveis[jogada][1],start_table)
        else:
            print("Sem jogadas possíveis nessa peça")
    if tipo_de_peca == "K":
        movimentos_possiveis = check_move_king(x0,y0,start_table)

        #movimentos_validos = checar_cheque(movimentos_possiveis,start_table)
        if len(movimentos_possiveis):
            print("Os movimentos válidos são: ", movimentos_possiveis)
            print("Escolha uma jogada de 0 a",len(movimentos_possiveis)-1)
            jogada = int(input())
            start_table = move(x0,y0,movimentos_possiveis[jogada][0],movimentos_possiveis[jogada][1],start_table)
        else:
            print("Sem jogadas possíveis nessa peça")
    for line in start_table:
        print(line)

    print("Cemiteiro Black: ", cemiterio_B)
    print("Cemiterio White: ", cemiterio_W)


    exit = int(input("Sair?"))