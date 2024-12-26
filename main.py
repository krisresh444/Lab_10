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