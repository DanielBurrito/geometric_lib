import circle
import square

# Доступные фигуры и функции
figs = ['circle', 'square']
funcs = ['perimeter', 'area']
sizes = {}  # Словарь для хранения количества необходимых параметров для фигур и функций

def calc(fig, func, size):
    # Проверка корректности введенных данных
    assert fig in figs
    assert func in funcs

    # Динамический вызов функции с использованием eval
    result = eval(f'{fig}.{func}(*{size})')
    return result
    
if __name__ == "__main__":
    func = ''
    fig = ''
    size = list()
    
    # Запрос фигуры у пользователя
    while fig not in figs:
        fig = input(f"Enter figure name, available are {figs}:\n")
    
    # Запрос функции у пользователя
    while func not in funcs:
        func = input(f"Enter function name, available are {funcs}:\n")
    
    # Запрос размеров фигуры у пользователя
    while len(size) != sizes.get(f"{func}-{fig}", 1):
        size = list(map(int, input("Input figure sizes separated by space, 1 for circle and square\n").split(' ')))




