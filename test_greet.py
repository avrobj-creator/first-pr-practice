from greet import greet


def test_greet_with_name():
    assert greet("Ada") == "Hello, Ada!"


if __name__ == "__main__":
    test_greet_with_name()
    print("All tests passed.")
