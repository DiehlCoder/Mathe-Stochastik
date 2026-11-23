# Stochastik Masterguide – Mathe LK Abitur 2027 (Hessen)

> **Grundlage:** Kerncurriculum Gymnasiale Oberstufe Hessen (KCGO 2024), Abiturerlass 2027, offizielle IQB-Formelsammlung (`00_Formelsammlung_Abitur_Theorie.pdf`, S. 7–8) sowie alle Unterrichtsmaterialien des Ordners `Mathe Stochastik/`.

---

## 1. Lehrplan-Check & Abitur-Relevanz (Hessen LK 2027)

### Prüfungsformat Abitur 2027 (Mathematik Leistungskurs)
* **Prüfungstermin & Arbeitszeit:** Mittwoch, 05. Mai 2027 | **330 Minuten** (inkl. Auswahlzeit).
* **Teil 1 (Teil A – Hilfsmittelfrei):**
  * **Hilfsmittel:** Keine (weder WTR/CAS noch Formelsammlung).
  * **Umfang:** 10 vorgelegte Aufgaben aus Analysis, Geometrie und Stochastik, davon **6 zu bearbeiten** (**30 BE** gesamt).
* **Teil 2 (Teil B – Mit Hilfsmitteln):**
  * **Hilfsmittel:** WTR oder CAS (je nach Schule) + **ausschließlich** die beigefügte IQB-Formelsammlung ([`00_Formelsammlung_Abitur_Theorie.pdf`](00_Formelsammlung_Abitur_Theorie.pdf)).
  * **Umfang Stochastik:** 1 Pflichtaufgabe (**20 BE**).
* **Wichtige Neuerung ab 2027:** Es werden **keine gedruckten Tabellen** zur kumulierten Binomialverteilung mehr ausgegeben. Alle Werte ($B(n;p;k)$, $F(n;p;k)$, Normalverteilung) müssen über den WTR/CAS bestimmt werden.

### Pflichtthemen im Überblick (Q3.1 – Q3.3)

| Bereich | Pflichtthemen laut KCGO & Unterricht | Abitur-Relevanz |
| :--- | :--- | :--- |
| **Q3.1 Grundlagen** | Zufallsversuch, relative Häufigkeit, Gesetz der großen Zahlen, Laplace, mehrstufige Zufallsexperimente (Baumdiagramme, Pfadregeln), Ereignisverknüpfungen ($\cap, \cup, \setminus, \bar{E}$) & Additionssatz | Basis für fast jede Teil-A- und Teil-B-Aufgabe |
| **Q3.1 Bedingte Wahrscheinlichkeit & Kombinatorik** | Vierfeldertafel, bedingte Wahrscheinlichkeit $P_A(B)$, totale Wahrscheinlichkeit / Satz von Bayes, stochastische Unabhängigkeit, Kombinatorik (Urnenmodelle, Binomialkoeffizient $\binom{n}{k}$) | Sehr hoch (Teil A: 4–5 BE Standardaufgabe; Teil B: Einstieg) |
| **Q3.2 Zufallsgrößen & Binomialverteilung** | Diskrete Zufallsgrößen, Wahrscheinlichkeitsverteilung, Erwartungswert $E(X)$, Varianz $\operatorname{Var}(X)$, Standardabweichung $\sigma$, Bernoulli-Kette, Binomialverteilung, kumulierte Wahrscheinlichkeiten $F(n;p;k)$, 3-Mindestens-Aufgaben, inverse Fragestellungen ($n, p, k$ gesucht) | Kernthema in Teil B (fast immer 8–12 BE) und Teil A (kleine Rechnungen/Begründungen) |
| **Q3.2 LK Normalverteilung & Sigma-Regeln** | Stetige vs. diskrete Zufallsgrößen, Gaußsche Glockenkurve & Dichtefunktion $\varphi_{\mu,\sigma}(x)$, Analysis der Glockenkurve (HP/WP), Sigma-Regeln ($68{,}3\,\%$, $95{,}4\,\%$, $99{,}7\,\%$), Intervall- & Punktwahrscheinlichkeiten, Invertierung (`Inv. Normal-V.`), Bestimmung von $\mu$ oder $\sigma$, Prognose-/Konfidenzintervall | LK-Schwerpunkt in Teil B (häufig 4–8 BE) |
| **Q3.3 Hypothesentests (LK-exklusiv)** | Alternativtest, einseitige & zweiseitige Signifikanztests, Null- & Gegenhypothese ($H_0, H_1$), Entscheidungsregel / kritische Zahl $k$, Fehler 1. Art ($\alpha$) und Fehler 2. Art ($\beta$), Gütefunktion | LK-Pflichtthema (oft Teil B-Abschluss oder Teil A-Konzeptfrage) |

**Quellen zum Nachschlagen:** [`00_Themenuebersicht_Stochastik_Q3_Theorie.png`](00_Themenuebersicht_Stochastik_Q3_Theorie.png), [`00_Formelsammlung_Abitur_Theorie.pdf`](00_Formelsammlung_Abitur_Theorie.pdf)

---

## 2. Konzept-Erklärungen (First Principles)

> **Hinweis zu den WTR-Befehlen:** Die Befehle orientieren sich am **Casio fx-991DE X / ClassWiz** (wie im Unterrichtsmaterial `Inv. Normal-V.` verwendet). Bei einem **TI-Nspire / CAS** entsprechen sie `binomPdf`, `binomCdf`, `normCdf` und `invNorm`.

---

### 2.1 Grundbegriffe, Laplace & Mehrstufige Zufallsexperimente

* **Intuition (First Principles):**
  Wahrscheinlichkeit ist kein Bauchgefühl, sondern der **langfristige Stabilisierungswert** der relativen Häufigkeit bei sehr vielen Wiederholungen (*Gesetz der großen Zahlen*). Bei symmetrischen Versuchen (Würfel, Münze) hat jedes Ergebnis dieselbe Chance (*Laplace*). Werden mehrere Versuche hintereinander ausgeführt, verzweigen sich die Möglichkeiten wie Äste eines Baumes: Entlang eines Pfades werden Chancenanteile immer weiter „aufgeteilt“ (Multiplikation), verschiedene passende Pfade werden zusammengezählt (Addition).

* **Exakte Formeln:**
  * Relative Häufigkeit: $h_n(E) = \frac{H_n(E)}{n}$
  * Laplace-Regel: $P(E) = \frac{|E|}{|\Omega|}$
  * Komplementärregel: $P(\bar{E}) = 1 - P(E)$
  * **Additionssatz:** $P(E_1 \cup E_2) = P(E_1) + P(E_2) - P(E_1 \cap E_2)$
  * **1. Pfadregel (Multiplikation):** Die Wahrscheinlichkeit eines Ergebnisses ist das Produkt der Wahrscheinlichkeiten längs des zugehörigen Pfades.
  * **2. Pfadregel (Addition):** Die Wahrscheinlichkeit eines Ereignisses ist die Summe der zugehörigen Pfadwahrscheinlichkeiten.

* **Kochrezept (Mehrstufige Experimente):**
  1. Ergebnismenge $\Omega$ bzw. Stufenanzahl klären (**mit** oder **ohne** Zurücklegen? $\rightarrow$ ändern sich die Nenner?).
  2. Baumdiagramm zeichnen (bei vielen Stufen: **verkürzten Baum** nur für die relevanten Pfade zeichnen).
  3. Prüfen, ob das **Gegenereignis** $\bar{E}$ deutlich weniger Pfade hat (z. B. bei *„mindestens einmal“* $\rightarrow 1 - P(\text{keinmal})$).
  4. Pfadwahrscheinlichkeiten multiplizieren und günstige Pfade addieren.

* **Quellen zum Nachschlagen:**
  [`01_Grundbegriffe_Zufallsversuch_Uebung.pdf`](01_Grundbegriffe_Zufallsversuch_Uebung.pdf) · [`02_Laplace_Wahrscheinlichkeiten_Theorie_Uebung.pdf`](02_Laplace_Wahrscheinlichkeiten_Theorie_Uebung.pdf) · [`03_Mehrstufige_Zufallsexperimente_Baumdiagramm_Theorie_Uebung.pdf`](03_Mehrstufige_Zufallsexperimente_Baumdiagramm_Theorie_Uebung.pdf) · [`03_Mehrstufige_Zufallsexperimente_Uebung_Loesung.pdf`](03_Mehrstufige_Zufallsexperimente_Uebung_Loesung.pdf) · [`04_Verknuepfung_von_Ereignissen_Mengen_Theorie.pdf`](04_Verknuepfung_von_Ereignissen_Mengen_Theorie.pdf) · [`04_Additionssatz_Mengendarstellung_Theorie_Uebung.pdf`](04_Additionssatz_Mengendarstellung_Theorie_Uebung.pdf)

---

### 2.2 Bedingte Wahrscheinlichkeit, Vierfeldertafel & Stochastische Unabhängigkeit

* **Intuition (First Principles):**
  Bei der bedingten Wahrscheinlichkeit $P_A(B)$ (auch $P(B \mid A)$) weiß man bereits, dass $A$ eingetreten ist. Dadurch schrumpft die Grundmenge von $\Omega$ auf $A$ zusammen! Man fragt also nicht mehr „Welcher Anteil von allen hat $A$ und $B$?“, sondern „Welcher Anteil **innerhalb** von $A$ hat auch $B$?“. Zwei Ereignisse $A$ und $B$ sind **stochastisch unabhängig**, wenn dieses Vorwissen über $A$ die Chance für $B$ überhaupt nicht verändert.

* **Exakte Formeln (IQB-Formelsammlung S. 7):**
  * Bedingte Wahrscheinlichkeit:
    $$P_A(B) = \frac{P(A \cap B)}{P(A)} \quad \text{mit } P(A) > 0$$
  * Totale Wahrscheinlichkeit:
    $$P(B) = P(A) \cdot P_A(B) + P(\bar{A}) \cdot P_{\bar{A}}(B)$$
  * Satz von Bayes (Umkehrung der Baumrichtung):
    $$P_B(A) = \frac{P(A \cap B)}{P(B)} = \frac{P(A) \cdot P_A(B)}{P(A) \cdot P_A(B) + P(\bar{A}) \cdot P_{\bar{A}}(B)}$$
  * **Stochastische Unabhängigkeit** (äquivalente Kriterien):
    $$P(A \cap B) = P(A) \cdot P(B) \iff P_A(B) = P(B) \iff P_B(A) = P(A)$$

* **Kochrezept (Textaufgabe $\rightarrow$ Vierfeldertafel / Baum):**
  1. Zwei eindeutige Ereignisse $A, \bar{A}$ und $B, \bar{B}$ definieren.
  2. Gegebene Prozentwerte sauber unterscheiden: Steht im Text ein **„von“ / „unter“ / „falls“**, ist es eine **bedingte Wahrscheinlichkeit** (Ast auf der 2. Stufe des Baumes, z. B. $P_A(B)$). Steht dort **„und“ / „sowohl als auch“**, ist es eine **Schnittwahrscheinlichkeit** $P(A \cap B)$ (Inneres der Vierfeldertafel).
  3. Über $P(A \cap B) = P(A) \cdot P_A(B)$ in die Vierfeldertafel umrechnen, alle Randsummen (Zeilen-/Spaltensummen $= 1$) ergänzen.
  4. Gesuchte umgekehrte bedingte Wahrscheinlichkeit $P_B(A)$ direkt als Quotient $\frac{P(A \cap B)}{P(B)}$ aus der Vierfeldertafel ablesen.

* **Quellen zum Nachschlagen:**
  [`05_Vierfeldertafel_Baumdiagramm_Uebung.pdf`](05_Vierfeldertafel_Baumdiagramm_Uebung.pdf) · [`06_Bedingte_Wahrscheinlichkeit_Kreuz_und_Quer_Uebung.pdf`](06_Bedingte_Wahrscheinlichkeit_Kreuz_und_Quer_Uebung.pdf) · [`07_Bedingte_Wahrscheinlichkeit_Unabhaengigkeit_Uebung.pdf`](07_Bedingte_Wahrscheinlichkeit_Unabhaengigkeit_Uebung.pdf) · [`07_Bedingte_Wahrscheinlichkeit_Bayes_Laktose_Theorie_Uebung.pdf`](07_Bedingte_Wahrscheinlichkeit_Bayes_Laktose_Theorie_Uebung.pdf) · [`07_Baumdiagramm_Bedingte_Wahrscheinlichkeit_Abschlussuebung.pdf`](07_Baumdiagramm_Bedingte_Wahrscheinlichkeit_Abschlussuebung.pdf)

---

### 2.3 Kombinatorik & Abzählverfahren

* **Intuition (First Principles):**
  Statt riesige Baumdiagramme zu zeichnen, zählt man die Pfade systematisch: Hat Stufe 1 $n_1$ Optionen, Stufe 2 $n_2$ Optionen usw., multipliziert man (*Produktregel*). Werden gleiche Elemente mehrfach ausgewählt, teilt man bei egaler Reihenfolge durch die $k!$ möglichen Anordnungen derselben Auswahl – genau das liefert den Binomialkoeffizienten $\binom{n}{k}$.

* **Exakte Formeln:**
  * **Permutation** (alle $n$ Elemente anordnen):
    * ohne Wiederholung: $n!$
    * mit Wiederholung (Gruppen $m_1, \dots, m_r$ gleicher Elemente): $\frac{n!}{m_1! \cdot m_2! \cdot \ldots \cdot m_r!}$
  * **Urnenmodelle** ($k$-mal Ziehen aus $n$ Elementen):
    * mit Zurücklegen, mit Reihenfolge: $n^k$
    * ohne Zurücklegen, mit Reihenfolge: $\frac{n!}{(n-k)!}$
    * ohne Zurücklegen, ohne Reihenfolge: $\binom{n}{k} = \frac{n!}{k! \cdot (n-k)!}$
    * mit Zurücklegen, ohne Reihenfolge: $\binom{n+k-1}{k}$
  * **Hypergeometrische Verteilung** (Lotto-Modell, Ziehen **ohne** Zurücklegen aus $N$ Elementen mit $M$ Treffern):
    $$P(X = k) = \frac{\binom{M}{k} \cdot \binom{N-M}{n-k}}{\binom{N}{n}}$$

* **WTR-Befehle (Casio fx-991DE X):**
  * Fakultät $n!$: `n` $\rightarrow$ `SHIFT` `x⁻¹` (`x!`)
  * Binomialkoeffizient $\binom{n}{k}$: `n` $\rightarrow$ `SHIFT` `÷` (`nCr`) $\rightarrow$ `k`
  * Variation $\frac{n!}{(n-k)!}$: `n` $\rightarrow$ `SHIFT` `×` (`nPr`) $\rightarrow$ `k`

* **Kochrezept:**
  1. Entscheiden: Werden **alle** Elemente sortiert (Permutation) oder eine **Stichprobe** gezogen?
  2. Prüfen: Ist die **Reihenfolge** wichtig (z. B. Zahlencode, Siegerpodest) oder egal (z. B. Lotto, Kartenspiel, Ausschuss)?
  3. Prüfen: Wird **mit** oder **ohne** Zurücklegen gezogen?
  4. Bei Wahrscheinlichkeiten mit Zählverfahren: $\frac{\text{Anzahl günstiger Auswahlen}}{\text{Anzahl aller Auswahlen}}$.

* **Quellen zum Nachschlagen:**
  [`08_Kombinatorik_Entscheidungsbaum_Formeln_Theorie.png`](08_Kombinatorik_Entscheidungsbaum_Formeln_Theorie.png) · [`08_Kombinatorische_Abzaehlverfahren_Theorie_Uebung_Loesung.pdf`](08_Kombinatorische_Abzaehlverfahren_Theorie_Uebung_Loesung.pdf) · [`08_Kombinatorik_Kreuz_und_Quer_Uebung.pdf`](08_Kombinatorik_Kreuz_und_Quer_Uebung.pdf)

---

### 2.4 Zufallsgrößen, Erwartungswert, Varianz & Standardabweichung

* **Intuition (First Principles):**
  Eine Zufallsgröße $X$ übersetzt Ergebnisse in Zahlen (z. B. Gewinn in €, Anzahl Treffer). Der **Erwartungswert $E(X)$** ist der langfristige Durchschnitt pro Spiel – man gewichtet jeden Wert $x_i$ mit seiner Wahrscheinlichkeit. Um die **Streuung** zu messen, bildet man die Abstände $(x_i - \mu)$, quadriert sie (damit sich $+$ und $-$ nicht aufheben $\rightarrow$ **Varianz**) und zieht am Ende die Wurzel, um wieder in der ursprünglichen Einheit zu landen (**Standardabweichung $\sigma$**).

* **Exakte Formeln (IQB-Formelsammlung S. 7):**
  * Erwartungswert:
    $$\mu = E(X) = \sum_{i=1}^{n} x_i \cdot P(X = x_i)$$
  * Varianz:
    $$V(X) = \operatorname{Var}(X) = \sum_{i=1}^{n} (x_i - E(X))^2 \cdot P(X = x_i)$$
  * Standardabweichung:
    $$\sigma = \sqrt{\operatorname{Var}(X)}$$
  * **Faires Spiel:** $E(\text{Gewinn}) = 0$ bzw. $E(\text{Auszahlung}) = \text{Einsatz}$.

* **WTR-Befehle (Casio fx-991DE X):**
  * `MENU` $\rightarrow$ `6` (Statistik) $\rightarrow$ `1` (`1-Variab`)
  * `SHIFT` `MENU` $\rightarrow$ `Statistik` $\rightarrow$ `Häufigkeit: Ein` (falls nötig)
  * $x_i$-Werte in Spalte `x`, zugehörige Wahrscheinlichkeiten $P(X=x_i)$ in Spalte `Freq` eingeben $\rightarrow$ `OPTN` $\rightarrow$ `2` (`1-Variab-Ber.`).
  * Ablesen: $\bar{x} = \mu = E(X)$ und $\sigma_x = \sigma(X)$ (Hinweis: Summe der `Freq` muss $1$ sein!).

* **Kochrezept:**
  1. Zufallsgröße $X$ präzise definieren (Achtung: *Auszahlung* vs. *Reingewinn = Auszahlung − Einsatz*!).
  2. Alle möglichen Werte $x_i$ auflisten und $P(X = x_i)$ bestimmen (Kontrolle: $\sum P(X = x_i) = 1$).
  3. $E(X)$ berechnen und bei fairem Spiel $= 0$ setzen (nach dem gesuchten Einsatz oder Auszahlungsbetrag auflösen).
  4. Zur Streuungsbewertung $\operatorname{Var}(X)$ und $\sigma$ berechnen.

* **Quellen zum Nachschlagen:**
  [`09_Zufallsgroessen_Wahrscheinlichkeitsverteilung_Theorie_Uebung.pdf`](09_Zufallsgroessen_Wahrscheinlichkeitsverteilung_Theorie_Uebung.pdf) · [`10_Erwartungswert_Zufallsgroesse_Theorie_Uebung.pdf`](10_Erwartungswert_Zufallsgroesse_Theorie_Uebung.pdf) · [`10_Erwartungswert_Zufallsgroesse_Loesung.pdf`](10_Erwartungswert_Zufallsgroesse_Loesung.pdf) · [`19_Standardabweichung_Einstieg_Basketball_Uebung.pdf`](19_Standardabweichung_Einstieg_Basketball_Uebung.pdf) · [`19_Standardabweichung_Varianz_Sigmaregeln_Theorie_Uebung.pdf`](19_Standardabweichung_Varianz_Sigmaregeln_Theorie_Uebung.pdf)

---

### 2.5 Bernoulli-Ketten, Binomialverteilung & 3-Mindestens-Aufgaben

* **Intuition (First Principles):**
  Wiederholt man ein Ja/Nein-Experiment (Erfolg/Misserfolg) $n$-mal **unabhängig** mit **konstanter** Erfolgswahrscheinlichkeit $p$, zählt $X$ die Anzahl der Erfolge. Jeder Pfad mit genau $k$ Erfolgen hat die Wahrscheinlichkeit $p^k \cdot (1-p)^{n-k}$. Weil es $\binom{n}{k}$ solcher Pfade gibt, multipliziert man einfach beides. Da man bei großen $n$ nicht alle einzelnen $P(X=i)$ addieren will, nutzt man die **kumulierte** Verteilung $F(n;p;k) = P(X \le k)$.

* **Exakte Formeln (IQB-Formelsammlung S. 7):**
  * Bernoulli-Formel:
    $$P(X = k) = B(n; p; k) = \binom{n}{k} \cdot p^k \cdot (1-p)^{n-k}$$
  * Kumulierte Binomialverteilung:
    $$F(n; p; k) = P(X \le k) = \sum_{i=0}^{k} \binom{n}{i} \cdot p^i \cdot (1-p)^{n-i}$$
  * Kenngrößen der Binomialverteilung:
    $$\mu = n \cdot p \qquad \sigma = \sqrt{n \cdot p \cdot (1-p)}$$
  * **Umrechnung für alle Ungleichungen (auf $\le$ zurückführen!):**
    * $P(X < k) = P(X \le k-1)$
    * $P(X \ge k) = 1 - P(X \le k-1)$
    * $P(X > k) = 1 - P(X \le k)$
    * $P(a \le X \le b) = P(X \le b) - P(X \le a-1)$
  * **3-Mindestens-Ansatz** (gesucht: Mindestanzahl $n$ für *„mindestens 1 Treffer mit mind. Wahrscheinlichkeit $\gamma$“*):
    $$P(X \ge 1) \ge \gamma \iff 1 - (1-p)^n \ge \gamma \iff (1-p)^n \le 1 - \gamma \iff n \ge \frac{\ln(1-\gamma)}{\ln(1-p)}$$

* **WTR-Befehle (Casio fx-991DE X):**
  * Menü: `MENU` $\rightarrow$ `7` (`Verteilungsfkt.`)
  * Einzelwahrscheinlichkeit $P(X = k)$: `4` (`Binomial-Dichte`) $\rightarrow$ `2` (`Variab.`) $\rightarrow$ `x` ($=k$), `N` ($=n$), `p` eingeben.
  * Kumulierte Wahrscheinlichkeit $P(X \le k)$: `▼` $\rightarrow$ `1` (`Kumul. Binom.-V.`) $\rightarrow$ `2` (`Variab.`) $\rightarrow$ `x` ($=k$), `N` ($=n$), `p` eingeben.
  * Inverse Suche ($n$, $p$ oder $k$ gesucht, wenn $P(X \le k)$ vorgegeben): `Kumul. Binom.-V.` $\rightarrow$ `1` (`Liste`) mit Wertetabelle oder im `MENU` `9` (`Tabellen`) mit $f(x)$ testen. *(Tipp für $p$ oder $n$: Auch über `SOLVE` bzw. Wertetabelle der kumulierten Funktion).*

* **Kochrezept:**
  1. **Begründung Bernoulli-Kette** (falls gefordert): Zwei Ausgänge (Erfolg/Misserfolg), $n$ unabhängige Durchführungen, konstante Trefferwahrscheinlichkeit $p$.
  2. Zufallsgröße $X$, $n$ und $p$ explizit angeben: $X \sim B_{n;p}$.
  3. Ereignis sauber als Ungleichung schreiben (*mindestens* $\ge$, *höchstens* $\le$, *weniger als* $<$, *mehr als* $>$) und auf $P(X \le \dots)$ umschreiben.
  4. Mit WTR ausrechnen (oder bei 3-Mindestens-Aufgaben mit Logarithmus nach $n$ auflösen und **immer aufrunden**!).

* **Quellen zum Nachschlagen:**
  [`11_Dreimal_Mindestens_Aufgaben_Theorie_Uebung.pdf`](11_Dreimal_Mindestens_Aufgaben_Theorie_Uebung.pdf) · [`12_Bernoulli_Ketten_Binomialverteilung_Theorie_Uebung.pdf`](12_Bernoulli_Ketten_Binomialverteilung_Theorie_Uebung.pdf) · [`13_Binomialverteilung_Robinsons_Insel_Uebung.png`](13_Binomialverteilung_Robinsons_Insel_Uebung.png) · [`14_Binomialverteilung_Histogramme_Zuordnung_Uebung.pdf`](14_Binomialverteilung_Histogramme_Zuordnung_Uebung.pdf) · [`15_Bernoulli_Kette_Binomialverteilung_Uebung.pdf`](15_Bernoulli_Kette_Binomialverteilung_Uebung.pdf) · [`16_Kumulierte_Wahrscheinlichkeiten_Theorie_Uebung.pdf`](16_Kumulierte_Wahrscheinlichkeiten_Theorie_Uebung.pdf) · [`16_Kumulierte_Wahrscheinlichkeiten_Tafelbild_Loesung.pdf`](16_Kumulierte_Wahrscheinlichkeiten_Tafelbild_Loesung.pdf) · [`16_Kumulierte_Wahrscheinlichkeiten_Auslastungsmodelle_Uebung.pdf`](16_Kumulierte_Wahrscheinlichkeiten_Auslastungsmodelle_Uebung.pdf) · [`17_Binomialverteilung_Anwendungskontexte_Parameter_Theorie_Uebung.pdf`](17_Binomialverteilung_Anwendungskontexte_Parameter_Theorie_Uebung.pdf) · [`18_Binomialverteilung_Anwendungskontexte_Uebung_Loesung.pdf`](18_Binomialverteilung_Anwendungskontexte_Uebung_Loesung.pdf)

---

### 2.6 Stetige Zufallsgrößen, Normalverteilung & Sigma-Regeln (LK)

* **Intuition (First Principles):**
  Bei Messgrößen (Körpergröße, Gewicht, Zeit) kann eine Zufallsgröße **beliebige reelle Zahlen** annehmen. Die Säulen eines Histogramms werden unendlich schmal – die Wahrscheinlichkeit für einen *exakten* Einzelwert $P(X = a)$ ist $0$, weil ein Strich keine Fläche hat! Wahrscheinlichkeiten entsprechen daher **Flächeninhalten (Integralen)** unter der **Gaußschen Glockenkurve** $\varphi_{\mu,\sigma}(x)$. Die Kurve entsteht aus $e^{-x^2}$ durch Verschiebung um $\mu$, Streckung in $x$-Richtung mit $\sigma$ und Stauchung in $y$-Richtung mit $\frac{1}{\sigma \sqrt{2\pi}}$, sodass die Gesamtfläche exakt $1$ beträgt.

* **Exakte Formeln (IQB-Formelsammlung S. 7–8):**
  * Dichtefunktion:
    $$\varphi_{\mu,\sigma}(x) = \frac{1}{\sigma \cdot \sqrt{2\pi}} \cdot e^{-\frac{1}{2}\left(\frac{x-\mu}{\sigma}\right)^2}$$
  * Intervallwahrscheinlichkeit:
    $$P(a \le X \le b) = \int_a^b \varphi_{\mu,\sigma}(x) \, \mathrm{d}x$$
  * **Analysis-Eigenschaften der Glockenkurve:**
    * Achsensymmetrisch zur Geraden $x = \mu$
    * Hochpunkt bei $H\left(\mu \,\middle|\, \frac{1}{\sigma\sqrt{2\pi}}\right)$
    * Wendepunkte bei $W_{1,2}\left(\mu \pm \sigma \,\middle|\, \frac{1}{\sigma\sqrt{2\pi}} \cdot e^{-\frac{1}{2}}\right)$
    * Asymptote: $\lim_{x \to \pm \infty} \varphi_{\mu,\sigma}(x) = 0$
  * **Sigma-Regeln:**
    * $P(\mu - \sigma \le X \le \mu + \sigma) \approx 68{,}3\,\%$
    * $P(\mu - 1{,}64\sigma \le X \le \mu + 1{,}64\sigma) \approx 90{,}0\,\%$
    * $P(\mu - 1{,}96\sigma \le X \le \mu + 1{,}96\sigma) \approx 95{,}0\,\%$
    * $P(\mu - 2\sigma \le X \le \mu + 2\sigma) \approx 95{,}4\,\%$
    * $P(\mu - 2{,}58\sigma \le X \le \mu + 2{,}58\sigma) \approx 99{,}0\,\%$
    * $P(\mu - 3\sigma \le X \le \mu + 3\sigma) \approx 99{,}7\,\%$
  * **Lokale Näherungsformel** (Approximation der Binomialverteilung für $\sigma > 3$):
    $$P(X = k) \approx \varphi_{\mu,\sigma}(k) \quad \text{bzw. mit Stetigkeitskorrektur: } P(a \le X \le b) \approx \int_{a-0{,}5}^{b+0{,}5} \varphi_{\mu,\sigma}(x)\,\mathrm{d}x$$
  * **Prognose- und Konfidenzintervall** (Formelsammlung S. 8):
    * Prognoseintervall: $\left[ p - c \cdot \sqrt{\frac{p(1-p)}{n}} \,;\, p + c \cdot \sqrt{\frac{p(1-p)}{n}} \right]$
    * Konfidenzintervall für $p$: $|h - p| = c \cdot \sqrt{\frac{p(1-p)}{n}}$

* **WTR-Befehle (Casio fx-991DE X):**
  * Menü: `MENU` $\rightarrow$ `7` (`Verteilungsfkt.`)
  * Intervallwahrscheinlichkeit $P(a \le X \le b)$: `2` (`Kumul. Normal-V.`) $\rightarrow$ `Untere` ($=a$), `Obere` ($=b$), `σ`, `μ` eingeben. *(Für $P(X \le b)$: `Untere = -1E99` oder `-999999`; für $P(X \ge a)$: `Obere = 1E99`).*
  * **Invertierung** (Grenze $b$ bei gegebenem $P(X \le b) = p_{\text{Fläche}}$ gesucht): `3` (`Inv. Normal-V.`) $\rightarrow$ `Fläche` ($=p_{\text{Fläche}}$ als linksseitige Fläche!), `σ`, `μ` eingeben $\rightarrow$ liefert `xInv`.
  * **Unbekanntes $\mu$ oder $\sigma$ berechnen:** Zuerst mit `Inv. Normal-V.` für die Standardnormalverteilung ($\mu_{\text{std}} = 0$, $\sigma_{\text{std}} = 1$) den $z$-Wert bestimmen und in $z = \frac{x - \mu}{\sigma}$ einsetzen!

* **Kochrezept (Normalverteilung & Invertierung):**
  1. $\mu$ und $\sigma$ notieren und ggf. Rundungsgrenzen (Stetigkeitskorrektur bei gerundeten Messwerten, z. B. „genau $60\,\text{g}$“ $\rightarrow [59{,}5; 60{,}5]$) prüfen!
  2. Prüfen: Ist die **Wahrscheinlichkeit gesucht** $\rightarrow$ `Kumul. Normal-V.`. Sind **Grenzen / Intervalle gesucht** $\rightarrow$ `Inv. Normal-V.` (oder bei symmetrischem Intervall um $\mu$ einfach `Fläche` $=\frac{1 + p_{\text{Intervall}}}{2}$ für die obere Grenze nutzen, oder Sigma-Regel anwenden).
  3. Ist $\mu$ oder $\sigma$ unbekannt: $P(X \le x) = p_0 \implies \Phi\left(\frac{x-\mu}{\sigma}\right) = p_0 \implies \frac{x-\mu}{\sigma} = \text{InvNorm}(p_0; 0; 1)$ nach der gesuchten Größe auflösen.

* **Quellen zum Nachschlagen:**
  [`20_Gausssche_Glockenkurve_Normalverteilung_Praesentation_Theorie.pptx`](20_Gausssche_Glockenkurve_Normalverteilung_Praesentation_Theorie.pptx) · [`20_Normalverteilung_Glockenkurve_Einfuehrung_Theorie_Uebung.pdf`](20_Normalverteilung_Glockenkurve_Einfuehrung_Theorie_Uebung.pdf) · [`21_Normalverteilung_Stetige_Zufallsgroessen_Theorie_Uebung.pptx`](21_Normalverteilung_Stetige_Zufallsgroessen_Theorie_Uebung.pptx) · [`21_Normalverteilung_Analysis_Invertierung_Theorie_Uebung.pdf`](21_Normalverteilung_Analysis_Invertierung_Theorie_Uebung.pdf) · [`21_Normalverteilung_Invertierung_Zusatzaufgaben_Uebung.pdf`](21_Normalverteilung_Invertierung_Zusatzaufgaben_Uebung.pdf)

---

### 2.7 Hypothesentests: Alternativ- & Signifikanztests (LK)

* **Intuition (First Principles):**
  Man kennt die wahre Trefferwahrscheinlichkeit $p$ nicht, hat aber eine Vermutung. Weil eine Stichprobe zufällig schwankt, kann man $p$ nie zu $100\,\%$ beweisen – man formuliert daher eine **Nullhypothese $H_0$** (Status quo / „nichts hat sich geändert“ oder der Fall, dessen irrtümliche Ablehnung schlimmer ist) und eine **Gegenhypothese $H_1$** (das, was man belegen möchte). Liegt das Stichprobenergebnis extrem weit weg vom Erwartungswert unter $H_0$ (im **Ablehnungsbereich** $K$), verwirft man $H_0$ und nimmt $H_1$ an.

* **Exakte Definitionen & Formeln (IQB-Formelsammlung S. 8):**
  * **Testarten:**
    * *Alternativtest:* $H_0: p = p_0$ gegen $H_1: p = p_1$
    * *Rechtsseitiger Signifikanztest:* $H_0: p \le p_0$ (bzw. $p = p_0$) gegen $H_1: p > p_0$ $\rightarrow$ Ablehnungsbereich $K = \{k, k+1, \dots, n\}$
    * *Linksseitiger Signifikanztest:* $H_0: p \ge p_0$ (bzw. $p = p_0$) gegen $H_1: p < p_0$ $\rightarrow$ Ablehnungsbereich $K = \{0, 1, \dots, k\}$
    * *Zweiseitiger Signifikanztest:* $H_0: p = p_0$ gegen $H_1: p \ne p_0$ $\rightarrow$ Ablehnungsbereich $K = \{0, \dots, k_1\} \cup \{k_2, \dots, n\}$ (Risiko $\alpha$ wird i. d. R. halbiert: je $\le \frac{\alpha}{2}$)
  * **Fehlerarten:**
    * **Fehler 1. Art ($\alpha$-Fehler):** $H_0$ wird verworfen, obwohl $H_0$ wahr ist:
      $$\alpha = P_{H_0}(X \in K) \le \alpha_{\max} \text{ (Signifikanzniveau)}$$
    * **Fehler 2. Art ($\beta$-Fehler):** $H_0$ wird *nicht* verworfen, obwohl $H_1$ wahr ist:
      $$\beta = P_{H_1}(X \notin K)$$
  * **Gütefunktion (LK):** $g(p) = P_p(X \in K)$ beschreibt die Wahrscheinlichkeit, $H_0$ in Abhängigkeit vom wahren Parameter $p$ abzulehnen.

* **WTR-Befehle:**
  Bestimmung der kritischen Zahl $k$ über `MENU` $\rightarrow$ `7` (`Verteilungsfkt.`) $\rightarrow$ `Kumul. Binom.-V.` (`1: Liste` oder `MENU 9` Tabelle für $F(n; p_0; x)$).

* **Kochrezept (Hypothesentest in 5 Schritten):**
  1. **Testgröße & Hypothesen:** $n$, $X$ definieren; $H_0$ und $H_1$ aufstellen (was soll belegt werden $\rightarrow H_1$! Bzw. bei vorgegebener $\alpha$-Grenze: welchen Fehler will man unter $\alpha$ drücken $\rightarrow$ dessen Ausgangshypothese ist $H_0$!).
  2. **Testrichtung:** Links-, rechts- oder zweiseitig? Ablehnungsbereich mit Parameter $k$ ansetzen.
  3. **Kritische Zahl $k$ bestimmen:** Bedingung $P_{H_0}(X \in K) \le \alpha$ mit der kumulierten Binomialverteilung lösen (zwei benachbarte Werte für $k$ angeben: einen, der $\le \alpha$ erfüllt, und einen, der $> \alpha$ liegt!).
  4. **Entscheidungsregel** sauber im Sachzusammenhang formulieren (inkl. Annahme- und Verwerfungsbereich).
  5. Falls gefragt: **$\beta$-Fehler** für konkretes $p_1$ mit dem gefundenen Annahmebereich berechnen und **Fehler 1. / 2. Art im Sachkontext** deuten.

* **Quellen zum Nachschlagen:**
  [`22_Hypothesentest_Alternativtest_Einfuehrung_Theorie_Uebung_Loesung.pdf`](22_Hypothesentest_Alternativtest_Einfuehrung_Theorie_Uebung_Loesung.pdf)

---

## 3. Teil A (hilfsmittelfrei) vs. Teil B (mit WTR)

| Kriterium | Teil A (Teil 1 – hilfsmittelfrei) | Teil B (Teil 2 – mit WTR & Formelsammlung) |
| :--- | :--- | :--- |
| **Erlaubte Hilfsmittel** | **Keine** (kein WTR/CAS, keine Formelsammlung) | WTR/CAS + **nur** offizielle IQB-Formelsammlung |
| **Umfang Stochastik** | ca. 2–3 Aufgaben innerhalb der 6 aus 10 Wahlaufgaben | 1 feste Pflichtaufgabe (**20 BE** im LK) |
| **Typische Aufgabentypen** | • Baumdiagramm / Vierfeldertafel mit einfachen Brüchen/Dezimalzahlen (`0,5`, `0,2`, `1/6`) ergänzen<br>• Bedingte Wahrscheinlichkeit & stochastische Unabhängigkeit prüfen<br>• Kleine Bernoulli-Terme aufstellen oder interpretieren (z. B. $1 - 0{,}6^5$ oder $\binom{4}{2} \cdot p^2 (1-p)^2$)<br>• Erwartungswert einer kleinen Tabelle berechnen (inkl. *„fair machen“*)<br>• Kombinatorik-Terme mit Fakultäten/Binomialkoeffizienten aufstellen oder zuordnen<br>• Glockenkurve skizzieren / Eigenschaften von $\mu$ und $\sigma$ grafisch ablesen (Hoch-/Wendepunkte, Flächenanteile mit Sigma-Regeln) | • Mehrstufige Sachkontexte mit großen Stichproben ($n = 100, 200, 500$)<br>• Kumulierte Binomialverteilungen $F(n;p;k)$ & inverse Suche nach $n, p, k$<br>• 3-Mindestens-Aufgaben (mit $\ln$ lösen oder tabellieren)<br>• Normalverteilung: Intervallwahrscheinlichkeiten, `Inv. Normal-V.`, Berechnung von unbekanntem $\mu$ oder $\sigma$, Stetigkeitskorrektur<br>• Vollständiger Hypothesentest (Hypothesen, kritische Zahl $k$, $\alpha$/$\beta$-Fehler, Sachdeutung) |
| **Lösungsstrategie Teil A** | **1.** Brüche statt Dezimalzahlen nutzen (kürzt sich oft sofort weg!).<br>**2.** Bei „Zeigen Sie“ / „Begründen Sie“: oft reicht der **Termansatz** ohne Ausrechnen (z. B. im Abi 2024/2025: Gleichung für faires Spiel aufstellen ohne nach $x$ aufzulösen).<br>**3.** Flächen unter der Normalverteilung über **Symmetrie** ($\mu$ halbiert die Fläche zu $0{,}5$) und die **1-/2-/3-$\sigma$-Regeln** ($68\,\%$, $95\,\%$, $99{,}7\,\%$) berechnen! | **1.** WTR-Befehl und Parameter ($n, p, k$ bzw. $\mu, \sigma$) sauber hinschreiben (z. B. $P(X \le 170) = F(200; 0{,}8; 170) \approx \dots$).<br>**2.** Bei Suche nach $k$ oder $n$: Immer die zwei entscheidenden Werte aus der Wertetabelle dokumentieren (Grenzwertnachweis!). |

**Typische Original-Beispiele zum Üben:**
* [`23_Klausurtraining_Probeklausur_Lambacher_Theorie_Uebung.pdf`](23_Klausurtraining_Probeklausur_Lambacher_Theorie_Uebung.pdf) (S. 6: Teil A hilfsmittelfrei; S. 7–8: Teil B mit Hilfsmitteln)
* [`24_Abituraufgaben_Baumdiagramm_Bedingte_Wahrscheinlichkeit_Loesung.pdf`](24_Abituraufgaben_Baumdiagramm_Bedingte_Wahrscheinlichkeit_Loesung.pdf)
* [`25_Abituraufgaben_Stochastik_Q3_2021_2026_Loesung.pdf`](25_Abituraufgaben_Stochastik_Q3_2021_2026_Loesung.pdf) (enthält exakt nach *HFT* = Teil A und *mit TR* = Teil B getrennte hessische Abituraufgaben 2021–2026!)

---

## 4. Typische Klausur-Fallen & Operator-Guide (Hessen)

### Operator-Guide (Worauf Korrektoren in Hessen achten)

| Operator | AFB | Was erwartet wird | Häufigster Punktabzug |
| :--- | :--- | :--- | :--- |
| **Berechnen** | I–II | Konkreter, dokumentierter Rechenweg (Formel, Einsetzen, Zwischenschritte, Ergebnis). | Nur das WTR-Endergebnis hinschreiben $\rightarrow$ **0 Punkte auf den Weg!** |
| **Bestimmen / Ermitteln** | I–II | Lösungsweg/Ansatz aufzeigen (z. B. Ansatz $P(X \le k) \le 0{,}05$ + zwei Nachbarwerte aus dem WTR) und Ergebnis formulieren. | Fehlender Ansatz / fehlende Benennung der WTR-Eingabegrößen. |
| **Begründen** | II | Argumentation auf mathematische Gesetze, Definitionen oder Eigenschaften zurückführen (Text!). | Nur eine Rechnung ohne erklärenden Satz. |
| **Untersuchen** | II–III | Systematische Analyse anhand eines Kriteriums (z. B. $P(A \cap B) \stackrel{?}{=} P(A) \cdot P(B)$), Rechnung **und** abschließendes Urteil im Sachkontext. | Rechnung durchgeführt, aber **kein Antwortsatz** mit „stochastisch unabhängig / nicht unabhängig“ bzw. Vergleich. |
| **Deuten / Interpretieren** | II–III | Mathematisches Ergebnis in den konkreten Sachzusammenhang der Aufgabe übersetzen (mit Einheiten/Prozenten/Personen). | Allgemeine Lehrbuchdefinition statt Bezug zum konkreten Text (z. B. „Zitronen“, „Laktose“, „Pkw“). |
| **Zeigen / Nachweisen** | II–III | Lückenlose Herleitung eines bereits in der Aufgabe angegebenen Kontrollergebnisses. | Mit dem Kontrollergebnis weiterrechnen, statt es herzuleiten. |

### Die 7 häufigsten Stochastik-Fallen im Hessen-Abi

1. **Verwechslung von $P(A \cap B)$ und $P_A(B)$:**
   * *„Unter den Abiturienten sind $55\,\%$ Mädchen“* = $P_{\text{Abi}}(M) = 0{,}55$ (bedingte Wahrscheinlichkeit!).
   * *„$20\,\%$ aller Schüler sind Mädchen mit Abitur“* = $P(M \cap \text{Abi}) = 0{,}20$ (Schnittwahrscheinlichkeit!).
2. **Vergessenes $-1$ bei der Gegenwahrscheinlichkeit (Binomialverteilung):**
   $P(X \ge k) = 1 - P(X \le k\mathbf{-1})$, aber $P(X > k) = 1 - P(X \le k)$. Ein Zahlendreher kostet hier die komplette Aufgabe!
3. **Einsatz vs. Gewinn beim Erwartungswert:**
   Ist $X$ die *Auszahlung* oder der *Gewinn* (Auszahlung $-$ Einsatz)? Immer genau lesen, was definiert ist!
4. **Fehlende Stetigkeitskorrektur / Rundungsgrenzen bei der Normalverteilung:**
   Wenn Gewichte auf ganze Gramm gerundet werden, entspricht „genau $60\,\text{g}$“ dem Intervall $[59{,}5; 60{,}5]$ – nicht $P(X = 60) = 0$!
5. **Rechte vs. linke Fläche bei `Inv. Normal-V.`:**
   Der Casio WTR erwartet bei `Inv. Normal-V.` immer die **linksseitige** Fläche $P(X \le x)$. Ist $P(X \ge x) = 0{,}10$ gesucht (die obersten $10\,\%$), muss man `Fläche = 0.90` eingeben!
6. **Hypothesentest – Hypothesen vertauscht:**
   Die Behauptung/Vermutung, die man *beweisen* will, kommt in **$H_1$**, das Gegenteil in **$H_0$**. Alternativ: Der Fehler, der sicher unter $\alpha$ (z. B. $5\,\%$) begrenzt werden soll, bestimmt $H_0$!
7. **Unabhängigkeit vs. Unvereinbarkeit:**
   Unvereinbar ($P(A \cap B) = 0$) ist **nicht** dasselbe wie stochastisch unabhängig ($P(A \cap B) = P(A)\cdot P(B)$)! Zwei unvereinbare Ereignisse mit $P(A), P(B) > 0$ sind sogar *immer abhängig*.

---

## 5. Komplettes Dateiverzeichnis (`Mathe Stochastik/`)

* **Übersicht & Formeln:** [`00_Themenuebersicht_Stochastik_Q3_Theorie.png`](00_Themenuebersicht_Stochastik_Q3_Theorie.png) · [`00_Formelsammlung_Abitur_Theorie.pdf`](00_Formelsammlung_Abitur_Theorie.pdf)
* **Q3.1 Grundlagen & Mehrstufige Experimente:** [`01_Grundbegriffe_Zufallsversuch_Uebung.pdf`](01_Grundbegriffe_Zufallsversuch_Uebung.pdf) · [`02_Laplace_Wahrscheinlichkeiten_Theorie_Uebung.pdf`](02_Laplace_Wahrscheinlichkeiten_Theorie_Uebung.pdf) · [`03_Mehrstufige_Zufallsexperimente_Baumdiagramm_Theorie_Uebung.pdf`](03_Mehrstufige_Zufallsexperimente_Baumdiagramm_Theorie_Uebung.pdf) · [`03_Mehrstufige_Zufallsexperimente_Uebung_Loesung.pdf`](03_Mehrstufige_Zufallsexperimente_Uebung_Loesung.pdf) · [`04_Verknuepfung_von_Ereignissen_Mengen_Theorie.pdf`](04_Verknuepfung_von_Ereignissen_Mengen_Theorie.pdf) · [`04_Additionssatz_Mengendarstellung_Theorie_Uebung.pdf`](04_Additionssatz_Mengendarstellung_Theorie_Uebung.pdf)
* **Q3.1 Bedingte Wahrscheinlichkeit & Kombinatorik:** [`05_Vierfeldertafel_Baumdiagramm_Uebung.pdf`](05_Vierfeldertafel_Baumdiagramm_Uebung.pdf) · [`06_Bedingte_Wahrscheinlichkeit_Kreuz_und_Quer_Uebung.pdf`](06_Bedingte_Wahrscheinlichkeit_Kreuz_und_Quer_Uebung.pdf) · [`07_Bedingte_Wahrscheinlichkeit_Unabhaengigkeit_Uebung.pdf`](07_Bedingte_Wahrscheinlichkeit_Unabhaengigkeit_Uebung.pdf) · [`07_Bedingte_Wahrscheinlichkeit_Bayes_Laktose_Theorie_Uebung.pdf`](07_Bedingte_Wahrscheinlichkeit_Bayes_Laktose_Theorie_Uebung.pdf) · [`07_Baumdiagramm_Bedingte_Wahrscheinlichkeit_Abschlussuebung.pdf`](07_Baumdiagramm_Bedingte_Wahrscheinlichkeit_Abschlussuebung.pdf) · [`08_Kombinatorik_Entscheidungsbaum_Formeln_Theorie.png`](08_Kombinatorik_Entscheidungsbaum_Formeln_Theorie.png) · [`08_Kombinatorische_Abzaehlverfahren_Theorie_Uebung_Loesung.pdf`](08_Kombinatorische_Abzaehlverfahren_Theorie_Uebung_Loesung.pdf) · [`08_Kombinatorik_Kreuz_und_Quer_Uebung.pdf`](08_Kombinatorik_Kreuz_und_Quer_Uebung.pdf)
* **Q3.2 Zufallsgrößen & Binomialverteilung:** [`09_Zufallsgroessen_Wahrscheinlichkeitsverteilung_Theorie_Uebung.pdf`](09_Zufallsgroessen_Wahrscheinlichkeitsverteilung_Theorie_Uebung.pdf) · [`10_Erwartungswert_Zufallsgroesse_Theorie_Uebung.pdf`](10_Erwartungswert_Zufallsgroesse_Theorie_Uebung.pdf) · [`10_Erwartungswert_Zufallsgroesse_Loesung.pdf`](10_Erwartungswert_Zufallsgroesse_Loesung.pdf) · [`11_Dreimal_Mindestens_Aufgaben_Theorie_Uebung.pdf`](11_Dreimal_Mindestens_Aufgaben_Theorie_Uebung.pdf) · [`12_Bernoulli_Ketten_Binomialverteilung_Theorie_Uebung.pdf`](12_Bernoulli_Ketten_Binomialverteilung_Theorie_Uebung.pdf) · [`13_Binomialverteilung_Robinsons_Insel_Uebung.png`](13_Binomialverteilung_Robinsons_Insel_Uebung.png) · [`14_Binomialverteilung_Histogramme_Zuordnung_Uebung.pdf`](14_Binomialverteilung_Histogramme_Zuordnung_Uebung.pdf) · [`15_Bernoulli_Kette_Binomialverteilung_Uebung.pdf`](15_Bernoulli_Kette_Binomialverteilung_Uebung.pdf) · [`16_Kumulierte_Wahrscheinlichkeiten_Theorie_Uebung.pdf`](16_Kumulierte_Wahrscheinlichkeiten_Theorie_Uebung.pdf) · [`16_Kumulierte_Wahrscheinlichkeiten_Tafelbild_Loesung.pdf`](16_Kumulierte_Wahrscheinlichkeiten_Tafelbild_Loesung.pdf) · [`16_Kumulierte_Wahrscheinlichkeiten_Auslastungsmodelle_Uebung.pdf`](16_Kumulierte_Wahrscheinlichkeiten_Auslastungsmodelle_Uebung.pdf) · [`17_Binomialverteilung_Anwendungskontexte_Parameter_Theorie_Uebung.pdf`](17_Binomialverteilung_Anwendungskontexte_Parameter_Theorie_Uebung.pdf) · [`18_Binomialverteilung_Anwendungskontexte_Uebung_Loesung.pdf`](18_Binomialverteilung_Anwendungskontexte_Uebung_Loesung.pdf) · [`19_Standardabweichung_Einstieg_Basketball_Uebung.pdf`](19_Standardabweichung_Einstieg_Basketball_Uebung.pdf) · [`19_Standardabweichung_Varianz_Sigmaregeln_Theorie_Uebung.pdf`](19_Standardabweichung_Varianz_Sigmaregeln_Theorie_Uebung.pdf)
* **Q3.2 LK Normalverteilung:** [`20_Gausssche_Glockenkurve_Normalverteilung_Praesentation_Theorie.pptx`](20_Gausssche_Glockenkurve_Normalverteilung_Praesentation_Theorie.pptx) · [`20_Normalverteilung_Glockenkurve_Einfuehrung_Theorie_Uebung.pdf`](20_Normalverteilung_Glockenkurve_Einfuehrung_Theorie_Uebung.pdf) · [`21_Normalverteilung_Stetige_Zufallsgroessen_Theorie_Uebung.pptx`](21_Normalverteilung_Stetige_Zufallsgroessen_Theorie_Uebung.pptx) · [`21_Normalverteilung_Analysis_Invertierung_Theorie_Uebung.pdf`](21_Normalverteilung_Analysis_Invertierung_Theorie_Uebung.pdf) · [`21_Normalverteilung_Invertierung_Zusatzaufgaben_Uebung.pdf`](21_Normalverteilung_Invertierung_Zusatzaufgaben_Uebung.pdf)
* **Q3.3 Hypothesentests & Abiturtraining:** [`22_Hypothesentest_Alternativtest_Einfuehrung_Theorie_Uebung_Loesung.pdf`](22_Hypothesentest_Alternativtest_Einfuehrung_Theorie_Uebung_Loesung.pdf) · [`23_Klausurtraining_Probeklausur_Lambacher_Theorie_Uebung.pdf`](23_Klausurtraining_Probeklausur_Lambacher_Theorie_Uebung.pdf) · [`24_Abituraufgaben_Baumdiagramm_Bedingte_Wahrscheinlichkeit_Loesung.pdf`](24_Abituraufgaben_Baumdiagramm_Bedingte_Wahrscheinlichkeit_Loesung.pdf) · [`25_Abituraufgaben_Stochastik_Q3_2021_2026_Loesung.pdf`](25_Abituraufgaben_Stochastik_Q3_2021_2026_Loesung.pdf)
