def rec_row(num, sharps):
    print('_'*(num-sharps), end="")
    print('#'*sharps, end="")
    print()


def rec_pattern(num, row=0):
    if num > 0:
        if row < num:
            row += 1
            rec_row(num, row)
            rec_pattern(num, row)
    elif num == 0:
        print('Not Draw!')
    else:
        if row < abs(num):
            rec_row(abs(num), abs(num)-row)
            row += 1
            rec_pattern(num, row)


num = int(input("Enter Input : "))
rec_pattern(num)
