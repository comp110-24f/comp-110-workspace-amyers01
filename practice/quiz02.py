x: list[int] = [9, -1, 8, 5]
y: list[str] = ["cat", "dog", "turtle", "elephant", "fish"]
z: list[str] = ["z"]

index: int = 0
while index < len(y):
    # print(x[index])
    print(f"Index {index}: {y[index]}")
    # print(z[index])
    index += 1

for word in x:
    print(word)

for idx in range(0, len(x)):
    print(f"Index {idx}: {x[idx]}")


def func(a: list[str]) -> int:
    sum: int = 0
    for x in a:
        sum += len(x)
    return sum


def max_sum_dict(d: dict[str, list[int]]) -> str:
    keys = []
    for key in d:
        keys.append(key)

    values_list_1 = d[keys[0]]
    values_list_2 = d[keys[1]]

    total_1 = 0
    for value in values_list_1:
        total_1 += value

    total_2 = 0
    for value in values_list_2:
        total_2 += value

    if total_1 > total_2:
        return keys[0]
    else:
        return keys[1]


# print(max_sum_dict(d={"a": [1, 2, 3], "b": [4, 5]}))


def f(x: list[str]) -> str:
    print(len(x))
    for y in range(0, len(x)):
        x[y] += "x"
    return x[y]


def g(x: list[str]) -> list[str]:
    new_list: list[str] = []
    for z in x:
        new_list.append(str(z))
    return new_list


record: list[str] = ["x", "y"]
# print(f(record))
# print(g(record))

x: list[float] = [1.0, 2.0]
y: list[float] = [3.0, 4.0]
y = x
x[0] = 3.0

print(x)
print(y)
