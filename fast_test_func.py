# import pytest
from linked_list_unordered import UnorderedList


# @pytest.fixture
def exp_res():
    return {
        'case2': None,
        'case3': None,
        'case4': None,
        'case5': None,
        'case6': None,
        'case7': None,
        'case8': 8,
        'case9': None,
        'case10': 6,
        'case11': 7,
        'case12': None
    }


# @pytest.fixture
def linked_list_methods():
    results = dict()
    ll = UnorderedList()
    results['case2'] = ll.add(7)
    results['case3'] = ll.append(7)
    results['case4'] = ll.add(9)
    results['case5'] = ll.append(8)
    results['case6'] = ll.add(6)
    results['case7'] = ll.add(0)
    results['case8'] = ll.get(5)
    results['case9'] = ll.add(0)
    results['case10'] = ll.get(2)
    results['case11'] = ll.get(5)
    results['case12'] = ll.append(4)
    return results


print(exp_res())
print(linked_list_methods())


# def test_linked_list_methods():
#     results = linked_list_methods()
#     exp_results = exp_res()
#     for res, exp in zip(results, exp_results):  # Попытался быстро напсать мини тест, но он работает некорректно
#         assert res == exp


'''
Тесты с leetcode. Я пока не разобрался, как строки из списка превращать в вызов функций.

Input:
["MyLinkedList","addAtHead","addAtTail","addAtHead","addAtTail","addAtHead","addAtHead","get","addAtHead","get","get","addAtTail"]
[[],[7],[7],[9],[8],[6],[0],[5],[0],[2],[5],[4]]
Output:
[null,null,null,null,null,null,null,8,null,6,8,null]      # Это неправильный результат кода
Expected:
[null,null,null,null,null,null,null,8,null,6,7,null]
'''


