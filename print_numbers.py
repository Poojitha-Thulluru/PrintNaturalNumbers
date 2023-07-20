def get_numbers_till_n(target_num: int) -> None:
    if target_num == 1:
        print(1, end=' ')
    else:
        get_numbers_till_n(target_num - 1)
        print(target_num, end=' ')


if __name__ == "__main__":
    target = int(input("Enter number to print its natural numbers : "))
    get_numbers_till_n(target)
    print()
