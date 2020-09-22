from timeit import default_timer as timer
import random
def insert_sort(a_list):
    start = timer()
    for index in range(1, len(a_list)):
        current_value = a_list[index]
        position = index
        while position > 0 and a_list[position - 1] > current_value:
            a_list[position] = a_list[position - 1]
            position = position -1
        a_list[position] = current_value
    end = timer()
    return (a_list, (end-start))

def shell_sort(a_list):
    start = timer()
    sublist_count = len(a_list) // 2
    while sublist_count > 0:
        for start_position in range(sublist_count):
            gap_insertion_sort(a_list, start_position, sublist_count)
        # print('After increments of size', sublist_count, 'The list is', a_list)
        sublist_count = sublist_count // 2
    end = timer()
    return (a_list, (end-start))

def gap_insertion_sort(a_list, start, gap):
    for i in range(start + gap, len(a_list), gap):
        current_value = a_list[i]
        position = i
        while position >= gap and a_list[position - gap] > current_value:
            a_list[position] = a_list[position - gap]
            position = position - gap
            a_list[position] = current_value

def python_sort(a_list):
    start = timer()
    a_list.sort()
    end = timer()
    return (a_list, (end-start))

def main():
    a_list = [sorted(random.sample(range(1, 10001), 500)) for i in range(100)]

    s = 0
    for x in a_list:
        r, t = insert_sort(x)
        s += t
    print('Insert sort took %10.7f seconds, on average' % (t/100))

    s = 0
    for x in a_list:
        r, t = shell_sort(x)
        s += t
    print('Shell sort took %10.7f seconds, on average' % (t/100))

    s = 0
    for x in a_list:
        r, t = python_sort(x)
        s += t
    print('Python sort took %10.7f seconds, on average' % (t/100))

main()
