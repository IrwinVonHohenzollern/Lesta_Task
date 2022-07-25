#  На языке Python реализовать функцию, которая быстрее всего (по процессорным тикам) отсортирует данный ей массив чисел. 
# Массив может быть любого размера со случайным порядком чисел (в том числе и отсортированным). 
# Объяснить почему вы считаете, что функция соответствует заданным критериям.

# Самая быстрая сортировка - TimSort - уже реализована в языке Python. Она используется как метод класса list (list.sort()).
# Поэтому реализуем метод QuickSort, работающий за O(n * log(n)), тогда как другие алгоритмы работают за время квадратично
# зависящее от числа элементов в массиве O(n^2).

from random import randint, choices

def user_sorting(array: list) -> list:
    
    def is_sorted(array: list) -> bool:
        """Function checks if array is already sorted."""
        for i in range(1, len(array)):
            if array[i - 1] > array[i]:
                return False
        return True

    def quick_sort(array: list) -> list:
        """Function realises QuickSort method. This  method is recursive and it is rather fast compared to another method."""

        if len(array) < 2:
            return array

        low, same, high = [], [], []
        pivot = array[randint(0, len(array) - 1)]

        for item in array:
            if item < pivot:
                low.append(item)
            elif item == pivot:
                same.append(item)
            elif item > pivot:
                high.append(item)

        return quick_sort(low) + same + quick_sort(high)

    if is_sorted(array):
        return array

    if is_sorted(array[::-1]):
        return array[::-1]
    
    return quick_sort(array)

if __name__ == "__main__":
    array = choices(range(0, 51), k=20)
    print(array)
    print(user_sorting(array))