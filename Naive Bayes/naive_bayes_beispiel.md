# Naive Bayes -- Training und Klassifikation

## Datensatz

  Nr.   Alter   Einkommen   Bildung    Kandidat
  ----- ------- ----------- ---------- ----------
  1     ≥35     hoch        Abitur     O
  2     \<35    niedrig     Master     O
  3     ≥35     hoch        Bachelor   M
  4     ≥35     niedrig     Abitur     M
  5     ≥35     hoch        Master     O
  6     \<35    hoch        Bachelor   O
  7     \<35    niedrig     Abitur     M

------------------------------------------------------------------------

## 1. Klassenwahrscheinlichkeiten

O: 4\
M: 3

$$
P(O)=\frac{4}{7}, \quad P(M)=\frac{3}{7}
$$

------------------------------------------------------------------------

## 2. Bedingte Wahrscheinlichkeiten

### Alter

  Alter   O   M
  ------- --- ---
  ≥35     2   2
  \<35    2   1

$$
P(<35 \mid O)=0.5, \quad P(<35 \mid M)=\frac{1}{3}
$$

------------------------------------------------------------------------

### Einkommen (Laplace-Glättung)

  Einkommen   O   M
  ----------- --- ---
  hoch        4   1
  niedrig     0   2

$$
P(\text{niedrig} \mid O)=\frac{1}{6}, \quad P(\text{niedrig} \mid M)=\frac{3}{5}
$$

------------------------------------------------------------------------

### Bildung (Laplace-Glättung)

  Bildung    O   M
  ---------- --- ---
  Abitur     1   2
  Bachelor   1   1
  Master     2   0

$$
P(\text{Bachelor} \mid O)=\frac{2}{7}, \quad P(\text{Bachelor} \mid M)=\frac{1}{3}
$$

------------------------------------------------------------------------

## 3. Klassifikation des Beispiels

**Beispiel:**

-   Alter \< 35\
-   Einkommen niedrig\
-   Bildung Bachelor

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

------------------------------------------------------------------------

## 4. Entscheidung

$$
P(M \mid x) > P(O \mid x)
$$

➡️ **Klassifikation: Kandidat M**
