import check50

@check50.check()
def exists():
    """Checking if hello.py exists"""
    check50.exists("hello.py")

@check50.check(exists)
def prints_hello():
    """Checking if program prints "Hello there" """
    check50.run("python3 hello.py").stdout("[Hh]ello there?\n", regex=True).exit(0)
