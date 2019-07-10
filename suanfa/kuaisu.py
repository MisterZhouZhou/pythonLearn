'''
 快速排序
'''

def quick_sort(a):
    if a == []:
        return []
    else:
        afirst = a[0]
        aless = quick_sort([l for l in a[1:] if l < afirst])
        amore = quick_sort([m for m in a[1:] if m > afirst])
        return aless + [afirst] + amore

a = quick_sort([3,4,5,9,8,7,1,2,6])
print(a)