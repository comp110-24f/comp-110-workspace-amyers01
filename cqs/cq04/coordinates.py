"""Challenge Question 04 - Coordinates"""

__author__ = "730654167"


def get_coords(xs: str, ys: str) -> None:
    xind: int = 0
    yind: int = 0
    while xind < len(xs):
        while yind < len(ys):
            print(f"({xs[xind]},{ys[yind]})")
            yind += 1
        xind += 1
        yind = 0


if __name__ == "__main__":
    xs: str = "hi"
    ys: str = "bye"
    get_coords(xs, ys)
