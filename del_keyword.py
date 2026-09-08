class Companies:
    def __init__(self, names):
        self.names = names
c1 = Companies("Gitlab")
print(c1.names)
del c1.names
print(c1.names)

# For using del keyword c1.names has been deleted