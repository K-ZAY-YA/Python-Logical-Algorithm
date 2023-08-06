for i in range(4):
    for j in range(13):
        if ((j%6==0) and (i==0) or (j==i) and (i==1) or (j+i==6) and (i==1) or (j+i==8) and (i==1) or (j+i==12) and (i==1) or (j==i) and (i==2) or (j+i==6) and (i==2) or (j+i==10) and (i==2) or (j+i==12) and (i==2) or (j==i) and (i==3) or (j+i==12) and (i==3)):
            print('*',end=" ")
        else:
            print(' ',end=" ")
    print()