seq = []
msg_result = f"The answer is %d.\n"

file = open('day1-input.txt', 'r')
for line in file.readlines():
    seq.append(int(line.rstrip()))

seq.sort()


def summer(num1, num2):
    msg_skip = "skipping..."
    msg_test = f"\ntesting %d + %d..."
    msg_fail = "nope."
    msg_pass = "yep!"

    print(msg_test % (num1, num2))
    if num1 == num2:
        print(msg_skip)
    elif num1 + num2 != 2020:
        print(msg_fail)
        return None
    else:
        print(msg_pass)
        ans = num1 * num2
        return ans


def looper(seq):
    for num1 in seq:
        for num2 in seq:
            ans = summer(num1, num2)
            if ans != None:
                return ans


ans = looper(seq)
print(msg_result % ans)
