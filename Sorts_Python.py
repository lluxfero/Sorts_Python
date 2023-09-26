# -*- coding: cp1251 -*-

def BubbleSortImp(lst):  
    for i in range(0,len(lst)-1): 
        for j in range(len(lst)-1): 
            if(lst[j] > lst[j+1]): 
                lst[j], lst[j+1] = lst[j+1], lst[j]
    return lst

# ���������, ������������ �� ������
def is_sorted_BubFunc(lst):
    return all(lst[i] <= lst[i+1] for i in range(len(lst)-1))
# �������� �� ������ � ������ ������� �������� ��������, ���� ��� �� � ���������� �������
def bubble_pass_BubFunc(lst):
    if len(lst) <= 1:
        return lst
    else:
        head, *tail = lst # ��������� ������ �� ������ � �����
        if head > tail[0]: # ���� ������ ������ ������� �������� ������, ������ �� �������
            head, tail[0] = tail[0], head
        return [head] + bubble_pass_BubFunc(tail) # ���������� ������ �� ������ � ���������������� ������
# ��������� ������ �� ������, ���� �� �� ����� ������������
def BubbleSortFunc(lst):
    if is_sorted_BubFunc(lst): # ��� ������������, ���������� ���
        return lst
    else:
        return BubbleSortFunc(bubble_pass_BubFunc(lst)) # ������ ������ �� ������ � ��������� ����������


def InsertionSortImp(lst):
    for i in range(1, len(lst)):
        key = lst[i]
        j = i-1
        while j >=0 and key < lst[j] :
            lst[j+1] = lst[j]
            j -= 1
        lst[j+1] = key 
    return lst

# ��������� ������� � ��������������� ������ �� ���������� �������
def insert_InsertFunc(lst, elem):
    return [elem] if not lst else [min(lst[0], elem)] + insert_InsertFunc(lst[1:], max(lst[0], elem))
# ��������� ������, ��������� ������� �������
def InsertionSortFunc(lst):
    return [] if not lst else insert_InsertFunc(InsertionSortFunc(lst[:-1]), lst[-1])
    

def SelectionSortImp(lst):
    n = len(lst)
    for i in range(n-1):
        m = i
        for j in range(i+1, n):
            if lst[j] < lst[m]:
                m = j
        lst[i], lst[m] = lst[m], lst[i]
    return lst

# ������� ����������� ������� � ������
def find_min_SelFunc(lst):
    return lst[0] if len(lst) == 1 else min(lst[0], find_min_SelFunc(lst[1:]))
# ������� ������� �� ������
def remove_SelFunc(lst, elem):
    return lst[1:] if lst[0] == elem else [lst[0]] + remove_SelFunc(lst[1:], elem)
# ��������� ������, ��������� ������� ������ �������� � ��������
def SelectionSortFunc(lst):
    return [] if not lst else [find_min_SelFunc(lst)] + SelectionSortFunc(remove_SelFunc(lst, find_min_SelFunc(lst)))

 
lst = [-5, 16, 87, 0, -33, 25, -11]
print("bubble sort | imp: ", BubbleSortImp(lst)) 
lst = [-5, 16, 87, 0, -33, 25, -11]
print("bubble sort | func: ", BubbleSortFunc(lst)) 

lst = [-5, 16, 87, 0, -33, 25, -11]
print("insertion sort | imp: ", InsertionSortImp(lst)) 
lst = [-5, 16, 87, 0, -33, 25, -11]
print("insertion sort | func: ", InsertionSortFunc(lst)) 

lst = [-5, 16, 87, 0, -33, 25, -11]
print("selection sort | imp: ", SelectionSortImp(lst)) 
lst = [-5, 16, 87, 0, -33, 25, -11]
print("selection sort | func: ", SelectionSortFunc(lst)) 
