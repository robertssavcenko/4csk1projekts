def rezultats(sk1, sk2):
    if sk1<6 and sk2<6:
        rez = sk1*sk2
    else:
        rez = sk1+sk2
        return rez
    
for skaitlis in range(1, 11, 2): #range funkcija kas skaita skaitlus
    for skaitlis2 in range(1, 11, 2):
        print("mūsu skaitlis:", skaitlis, "rezultāts:", rezultats(4, skaitlis))

def zvaigznites1(skaits):
    for rindasNr in range(1, skaits+1):
        for zvaigzne in range(rindasNr):
            print("*")
        print("*"*rindasNr)

zvaigznites1(7)

saraksts1 = [1, 7, 5, 9, 35, 2]
saraksts2 = [4, 2, 2, 39, 6, 4]

for skaititajs in range(len(saraksts1)):
    print("skaititajs:", skaititajs, "pirmais skaitlis:", saraksts1[skaititajs], "otrais skaitlis:", saraksts2[skaititajs], "rezultats:", rezultats(saraksts1[skaititajs], saraksts2[skaititajs]))