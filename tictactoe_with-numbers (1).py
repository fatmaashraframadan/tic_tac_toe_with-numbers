print("\t","\t","welcome in tic_tac_toe with numbers","\t","\t")
def rows(a):
    array =["z1","z2", "z3","z4" , "z5","z6","z7" , "z8", "z9"]
    for i in range(3):
        summ = 0
        if a[i][0] not in array:
            summ = summ + a[i][0]
        else:
            summ = 0
        if a[i][1] not in array:
            summ = summ + a[i][1]
        else:
            summ = 0
        if a[i][2] not in array:
            summ = summ + a[i][2]
        else:
            summ = 0
        if summ == 15:
            return 15

def column(a):
    array =["z1","z2", "z3","z4" , "z5","z6","z7" , "z8", "z9"]
    for i in range(3):
        summ = 0
        if a[0][i] not in array:
            summ = summ + a[0][i]
        else:
            summ = 0
        if a[1][i] not in array:
            summ = summ + a[1][i]
        else:
            summ = 0
        if a[2][i] not in array:
            summ = summ + a[2][i]
        else:
            summ = 0
        if summ == 15:
            return 15

def diagonal(a):
    array =["z1","z2", "z3","z4" , "z5","z6","z7" , "z8", "z9"]
    summ = 0
    summ1 = 0
    if a[0][0] not in array:
        summ = summ + a[0][0]
    else:
            summ = 0
    if a[1][1] not in array:
        summ = summ + a[1][1]
    else:
            summ = 0
    if a[2][2] not in array:
        summ = summ + a[2][2]
    else:
        summ = 0

    if a[0][2] not in array:
        summ1 = summ1 + a[0][2]
    else:
        summ = 0
    if a[1][1] not in array:
        summ1 = summ1 + a[1][1]
    else:
        summ = 0
    if a[2][0] not in array:
        summ1 = summ1 + a[2][0]
    else:
        summ = 0

    if summ == 15 or summ1 == 15:
        return 15


array =[["z1","z2", "z3"],["z4" , "z5","z6"],["z7" , "z8", "z9"]]
even=[0,2,4,6,8]
odd=[1,3,5,7,9]

c = 0

for m in range (0,3):
    for n in range(0,1):
        print (array[m][n],"|",array[m][n+1],"|",array[m][n+2])    
for i in range(9):
    pos1=str(input("player1, choose a symbol for position"))
    if pos1 in array[0] or pos1 in array[1] or pos1 in array[2]:
        print(odd)
        y = int (input("player1 , choose your value"))
        if y in odd:
            for i in range(3):
                for j in range(3):
                           
                    if array[i][j]==pos1:
                        array[i][j]=y
                        odd.remove(y)
                        pass
        else:
            print("refused!! enter another number")
            y = int (input())
            if y in odd:
                for i in range(3):
                    for j in range(3):
                        if array[i][j]==pos1:
                            array[i][j]=y
                            odd.remove(y)
                            pass
            else:
                print("you entered invaled number twice!! turn skipped")
    else:
        print("player1, choose another symbol for position")
        pos1=str(input())
        if pos1 in array[0] or pos1 in array[1] or pos1 in array[2]:
            print(odd)
            y = int (input("player1 , choose your value"))
            if y in odd:
                for i in range(3):
                    for j in range(3):
                        if array[i][j]==pos1:
                            array[i][j]=y
                            odd.remove(y)
                            pass
            if y not in odd:
                print("refused!! enter another number")
                y = int (input("player1 , enter your value"))
                if y in odd:
                    for i in range(3):
                        for j in range(3):
                            if array[i][j]==pos1:
                                array[i][j]=y
                                odd.remove(y)
                                pass                     
            else:
                print("turn skipped!")
    if (rows(array)== 15) or (column(array) == 15) or (diagonal(array) == 15):
        print("Player1 won!!")
        drew = True
        break

    c = c + 1
    if c == 5:
        break


    for m in range (0,3):
        for n in range(0,1):
            print (array[m][n],"|",array[m][n+1],"|",array[m][n+2])    
    pos2=str(input("player2, choose a symbol fot position"))
    if pos2 in array[0] or pos2 in array[1] or pos2 in array[2]:
        print(even)
        y2 = int (input("player2 , choose your value"))
        
        if y2 in even:
            for i in range(3):
                for j in range(3):
                    if array[i][j]==pos2:
                        array[i][j]=y2
                        even.remove(y2)
                        pass
        else:
            print(even)
            print("refused!! choose another value")
            y2 = int (input())
            if y2 in even:
                for i in range(3):
                    for j in range(3):
                        if array[i][j]==pos2:
                            array[i][j]=y2
                            even.remove(y2)
                            pass
            else:
                print("player2,you entered invaled number twice!! turn skipped")
    else:
        print("player2, choose another symbol for position")
        pos2=str(input())
        if pos2 in array[0] or pos2 in array[1] or pos2 in array[2]:
            print(even)
            y2 = int (input("player2 , choose your value"))
            if y2 in even:
                for i in range(3):
                    for j in range(3):
                        if array[i][j]==pos2:
                                
                            array[i][j]=y2
                            even.remove(y2)
                            pass
            else:
                        
                print("refused!! choose another value")
                print(even)
                y2 = int (input("player2 , choose your value"))
                if y2 in even:
                    for i in range(3):
                        for j in range(3):
                            if array[i][j]==pos2:
                                array[i][j]=y2
                                even.remove(y2)
                                pass
                    
                else:   
                    print("turn skipped!")
    for m in range (0,3):
        for n in range(0,1):
            print (array[m][n],"|",array[m][n+1],"|",array[m][n+2])     
    if rows(array) == 15 or column(array) == 15 or diagonal(array) == 15:
         print("Player2 won!!")
         drew = True
         break

if c == 5:
    print("draw")
        
