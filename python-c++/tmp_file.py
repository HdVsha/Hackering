import cython as cpp


def test(x):
    y = 0
    for i in range(x):
        y += i
    return y


if __name__ == "__main__":
    print(test(10))

