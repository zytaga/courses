def apply_twice(func, arg):
   return func(func(arg))

def add_five(x):
   return x + 5

print(apply_twice(add_five, 10))

def pure_function(x, y):
  temp = x + 2*y
  return temp / (2*x + y)

some_list = []

def impure(arg):
  some_list.append(arg)

  y = x ** 2
  z = x + y
  return z

def my_func(f, arg):
  return f(arg)

my_func(lambda x: 2*x*x, 5)


def factorial(x):
    if x == 1:
        return 1
    else:
        return x * factorial(x - 1)


print(factorial(5))


def factorial(x):
    return x * factorial(x - 1)


print(factorial(5))



def is_even(x):
  if x == 0:
    return True
  else:
    return is_odd(x-1)

def is_odd(x):
  return not is_even(x)


print(is_odd(17))
print(is_even(23))



def fib(x):
  if x == 0 or x == 1:
    return 1
  else:
    return fib(x-1) + fib(x-2)
print(fib(4))



num_set = {1, 2, 3, 4, 5}
word_set = set(["spam", "eggs", "sausage"])

print(3 in num_set)
print("spam" not in word_set)'''


nums = {1, 2, 1, 3, 1, 4, 5, 6}
print(nums)
nums.add(-7)
nums.remove(3)
print(nums)'''


first = {1, 2, 3, 4, 5, 6}
second = {4, 5, 6, 7, 8, 9}

print(first | second)
print(first & second)
print(first - second)
print(second - first)
print(first ^ second)



a = {1, 2, 3}
b = {0, 3, 4, 5}
print(a & b)


rom itertools import count

for i in count(3):
  print(i)
  if i >=11:
    break

    from itertools import accumulate, takewhile

    nums = list(accumulate(range(8)))
    print(nums)
    print(list(takewhile(lambda x: x <= 6, nums)))

    from itertools import product, permutations

    letters = ("A", "B")
    print(list(product(letters, range(2))))
    print(list(permutations(letters))) 








