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
a = [1, 2, 3]
it = iter(a)
next(it)
next(it)
next(it)
# next(it) - Error StopIteration

# При вызове iter всегда создается новый итератор, который не зависит от другого.
# Т.е. итератор по сути запоминает по чему он итерируется
# и на каком месте остановился
it_new = iter(a)
print(next(it_new), a)  # index == 0

# В случае списка можно представить, что он запоминает индекс
a.insert(0, -1)
print(next(it_new), a)  # index == 1
a.insert(0, -2)
a.insert(0, -3)
print(next(it_new), a)  # index == 2
print(next(it_new), a)  # index == 3

# Про генераторные выражения
print(' Про генераторные выражения')

generator = (x for x in range(20) if x % 2 == 0)
print(next(generator))
print(next(generator))

# Про достоинства генераторов
print('Про достоинства генераторов')


# генератор вычисляют по одному значению, а не вычисляют все значения сразу
def create_generator(start=0):
    num = start
    while True:
        yield num
        num += 1


gen = create_generator()
for i in gen:
    print(i)
    if i >= 7:
        gen.close()

gen = create_generator()
for i in generator:
    print(i)
    if i > 7:
        generator.throw(ValueError("Unexpected value > 7"))  # Генератор при этом не закрывается, продолжит работу

print('Метод send')


def create_my_generator():
    for x in range(10):
        if x % 2 == 0:
            val = yield x ** 2  # val = yield(x ** 2)
            print(f"'{val}' was sent to generator, current state: {x}")
        else:
            val = yield -x  # val = yield(-x)
            print(f"'{val}' was sent to generator, current state: {x}")


generator = create_my_generator()

first_val = next(generator)
print(f"First: , {first_val}")
second_val = generator.send("Out val")
print(f"Second: , {second_val}")

# через Next и for не удается передать значения, необходимо использовать цикл while и метод send
for i in generator:
    print(f"From for {i}")

# Небольшой итог
print("Небольшой итог")
