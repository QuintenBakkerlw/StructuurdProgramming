import random
"opdracht 1 - Piramide"

# length = 15
# def piramide(length):
#     for x in range(1, length + 1):
#         print(x * '*')
#     for i in range(length - 1, 0, -1):
#         print(i * '*')
#     return 'Your Piramide'
#
# print(piramide(length))

"Opdracht 2 -TekstCheck"
# str2 = 'abcdefg'
# str1 = 'abddefghijklmnop'
# def tekstchecker(string1, string2):
#     count = 0
#     for i in range(len(string1)):
#         print(string1[i], string2[i])
#
#         if (i + 1) == len(string2):
#             break
#
#         if string1[i] == string2[i]:
#             count += 1
#         else:
#             break
#     return count
#
#
# print(tekstchecker(str1, str2))
#
#
# "Opdracht 3 -Lijstcheck"
# lst = [1,5,6,7,7,8,9,10,12,24,15,66,77,5,5,5,5,5]
# def frequentiex(xgetal, lst):
#     count = 0
#     for item in lst:
#         if item == xgetal:
#             count += 1
#     return count
#
# print(frequentiex(5,lst))
#
# def verschillberekenen(lst):
#     maxgetal = max(lst)
#     mingetal = min(lst)
#     verschill = maxgetal - mingetal
#     return verschill
# print(verschillberekenen(lst))

# lst1010 = [1,0,1,0,0,1,1,0,0,0,1,1,1,1,0,1,0,1,0,0,0,1,1,1]
# def CheckLst(lst):
#     N1 = 0
#     N0 = 0
#     for item in lst:
#         if item == 1:
#             N1 += 1
#         else:
#             N0 += 1
#     if N0 > 12:
#         return False
#     if N1 > N0:
#         return True
#     else:
#         return False
#
#
# print(CheckLst(lst1010))



"Opdracht 4 -Palindroom"
str = 'meetsysteem'

def checkPalindroom(str):
    strreverse = str[::-1]
    index = -1
    for i in str:
        index += 1
        if str[index] != strreverse[index]:
            return False
    return True

def checkPalindroomHandmatig(str):
    strreversed = []
    index = len(str)
    while index > 0:
        strreversed += str[index - 1]
        index = index - 1
    strreversed = ''.join(strreversed)
    index2 = len(str) - 1
    while index2 > 0:
        print(index2)
        if str[index2] != strreversed[index2]:
            return False
        else:
            index2 = index2 - 1
            return True


"Opdracht 5 -Sorteren"
## Bron
"https://stackabuse.com/sorting-algorithms-in-python/"
# def bubble_sort(nums):
#     # We set swapped to True so the loop looks runs at least once
#     swapped = True
#     while swapped:
#         swapped = False
#         for i in range(len(nums) - 1):
#             if nums[i] > nums[i + 1]:
#                 # Swap the elements
#                 nums[i], nums[i + 1] = nums[i + 1], nums[i]
#                 # Set the flag to True so we'll loop again
#                 swapped = True
#
#
# # Verify it works
# random_list_of_nums = [5, 2, 1, 8, 4]
# bubble_sort(random_list_of_nums)
# print(random_list_of_nums)
#
# print(bubble_sort(random_list_of_nums))


"Opdracht 6 -Gemiddelde berekenen"
# lst = [1,2,3,4,5,6,7,8,9,10]
# def gemiddelde(lst):
#     total = sum(lst)
#     lenght = len(lst)
#     gemiddelde = total/lenght
#     return gemiddelde
# print(gemiddelde(lst))

"Opdracht 7-Random"

def randomgame():
    randomgenerator = random.randint(0, 50)
    print(randomgenerator)
    while True:
        number = int(input('choose a number'))
        if number == randomgenerator:
            return False
        else:
            number
print(randomgame())