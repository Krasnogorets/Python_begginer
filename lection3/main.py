# def sum_numbers(n, y):
#     sum=0
#     for i in range(1,n+1):
#         sum+=i +y
#     return sum
# print(sum_numbers(5, 8))

# def sum_args(*args):
#     res=""
#     for i in args:
#         res+=i
#     return res
# print(sum_args('f','i','l','l'))
# import module1
# from module1 import * # импорт всех функций
# print(max_num(6,9))
# import module1 as m1
# print(m1.max_num(6,9))

# def fib(n):
#     if n in [1, 2]:
#         return 1
#     return fib(n - 1) + fib(n - 2)
#
#
# list1 = []
# for i in range(1, 40):
#     list1.append(fib(i))
#
# print(*list1)

# Быстрая сортировка

def quicksort(array):
    if len(array) < 2:
        return array
    else:
        pivot = array[0]
    less = [i for i in array[1:] if i <= pivot]
    greater = [i for i in array[1:] if i > pivot]
    return quicksort(less) + [pivot] + quicksort(greater)


# print(quicksort([10, 5, 2, 3]))

def merge_sort(nums):
    if len(nums) > 1:
        mid = len(nums) // 2
        left = nums[:mid]
        right = nums[mid:]
        print(left,right,nums)
        merge_sort(left)
        merge_sort(right)
        i = j = k = 0

        while i < len(left) and j < len(right):
            print(left, right, nums)
            if left[i] < right[j]:
                nums[k] = left[i]
                i += 1
            else:
                nums[k] = right[j]
                j += 1
            k += 1
        while i < len(left):
            nums[k] = left[i]
            i += 1
            k += 1
        while j < len(right):
            nums[k] = right[j]
            j += 1
            k += 1


list2 = [1, 4, 7, 34, 23, 56, 34, 4, 8, 90, 56, 67, 45, 54, 23, 8, 4, 5, 55, 5, 6, 56]
merge_sort(list2)
print(list2)
