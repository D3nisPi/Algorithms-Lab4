# Algorithms-Lab4

## Задания

### Задание №1

Имеется список из нот:
```
p = ['до', 'ре', 'ми', 'фа', 'соль', 'ля', 'си']
```
Необходимо записать генератор, 
который бы случайным образом выдавал ноты
из этого списка 1_000_000 раз. 
Для случайного выбора нот, используйте функцию choice модуля random. 
Выведите на экран первые 20 значений этого генератора.

### Задание №2
Определите функцию-генератор, 
которая бы возвращала целые числа кратные 3, 
начиная поиск от значения a, 
которое задается через параметр функции. 
Вызовите эту функции со значением аргумента `a=-100`
и выведите первые 20 чисел, 
возвращенных этой функцией-генератором. 
Какие-либо коллекции в программе не использовать.

### Задание №3
Вводится список email-адресов в одну строчку через пробел. 
Среди них нужно оставить только корректно записанные адреса. 
Будем полагать, что к таким относятся те, 
что используют латинские буквы, цифры и символ подчеркивания. 
А также в адресе сначала должен идти символ `@`, 
а затем  `.` (между ними, конечно же, могут быть и другие символы).
Отобразить результат отбора корректных адресов на экране.

## Запуск

### Задание 1

```commandline
python random_notes.py
```

### Задание 2

```commandline
python multiples_of_three.py
```

### Задание 3

```commandline
python filter_emails.py
```
