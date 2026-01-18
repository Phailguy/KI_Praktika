# Naive Bayes -- Training & Beispielrechnung

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

  Klasse   Anzahl   Prior
  -------- -------- ----------------------------
  O        4        (P(O)=`\frac{4}{7}`{=tex})
  M        3        (P(M)=`\frac{3}{7}`{=tex})

------------------------------------------------------------------------

## 2. Bedingte Wahrscheinlichkeiten pro Feature (ungeglättet)

### **Alter**

  Alter   O   M
  ------- --- ---
  ≥35     2   2
  \<35    2   1

\[
P(`\ge35`{=tex}\|O)=`\frac{2}{4}`{=tex}=0.5,`\quad `{=tex}P(\<35\|O)=0.5
\] \[
P(`\ge35`{=tex}\|M)=`\frac{2}{3}`{=tex},`\quad `{=tex}P(\<35\|M)=`\frac{1}{3}`{=tex}
\]

------------------------------------------------------------------------

### **Einkommen**

  Einkommen   O   M
  ----------- --- ---
  hoch        4   1
  niedrig     0   2

\[
P(`\text{hoch}`{=tex}\|O)=1.0,`\quad `{=tex}P(`\text{niedrig}`{=tex}\|O)=0
\] \[
P(`\text{hoch}`{=tex}\|M)=`\frac{1}{3}`{=tex},`\quad `{=tex}P(`\text{niedrig}`{=tex}\|M)=`\frac{2}{3}`{=tex}
\]

------------------------------------------------------------------------

### **Bildung**

  Bildung    O   M
  ---------- --- ---
  Abitur     1   2
  Bachelor   1   1
  Master     2   0

\[ P(`\text{Abitur}`{=tex}\|O)=`\frac{1}{4}`{=tex},;
P(`\text{Bachelor}`{=tex}\|O)=`\frac{1}{4}`{=tex},;
P(`\text{Master}`{=tex}\|O)=`\frac{2}{4}`{=tex} \]

\[ P(`\text{Abitur}`{=tex}\|M)=`\frac{2}{3}`{=tex},;
P(`\text{Bachelor}`{=tex}\|M)=`\frac{1}{3}`{=tex},;
P(`\text{Master}`{=tex}\|M)=0 \]

------------------------------------------------------------------------

## 3. Laplace-Glättung

Allgemeine Formel:

\[ P(x_i\|C)=`\frac{n_{x_i,C}+1}{n_C+k}`{=tex} \]

Dabei ist\
- (n\_{x_i,C}) = Anzahl der Beobachtungen mit Wert (x_i) in Klasse (C)\
- (n_C) = Anzahl aller Beobachtungen der Klasse\
- (k) = Anzahl möglicher Werte des Features

------------------------------------------------------------------------

### **Alter** (k = 2)

  Wert   Formel O      Ergebnis O      Formel M      Ergebnis M
  ------ ------------- --------------- ------------- ---------------
  ≥35    (2+1)/(4+2)   3/6 = **0.5**   (2+1)/(3+2)   3/5 = **0.6**
  \<35   (2+1)/(4+2)   3/6 = **0.5**   (1+1)/(3+2)   2/5 = **0.4**

------------------------------------------------------------------------

### **Einkommen** (k = 2)

  ---------------------------------------------------------------------------
  Wert      Formel O       Ergebnis O        Formel M       Ergebnis M
  --------- -------------- ----------------- -------------- -----------------
  hoch      (4+1)/(4+2)    5/6 = **0.833**   (1+1)/(3+2)    2/5 = **0.4**

  niedrig   (0+1)/(4+2)    1/6 = **0.167**   (2+1)/(3+2)    3/5 = **0.6**
  ---------------------------------------------------------------------------

------------------------------------------------------------------------

### **Bildung** (k = 3)

  ----------------------------------------------------------------------------
  Wert       Formel O       Ergebnis O        Formel M       Ergebnis M
  ---------- -------------- ----------------- -------------- -----------------
  Abitur     (1+1)/(4+3)    2/7 = **0.286**   (2+1)/(3+3)    3/6 = **0.5**

  Bachelor   (1+1)/(4+3)    2/7 = **0.286**   (1+1)/(3+3)    2/6 = **0.333**

  Master     (2+1)/(4+3)    3/7 = **0.429**   (0+1)/(3+3)    1/6 = **0.167**
  ----------------------------------------------------------------------------

------------------------------------------------------------------------

## 4. Klassifikation des Beispiels

**Beispiel:**

Alter \<35, Einkommen niedrig, Bildung Bachelor

\[
P(O\|x)`\propto `{=tex}`\frac{4}{7}`{=tex}`\cdot 0.5`{=tex}`\cdot `{=tex}`\frac{1}{6}`{=tex}`\cdot `{=tex}`\frac{2}{7}`{=tex}=0.0136
\]

\[
P(M\|x)`\propto `{=tex}`\frac{3}{7}`{=tex}`\cdot 0.4`{=tex}`\cdot `{=tex}`\frac{3}{5}`{=tex}`\cdot `{=tex}`\frac{1}{3}`{=tex}=0.0286
\]

➡️ **Ergebnis: Kandidat = M**
