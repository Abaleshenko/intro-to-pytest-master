lst = [0, 1]


def find_fibonacci(limit):
    for i in range(3,int(limit)+1):
        length = len(lst)
        second_last_number = length - 2
        lst.append(lst[-1] + lst[second_last_number])
        return lst


#limit = input('Enter a non zero integer number : ')
find_fibonacci(8)

#find_fibonacci(8)