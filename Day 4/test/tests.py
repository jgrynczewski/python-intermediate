from main2 import add

# Asercja pod spodem
# if result == 7:
#     pass
# else:
#     raise AssertionError("Failed")

def test_add():
    assert add(3, 4) == 7
    assert add(0, 0) == 0
    assert add(-1, -1) == -2


test_add()
