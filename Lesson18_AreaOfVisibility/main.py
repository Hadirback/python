global_b = 1
# Область видимости объекта это набор модулей или функций внутри которых допустимо использование имени объекта

def my_f(my_var):
    my_var = 999
    print('Внутри функци: ', my_var)

a = 1
my_f(a)
print('После выхода функции', a)

def some_f():
    global global_b
    global_b = 999
    print('Переменная внутри функции:', global_b)


some_f()
print('Переменная после выхода из функции', global_b)

# Почему стоит избегать использование глобальных переменных

global_var = 2

def my_func():
    result = global_var ** 5
    print(result)

def my_change_func():
    global global_var
    global_var = 100

my_func()
print(global_var)

my_change_func()
my_func()

# Относительная видимость

m = 'Меня видно везде'

def a():
    ma = 'Меня видно и в b() и в a()'
    m = 'sdfsdf'
    print(m)
    def b():
        print(m)
        print(ma)
        mb = 'Меня видно в c() и в b() но невидно в a'

        def c():
            print(m)
            print(ma)
            print(mb)
            mc = 'Меня видно только в c'

        c()
    b()
a()
print(m)

