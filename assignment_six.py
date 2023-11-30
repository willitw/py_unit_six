def get_numbers(upper_limit):
    """
    Generates a list of numbers from 2 to the inputed upper limit
    :param upper_limit: The upper limit for the generated numbers
    :return: A list of numbers from 2 to upper_limit
    """
    return list(range(2, upper_limit + 1))

def get_primes(numbers):
    """
    Finds the prime numbers from the inputed list of numbers by getting rid of all muiltibles of prime numbers starting from 2
    :param numbers: A list of numbers
    :return: A list of prime numbers
    """
    primes = []                                                         # start an empty list to store prime numbers
    checking = numbers[0]                                               # assign the first number in the numbers list as checking

    while len(numbers) > 0:                                             # continue the loop as long as there are numbers in the list
        primes.append(checking)                                         # add checking to the list of primes
        numbers = [num for num in numbers if num % checking != 0]       # remove multiples of checking from the numbers list

        if len(numbers) > 0:                                            # if there are still numbers in the numbers list make checking the next number in the numbers list
            checking = numbers[0]                                       # assign the next number as checking

    return primes                                                       # return the list of primes

def main():

    print("This program will tell you what prime numbers there are starting at two and going up to limit you input.")
    upper_limit = int(input("Enter the upper limit (2 or above): "))    # get user input for the upper limit for numbers list
    numbers = get_numbers(upper_limit)                                  # make a list of numbers up to the inputed limit called numberscusing the get_numbers function
    primes = get_primes(numbers)                                        # find prime numbers from the generated list using the get_primes function
    print("Primes:", primes)                                            # print the list of prime numbers
    print("Number of Primes:", len(primes))                             # prints the number of prime numbers in the primes list

if __name__ == "__main__":
    main()
