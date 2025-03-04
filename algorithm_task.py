def check_number(num):
    print('Hello') if num > 7 else None


def check_name(name):
    print('Hello, John') if name == 'John' else print('There is no such name')


def check_array(array):
    result = [x for x in array if x % 3 == 0]
    print(result)


def main():
    num = int(input('Enter a test number: '))
    check_number(num)

    name = input('Enter a test name: ')
    check_name(name)

    array = list(map(int, input('Enter any number sequence separated by space ').split()))
    check_array(array)


if __name__ == '__main__':
    main()
