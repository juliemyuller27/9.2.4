numbers = input("Введите числа через пробел : ")
rand_num = int(input("Введите любое число: "))
list = numbers.split(" ")

for i in range(len(list)):  # проходим по всему массиву
    idx_min = i  # сохраняем индекс предположительно минимального элемента
    for j in range(i, len(list)):
        if int(list[j]) < int(list[idx_min]):
            idx_min = j
    if i != idx_min:  # если индекс не совпадает с минимальным, меняем
        list[i], list[idx_min] = list[idx_min], list[i]

def binary_search(array, element, left, right,inc=-1):
    if left > right:
        print("error-", left,right)
        return False

    middle = (right + left) // 2

    if(inc != -1 ):
        middle = inc;

    print("--",middle,"|",array[middle],element)

    if int(array[0]) > element:
        return "Ваше число меньше минимального, введите другое число";
    elif int(array[middle]) < element and int(array[middle+1]) >= element:
        return middle
    elif int(array[middle]) < element and int(array[middle+1]) < element:
        return binary_search(array, element, left, right, middle + 1)
    elif int(array[middle]) > element:
        return binary_search(array, element, left, right,middle<1)
    else:
        return binary_search(array, element, left, right,middle-1)

print(list)
print('List :',list)
search = binary_search(list, rand_num, 0, len(list))
print(len(list)-1)
print(search)

