import numpy as np

global X, p1, p2, direction, y, X_Bias,m
# ------------------------------------------
# 1. 10 gleichverteilte Zufallspunkte erzeugen
# ------------------------------------------
def init():
    global X,m
    X = np.random.uniform(-1, 1, size=(m, 2))  # m Punkte in 2D

# ------------------------------------------
# 2. Zwei zufällige Punkte als Entscheidungsgrenze
# ------------------------------------------
def directions():
    global p1,p2,direction
    p1 = np.random.uniform(-1, 1, size=2)
    p2 = np.random.uniform(-1, 1, size=2)
    # Richtungsvektor der Geraden
    direction = p2 - p1


# ------------------------------------------
# 3. Zielfunktion f definieren
#    (Vorzeichen von (x - p1) × direction)
# ------------------------------------------
def predict(x):

    #Berechnet das Label für Punkt x basierend auf der Geraden durch p1 und p2.
    #Cross-Product in 2D -> Skalar:
    #(x - p1)_x * direction_y - (x - p1)_y * direction_x

    value = (x[0] - p1[0]) * direction[1] - (x[1] - p1[1]) * direction[0]

    # positive Seite = +1 (frei wählbar)
    return 1 if value > 0 else -1


# ------------------------------------------
# 4. Labels für alle Punkte berechnen
# ------------------------------------------
def labels():
    global y,X
    y = np.array([predict(x) for x in X])

# ------------------------------------------
# 5. Bias-Term hinzufügen
# ------------------------------------------
def bias():
    global X_Bias,X,m
    X_Bias = np.hstack([np.ones((m, 1)), X])  # shape (m, 3)


# ------------------------------------------
# 6. Perzeptron-Funktion (ein Durchlauf)
# ------------------------------------------
def perceptron_run(a):
    init()
    directions()
    labels()
    bias()
    w = np.zeros(3)   # Startgewichte
    steps = 0

    while True:
        # Vorhersagen
        predictions = np.sign(X_Bias @ w)
        predictions[predictions == 0] = 1  # falls 0 => 1 nehmen

        # falsch klassifizierte Punkte
        missed_index = np.where(predictions != y)[0]

        if len(missed_index) == 0:
            return steps  # konvergiert

        # zufällig einen falsch klassifizierten Punkt wählen
        i = np.random.choice(missed_index)

        # Update: w := w + (y - h(x))*x
        w = w + a * (y[i] - predictions[i]) * X_Bias[i]

        steps += 1

        # Sicherheit, falls etwas schiefgeht
        if steps > 1000000:
            return steps

# ------------------------------------------
# 7. Experiment wiederholen
# ------------------------------------------

#Anzahl runs
runs = 1000
#Lernrate alpha
a = 0.1
#Datensatz größe
m = 1000
#Durchführung runs
steps_list = [perceptron_run(a) for _ in range(runs)]
#wieder zu Array machen
steps = np.array(steps_list)

# ------------------------------------------
# Ausgabe
# ------------------------------------------
print("=== Perzeptron-Experiment ===")
print(f"Anzahl Durchläufe: "+ str(runs))
print("Lernrate alpha = "+str(a))
print("Datensatzgröße m = "+str(m))
print("Durchschnittliche Schritte:", steps.mean())
print("Median:", np.median(steps))
print("Minimum:", steps.min())
print("Maximum:", steps.max())
print("Standardabweichung:", steps.std())
