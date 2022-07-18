mydict = {'2':'radiohead','1':'five finger death punch', '5':'linkin park', '4':'scorpions', '3':'three days grace'}

a = []
for k in mydict.keys():
    a.append(k)

def minimum_index(arr):
    mi = 0
    m = arr[mi]
    if len(arr) > 1:
        for i in range(1, len(arr)):
            if arr[i] < m:
                m = arr[i] #min элемент по умолчанию
                mi = i #index min элемента
    return mi

def sort_asc(arr):
    b = []
    for _ in range(len(arr)):
        j = minimum_index(arr)
        b.append(arr[j])
        arr.pop(j)
    return b

c = sort_asc(a)
for ci in c:
    print(ci, '-', mydict[ci])