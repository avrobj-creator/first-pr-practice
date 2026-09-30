from greet import greet


def test_greet_with_name():
    assert greet("Ada") == "Hello, Ada!"


def test_greet_with_no_name():
    assert greet("") == "Hello, stranger!"


if __name__ == "__main__":
    test_greet_with_name()
    test_greet_with_no_name()
    print("All tests passed.")
