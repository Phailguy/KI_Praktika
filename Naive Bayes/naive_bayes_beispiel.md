# Naive Bayes -- Training & Beispielrechnung

## Datensatz

|  Nr.  | Alter |  Einkommen  | Bildung    |Kandidat|
|  -----| ------- |-----------| ---------- |----------|
| 1   |  ≥35  |   hoch    |    Abitur  |   O|
| 2  |   \<35 |   niedrig  |   Master   |  O| 
| 3   |  ≥35   |  hoch     |   Bachelor |  M| 
| 4   |  ≥35  |   niedrig  |   Abitur  |   M|
| 5   |  ≥35   |  hoch     |   Master  |   O|
| 6   |  \<35  |  hoch    |    Bachelor |  O|
| 7   |  \<35  |  niedrig  |   Abitur   |  M|

------------------------------------------------------------------------

## 1. Klassenwahrscheinlichkeiten

$$
P(O)=\frac{4}{7}, \quad P(M)=\frac{3}{7}
$$

------------------------------------------------------------------------

## 2. Bedingte Wahrscheinlichkeiten pro Feature (ungeglättet)

### **Alter**


  |Alter  | O |  M|
  |-------|---|---|
 |≥35    | 2|   2|
  |<35   | 2 |  1|

$$
P(<35 \mid O)=0.5, \quad P(<35 \mid M)=\frac{1}{3}
$$

------------------------------------------------------------------------

### **Einkommen**

|Einkommen  | O  | M|
|-----------|---|---|
|hoch       | 4 |  1|
|niedrig    | 0 |  2|

$$
P(\text{niedrig} \mid O)=\frac{1}{6}, \quad P(\text{niedrig} \mid M)=\frac{3}{5}
$$

------------------------------------------------------------------------

### **Bildung**

  |Bildung   | O |  M|
  |----------| --- |---|
 | Abitur    | 1  | 2|
 | Bachelor  | 1   |1|
 | Master   |  2 |  0|


$$
P(\text{Bachelor} \mid O)=\frac{2}{7}, \quad P(\text{Bachelor} \mid M)=\frac{1}{3}
$$

------------------------------------------------------------------------

## 3. Laplace-Glättung


Für ein Feature \(x_i\) mit \(k\) möglichen Ausprägungen und eine Klasse \(C\):

$$
P(x_i \mid C) = \frac{n_{x_i,C} + 1}{n_C + k}
$$

Dabei gilt:

- \(n_{x_i,C}\): Anzahl der Trainingsbeispiele in Klasse \(C\), bei denen \(x_i\) den Wert annimmt
- \(n_C\): Gesamtanzahl der Trainingsbeispiele der Klasse \(C\)
- \(k\): Anzahl möglicher Werte (Kategorien) des Features \(x_i\)

------------------------------------------------------------------------

### **Alter** (k = 2)

  |Wert  | Formel O     | Ergebnis O     | Formel M     | Ergebnis M|
  |------| -------------| ---------------| ------------- |---------------|
  |≥35   | (2+1)/(4+2)  | 3/6 = **0.5**  | (2+1)/(3+2)  | 3/5 = **0.6**|
  |\<35  | (2+1)/(4+2)  | 3/6 = **0.5**  | (1+1)/(3+2)  | 2/5 = **0.4**|

------------------------------------------------------------------------

### **Einkommen** (k = 2)

  
 | Wert     | Formel O      | Ergebnis O       | Formel M      | Ergebnis M|
 | ---------| --------------| -----------------| --------------| -----------------|
 | hoch     | (4+1)/(4+2)   | 5/6 = **0.833**  | (1+1)/(3+2)    |2/5 = **0.4**|
 | niedrig  | (0+1)/(4+2)   | 1/6 = **0.167**  | (2+1)/(3+2)   | 3/5 = **0.6**|


------------------------------------------------------------------------

### **Bildung** (k = 3)

 
| Wert     |  Formel O     |  Ergebnis O      |  Formel M     |  Ergebnis M|
| ----------| --------------| -----------------| -------------- |-----------------|
|Abitur   |  (1+1)/(4+3)   | 2/7 = **0.286**  | (2+1)/(3+3)  |  3/6 = **0.5**|
|Bachelor  | (1+1)/(4+3) |   2/7 = **0.286**  | (1+1)/(3+3)  |  2/6 = **0.333**|
|Master    | (2+1)/(4+3) |   3/7 = **0.429**  | (0+1)/(3+3)  |  1/6 = **0.167**|


------------------------------------------------------------------------

## 4. Klassifikation des Beispiels

**Beispiel:**

Alter \<35, Einkommen niedrig, Bildung Bachelor

### Für Klasse O

$$
P(O \mid x) \propto \frac{4}{7} \cdot 0.5 \cdot \frac{1}{6} \cdot \frac{2}{7}
= 0.0136
$$

### Für Klasse M

$$
P(M \mid x) \propto \frac{3}{7} \cdot \frac{1}{3} \cdot \frac{3}{5} \cdot \frac{1}{3}
= 0.0286
$$

➡️ **Ergebnis: Kandidat = M**
