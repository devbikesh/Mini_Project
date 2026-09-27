numbers = []

for number_count in range(5):
    current_number = int(input("Enter a number: "))
    numbers.append(current_number)


def calculate_total():
    total_sum = sum(numbers)
    print("Total:", total_sum)


def calculate_average():
    total_sum = sum(numbers)
    average = total_sum / len(numbers)
    print("Average:", average)


def find_largest_number():
    largest_number = max(numbers)
    print("Largest number:", largest_number)


def find_smallest_number():
    smallest_number = min(numbers)
    print("Smallest number:", smallest_number)


def count_odd_even():
    even_count = 0
    odd_count = 0

    for current_number in numbers:
        if current_number % 2 == 0:
            even_count += 1
        else:
            odd_count += 1

    print("Even numbers:", even_count)
    print("Odd numbers:", odd_count)


calculate_total()
calculate_average()
find_largest_number()
find_smallest_number()
count_odd_even()
