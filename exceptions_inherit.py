exceptions_dict = {}        # цепочка наследований
drops = []                  # лишние исключения
stack = []                  # стек помеченых исключений

num = int(input())          # количество цепочек наследования
num_count = 0               # счётчик цепочек
while num_count < num:
    '''Прорабатываем цепочки наследования'''
    row = input().replace(' : ', ':').split(':')    # разделяем ключ и значения (наследников)
    if len(row)<2:
        if not exceptions_dict.get(row[0]):
            exceptions_dict[row[0]] = []
    else:
        for inherit in row[1].split():
            if not exceptions_dict.get(row[0]):
                exceptions_dict[row[0]] = []
            if exceptions_dict.get(inherit):
                exceptions_dict[inherit].append(row[0])
            else:
                exceptions_dict[inherit] = [row[0]]

    num_count += 1          # наращаем счётчик наследования


def check_exceptions(start_exc):
    '''формирование стека ошибок (помечаем ошибки)'''
    for exc in exceptions_dict[start_exc]:
        stack.append(exc)
        check_exceptions(exc)


num_exc = int(input())      # количество обработчиков исключений
num_exc_count = 0           # счётчик исключений
while num_exc_count < num_exc:
    '''Прорабатываем цепочки исключений'''
    inherit_exc = input()

    if inherit_exc in stack:
        '''проверяем на наличие в стеке'''
        if not inherit_exc in drops:
            drops.append(inherit_exc)
        num_exc_count += 1          # наращаем счётчик обработчников исключений
        continue

    stack.append(inherit_exc)       # формируем стек помеченных исключений
    check_exceptions(inherit_exc)   # добавляем наследников в стек

    num_exc_count += 1              # наращаем счётчик обработчников исключений

for drop in drops:
    print(drop)