import argparse
from pathlib import Path

RENAME_MAP: dict[str, str] = {
    # 00: Übergreifendes (Themenübersicht & Formelsammlung)
    "Themen_Übersicht.png": "00_Themenuebersicht_Stochastik_Q3_Theorie.png",
    "Mathematisch-naturwissenschaftliche_Formelsammlung.pdf": "00_Formelsammlung_Abitur_Theorie.pdf",
    # 01–04: Grundbegriffe, Laplace, Mehrstufige Zufallsexperimente & Ereignisverknüpfungen
    "01_Zufallsversuch und grundlegende Begriffe _2270.pdf": "01_Grundbegriffe_Zufallsversuch_Uebung.pdf",
    "02_Laplace_0696.pdf": "02_Laplace_Wahrscheinlichkeiten_Theorie_Uebung.pdf",
    "03_Mehrstufige Zufallsexperimente_8179.pdf": "03_Mehrstufige_Zufallsexperimente_Baumdiagramm_Theorie_Uebung.pdf",
    "03_Mehrstufige Zufallsexperimente_übungsaufgaben_6652.pdf": "03_Mehrstufige_Zufallsexperimente_Uebung_Loesung.pdf",
    "03_Verknüpfung von Ereignissen _9596.pdf": "04_Verknuepfung_von_Ereignissen_Mengen_Theorie.pdf",
    "03_Mehrstufige Zufallsexperimente_mengendarstellung_3796.pdf": "04_Additionssatz_Mengendarstellung_Theorie_Uebung.pdf",
    # 05–07: Vierfeldertafel, Bedingte Wahrscheinlichkeit, Satz von Bayes & Unabhängigkeit
    "05_Übungsaufgaben Vierfeldertafel_0357.pdf": "05_Vierfeldertafel_Baumdiagramm_Uebung.pdf",
    "06_Kreuz und Quer_4931.pdf": "06_Bedingte_Wahrscheinlichkeit_Kreuz_und_Quer_Uebung.pdf",
    "07_bedingte Wahrscheinlichkeit verstehen_7889.pdf": "07_Bedingte_Wahrscheinlichkeit_Unabhaengigkeit_Uebung.pdf",
    "07_bedingte Wahrscheinlichkeit_9922.pdf": "07_Bedingte_Wahrscheinlichkeit_Bayes_Laktose_Theorie_Uebung.pdf",
    "08_Abschlussübungen_0714.pdf": "07_Baumdiagramm_Bedingte_Wahrscheinlichkeit_Abschlussuebung.pdf",
    # 08: Kombinatorik
    "Bildschirmfoto 2026-09-28 um 21.10.44.png": "08_Kombinatorik_Entscheidungsbaum_Formeln_Theorie.png",
    "Kombinatorische Abzählverfahren_0762.pdf": "08_Kombinatorische_Abzaehlverfahren_Theorie_Uebung_Loesung.pdf",
    "08_Kobinatorik_Kreuz und Quer Kopie.pdf": "08_Kombinatorik_Kreuz_und_Quer_Uebung.pdf",
    # 09–10: Zufallsgrößen, Wahrscheinlichkeitsverteilung & Erwartungswert
    "09_Wahrscheinlichkeitsverteilung.pdf": "09_Zufallsgroessen_Wahrscheinlichkeitsverteilung_Theorie_Uebung.pdf",
    "10_Erwartungswwert.pdf": "10_Erwartungswert_Zufallsgroesse_Theorie_Uebung.pdf",
    "10_Erwartungswert_lösung_8400.pdf": "10_Erwartungswert_Zufallsgroesse_Loesung.pdf",
    # 11–18: Dreimal-Mindestens, Bernoulli-Ketten & Binomialverteilung
    "11_3mindestens.pdf": "11_Dreimal_Mindestens_Aufgaben_Theorie_Uebung.pdf",
    "12_Bernoulli_Ketten_3375 (1).pdf": "12_Bernoulli_Ketten_Binomialverteilung_Theorie_Uebung.pdf",
    "Image (5).png": "13_Binomialverteilung_Robinsons_Insel_Uebung.png",
    "14_Zuordnungsaufgaben.pdf": "14_Binomialverteilung_Histogramme_Zuordnung_Uebung.pdf",
    "15_Übungsaufgaben.pdf": "15_Bernoulli_Kette_Binomialverteilung_Uebung.pdf",
    "16_Kumulierte Wahrscheinlichkeiten.pdf": "16_Kumulierte_Wahrscheinlichkeiten_Theorie_Uebung.pdf",
    "Kumulierte Wahrscheinlichkeiten.pdf": "16_Kumulierte_Wahrscheinlichkeiten_Tafelbild_Loesung.pdf",
    "16_Kumulierte Wahrscheinlichkeiten_Übung_4014.pdf": "16_Kumulierte_Wahrscheinlichkeiten_Auslastungsmodelle_Uebung.pdf",
    "17_Die Binomialverteilung in Anwendungskontexten.pdf": "17_Binomialverteilung_Anwendungskontexte_Parameter_Theorie_Uebung.pdf",
    "18_Übung.pdf": "18_Binomialverteilung_Anwendungskontexte_Uebung_Loesung.pdf",
    # 19: Varianz, Standardabweichung & Sigmaregeln
    "19_Standardabweichung_Leistungen beim Basketball_1_8798.pdf": "19_Standardabweichung_Einstieg_Basketball_Uebung.pdf",
    "19_Standardabweichung_Leistungen beim Basketball_2_2176.pdf": "19_Standardabweichung_Varianz_Sigmaregeln_Theorie_Uebung.pdf",
    # 20–21: Gaußsche Glockenkurve & Normalverteilung (Q3.2 LK)
    "Glockenkurve_Praesentation_1441.pptx": "20_Gausssche_Glockenkurve_Normalverteilung_Praesentation_Theorie.pptx",
    "Normalverteilung.pdf": "20_Normalverteilung_Glockenkurve_Einfuehrung_Theorie_Uebung.pdf",
    "21_Ergänzung NV.pptx": "21_Normalverteilung_Stetige_Zufallsgroessen_Theorie_Uebung.pptx",
    "21_Ergänzung NV_02 (2).pdf": "21_Normalverteilung_Analysis_Invertierung_Theorie_Uebung.pdf",
    "21_Ergänzung NV_03 (1).pdf": "21_Normalverteilung_Invertierung_Zusatzaufgaben_Uebung.pdf",
    # 22: Hypothesentests (Q3.3)
    "Hypothesentest Einführung Q3.pdf": "22_Hypothesentest_Alternativtest_Einfuehrung_Theorie_Uebung_Loesung.pdf",
    # 23–25: Klausurtraining & Abituraufgaben
    "Übungsmaterial_Stochastik_Lambacher.pdf": "23_Klausurtraining_Probeklausur_Lambacher_Theorie_Uebung.pdf",
    "AbiAufgaben_Baumdiagramm_bed. W.keit_0558.pdf": "24_Abituraufgaben_Baumdiagramm_Bedingte_Wahrscheinlichkeit_Loesung.pdf",
    "Aufgaben aus dem Abi Q3_Klausur1_7730.pdf": "25_Abituraufgaben_Stochastik_Q3_2021_2026_Loesung.pdf",
}


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Benennt die Dateien im Ordner Mathe Stochastik nach dem Schema XX_Thema_Typ.endung um."
    )
    parser.add_argument(
        "--apply",
        action="store_true",
        help="Führt die Umbenennung tatsächlich durch (ohne --apply läuft nur ein Dry-Run).",
    )
    args = parser.parse_args()

    root = Path(".")
    missing = []
    conflicts = []

    for old_name, new_name in RENAME_MAP.items():
        old_path = root / old_name
        new_path = root / new_name
        if not old_path.exists():
            missing.append(old_name)
        if new_path.exists() and old_path.resolve() != new_path.resolve():
            conflicts.append(new_name)

    if len(set(RENAME_MAP.values())) != len(RENAME_MAP):
        raise ValueError("Doppelte Ziel-Dateinamen in RENAME_MAP gefunden!")

    print(f"Geprüfte Dateien: {len(RENAME_MAP)}")
    if missing:
        print(f"WARNUNG - Nicht gefundene Quelldateien ({len(missing)}): {missing}")
    if conflicts:
        print(f"WARNUNG - Bereits existierende Zieldateien ({len(conflicts)}): {conflicts}")

    for old_name, new_name in RENAME_MAP.items():
        old_path = root / old_name
        new_path = root / new_name
        if args.apply:
            if old_path.exists():
                old_path.rename(new_path)
                print(f"[UMBENANNT] {old_name} -> {new_name}")
        else:
            print(f"[DRY-RUN]   {old_name} -> {new_name}")

    if not args.apply:
        print("\nHinweis: Dies war ein Dry-Run. Zum tatsächlichen Umbenennen '--apply' übergeben.")


if __name__ == "__main__":
    main()
