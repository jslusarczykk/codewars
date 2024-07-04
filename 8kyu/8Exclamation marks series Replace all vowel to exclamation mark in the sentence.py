def replace_exclamation(st):
    st2=""
    for i in range(len(st)):
        if st[i]=="a" or st[i]=="e" or st[i]=="i" or st[i]=="o" or st[i]=="u" or st[i]=="A" or st[i]=="E" or st[i]=="I" or st[i]=="O" or st[i]=="U" :
            st2+="!"
        else:
            st2+=st[i]
    return st2
print(replace_exclamation("aeiou"))

#import re

#def replace_exclamation(s):
    #return re.sub('[aeiouAEIOU]', '!', s)