# 2. Filtering even numbers
# nums to check 1, 1, 2, 3, 5, 8, 13, 21, 34, 55
# 9, 0, 32, 8, 2, 8, 64, 29, 42, 99


def filter_even_nums(input_list):
    list_of_int = [int(str) for str in input_list]
    filtered = [num for num in list_of_int if num % 2 != 0]
    return filtered


################Tests################


def test_filtering_even_nums():
    assert filter_even_nums(
        ["1", " 1", " 2", " 3", " 5", " 8", " 13", " 21", " 34", " 55"]
    ) == [
        1,
        1,
        3,
        5,
        13,
        21,
        55,
    ], "should be [1, 1, 3, 5, 13, 21, 55]"
    assert filter_even_nums(
        ["9", " 0", " 32", " 8", " 2", " 8", " 64", " 29", " 42", " 99"]
    ) == [9, 29, 99], "should be [9, 29, 99]"


if __name__ == "__main__":
    test_filtering_even_nums()
    print("passed")
