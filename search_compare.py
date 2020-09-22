import random
from timeit import default_timer as timer

def sequential_search(a_list, item):
    start = timer()
    pos = 0
    found = False

    while pos < len(a_list) and not found:
        if a_list[pos] == item:
            found = True
        else:
            pos = pos+1
    end = timer()
    return (found, (end - start))

def ordered_sequential_search(a_list, item):
    start = timer()
    pos = 0
    found = False
    stop = False
    while pos < len(a_list) and not found and not stop:
        if a_list[pos] == item:
            found = True
        else:
            if a_list[pos] > item:
                stop = True
            else:
                pos = pos+1
    end = timer()
    return (found, (end-start))

def binary_search_iterative(a_list, item):
    start = timer()
    first = 0
    last = len(a_list) - 1
    found = False

    while first <= last and not found:
        midpoint = (first + last) // 2
        if a_list[midpoint] == item:
            found = True
        else:
            if item < a_list[midpoint]:
                last = midpoint - 1
            else:
                first = midpoint + 1
    end = timer()
    return (found, (end-start))

def binary_search_recursive(a_list, item):
    start = timer()
    if len(a_list) == 0:
        end = timer()
        return (False, (end-start))
    else:
        midpoint = len(a_list) // 2
    if a_list[midpoint] == item:
        end = timer()
        return (True, (end-start))
    else:
        if item < a_list[midpoint]:
            return binary_search_recursive(a_list[:midpoint], item)
        else:
            return binary_search_recursive(a_list[midpoint+1:], item)

def main():
    ls = [sorted(random.sample(range(1, 10001), 500)) for i in range(100)]

    s = 0
    for x in ls:
        res, t = sequential_search(x, -1)
        s += t
    print('Sequential search took %10.7f seconds, on average.' % (s/100))

    s = 0
    for x in ls:
        res, t = ordered_sequential_search(x, -1)
        s += t
    print('Ordered sequential search took %10.7f seconds, on average.' % (s/100))


    s = 0
    for x in ls:
        res, t = binary_search_iterative(x, -1)
        s += t
    print('Binary (iterative) search took %10.7f seconds, on average.' % (s/100))


    s = 0
    for x in ls:
        res, t = binary_search_recursive(x, -1)
        s += t
    print('Binary (recursive) search took %10.7f seconds, on average.' % (s/100))

main()
