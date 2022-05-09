#Reto 2

def Moderador():
    s_return=""
    s = ""
    cv = 0
    cf =0
    for m in (moderador):
        s=m

        for v in (valentina):
            if v==s:
                cv +=1

        for f in (felipe):
            if f==s:
                cf +=1

        if cv==cf:
            s_return+="≈"
        elif cf>cv:
            s_return += "F"
        elif cf<cv:
            s_return += "V"

    return s_return

valentina=str(input("T1"))
felipe=str(input("T2"))
moderador=str(input("T3"))
print(str(Moderador()))