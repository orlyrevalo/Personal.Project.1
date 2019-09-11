def raise_to_power(base_num, pow_num):
    result = 1
    for index in range(pow_num):
        result = result * base_num
    return result


base_num = int(input("What is the base number? "))
pow_num = int(input("What is its power? "))
print(str(base_num) + " raised to " + str(pow_num) + " is " + str(raise_to_power(base_num,pow_num)))

