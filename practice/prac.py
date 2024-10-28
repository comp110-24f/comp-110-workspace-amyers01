def num_instances(inp_str: str, search_str: str):
    count = 0
    index = 0

    while index <= len(inp_str) - len(search_str):
        match = True
        sub_index = 0

        while sub_index < len(search_str):
            if inp_str[index + sub_index] != search_str[sub_index]:
                match = False
            sub_index += 1

        if match:
            count += 1
            index += len(search_str)
        else:
            index += 1

    print(count)


# num_instances("Livelive", "ve")


def prac(machine: str) -> str:
    bike = machine
    print(bike[0])
    return machine


# print(prac(machine="test"))


def chars(msg: str) -> str:
    idx: int = 0
    copy: str = msg
    while idx < len(msg):
        print(idx)
        idx += 1
    return copy


# a: str = "Hey"
# b: str = "Hi"
# chars(msg=a)


def reverse_multiply(a: list[int]) -> list[int]:
    idx: int = len(a) - 1
    values: list[int] = []
    while idx >= 0:
        values.append(a[idx] * 2)
        idx -= 1
    return values


# print(reverse_multiply([2, 4, 6, 8]))
