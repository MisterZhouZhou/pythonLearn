'''
 插入排序
'''
def insert_sort(a):
    count = len(a)
    for i in range(count):
        for j in range(i):
            if a[i] < a[j]:
                a.insert(j, a.pop(i))
                break
    return a

insert_sort([3,4,5,9,8,7,1,2,6])
