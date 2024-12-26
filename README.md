# Лабораторная работа №10
## Задание
Создайте пакет, содержащий 3 модуля на основе лабораторных работ №№ 7-9
Напишите запускающий модуль на основе Typer, который позволит выбирать и настраивать параметры запуска логики из пакета.
Оформите отчёт в README.md. Отчёт должен содержать:
Условия задач
Описание проделанной работы
Скриншоты результатов
Ссылки на используемые материалы
### Пакет, содержащий 3 модуля на основе лабораторных работ №№ 7-9
- Лабораторная работа №7
```
def w(i):
    if i ==1:
        return 0.3
    if i ==2:
        return -1.5
    return w(i-1)*w(i-2)*(i-2)**2/(i+1)**3

def lab10(i):
    print(w(i))
```

- Лабораторная работа №8
```
def hp():
    hp =100

    def changes_hp(sum):
        nonlocal hp
        hp +=sum
        if hp>100:
            hp = 100 #max
        if hp<0:
            hp = 0 #min
        return hp
    return changes_hp
```

- Лабораторная работа №9
```
def f(n):
    def chisla(x):
        for i in range(2, int(x**0.5)+3):
            if x % i == 0: 
                return False 
        return True
    for i in range(2, n+1):
        if chisla(i):
            yield i 
```
- Пакет
```
from . import l7, l8,l9
```
- Запускающий модуль
```
import Paket
import typer

app = typer.Typer()

@app.command()
def lab7(i: int):
    print("решение с рекурсией:")
    Paket.l7.lab10(i)

@app.command()
def lab8(hp: int):
    Paket.l8.lab10()

@app.command()
def lab9(n: int):
    otvet=Paket.l9.f(n)
    for i in otvet:
        print(i)

app()
```

### Результат работы программы
<image src = 1.png alt="результат программы">
<image src = 2.png alt="результат программы">

#### Ccылки на используемые материалы
- https://typer.tiangolo.com/#an-example-with-two-subcommands
- https://www.youtube.com/watch?v=6K1f0DvW1uM&ab_channel=selfedu