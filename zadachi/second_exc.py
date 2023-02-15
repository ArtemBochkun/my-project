


def solution_plus(x:int, y:int) -> int:
    return x + y


def solution_minus(x:int, y:int) -> int:
    return x - y


def solution_choice(x: str, y:int, z:int) -> int:
    if x == "+":
        return solution_plus(y, z)
    elif x == "-":
        return solution_minus(y, z)


print(solution_choice("+", 2, 3))
