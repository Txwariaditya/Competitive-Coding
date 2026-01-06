list1 = [10, 20, 10, 30, 50]

def nxtG(lst):
    while lst:
        a = lst.pop()
        if lst and a < lst[-1]:   
            print(True)
        else:
            print(False)

nxtG(list1)

list2 = [10, 20, 30, 30, 50]
listUnique = []

def nxtG(lst):
    while lst:
        a = lst.pop()
        if lst and a != lst[-1]:   
            listUnique.append(a)
            
    print(listUnique)

nxtG(list2)
