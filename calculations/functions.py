import random


def testmultdiv(x):
    example = []
    correctresult = []
    while len(example) < x:
        result = mult()
        if result[0] in example:
            continue
        example.append(result[0])
        correctresult.append(result[1])
    return example, correctresult


def randomnumber():
    num = [2, 3, 4, 5, 6, 7, 8, 9]
    randomnumber = random.choice(num)
    return randomnumber


def mult():
    firstnum = randomnumber()
    secondnum = randomnumber()
    correctresult = firstnum * secondnum
    example = str(firstnum) + ' * ' + str(secondnum) + " ="
    return [example, correctresult]





