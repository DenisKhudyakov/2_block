

def is_palindrome(numList):
    revers_list = []
    for i in range(len(numList) - 1, -1, -1):
        revers_list.append(numList[i])
    if revers_list == numList:
        return True
    else:
        return False


massiv = [1, 2, 3, 4, 5]
new_nums = []
answer = []

for i in range(0, len(massiv)):
    for j in range(i, len(massiv)):
        new_nums.append(massiv[j])
        print(new_nums)
    if is_palindrome(new_nums):
        for i_answer in range(0, i):
            answer.append(massiv[i_answer])
        print(answer)
        answer.reverse()
        break
    new_nums = []

print(massiv)
print(len(answer))
print(answer)


