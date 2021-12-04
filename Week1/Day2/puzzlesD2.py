def p1():
    horizontal = depth =  0
    with open('data2.txt') as file:
        for line in file.readlines():
            com, move = line.strip().split()
            move = int(move)
            if com == 'up':
                depth -= move
            if com == 'down':
                depth += move
            if com == 'forward':
                horizontal += move
    print( horizontal * depth)

def p2():
    h =  d = aim = 0
    with open('data2.txt') as file:
        for line in file.readlines():
            x = line.split()
            match x :
                case "forward", amount:
                    h += int(amount)
                    d += aim * int(amount)
                case "up", amount:
                    aim -= int(amount)
                case "down", amount:
                    aim += int(amount)

    print(h * aim, h * d)

if __name__=='__main__':
    p1()
    p2()
   
