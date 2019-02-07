'''
def f():
    # x = 42
    def g():
        global x
        x = 43

    print("Before calling g: " + str(x))
    print("Calling g now:")
    g()
    print("After calling g: " + str(x))


x = 3
f()
print("x in main: " + str(x))
'''

'''
def check_binary_search_tree_(root):

    def in_order(root):
        nonlocal last_node
        if root is None:
            return True

        left_valid = in_order(root.left)
        if left_valid is False:
            return False

        if root.data <= last_node:
            return False

        last_node = root.data
        return in_order(root.right)

    last_node = -1
    return in_order(root)

'''


def f():
    x = 42
    def g():
        nonlocal x  # nonlocal variables couldn't defined or effect in main or module scope it works only in nested scope
        x = 43  # But global variables works in all scope as well

    print("Before calling g: " + str(x))
    print("Calling g now:")
    g()
    print("After calling g: " + str(x))


x = 3
f()
print("x in main: " + str(x))