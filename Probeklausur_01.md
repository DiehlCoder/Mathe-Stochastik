# Probeklausur 01 – Mathematik Leistungskurs (Q3 Stochastik)
**Orientiert am Landesabitur Hessen 2027 (KCGO)**

* **Gesamtbearbeitungszeit:** ca. 135 Minuten (Teil A: ca. 45 Min. | Teil B: ca. 90 Min.)
* **Gesamtpunktzahl:** **60 BE** (Teil A: 20 BE | Teil B: 40 BE)
* **Wichtiger Hinweis:** Bearbeite zuerst **Teil A** vollständig *ohne* Taschenrechner und *ohne* Formelsammlung. Erst danach darfst du für **Teil B** deinen WTR/CAS und die offizielle IQB-Formelsammlung (`00_Formelsammlung_Abitur_Theorie.pdf`) verwenden. Achte auf eine saubere Dokumentation aller Rechenschritte und Antwortsätze entsprechend der hessischen Operatoren.

---

## Teil A – Hilfsmittelfreier Teil (20 BE)

> **Erlaubte Hilfsmittel:** Keine (weder Taschenrechner noch Formelsammlung).

### Aufgabe A1: Würfelspiel & Erwartungswert (5 BE)

Bei einem Schulfest wird ein Glücksspiel angeboten: Ein fairer sechsseitiger Würfel (Augenzahlen $1$ bis $6$) wird zweimal hintereinander geworfen. Der Einsatz pro Spiel beträgt $2{,}00\,\text{€}$.
* Zeigen **beide** Würfe eine $6$, erhält der Spieler eine Auszahlung von $x\,\text{€}$.
* Zeigt **genau ein** Wurf eine $6$, erhält der Spieler eine Auszahlung von $3{,}00\,\text{€}$.
* Fällt **keine** $6$, erfolgt keine Auszahlung.

1.1 Begründen Sie, dass die Wahrscheinlichkeit, bei einem Spiel keine $6$ zu werfen, $\frac{25}{36}$ beträgt. *(2 BE)*

1.2 Die Zufallsgröße $G$ beschreibt den Reingewinn des Spielers (Auszahlung minus Einsatz) in Euro.
Geben Sie die Wahrscheinlichkeitsverteilung von $G$ in einer Tabelle an und berechnen Sie den Wert für $x$, sodass das Spiel fair ist. *(3 BE)*

---

### Aufgabe A2: Mediennutzung in der Oberstufe (6 BE)

An einem Gymnasium wurden die Schülerinnen und Schüler der Oberstufe befragt, ob sie regelmäßig Nachrichten über soziale Medien konsumieren ($N$) und ob sie zusätzlich eine Tageszeitung lesen ($Z$).
Dabei gaben $80\,\%$ der Befragten an, regelmäßig Nachrichten über soziale Medien zu konsumieren. $15\,\%$ aller Befragten nutzen soziale Medien für Nachrichten **und** lesen eine Tageszeitung. Von den Personen, die *keine* Nachrichten über soziale Medien konsumieren, lesen $50\,\%$ eine Tageszeitung.

2.1 Stellen Sie den Sachverhalt in einer vollständig ausgefüllten Vierfeldertafel dar. *(2 BE)*

2.2 Bestimmen Sie die Wahrscheinlichkeit dafür, dass eine zufällig ausgewählte Person, die eine Tageszeitung liest, regelmäßig Nachrichten über soziale Medien konsumiert. *(2 BE)*

2.3 Untersuchen Sie die Ereignisse $N$ und $Z$ auf stochastische Unabhängigkeit. *(2 BE)*

---

### Aufgabe A3: Kombinatorik & Bernoulli-Terme (5 BE)

3.1 Für ein digitales Schließfach muss ein 4-stelliger Zahlencode aus den Ziffern $0$ bis $9$ festgelegt werden.
* Berechnen Sie, wie viele verschiedene Codes möglich sind, wenn jede Ziffer höchstens einmal vorkommen darf. *(1 BE)*
* Geben Sie einen Term an, mit dem die Anzahl der möglichen Codes berechnet werden kann, wenn Ziffern mehrfach vorkommen dürfen und der Code zusätzlich auf eine ungerade Ziffer enden muss. *(1 BE)*

3.2 Ein Laplace-Würfel wird $5$-mal geworfen. Betrachten Sie die folgenden Terme:
* Term I: $\binom{5}{2} \cdot \left(\frac{1}{6}\right)^2 \cdot \left(\frac{5}{6}\right)^3$
* Term II: $1 - \left(\frac{5}{6}\right)^5 - 5 \cdot \frac{1}{6} \cdot \left(\frac{5}{6}\right)^4$

Formulieren Sie jeweils ein passendes Ereignis im Sachkontext, dessen Wahrscheinlichkeit durch Term I bzw. Term II beschrieben wird, und begründen Sie kurz Ihren Ansatz für Term II. *(3 BE)*

---

### Aufgabe A4: Normalverteilung ohne Hilfsmittel (4 BE)

Die Füllmenge $X$ (in $\text{ml}$) von Kaffeebechern eines Getränkeautomaten wird als normalverteilt mit dem Erwartungswert $\mu = 200\,\text{ml}$ und der Standardabweichung $\sigma = 5\,\text{ml}$ angenommen.

4.1 Geben Sie die $x$-Koordinate des Hochpunkts sowie die $x$-Koordinaten der beiden Wendepunkte des Graphen der zugehörigen Dichtefunktion $\varphi_{\mu,\sigma}$ an. Begründen Sie zudem kurz, warum $P(X = 200) = 0$ gilt. *(2 BE)*

4.2 Für eine normalverteilte Zufallsgröße gilt bekanntlich $P(\mu - \sigma \le X \le \mu + \sigma) \approx 68{,}3\,\%$ und $P(\mu - 2\sigma \le X \le \mu + 2\sigma) \approx 95{,}4\,\%$.
Bestimmen Sie mithilfe dieser Angaben näherungsweise die Wahrscheinlichkeit $P(X \ge 205)$. *(2 BE)*

---

## Teil B – Teil mit Hilfsmitteln (40 BE)

> **Erlaubte Hilfsmittel:** WTR/CAS und die offizielle IQB-Formelsammlung (`00_Formelsammlung_Abitur_Theorie.pdf`).
> **Hinweis:** Dokumentieren Sie bei allen WTR-Berechnungen den mathematischen Ansatz, die verwendeten Parameter und ggf. zwei benachbarte Vergleichswerte.

### Aufgabe B1: Medizinisches Screening (11 BE)

Bei einer Vorsorgeuntersuchung wird ein Schnelltest zur Erkennung einer Stoffwechselerkrankung eingesetzt. Aus langjährigen Studien ist bekannt, dass $4\,\%$ der getesteten Personen tatsächlich an dieser Erkrankung leiden ($K$). Bei erkrankten Personen fällt der Test mit einer Wahrscheinlichkeit von $95\,\%$ positiv ($T$) aus. Bei gesunden Personen ($\bar{K}$) liefert der Test in $8\,\%$ der Fälle fälschlicherweise ein positives Ergebnis.

1.1 Stellen Sie den Sachverhalt in einem vollständig beschrifteten Baumdiagramm dar. *(3 BE)*

1.2 Berechnen Sie die Wahrscheinlichkeit dafür, dass eine zufällig ausgewählte Person ein positives Testergebnis erhält. *(2 BE)*

1.3 Eine Person erhält ein positives Testergebnis. Bestimmen Sie die Wahrscheinlichkeit dafür, dass diese Person tatsächlich erkrankt ist, und bewerten Sie die Aussagekraft des positiven Testergebnisses im Sachzusammenhang. *(3 BE)*

1.4 Untersuchen Sie, ob die Ereignisse $K$ und $T$ stochastisch unabhängig sind, und deuten Sie Ihr Ergebnis im Sachkontext. *(3 BE)*

---

### Aufgabe B2: Online-Versandhandel & Binomialverteilung (12 BE)

Ein großer Online-Händler weiß aus Erfahrung, dass $12\,\%$ aller bestellten Kleidungsstücke wegen falscher Größe retourniert werden. An einem Tag werden $n = 150$ Bestellungen unabhängig voneinander betrachtet. Die Zufallsgröße $X$ beschreibt die Anzahl der retournierten Kleidungsstücke.

2.1 Begründen Sie, warum die Zufallsgröße $X$ näherungsweise als binomialverteilt modelliert werden kann. *(2 BE)*

2.2 Berechnen Sie die Wahrscheinlichkeit dafür, dass von den $150$ Bestellungen
* (a) genau $18$ Kleidungsstücke retourniert werden,
* (b) mindestens $25$ Kleidungsstücke retourniert werden,
* (c) mehr als $12$, aber höchstens $20$ Kleidungsstücke retourniert werden. *(4 BE)*

2.3 Wie viele Bestellungen müsste der Händler mindestens betrachten, damit mit einer Wahrscheinlichkeit von mindestens $99\,\%$ mindestens ein Kleidungsstück retourniert wird? Berechnen Sie die Mindestanzahl. *(3 BE)*

2.4 Für eine Sonderaktion werden $80$ Pakete gepackt. Die Retourenabteilung möchte für die Prüfung der Rücksendungen eine feste Kapazität an Prüfplätzen vorhalten. Bestimmen Sie, wie viele Prüfplätze mindestens eingeplant werden müssen, damit die Kapazität für die erwarteten Retouren aus diesen $80$ Paketen mit einer Wahrscheinlichkeit von mindestens $95\,\%$ ausreicht. *(3 BE)*

---

### Aufgabe B3: Qualitätskontrolle & Normalverteilung (8 BE)

Eine Rösterei füllt Kaffeebohnen maschinell in Packungen ab. Das tatsächliche Abfüllgewicht $Y$ (in $\text{g}$) ist normalverteilt mit $\mu = 500\,\text{g}$ und $\sigma = 6\,\text{g}$.

3.1 Berechnen Sie die Wahrscheinlichkeit dafür, dass eine zufällig ausgewählte Packung zwischen $492\,\text{g}$ und $509\,\text{g}$ wiegt. *(2 BE)*

3.2 Bestimmen Sie:
* (a) ein symmetrisches Intervall um den Erwartungswert $\mu$, in dem die Gewichte von $90\,\%$ aller Packungen liegen,
* (b) das Mindestgewicht, das von den schwersten $5\,\%$ aller Packungen erreicht bzw. überschritten wird. *(3 BE)*

3.3 Um Reklamationen zu vermeiden, soll der Sollwert $\mu$ an der Abfüllmaschine bei unveränderter Standardabweichung $\sigma = 6\,\text{g}$ so nachjustiert werden, dass höchstens $1\,\%$ aller Packungen weniger als $500\,\text{g}$ wiegen. Bestimmen Sie den neu einzustellenden Erwartungswert $\mu_{\text{neu}}$. *(3 BE)*

---

### Aufgabe B4: Hypothesentest in der Produktion (9 BE)

Der Hersteller der Abfüllanlage aus Aufgabe B3 behauptet, dass durch ein neues Wartungsverfahren der Anteil von Packungen mit zu starker Abweichung (Ausschuss) von bisher $p_0 = 0{,}15$ **gesunken** sei. Um diese Behauptung zu überprüfen, wird eine Stichprobe von $n = 100$ Packungen entnommen und die Anzahl $Z$ der Ausschuss-Packungen gezählt. Der Test soll auf einem Signifikanzniveau von $\alpha = 5\,\%$ durchgeführt werden.

4.1 Formulieren Sie die Nullhypothese $H_0$ und die Gegenhypothese $H_1$ und begründen Sie Ihre Wahl. *(2 BE)*

4.2 Bestimmen Sie für den Test eine Entscheidungsregel auf dem Signifikanzniveau $\alpha = 5\,\%$. *(4 BE)*

4.3 Erläutern Sie die Bedeutung eines Fehlers 1. Art und eines Fehlers 2. Art im Sachzusammenhang. Berechnen Sie zudem die Wahrscheinlichkeit für einen Fehler 2. Art für den Fall, dass der tatsächliche Ausschussanteil tatsächlich auf $p_1 = 0{,}08$ gesunken ist. *(3 BE)*
