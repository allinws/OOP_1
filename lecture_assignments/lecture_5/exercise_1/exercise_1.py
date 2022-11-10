
def return_five():
    return 6

def test_function():
    value = return_five()
    assert value == 5

if __name__ == '__main__':
    test_function()
