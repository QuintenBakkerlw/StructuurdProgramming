import random
"Quinten Bakker"


"opdracht 1 - Piramide"


length = 15
def piramide(length):
        ## maakt eerste helft van de piramide ##
    for x in range(1, length + 1):
        print(x * '*')
        ## maakt tweede helft van de piramide
    for i in range(length - 1, 0, -1):
        print(i * '*')
    return 'Your Piramide'

print(piramide(length))



"Opdracht 2 -TekstCheck"


str2 = 'abcdefg'
str1 = 'abddefghijklmnop'
def tekstchecker(string1, string2):
        ## houdt de index bij ##
    count = 0
    for i in range(len(string1)):

            ## als de string langer is dan de andere
        if (i + 1) == len(string2):
            break
            ## kijkt of de elementen overeen komen ##
        if string1[i] == string2[i]:
            count += 1

    return count

print(tekstchecker(str1, str2))


"Opdracht 3 -Lijstcheck"


lst = [1,5,6,7,7,8,9,10,12,24,15,66,77,5,5,5,5,5]

"Opdracht A"

xgetal = 5
def frequentiex(xgetal, lst):
        ## houdt bij hoevaak xgetal voor komt ##
    count = 0
        ## kijkt bij elke element in lst of het dezelfde is als xgetal ##
    for i in lst:
        if i == xgetal:
            count += 1
    return count

print(frequentiex(xgetal,lst))



"Opdacht B"

def verschillberekenen(lst):
        ## berekent de max en min en berekent het verschill ##
    maxgetal = max(lst)
    mingetal = min(lst)
    verschill = maxgetal - mingetal
    return verschill

print(verschillberekenen(lst))

lst1010 = [1,0,1,0,0,1,1,0,0,0,1,1,1,1,0,1,0,1,0,0,0,1,1,1]

"Opdracht C"

def CheckLst(lst):
        ## N1 en N0 houdt bij hoeveel 1 en 0 er in de lijst bevindt ##
    N1 = 0
    N0 = 0
    for item in lst:
        if item == 1:
            N1 += 1
        else:
            N0 += 1
        ## is de hoeveelheid 0 groter dan 12 ##
    if N0 > 12:
        return False
        ## is de hoeveelheid 1 groter dan 0 ##
    if N1 > N0:
        return True
    else:
        return False

print(CheckLst(lst1010))



"Opdracht 4 -Palindroom"


str = 'meetsysteem'
def checkPalindroom(str):
        ## draait de string om ##
    strreverse = str[::-1]
    index = -1
        ## kijkt voor elke element of het dezelfde is of niet ##
    for i in str:
        index += 1
        if str[index] != strreverse[index]:
            return False
    return True

print(checkPalindroom(str))



def checkPalindroomHandmatig(str):
    strreversed = []
    index = len(str)
        ## draait de input str om ##
    while index > 0:
        strreversed += str[index - 1]
        index = index - 1
    strreversed = ''.join(strreversed)
    index2 = len(str) - 1
    while index2 > 0:
            ## kijkt voor elke element of het dezelfde is of niet ##
        if str[index2] != strreversed[index2]:
            return False
        else:
            index2 = index2 - 1
            return True

print(checkPalindroomHandmatig(str))


"Opdracht 5 -Sorteren"


## Bron
"https://stackabuse.com/sorting-algorithms-in-python/"


def bubble_sort(nums):
    # We set swapped to True so the loop looks runs at least once
    swapped = True
    while swapped:
        swapped = False
        for i in range(len(nums) - 1):
            if nums[i] > nums[i + 1]:
                # Swap the elements
                nums[i], nums[i + 1] = nums[i + 1], nums[i]
                # Set the flag to True so we'll loop again
                swapped = True


# Verify it works
random_list_of_nums = [5, 2, 1, 8, 4]
bubble_sort(random_list_of_nums)
print(random_list_of_nums)

print(bubble_sort(random_list_of_nums))


"Opdracht 6 -Gemiddelde berekenen"


lst = [1,2,3,4,5,6,7,8,9,10]
def gemiddelde(lst):
        ## berekend sum van alle elemeten en deelt het door de aantal elementen ##
    total = sum(lst)
    lenght = len(lst)
    gemiddelde = total/lenght
    return gemiddelde

print(gemiddelde(lst))

"Opdracht 7-Random"


def randomgame():
        ## maakt een random getall tussen 0 en 50
    randomgenerator = random.randint(0, 50)
    x = 1
        ## loopt tot dat input juist is ##
    while x == 1:
        inputnumber = int(input('choose a number'))
        if inputnumber == randomgenerator:
            x += 1
            print('yes you did it!')
            return True

print(randomgame())



"Opdracht 8-Compressie"


def compressor():
        ## opent file een leest het ##
    f = open('text.txt', "r")
    compressed_text = []
        ## haalt onnodig elementen weg ##
    for item in f:
        compressed_text.append(item.strip().replace(" ", ''))
    f.close()
        ## opent file en write compressed text ##
    f = open('text.txt', 'w')
    f.write("".join(compressed_text))
    f.close()
    return "rearanged file"

print(compressor())


"Opdracht 9-Cyclish verschuiven"


ch = 'abcdef'
n = -1
def roller(ch,n):
    lst = []
        ## maakt van string lst ##
    for x in ch:
        lst.append(x)
        ## veranderd elementen in ch n keer #
    for i in range(0, n):
        if n > 0:
            memory1 = lst[0]
            lst.remove(lst[0])
            lst.append(memory1)
    for x in range(n,0):
        if n < 0:
            memory2 = lst[-1]
            lst.remove(lst[-1])
            lst.insert(0, memory2)
    return "".join(lst)

print(roller(ch,n))


"Opdracht 10-Fibonaci"


n = 5
def fibonaci(n):
    fibonaci = [0 , 1]
        ## count houdt bij hoevaakt het loopt heeft gedraait ##
    count = 0
    while count != n:
            ## pakt laaste en second last en telt ze bij elkaar op en voegt het toe aan lst ##
            ## herhaalt tot count == n ##
        latest_number = fibonaci[-1]
        second_latest_number = fibonaci[-2]
        combined = latest_number + second_latest_number
        fibonaci.append(combined)
        count += 1
    return fibonaci

print(fibonaci(n))


"Opdracht 11-Ceasarcijfer"


text = 'To be or not to be, That is the question'
def ceasar_salade(text):
    alfabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    rotatie = int(input('geef de rotatie aan: '))
    new_lijst = []
        ## kijkt naar elke element in text ##
    for item in text.lower():
            ## als element niet in text voeg het element toe naar new lijst ##
        if item not in alfabet:
            new_lijst.append(item)
        else:
                ## berekent nieuwe index van letter met rotatie ##
            index = alfabet.index(item) + rotatie
                ## als het over 25 gaat begint het over nieuwe met tellen ##
            if index >= 25:
                index = index - 26
                new_lijst.append(alfabet[index])
            else:
                new_lijst.append(alfabet[index])
    return ''.join(new_lijst)

print(ceasar_salade(text))


"Opdracht 12-Fizzbuzz"


def buzz_the_fizz():
    lijst = list(range(1 , 101))
        ## kijkt naar elke element in lijst ##
    for item in lijst:
        index = lijst.index(item)

            ## als het element deelbaar is door 3 en 5 replace het met FizzBuzz ##
        if item % 5 == 0 and item % 3 == 0:
            lijst[index] = 'FizzBuzz'

            ## als het element deelbaar is door 5 replace het met Fizz ##
        elif item % 5 == 0:
            lijst[index] = 'Fizz'

            ## als het element deelbaar is door 3 replace het met Fizz ##
        elif item % 3 == 0:
            lijst[index] = 'Buzz'
    return lst

print(buzz_the_fizz())

"Einde Opdracht ################"