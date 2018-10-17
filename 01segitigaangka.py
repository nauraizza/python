def loop(small, biggest):
    result = ""
    for i in range(small, biggest):
        result += str(i) + " "
    return result


for i in range(1, 10):
    print(loop(i, 10))