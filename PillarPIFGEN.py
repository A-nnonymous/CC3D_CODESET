def pifcomak(height, rows, columns):
    pifstr =[]
    pvol =height*rows*columns
    for j in range(rows+4):
        for k in range(columns+4):
                if (j+k)%2:
                    string = '{} pillar {} {} {} {} {} {}'.format(j*k,j,j,k,k,0,height)
                    pifstr.append(string)
    for j in range(rows):
        for k in range(columns):
            if not (j+k)%32:
                string = '{} Target {} {} {} {} {} {}'.format(pvol+j*k,j,j+4,k,k+4,height+1,height+1)
                pifstr.append(string)
    return pifstr

data = pifcomak(4,200,200)

with open('PILLAR_CELL.piff','w') as file:
    for i in data:
        file.write(i+'\n')
