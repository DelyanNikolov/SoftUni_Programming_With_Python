x = "global"


def outer():
    x = "local"

    def inner():
        nonlocal x  # added nonlocal x to connect inner and outer variable x
        x = "nonlocal"
        print("inner:", x)

    def change_global():
        global x  # added global x to connect local and global variable x
        x = "global: changed!"

    print("outer:", x)
    inner()
    print("outer:", x)
    change_global()


print(x)
outer()
print(x)

# expected output:

# global
# outer: local
# inner: nonlocal
# outer: nonlocal
# global: changed!
