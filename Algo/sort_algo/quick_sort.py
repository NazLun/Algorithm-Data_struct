
def quick_sort(arr: list) -> list:
    if len(arr) <= 1:
        return arr
    support_elem = arr[0]
    left_sub_arr = [elem for elem in arr[1:] if elem <= support_elem]
    right_sub_arr = [elem for elem in arr[1:] if elem > support_elem]
    return quick_sort(left_sub_arr) + [support_elem] + quick_sort(right_sub_arr)

"""
test_arr = [20, 34, 6, 8, 8, 6, 5, 43, 3, 6, 8, 90, 9, 7, 5, 4, 23, 65, 7, 76, 9, 9, 8, 6, 5, 5]
print(quick_sort(test_arr))
"""
