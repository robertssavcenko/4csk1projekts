def rezultats(sk1, sk2):
    if sk1<6 and sk2<6:
        rez = sk1*sk2
    else:
        rez = sk1+sk2
        return rez
    
for skaitlis in range(1, 11, 2): #range funkcija kas skaita skaitlus
    for skaitlis2 in range(1, 11, 2):
        print("mūsu skaitlis:", skaitlis, "rezultāts:", rezultats(4, skaitlis))

def zvaigznites(skats):
    for rindasNr in range(1, skaits+1):
        for zvaigzne in range(rindasNr):
            print("*")
        print("*"*rindasNr)



pirmais = "6"

print(pirmais)

vards2 = "dirs"

print(pirmais + vards2)