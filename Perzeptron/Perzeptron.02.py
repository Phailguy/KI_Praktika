import numpy as np

class Perceptron:
    def __init__(self, weights, bias):
        self.weights = np.array(weights)
        self.bias = bias

    def predict(self, x):
        x = np.array(x)
        activation = np.dot(self.weights, x) + self.bias
        return 1 if activation >= 0 else 0


# -------------------------------
# Perzeptron-Gewichte definieren
# -------------------------------

# UND: w1 = 1, w2 = 1, b = -2
p_and = Perceptron(weights=[1, 1], bias=-2)

# ODER: w1 = 1, w2 = 1, b = -1
p_or = Perceptron(weights=[1, 1], bias=-1)

# NOT: w = -1, b = 1
p_not = Perceptron(weights=[-1], bias=1)


# -------------------------------
# Demonstration
# -------------------------------
print("UND-Funktion:")
for x1 in [0, 1]:
    for x2 in [0, 1]:
        print(f"{x1} AND {x2} = {p_and.predict([x1, x2])}")

print("\nODER-Funktion:")
for x1 in [0, 1]:
    for x2 in [0, 1]:
        print(f"{x1} OR {x2} = {p_or.predict([x1, x2])}")

print("\nNOT-Funktion:")
for x in [0, 1]:
    print(f"NOT {x} = {p_not.predict([x])}")
