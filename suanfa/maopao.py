'''
  冒泡排序
'''
def bubble_sort(a):
    count = len(a)
    for i in range(0, count-1):
        for j in range(0, count - 1 - i):  # 已排序过的就不用再比较了
          if a[j] > a[j+1]:
              a[j], a[j+1] = a[j+1], a[j]
    return a

result = bubble_sort([3,4,5,9,8,7,1,2,6])
print(result)