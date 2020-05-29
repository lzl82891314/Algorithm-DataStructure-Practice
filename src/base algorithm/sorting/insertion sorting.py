# 插入排序算法

def insertion_sort(a: []):
    length = len(a)
    if not length:
        return 
    for i in range(1, length):
        value = a[i]
        j = i - 1
        for j in range(i - 1, -1, -1):
            if a[j] > value:
                a[j + 1] = a[j]
                print(a)
                j -= 1
            else:
                break
        a[j + 1] = value
        print(a)
        print('------------------')

# Testcase
a = [6, 5, 3, 1, 4, 2]
print('before sort: ')
print(a)
print('------------------')
insertion_sort(a)
print(a)
