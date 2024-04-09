mapa = []


def contar_dinheiro(mapa):
    count = 0
    current = 'D'
    x = 0
    c = 0
    y = 0
    numero_completo = 0
    for i in mapa:
        if i[0][0] == '-':
            x += c    
            break
        c += 1


    while mapa[x][y] != '#':
       
        if  mapa[x][y].isdigit() and mapa[x][y - 1].isdigit() and mapa[x][y - 2].isdigit() and mapa[x][y - 3].isdigit() and current == 'E':
            numero_completo = mapa[x][y - 3] + mapa[x][y - 2] + mapa[x][y - 1] + mapa[x][y] 
            print(int(numero_completo), end=(', '))
            count += int(numero_completo)
            mapa[x][y] = 'x'
            mapa[x][y - 1] = 'x'
            mapa[x][y - 2] = 'x'
            mapa[x][y - 3] = 'x'
            
        if  mapa[x][y].isdigit() and mapa[x][y + 1].isdigit() and mapa[x][y + 2].isdigit() and mapa[x][y + 3].isdigit() and current == 'D':
            numero_completo = mapa[x][y] + mapa[x][y +1] + mapa[x][y + 2] + mapa[x][y + 3]
            print(int(numero_completo), end=(', '))
            count += int(numero_completo)
            mapa[x][y] = 'x'
            mapa[x][y + 1] = 'x'
            mapa[x][y + 2] = 'x'
            mapa[x][y + 3] = 'x'

        if  mapa[x][y].isdigit() and mapa[x][y - 1].isdigit() and mapa[x][y - 2].isdigit() and current == 'E':
            numero_completo = mapa[x][y - 2] + mapa[x][y - 1] + mapa[x][y]
            print(int(numero_completo), end=(', '))
            count += int(numero_completo)
            mapa[x][y] = 'x'
            mapa[x][y - 1] = 'x'
            mapa[x][y - 2] = 'x'

        if  mapa[x][y].isdigit() and mapa[x][y + 1].isdigit() and mapa[x][y + 2].isdigit() and current == 'D':
            numero_completo = mapa[x][y] + mapa[x][y +1] + mapa[x][y + 2]
            print(int(numero_completo), end=(', '))
            count += int(numero_completo)
            mapa[x][y] = 'x'
            mapa[x][y + 1] = 'x'
            mapa[x][y + 2] = 'x'

        if  mapa[x][y].isdigit() and mapa[x][y - 1].isdigit() and current == 'E':
            numero_completo = mapa[x][y - 1] + mapa[x][y]
            print(int(numero_completo), end=(', '))
            count += int(numero_completo)
            mapa[x][y] = 'x'
            mapa[x][y - 1] = 'x'

        if  mapa[x][y].isdigit() and mapa[x][y + 1].isdigit() and current == 'D':
            numero_completo = mapa[x][y] + mapa[x][y +1]
            print(int(numero_completo), end=(', '))
            count += int(numero_completo)
            mapa[x][y] = 'x'
            mapa[x][y + 1] = 'x'

        if mapa[x][y].isdigit():
            print(mapa[x][y], end=(', '))
            count += int(mapa[x][y])
            mapa[x][y] = 'x'
       
        if current == 'D':
            y += 1
        elif current == 'E':
            y -= 1
        elif current == 'C':
            x -= 1
        elif current == 'B':
            x += 1
       
        if mapa[x][y] == '/' and current == 'D':
            x -= 1
            current = 'C'
        elif mapa[x][y] == '\\' and current == 'E':
            x -= 1
            current = 'C'
        elif mapa[x][y] == '/' and current == 'E':
            x += 1
            current = 'B'
        elif mapa[x][y] == '\\' and current == 'D':
            x += 1
            current = 'B'
        elif mapa[x][y] == '\\' and current == 'C':
            y -= 1
            current = 'E'
        elif mapa[x][y] == '\\' and current == 'B':
            y += 1
            current = 'D'
        elif mapa[x][y] == '/' and current == 'B':
            y -= 1
            current = 'E'
        elif mapa[x][y] == '/' and current == 'C':
            y += 1
            current = 'D'


    return count


def main():
    with open('casoG50.txt', 'r') as arquivo:
        conteudo = arquivo.readlines()
       
    for linha in conteudo:
        linhamapa = []
        for i in linha:
            if i != "\n":
                linhamapa.append(i)
        mapa.append(linhamapa)


    print('Ordem em que o dinheiro foi encontrado: ')
    print('\nA quantida total de dinheiro recuperada é: ', contar_dinheiro(mapa))


if __name__ == "__main__":
    main()


