
def add_sums(sum : int, index : int , my_list : [int]) -> int:
    "returns the sum of the indexes so far"
    if index == len(my_list):
        return sum
    sum += my_list[index]
    index += 1
    return add_sums(sum, index, my_list)


def get_sum(my_list : [int]) -> int:
    counter = 0
    return add_sums(0, 0, my_list)






