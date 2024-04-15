def create_generator():
    num = 0
    while True:
        yield num
        num += 1


generator = create_generator()

for i in generator:
    print(i)
    if i >= 10:
        break


# Можно создавать и вызывать с аргументами
print('Можно создавать и вызывать с аргументами \n')
def create_generator(start=0):
    num = start
    while True:
        yield num
        num += 1


for i in create_generator(7):
    print(i)
    if i >= 10:
        break

print('Можно писать сколько угодно yield \n')
# Можно писать сколько угодно yield
def gen_three():
    yield 1
    yield 2
    yield 3


for i in gen_three():
    print(i)

print('Можем получать каждое следующее значение с помощью Next \n')
# Можем получать каждое следующее значение с помощью Next
generator = create_generator()
print(next(generator))
print(next(generator))

print('При этом в конечно генераторе при достижении конца получим StopIteration \n')
# При этом в конечно генераторе при достижении конца получим StopIteration
generator = gen_three()
print(next(generator))
print(next(generator))
print(next(generator))
# print(next(generator)) - StopIteration

print('Каждый вызов функции создает генератор с нуля, новый никак не будет связан с другим \n')
# Каждый вызов функции создает генератор с нуля, новый никак не будет связан с другим
generator_2 = gen_three()
print(next(generator_2))

print('ПРО ДЕТАЛЬНУЮ РАБОТУ \n')
# ПРО ДЕТАЛЬНУЮ РАБОТУ


