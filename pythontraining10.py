for i in range(7):
    for k in range(6):
        if ((i+k==1) and (i==0)) or ((i+k==4) and (i==0)) or ((i+k==2) and (i==1)) or ((i+k==4) and (i==1)) or ((i+k==3) and (i==2)) or ((i-k==0) and (i==2)) or ((i+k==4) and (i==3)) or ((i+k==5) and (i==3)) or ((i+k==5) and (i==4)) or ((i+k==7) and (i==4)) or ((i+k==6) and (i==5)) or ((i+k==9) and (i==5)) or ((i+k==7) and (i==6)) or ((k+i==11) and (i==6)) :
            print('*',end=" ")
        else:
            print(' ',end=" ")
    print()