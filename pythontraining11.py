for i in range(5):
    for j in range(5):
        if ((j%4==0) and (i==0) or (i+j==1) and (i==1) or (i==j) and (i==1) or (i+j==5) and (i==1) or (j%2==0) and (i==2) or (j+i==3) and (i==3) or (j+i==6) and (i==3) or (j+i==7) and (i==3) or (j%4==0) and (i==4)):
            print('*',end=" ")
        else:
            print(' ',end=" ")
    print()