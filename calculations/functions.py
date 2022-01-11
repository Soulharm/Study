import random


def test_mult_div(num, operation_type):
    example = []
    correct_result = []
    while len(example) < num:
        result = mult() if operation_type == 'mult' else div()
        if result[0] in example:
            continue
        example.append(result[0])
        correct_result.append(result[1])
    return example, correct_result


def randomnumber():
    num = [2, 3, 4, 5, 6, 7, 8, 9]
    random_number = random.choice(num)
    return random_number


def mult():
    first_num = randomnumber()
    second_num = randomnumber()
    correct_result = first_num * second_num
    example = str(first_num) + ' * ' + str(second_num) + " ="
    return [example, correct_result]


def div():
    first_num = randomnumber()
    second_num = randomnumber()
    correct_result = first_num * second_num
    example = str(correct_result) + ' : ' + str(first_num) + " ="
    return [example, second_num]




