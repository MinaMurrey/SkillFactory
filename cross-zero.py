def draw_pole(matrix):
    print(" ----------------- ")
    for i in range(3):
        print(" | ", matrix[i*3+0], " | ",matrix[i*3+1], " | ",matrix[i*3+2], " | ")
        print(" ----------------- ")

def proverka(a,b):
    if a<0 or a>2 or b<0 or b>2:
        return False
    else:
        return True

def pobeda(matrix):
    if (matrix[0] == matrix[1] == matrix[2] == 'x' or
    matrix[0] == matrix[3] == matrix[6] == 'x' or
    matrix[1] == matrix[4] == matrix[7] == 'x' or
    matrix[2] == matrix[5] == matrix[8] == 'x' or
    matrix[3] == matrix[4] == matrix[5] == 'x' or
    matrix[6] == matrix[7] == matrix[8] == 'x' or
    matrix[0] == matrix[4] == matrix[8] == 'x' or
    matrix[2] == matrix[4] == matrix[6] == 'x'):
        return True
    elif (matrix[0] == matrix[1] == matrix[2]=='0' or
        matrix[0] == matrix[3] == matrix[6]=='0' or
        matrix[1] == matrix[4] == matrix[7]=='0' or
        matrix[2] == matrix[5] == matrix[8]=='0' or
        matrix[3] == matrix[4] == matrix[5]=='0' or
        matrix[6] == matrix[7] == matrix[8]=='0' or
        matrix[0] == matrix[4] == matrix[8]=='0' or
        matrix[2] == matrix[4] == matrix[6]=='0'
        ):
        return True
    else:
        return False


print ('Добро пожаловать в игру "Крестики-нолики"')

matrix=['' for int in range(9)]
count=0
pob=False
while True:
    pob=False
    while True:
        i=int(input('Ходит игрок х, введите номер строки '))
        j=int(input('Ходит игрок х, введите номер столбца '))
        if proverka(i,j):
            if matrix[i*3+j]=='':
                matrix[i * 3 + j] ='x'
                draw_pole(matrix)
                count+=1
                pob=pobeda(matrix)
                if pob:
                    print('Победил игрок X')
                break
            else:
                print('Клетка занята, введите новые координаты')
    if pob:
        break
    if count==9:
        print('Ничья')
        break
    while True:
        i=int(input('Ходит игрок 0, введите номер строки '))
        j=int(input('Ходит игрок 0, введите номер столбца '))
        if proverka(i,j):
            if matrix[i*3+j]=='':
                matrix[i * 3 + j] ='0'
                draw_pole(matrix)
                count+=1
                pob = pobeda(matrix)
                if pob:
                    print('Победил игрок О')
                break
            else:
                print('Клетка занята, введите новые координаты')

    if pob:
        break
    if count==9:
        print('Ничья')
        draw_pole(matrix)
        break

