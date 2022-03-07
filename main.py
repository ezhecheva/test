class MyMath:
    def __init__(self) -> None:
        pass

    def factorial(self, x: int):
        f = 1

        for number in range(1, x + 1):
            f *= number

        return f