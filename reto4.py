
Lista1=dict(input())
#Lista1={"carne": 2622, "arroz": 2092, "aceite": 1717, "límpido": 4687}
Lista2=list(input("lista").split(" "))

Lista3=[]
Lista4=[]
v=0

for i in Lista2:
    if i in Lista1.keys():
        key=i
        Lista3.append(key)
        Lista4=Lista1.get(key)
        v+=Lista4
print(v)
print(" ".join(Lista3))


