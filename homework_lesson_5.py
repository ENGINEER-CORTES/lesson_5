def num(n):
    for i in range( 1, n+ 1):
       if n %  i == 0: break
    return n ==  i
print('Является ли простым числом :', num(131))

def num_2(n):
    list = []
    for i in range( 1, n+ 1):
        if n %  i == 0: list == list.insert(0, i)
    return list
print('Список всех делителей без остатка :', num_2(131))

def num_max_smp (n):
    list = num_2(n)
    list_2 = []
    for i in range(-1, len(list) - 1):
        if num( list[ i]): list_2 ==  list_2.insert( i, list[i])
    return list_2[0]
print('Максимальный простой делитель без остатка :', num_max_smp(131))

def num_max (n):
    list=[]
    for i in range( 1, n+ 1):
        if n %  i == 0: list == list.insert(0,i)
    return list [0]
print('Максимальный делитель без остатка :', num_max(131))