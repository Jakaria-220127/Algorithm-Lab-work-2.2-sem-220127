def find_max_min_linear(numbers, count):
    max_value = min_value = numbers[0]
    for num in numbers[1:]:
        count += 1
        if num > max_value:
            max_value = num
        if num < min_value:
            min_value = num
    return max_value, min_value, count
def main():
    while True:
        print('\nMenu\n1. Find Max\n2. Find Min\n3. Exit')
        choice_1 = int(input('Enter your choice: '))
        if choice_1 == 3:
            print('Exiting... Thank You!')
            break
        elif choice_1 in [1, 2]:
            numbers = list(map(int, input('Enter numbers: ').split()))
            if not numbers:
                print("The list is empty! Please provide valid input.")
                continue
            count = 0
            max_value, min_value, count = find_max_min_linear(numbers, count)
            if choice_1 == 1:
                print(f'The max number is: {max_value}')
            elif choice_1 == 2:
                print(f'The min number is: {min_value}')
            print(f'The order of n (steps counted) is: {count}')
        else:
            print('Invalid Choice! Please try again.')
if __name__ == '__main__':
    main()