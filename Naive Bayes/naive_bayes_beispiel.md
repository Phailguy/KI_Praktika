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

-   O: 4\
-   M: 3

\[ P(O)=`\frac{4}{7}`{=tex}, `\quad `{=tex}P(M)=`\frac{3}{7}`{=tex} \]

------------------------------------------------------------------------

## 2. Bedingte Wahrscheinlichkeiten

### Alter

  Alter   O   M
  ------- --- ---
  ≥35     2   2
  \<35    2   1

\[ P(\<35\|O)=0.5, `\quad `{=tex}P(\<35\|M)=`\frac{1}{3}`{=tex} \]

------------------------------------------------------------------------

### Einkommen (mit Laplace)

  Einkommen   O   M
  ----------- --- ---
  hoch        4   1
  niedrig     0   2

\[ P(niedrig\|O)=`\frac{1}{6}`{=tex},
`\quad `{=tex}P(niedrig\|M)=`\frac{3}{5}`{=tex} \]

------------------------------------------------------------------------

### Bildung (mit Laplace)

  Bildung    O   M
  ---------- --- ---
  Abitur     1   2
  Bachelor   1   1
  Master     2   0

\[ P(Bachelor\|O)=`\frac{2}{7}`{=tex},
`\quad `{=tex}P(Bachelor\|M)=`\frac{1}{3}`{=tex} \]

------------------------------------------------------------------------

## 3. Klassifikation des Beispiels

**Beispiel:**

-   Alter \< 35\
-   Einkommen niedrig\
-   Bildung Bachelor

### Für Klasse O

\[ P(O\|x) `\propto `{=tex}`\frac{4}{7}`{=tex} `\cdot 0.5`{=tex}
`\cdot `{=tex}`\frac{1}{6}`{=tex} `\cdot `{=tex}`\frac{2}{7}`{=tex} =
0.0136 \]

### Für Klasse M

\[ P(M\|x) `\propto `{=tex}`\frac{3}{7}`{=tex}
`\cdot `{=tex}`\frac{1}{3}`{=tex} `\cdot `{=tex}`\frac{3}{5}`{=tex}
`\cdot `{=tex}`\frac{1}{3}`{=tex} = 0.0286 \]

------------------------------------------------------------------------

## 4. Entscheidung

\[ P(M\|x) \> P(O\|x) \]

➡️ **Naive Bayes klassifiziert das Beispiel als Kandidat M**
