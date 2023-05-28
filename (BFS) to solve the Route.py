Player = 'O'
Computer = 'X'
block = {1: '_', 2: '_', 3: '_',
         4: '_', 5: '_', 6: '_',
         7: '_', 8: '_', 9: '_'}


def print_block(block):
    print(block[1] + ' ' + block[2] + ' ' + block[3])
    print(block[4] + ' ' + block[5] + ' ' + block[6])
    print(block[7] + ' ' + block[8] + ' ' + block[9])


def is_free(position):
    if block[position] == '_':
        return True
    else:
        return False


def check_winer():
    if block[1] == block[2] and block[1] == block[3] and block[1] != '_':
        return True
    elif block[4] == block[5] and block[4] == block[6] and block[4] != '_':
        return True
    elif block[7] == block[8] and block[7] == block[9] and block[7] != '_':
        return True
    elif block[1] == block[5] and block[1] == block[9] and block[1] != '_':
        return True
    elif block[3] == block[5] and block[3] == block[7] and block[3] != '_':
        return True
    elif block[1] == block[4] and block[1] == block[7] and block[1] != '_':
        return True
    elif block[2] == block[5] and block[2] == block[8] and block[2] != '_':
        return True
    elif block[3] == block[6] and block[3] == block[9] and block[3] != '_':
        return True
    else:
        return False


def check_draw():
    for i in block.keys():
        if block[i] == '_':
            return False
    return True


def who_win(sign):
    if block[1] == block[2] and block[1] == block[3] and block[1] != 'sign':
        return True
    elif block[4] == block[5] and block[4] == block[6] and block[4] != 'sign':
        return True
    elif block[7] == block[8] and block[7] == block[9] and block[7] != 'sign':
        return True
    elif block[1] == block[5] and block[1] == block[9] and block[1] != 'sign':
        return True
    elif block[3] == block[5] and block[3] == block[7] and block[3] != 'sign':
        return True
    elif block[1] == block[4] and block[1] == block[7] and block[1] != 'sign':
        return True
    elif block[2] == block[5] and block[2] == block[8] and block[2] != 'sign':
        return True
    elif block[3] == block[6] and block[3] == block[9] and block[3] != 'sign':
        return True
    else:
        return False


def next_move(sign, position):
    if is_free(position):
        block[position] = sign
        print_block(block)

        if check_draw():
            print("Draw")
        elif check_winer():
            if sign == 'X':
                print("Computer")
            else:
                print("Player")
        return
    else:
        position = int(input())
        next_move(sign, position)


def player_move():
    position = int(input())
    next_move(Player, position)
    return


def computer_move():
    b = -999
    best = 0

    for i in block.keys():
        if block[i] == '_':
            block[i] = Computer
            cost = min_max(block, False)
            block[i] = '_'
            if cost > b:
                b = cost
                best = i
    next_move(Computer, best)
    return


def min_max(block, found):
    if who_win(Computer):
        return 1
    elif who_win(Player):
        return -1
    elif check_draw():
        return 0

    if found:
        best = -999
        for i in block.keys():
            if block[i] == '_':
                block[i] = Computer
                cost = min_max(block, False)
                block[i] = '_'
                if cost > best:
                    best = cost
        return best
    else:
        best = 999
        for i in block.keys():
            if block[i] == '_':
                block[i] = Player
                cost = min_max(block, True)
                block[i] = '_'
                if cost < best:
                    best = cost
        return best


while not check_winer():
    computer_move()
    player_move()






