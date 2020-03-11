#  # val: object
#  # print([bool(val) for val in lista =[0, [], '']])
# name = 'colt'
# print([char.upper() for char in name ])
#
# nums = [1,2,3]
#
# numery =[num * 10 for num in nums]
#
# print(numery)
# value = [bool(val) for val in [0 , [], '']]
# print(value)
#
# value2 = [bool(val) for val in [1, [1,2,3], 'KUPA']]
# print(value2)
#
# numbers = [ 1,2,3,4,5,6]
# strinumb = [str(num2) for num2 in numbers]
# print(strinumb)
#
# słowa = ['1', '2', '3']
# liczby = [int(stringi) for stringi in słowa]
# print(liczby)
#
# imiona = ['czarek', 'karolina', 'przemek', 'seba']
# zDuzej = [duza.upper() for duza in imiona]
# print(zDuzej)

# evens = [num for num in range(0,101) if num % 2 == 0]
# print(evens)
#
# odds =  [num for num in range(0,101) if num % 2 != 0]
# print(odds)
#
# answer = [person[0] for person in ["Elie", "Tim", "Matt"]]
# print(answer)

answer2 = [val[::-1].lower() for val in ["Elie", "Tim", "Matt"]]
print(answer2)
