for i in range(6):
    for j in range(7):
        if ((j%3 != 0) and (i==0)) or ((j%3 == 0) and (i == 1)) or ((j+i==2) and (i==2)) or ((i+j==8) and (i==2)) or ((i+j==4) and (i==3)) or ((i+j==8) and (i==3)) or ((i+j==6) and (i==4)) or ((i-j==0) and (i==4)) or ((i-j==2) and (i==5)):
            print('*',end=" ")
        else :
            print(' ',end=" ")
    print()