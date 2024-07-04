def create_phone_number(n):
    s=""
    for i in range(len(n)+4):
        if i == 0 :
            s+="("
        elif i<4:
            s+=str(n[i-1])
        elif i == 4:
            s+=")"
        elif i ==5 :
            s+=" "
        elif i>5 and i<9 :
            s+=str(n[i-3])
        elif i==9:
            s+="-"
        elif i>9:
            s+=str(n[i-4])
    
    return s
   