nums = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]


def squere_nums(nums):
    return [n * n for n in nums]


""" Tests """


def test_squere():
    assert squere_nums([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]) == [
        1,
        4,
        9,
        16,
        25,
        36,
        49,
        64,
        81,
        100,
        121,
    ], "Should be [1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 121]"

    assert squere_nums([1, 1, 2, 3, 5, 8, 13, 21, 34, 55]) == [
        1,
        1,
        4,
        9,
        25,
        64,
        169,
        441,
        1156,
        3025,
    ], "Should be [1, 1, 4, 9, 25, 64, 169, 441, 1156, 3025]"


if __name__ == "__main__":
    test_squere()
    print("passed")
