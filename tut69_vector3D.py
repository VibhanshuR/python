class vector:
    def __init__(self, vec):
        self.vec = vec

    def __str__(self):
            return f"{self.vec[0]}i + {self.vec[1]}j + {self.vec[2]}k "

    def __len__(self):
            return len(self.vec)

v1 = vector([1, 3, 6,8])
v2 = vector([8, 8, 9])
print(v1)
print(v2)
print(len(v1))
print(len(v2))