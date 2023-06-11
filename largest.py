def largest(l):
    maxim = l[0]
    for el in l:

        if el > maxim:
            maxim = el
    return maxim


print(largest([1, 10, 4, 3]))
