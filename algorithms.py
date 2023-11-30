
def add_numbers(numbers):
    """
    Ex. add_numbers([9, 5, 11, 6, 1, 15]) returns 47
    :param numbers: a list of numbers
    :return: the sum of all the numbers in the list
    """
    total_sum = 0             # create a variable to remeber the total sum
    for number in numbers:    # go through each of the numbers in the list
        total_sum += number   # add all he numbers to the total
    return total_sum          # reurn the total

result = add_numbers([9, 5, 11, 6, 1, 15])
print(result)                 # prints result it should be 47

def get_max(numbers):
    """
    Ex. get_max([45, 23, 99, 34, 67, 98, 0]) returns 99
    :param numbers: a list of numbers
    :return: The largest number in the list
    """

    max_number = numbers[0]      # creates a variable to keep track of the biggest number and sets its initial value to be the first item in the list
    for number in numbers:       # loops through all the numbers in the list
        if number > max_number:  # if the current number is bigger then the current max then set the max to that number
            max_number = number

    return max_number   # returns the biggest number

result = get_max([45, 23, 99, 34, 67, 98, 0])
print(result)  # prints the result it should be 99

# def get_min(numbers):
#     """
#     Ex. get_min([45, 23, 99, 34, 67, 98, 0]) returns 0
#     :param numbers: a list of numbers
#     :return: The smallest number in the list
#     """
#     pass # remove this line when starting your function
#
#
# def merge(list1, list2):
#     """
#     Ex. merge([3, 4, 7, 9], [1, 5, 8, 11]) return [1, 3, 4, 5, 7, 8, 9, 11]
#     :param list1: a list in sorted order
#     :param list2: a second list in sorted order
#     :return: a single list consisting of both smaller lists combined in sorted order.
#     """
#     pass # remove this line when starting your function