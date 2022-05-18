#letters = ["a", "b", "c", "d", "e"]
# print(len(letters))


#numbers= range(9)
#for number in numbers:
#    if number == 5:
#        continue
#        print("El continue pincha")
#    else:
#        print(number)
#Dicccionarios
#jhon = {"name": "Jhon Smith",
#         "age": 18,
#      }

#print(jhon)
#jhon["country"] = "Cuba"
#print(jhon.keys())
#print(jhon.values())

#--------------------

#sets
#set = {a}
#--------
#Class

#class Car:
# define init method
#     def __init__(self, x ,y ,z):
#         self.model = x
#         self.color = y
#        self.fuel_capacity = z

 #    def sayColor(self):
 #       print("My color is", self.color)

 #    def spendFuel(self, fuelAmount):
 #        self.fuel_capacity -= fuelAmount

#new_car = Car("BMW", "Blue", 20000)
#print(new_car.fuel_capacity)
#new_car.spendFuel(2000)
#print(new_car.fuel_capacity)

#________________________________________________________________________________
#import random

#while True:
#    rand_number = random.randint(1, 20)
#    list_of_guesses=[]
#    guess=0
#    while guess != rand_number:
#        guess = int(input("Please guess a number between 1 to 20 "))
#        list_of_guesses.append(guess)
#        if guess < rand_number:
#            print("The guess is too low!")
#            print("You guessed the following numbers: ", list_of_guesses)
#            continue
#        elif guess > rand_number:
#            print("The guess is too high!")
#            print("You guessed the following numbers: ", list_of_guesses)
#            continue
#        elif guess == rand_number:
#            print("You got it!")
#            print("You guessed the following numbers: ", list_of_guesses)
#            print("Let's Continue!")
#    continue
#______________________________________________________________________________________

#square = [i**2 for i in range(10) if i**2 % 2 == 0]

#print("lola".join(["spam", "eggs", "ham"]))

#print(abs([1, 2, 3,]))
#nums = [55,56,49,22,30]
#for v in enumerate(nums):
#    print(v)




#def count_words(text, word):
#    count = 0
#    lista = text.split(" ")
#    for c in lista:
#       if c == word:
#           print(True)
#            break
#        else:
#            print(False)
#            break

#with open(r'C:/Users/Diego/Desktop/TareasPendientes.txt') as f:
#    text = f.read()
#print(text)

#lista = ["Tipos", "de", "y"]
#for word in lista:
#    perc = 100 * count_words(text, word) / len(text.split(" "))
#    print("{0} - {1}%".format(word, round(perc, 2)))
#------------------------------------------------------------------
#def my_func(f, arg):
#    print(f(arg))

#my_func(lambda x: 2*x*x, 5)

#double = lambda x, y: x * 2 + y
#print(double(7))

#La funcion Map,le aplica una funcion a cada elemento de la lista pasada por parametro
#nums = [11, 6, 20, 30]
#result = list(map(lambda x: x+5, nums))
#print(result)

#The function filter filters an iterable by removing items that don't match a predicate (a function that returns a Boolean).
#nums = [11, 6, 20, 30]
#result = list(filter(lambda x: x%2==0, nums))
#print(result)

#---------------------------------------------------------------------------
#Generators are a type of iterable, like lists or tuples.
#The yield statement is used to define a generator,
#replacing the return of a function to provide a result to its caller
#without destroying local variables.

#def countdown(i):

#   while i > 0:
#        yield i
#        i -= 1
#for i in countdown(8):
#    print(i)
#-------------------------------------------------------------------------------
#Recursividad:
#def es_par(x):
#    if x == 0:
#        return True
#    else:
#        return es_impar(x-1)
#def es_impar(x):
#    return not es_par(x)
#-------------------------------------------------------------------------------
#Fibbonacci:
#def fib(x):
#    if x == 0 or x == 1:
#        return 1
#    else:
#        return fib(x-1) + fib(x-2)

#print(fib(4))
#------------------------------------------------------------------------------
#Retornar el cuadrado de todos los elementos de una lista sumados de forma recursiva
#def calc(list):
#    if len(list)==0:
#        return 0
#    else:
#        return list[0]*list[0] + calc(list[1:])

#list = [1, 3, 4, 2, 5]
#x = calc(list)
#print(x)
#----------------------------------------------------------------------------------
# Set son typos de datos estructurales que al igual que las listas permiten ciertas funciones,pero no permiten
#elementos repetidos dentro de ellos
nums = {1,2,1,3,1,2,6,8}
lo = {1,2,3,4,5,6,7}

print(nums.symmetric_difference(lo))

#As we have seen in the previous lessons, Python supports the following data structures: lists, dictionaries, tuples, sets.
#When to use a dictionary:
#- When you need a logical association between a key:value pair.
#- When you need fast lookup for your data, based on a custom key.
#- When your data is being constantly modified. Remember, dictionaries are mutable.

#When to use the other types:
#- Use lists if you have a collection of data that does not need random access. Try to choose lists when you need a simple, iterable collection that is modified frequently.
#- Use a set if you need uniqueness for the elements.
#- Use tuples when your data cannot change.