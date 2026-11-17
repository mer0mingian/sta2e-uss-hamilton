# Regel-Bausteine: „Wehen unter Jateran“

**Status:** Arbeitsfassung (regelbasierte GM-Hilfen).  
**Zweck:** Praktische, regelkonforme Bausteine für Tasks, Extended Tasks, Komplikationen und NSC-Kontakte.  
**Hinweis:** Keine Scientific-Method-Erweiterungsregeln verwendet. Annahmen sind als *Annahme* markiert.

---

## 1) Regelanker (Kurzreferenz)

| Thema | Kernregel | Referenz |
|---|---|---|
| Task-Grundablauf | SL setzt **Difficulty (0–5)**. Spielende wählen **Attribute + Department = Target Number (TN)**, würfeln normalerweise **2d20** (bis 5d20). Jeder Wurf ≤ TN = 1 Erfolg; mit passendem **Focus** zählt jedes Ergebnis ≤ Department als 2 Erfolge (kritisch), ohne Focus nur natürliche 1 als kritisch. Erfolge ≥ Difficulty = Erfolg; Überschuss = **Momentum**. | `clear-skies-source/reference/sta2e-rules-core.md` §3; `docs/game_mechanics/sta2e_rules/sta2ecore_ch07.md` (Tasks, Attempting a Task) |
| Komplikationen | Natürliche 20 = Komplikation (Range kann steigen). Komplikation kann ggf. durch **+2 Threat** abgekauft werden; Auflösung nach Task-Ergebnis. | `sta2ecore_ch07.md` (Complications); `sta2e-rules-core.md` Quick Reference |
| Schwierigkeit 0 / wann würfeln | Difficulty 0 = automatisch erfolgreich ohne Momentum/Risiko, außer Gruppe will bewusst würfeln (Chance auf Momentum/Komplikationen). Nicht würfeln, wenn Ergebnis narrativ klar, risikoarm und ohne interessanten Zeit-/Informationsdruck ist. | `sta2ecore_ch07.md` (Difficulty Zero tasks); `sta2e-rules-core.md` §3 |
| Assistance | Erste Assistenz kostenfrei; weitere kosten je 1 Momentum oder +1 Threat. Assistenz zählt nur, wenn Leitung ≥1 Erfolg erzielt. | `sta2ecore_ch07.md` (Teamwork And Assistance); `sta2e-rules-core.md` §3 |
| Momentum | Gruppenpool, **max 6**, missionsbezogen; am Szenenende ggf. −1. Relevante Ausgaben u. a. Bonuswürfel (1/2/3, Immediate), **Create Trait (2)**, **Obtain Information (1, Repeatable)**, **Extra Minor Action (1)**, **Swift/Extra Major Action (2, +1 Difficulty)**, **Keep the Initiative (2, Immediate)**. | `sta2ecore_ch07.md` (Momentum); `data_tables/momentum_spends.csv`; `sta2e-rules-core.md` §4 |
| Threat | SL-Ressource (Start typ. 2 pro SC/Abenteuer). Gewinne u. a. durch Immediate-Momentum-als-Threat, Komplikations-Abkauf (+2), Eskalation (+1), NPC-Überschusserfolge. Ausgaben u. a. NPC-Momentum-Äquivalente, Komplikationen erzeugen/abkaufen, Verstärkung, Umwelt-/Narrativeffekte. | `sta2ecore_ch07.md` (Threat); `data_tables/threat_spends.csv`; `sta2e-rules-core.md` §5 |
| Traits | Beschreiben relevante Fakten (Situation/Ort/Charakter/Ausrüstung), ändern oft Schwierigkeit/Möglichkeiten; bestehen, solange wahr. Potency zählt als mehrere Traits. | `sta2ecore_ch07.md` (Scenes and Traits); `sta2e-rules-core.md` §2 |
| Extended Tasks | Mehrere Task-Versuche gegen Fortschrittsziel bei Zeitdruck/Risiko/Komplexität; Widerstand/Impact/Breakthroughs möglich, auch unter Zeitdruck. Nicht für triviale Aktionen ohne Konsequenz. | `sta2e-rules-core.md` §10; `sta2ecore_ch09.md` (Extended Tasks and Challenges, ab ca. Zeile 951 ff.) |
| NPC-Kategorien | **Minor:** kein Stress wie SC, durch erfolgreichen Angriff sofort besiegt, keine Focuses/Values. **Notable:** typ. **Personal Threat 3**, kann Verletzung **1×/Szene** durch Threat vermeiden, wenige Focuses/1 Value. **Major:** größerer Personal Threat, umfangreicher. | `sta2ecore_ch11.md` (NPC Categories, Personal Threat/Values, Creating an NPC); `sta2e-rules-core.md` §9 |

---

## 2) Task-Vorschläge für Szenen 1–6

> **Format:** plausible **Attribute + Department**, **Difficulty (D)**, optionale **Focus**, **würfeln vs. nicht würfeln**, passende **Traits** (bestehend/erzeugbar).  
> *Annahme:* Departments entsprechen den 2e-Kernbezeichnungen **Command, Conn, Engineering, Medicine, Science, Security**.

### Szene 1 — Knox-Log (Einstieg)
- **Würfeln:** in der Regel **nein** (reine Exposition/Informationsübergabe).
- **Optionale Mikro-Interaktion (nur bei aktivem Spielwunsch):**
  - *Befehlskontext einordnen:* **Insight + Command**, D0–1, Focus *Starfleet Protocol* / *Composure* — liefert Tonlage/Dringlichkeit, kein Plot-Gate.
- **Traits:** `Geheime Kurzübertragung (Vozrax)`, `Tholianische Übersetzungsmatrix (T’Laar)`, `Distanzierter Logbucheintrag`.

### Szene 2 — Babyparty & Reise (Charakterspiel)
- **Würfeln:** meist **nein**; sozialer Spielraum steht im Vordergrund. Würfeln nur bei klarer Unsicherheit, Zeitdruck oder gewünschtem Nebeneffekt.
- **Optionale Tasks:**
  - *Stimmung halten / Ritual würdig rahmen:* **Presence + Command**, D1, Focus *Diplomacy* / *Etiquette* (*Annahme: Fokusname am Tisch*). Erfolg = Szene gewinnt verbindenden Ton; Momentum → **Obtain Information** (kleine persönliche Einsicht) oder **Create Trait** `Gestärkte Crewbindung`.
  - *Technische/medizinische Sorgen dezent klären (Gi’ral/Wehen-Teaser):* **Reason + Medicine**, D1, Focus *Prenatal Care* / *Xenobiology* (*Annahme*). Nur würfeln, wenn Fehleinschätzung interessant wäre.
  - *Beobachtung im Arboretum (Maren/Gi’ral, sensibel):* **Insight + Science** oder **Insight + Security**, D0–1, Focus *Empathy* / *Observation* (*Annahme*). Meist D0/kein Wurf; bei Wurf nur für Nuancen.
- **Traits:** `Feierliche Babyparty`, `Klingonisches Ritual der Verbundenheit`, `Cetacean-Becken / Arboretum`, `Unruhige Vorahnung`.

### Szene 3 — Ankunft, Pulse & Hypothesen
- **Würfeln:** **ja**, sobald Datenlage unscharf, Zeitfenster relevant oder Fehldeutung Konsequenzen hat.
- **Task-Vorschläge:**
  - *Puls C1/C2 analysieren & Ursprung eingrenzen:* **Reason + Science**, D2 (C1 unklar) → D2–3 (C2 mit besseren Daten), Focus *Astrophysics*, *Subspace Theory*, *Sensor Analysis* (*Annahme*). Erfolg: Muster/Intervall/Hemisphäre präziser; Momentum → **Obtain Information** oder **Create Trait** `Lokalisierter Pulsursprung`.
  - *Geologische/strukturelle Spannungsmuster lesen:* **Reason + Engineering** oder **Reason + Science**, D2, Focus *Geology* / *Structural Analysis* (*Annahme*). Nutzt Hinweise (lineare Zonen, Dilithium-Spuren).
  - *Flug- und Annäherungsdaten stabil halten:* **Control + Conn**, D1–2, Focus *Helm Operations* / *Stellar Navigation*. Nicht würfeln bei Routineflug ohne Störung.
  - *Koloniegespräch (Bebenlage, Evakuierungsdruck, Kooperationsbereitschaft):* **Presence + Command** oder **Presence + Security**, D1–2, Focus *Diplomacy*, *Crisis Management* (*Annahme*). Erfolg: verlässliche Lageinfos/Zugeständnisse; Komplikation: Panik, Misstrauen, unvollständige Angaben.
  - *Risikoeinschätzung „kohlenstoffbasierte Oberfläche als Ziel“:* **Insight + Medicine** oder **Reason + Science**, D2, Focus *Xenobiology* / *Exobiology* (*Annahme*). Ergebnis bereitet Ködersignal-Planung vor.
- **Traits (nutzen/erzeugen):** `Verkürzende Pulsintervalle`, `Synchrone Seismik`, `Verödete Hemisphäre`, `Ruhende Minen`, `Gefährdete Kolonie`, `Unvollständige Sensordaten` (erschwert ggf. +1).

### Szene 4 — Entdeckung & T’Laru (Kontakt auf Abstand)
- **Würfeln:** selektiv — bei taktischer Einschätzung, Kontaktführung mit Risiko oder Deutung knapper Signale.
- **Task-Vorschläge:**
  - *T’Laru lesen (Haltung, Bedrohungsschwelle, Distanzverhalten):* **Insight + Security** oder **Reason + Conn**, D2, Focus *Tactics* / *Threat Assessment* / *Sensor Operations* (*Annahme*). Erfolg: klarere Einschätzung ohne Offenlegung von GM-Geheimwissen.
  - *Kommunikation unter Druck (deeskalierend, aber bestimmt):* **Presence + Command**, D2–3 (je nach Provokation), Focus *Diplomacy*, *Composure*. *Annahme:* knappe, ritualisierte Antworten erhöhen Reibung → ggf. D3.
  - *Übersetzung/Nuancen prüfen (T’Laar/Sprachmatrix im Hintergrund):* **Reason + Science** oder **Insight + Command**, D1–2, Focus *Linguistics* / *Xenolinguistics* (*Annahme*). Nicht würfeln, wenn nur bereits bekannte Kernbotschaft wiederholt wird.
  - *Taktische Bereitschaft ohne Eskalation zeigen:* **Control + Security** oder **Daring + Conn**, D2, Focus *Starship Tactics* / *Shield Modulation* (*Annahme*). Erfolg: glaubhafte Schutzfähigkeit als Trait `Kontrollierte Gefechtsbereitschaft`.
- **Traits:** `T’Laru auf Abstand`, `Drohend-prüfender Kontakt`, `Beobachtete Schwelle`, `Zeitfenster schließt sich` (ab T-2h), `Empfindliche Erstkontaktsituation`.

### Szene 5 — Parallel: Nursery, Kaiserschnitt, Ködersignal, Eskalation
- **Würfeln:** **ja** (Kernszene mit Zeitdruck, Parallelaufgaben, Extended Tasks).
- **Extended Tasks:** siehe Abschnitt 3.
- **Unterstützende Einzel-Tasks (neben/zwischen Extended-Task-Versuchen):**
  - *Ködersignal justieren / Resonanzfenster treffen:* **Control + Engineering** oder **Reason + Science**, D2–3, Focus *Signal Processing* / *Subspace Communications* (*Annahme*). Kann als Beitrag/Assist zum passenden Versuch dienen.
  - *Kolonie beruhigen & Evakuierungsdisziplin halten:* **Presence + Command**, D2, Focus *Crisis Management*.
  - *Eskalation entschärfen (T’Laru-Reaktion managen):* **Presence + Command** oder **Control + Conn**, D2–3, Focus *Diplomacy* / *Composure* / *Helm Control*.
  - *Schadensbegrenzung bei Resonanzspitzen:* **Daring + Engineering**, D2, Focus *Damage Control* / *Emergency Repairs* (*Annahme*).
- **Traits:** `Parallele Einsatzlagen`, `Resonanzkopplung steigt (T-60m)`, `Geburtsfenster T-0`, `Kolonie im Risikokorridor`, `Tholianische Beobachtung`, erzeugbar z. B. `Stabiler Resonanzköder`, `Temporärer Sicherheitskorridor`.

### Szene 6 — Rettung, Nursery, Nachhall
- **Würfeln:** **situativ** — bei riskanter Führung/Transit, letzter Stabilisierung oder sensiblem Abschlusskontakt.
- **Task-Vorschläge:**
  - *Entität/Nursery-Anflug feinführen:* **Control + Conn**, D1–2, Focus *Helm Operations* / *Precision Flying*. Kein Wurf, wenn Extended Tasks sauber abgeschlossen und kein neuer Druck entsteht.
  - *Letzte Resonanz-/Strukturstabilisierung:* **Control + Engineering** oder **Reason + Science**, D2, Focus *Power Systems* / *Field Dynamics* (*Annahme*).
  - *Abschließender Kontakt mit T’Laru (Anerkennung ohne Bündnis):* **Presence + Command**, D1–2, Focus *Diplomacy* / *Composure*. Erfolg formt Ton (`Respektierte Durchführung`), Misserfolg nur knappe/kalte Reaktion.
  - *Sensorische Einordnung der Nursery (harmonische Antwort):* **Reason + Science**, D0–1, Focus *Sensor Analysis* / *Xenobotany* (*Annahme*). Eher Erkenntnisgewinn als Hindernis.
- **Traits:** `Harmonische Resonanzantwort (Nursery)`, `Kontrollierter Austritt`, `Offene Fragen zu Herkunft und Ritus`.

---

## 3) Extended-Task-Feinschliff

> **Grundlage aus Leitfaden (fixe Parameter):**  
> - **„Eine Wiege finden“:** Progress Track **12**, Difficulty **3**, Resistance **2**, Breakthroughs bei **6** und **9**.  
> - **„Kaiserschnitt“:** Progress Track **14**, Difficulty **4**, Resistance **2**, Breakthroughs bei **7** und **11**.  
> *Annahme (regelkonform, nicht im Wortlaut der Quellen belegt):* **Impact** pro erfolgreichem Versuch = erzielte Erfolge abzüglich Resistance (Minimum 1), sofern keine besonderen Effekte eingreifen; Breakthroughs bei Erreichen/Überschreiten der Schwellen anwenden. Zeitdruck über **Intervalle** gemäß Countdown.

### 3.1 „Eine Wiege finden“ (Nursery lokalisieren)

**Ziel:** unbewohnte, flora-dominante Class-L-Welt als passende „Wiege“ finden und stabilen Anflugkorridor ableiten.

**Beispielansätze pro Versuch (abwechselnd kombinierbar):**
1. **Grobraum-Scan & Resonanzvergleich:** **Reason + Science** (Focus *Astrophysics*, *Sensor Analysis*) — filtert Kandidatenwelten gegen Puls-/Resonanzsignatur.
2. **Kurs- und Fensterberechnung:** **Control + Conn** (Focus *Stellar Cartography*, *Helm Operations*, *Annahme*) — übersetzt Treffer in erreichbaren Kurs im Zeitfenster.
3. **Biosignatur-/Ausschlussprüfung:** **Reason + Science** oder **Insight + Medicine** (Focus *Xenobiology*, *Exobiology*) — prüft „kein intelligentes Leben / möglichst unbewohnt“.
4. **Schiffsassistierte Datenfusion:** Assistenz durch **Reason + Engineering** / **Control + Conn** bzw. Schiffssysteme (*Annahme: ship-assisted wie im Leitfaden*) — bündelt Sensorik, Navigation, Energieprofil.

**Breakthrough-Vorschläge (bei 6 und 9):**
- **Breakthrough 6 (Eingrenzung/Resonanz):** SL wählt 1 Effekt passend zur Lage, z. B. **Resistance −1** für Folgeversuche *oder* **Difficulty −1** für den nächsten Suchversuch, plus Trait `Eingegrenzter Resonanzkorridor`.
- **Breakthrough 9 (stabiler Kurs, Herkunft mysteriös):** Trait `Stabiler Nursery-Kurs` etablieren; nächster Versuch erhält narrativen Vorteil (z. B. klarer Fokus/geringere Unsicherheit). Herkunft/Ursache bleibt bewusst offen.

### 3.2 „Kaiserschnitt“ (kontrollierter Austritt)

**Ziel:** Austritt der Entität ermöglichen, ohne Planetenzerstörung und mit beherrschbarer Resonanzlage.

**Beispielansätze pro Versuch (abwechselnd kombinierbar):**
1. **Strukturelle Entlastung/Spannungsumleitung:** **Control + Engineering** (Focus *Structural Engineering*, *Power Systems*) — stabilisiert lokale Kruste/Energiepfade.
2. **Resonanzfenster modellieren:** **Reason + Science** (Focus *Subspace Theory*, *Geophysics*, *Annahme*) — bestimmt sicheren Zeitpunkt/Impulsrahmen.
3. **Präziser Eingriff unter Druck:** **Daring + Engineering** (Focus *Emergency Repairs*, *Damage Control*) — riskanter Eingriff bei knapper Phase; gut für dramatische Würfe.
4. **Medizinisch/xenologische Schonung (Sicherheitsparameter):** **Reason + Medicine** oder **Insight + Science** (Focus *Xenobiology*) — minimiert Kollateralschäden am „Geburtsprozess“ (*Annahme: beratender Beitrag/Assist*).

**Breakthrough-Vorschläge (bei 7 und 11):**
- **Breakthrough 7 (lokale Stabilisierung):** **Resistance −1** *oder* Erstellung/Verstärkung eines Traits wie `Lokalisierte Stabilitätszone`; reduziert Folgekomplikationen im betroffenen Sektor.
- **Breakthrough 11 (kontrollierbares Fenster):** Trait `Kontrollierbares Austrittsfenster` aktiv; Abschlussversuche werden klar fokussiert (SL kann Difficulty für letzten, sauber vorbereiteten Schritt situativ nicht weiter erhöhen, sofern narrativ gedeckt).

### 3.3 Zeitdruck / Intervalle (kompatibel mit Countdown)

| Countdown-Marker | Zeitlage | Intervall-Idee (praktisch) | SL-Nutzung |
|---|---:|---|---|
| **C2 / T-8h** | 78600.51 | Längere Intervalle (z. B. 30–45 min narrativ pro „Runde“ Planung + 1 Schwerpunktversuch) | Vorbereitung, Parallelisierung etablieren |
| **T-4h** | Mitte | Mittlere Intervalle (z. B. 20–30 min) | Druck steigt, Nebenaufgaben kosten spürbar Zeit |
| **C3 / T-2h** | 78600.76 | Kurze Intervalle (z. B. 10–20 min) | T’Laru präsent; Kontakt- oder Ködersignal-Entscheidungen binden Kapazität |
| **T-60m** | vor T-0 | Sehr kurze Intervalle (z. B. 5–10 min) | Jede Verzögerung/Komplikation verschärft Lage; klare Priorisierung |
| **T-0** | 78600.84 | Finales Intervall / letzter Versuch(sblock) | Fenster schließt sich; Erfolg/Teilerfolg/Preis ausspielen |

*Annahme:* Intervalldauer ist ein SL-Taktmittel (kein fester Regelwert im gelesenen Auszug); konsistent und transparent handhaben. **Momentum/Threat** können bei Zeitdruck regelkonform narrativ eingesetzt werden (z. B. Momentum für Effizienz/Koordination, Threat für zusätzliche Erschwernis oder Zeitverlust als Konsequenz) — siehe auch `data_tables/momentum_spends.csv` „Reduce Time“.

### 3.4 Relevante Momentum-/Threat-Nutzungen für Extended Tasks

- **Momentum:**
  - **Create Opportunity (1/2/3, Immediate):** zusätzliche Würfel in kritischen Versuchen (Kap max. 5d20).
  - **Obtain Information (1, Repeatable):** präzise Rückmeldung zu Resonanz, Kursfenster, Risiko („Was blockiert den nächsten Fortschritt am stärksten?“).
  - **Create Trait (2):** z. B. `Kalibrierter Köderimpuls`, `Stabilisierte Krustennaht`, `Synchronisierte Brückenteams`.
  - **Reduce Time (2):** wenn ein Teilschritt erzählerisch beschleunigt werden soll (*Annahme: Einsatz nur, wo sinnvoll, nicht als Automatismus pro Versuch*).
- **Threat:**
  - **Complication (2) / Narrative/Environmental Changes:** Resonanzspitzen, falsche Priorisierung, Kommunikationsrauschen, kurzfristige Systemüberlastung.
  - **Adversary/NPC-Momentum-Äquivalente:** *Annahme:* für T’Laru-Druckmomente (Warnmanöver, stärkere Präsenzsignale) regelkonform als SL-Ressourceneinsatz, ohne automatisch offenen Kampf auszulösen.

---

## 4) Ködersignal als konkrete Task-/Challenge-Optionen

> Ziel: Entität vom besiedelten Bereich weglenken (Resonanz-/Energie-/Stoffspur), glaubwürdig zur Spielsituation.  
> *Annahme:* Parameter D2–3 wie im Leitfaden vorgeschlagen; SL passt an Team, Vorbereitung und Traits an.

### Variante A — „Resonanz-Köder“ (Technik/Scan-Finesse)
- **Typ:** Einzel-Task oder 2-Schritt-Challenge (Kalibrieren → Ausstrahlen).
- **Ansatz:** **Control + Engineering** oder **Reason + Science**, **D3**, Focus *Subspace Communications*, *Signal Processing*, *Sensor Analysis* (*Annahme*).
- **Unterstützung:** Assistenz **Reason + Science** / **Control + Conn** sinnvoll.
- **Erfolg:** Köder koppelt an Pulsrhythmus; Trait `Glaubwürdige Resonanzspur` — Kolonie-Risiko sinkt spürbar, Extended Tasks gewinnen Spielraum.
- **Teilerfolg / Erfolg mit Preis:** Signal wirkt, aber instabil (Trait mit Potenz/Nachteil, z. B. `Flackernder Köder`), erfordert Nachjustierung im nächsten Intervall.
- **Misserfolg:** Keine wirksame Kopplung; Zeit/Intervall verstreicht, Lage bleibt angespannt.
- **Komplikation:** Resonanzspitze belastet lokale Systeme, lockt ungeplant Aufmerksamkeit (T’Laru oder Umweltreaktion), erhöht Komplikationsdruck.

### Variante B — „Materiespur / Dilithium-Lockstoff“ (physisch-chemischer Ansatz)
- **Typ:** Task mit klarer Ressourcen-/Logistikkomponente.
- **Ansatz:** **Daring + Engineering** oder **Reason + Science**, **D2–3**, Focus *Transporters*, *Warp/Power Dynamics*, *Material Science* (*Annahme*).
- **Erfolg:** Spur entlang ungefährlicher Route etabliert; Trait `Umgeleitete Nahrungs-/Energiespur`.
- **Teilerfolg:** Spur zieht an, aber Nähe zur Kolonie bleibt grenzwertig → Folge-Task nötig.
- **Misserfolg:** Spur verpufft oder ist zu schwach; evtl. Ressourcenbindung ohne Nutzen.
- **Komplikation:** Ungewollte Kopplung an Schiffssysteme/Industrieanlagen, lokale Bebenreaktion, erhöhte Umweltgefahr.

### Variante C — „Narrativer Lockruf & Koordination“ (Command/Conn-Challenge)
- **Typ:** kurzer Challenge-Block (2 Tasks): (1) Kolonie/Schiff koordinieren, (2) Signal-/Manöverfenster synchronisieren.
- **Ansätze:**  
  1. **Presence + Command**, **D2**, Focus *Crisis Management*, *Leadership* — Evakuierung/Verhalten der Kolonie synchronisieren.  
  2. **Control + Conn** oder **Control + Engineering**, **D2–3**, Focus *Flight Control*, *Operations* — Manöver/Köderausspielung im Pulsfenster timen.
- **Erfolg:** Kombinierter Trait `Koordinierter Ablenkungsplan`; reduziert Chaos, verbessert Erfolgschancen der Parallel-Tasks.
- **Teilerfolg:** Ein Teil gelingt (Information/Disziplin), Timing oder technische Umsetzung hakt.
- **Misserfolg:** Koordinationsbruch, widersprüchliche Signale/Bewegungen.
- **Komplikation:** Fehlalarm, Misstrauen bei Kolonie/Kontaktpartnern, zusätzlicher Zeitverlust im Intervall.

---

## 5) Komplikations- und Momentum/Threat-Vorschläge (szenariospezifisch)

### 5.1 Komplikationen (Beispiele, regelkonform als Traits/Folgen ausspielbar)

| Auslöser / Kontext | Komplikation (Beispiel) | Mögliche Auswirkung |
|---|---|---|
| **Pulsrhythmus verkürzt sich** | `Asynchrone Messfenster`, `Sensorrauschen im Peak` | +1 Difficulty oder erhöhte Komplikations-Range für nächsten Analyse-/Eingriffsversuch |
| **T’Laru auf Abstand, drohend** | `Provozierende Scanüberlagerung`, `Funkstille unter Druck` | Erschwerte Kommunikation/Koordination; sozial/taktisch stärkerer Druck |
| **Kolonie im Risikokorridor** | `Panik in der Siedlung`, `Unvollständige Evakuierungsdaten` | Nebenaufgabe bindet Intervall; Command/Medical-Task nötig |
| **Resonanz-/Engineering-Druck** | `Leistungsfluktuation`, `Überlastete EPS-Relais`, `Instabile Feldkopplung` | Teilfortschritt gefährdet, Trait mit negativer Wirkung, ggf. Folgeaufwand |
| **Ködersignal-Arbeiten** | `Köder driftet`, `Falsche Harmonische` | Erfolgreicher Versuch wirkt nur eingeschränkt; Risiko für Kolonie/Timing steigt |

### 5.2 Momentum-Ausgaben (passend zur Szene)

- **Obtain Information (1, Repeatable):** „Welcher Sektor reagiert als nächstes?“, „Wie groß ist das sichere Zeitfenster bis zum nächsten Puls?“, „Welche Koloniezone ist am exponiertesten?“
- **Create Trait (2):** `Synchronisierte Pulsprognose`, `Abgeschirmte Messbrücke`, `Beruhigte Koloniekanäle`, `Resonanzpuffer aktiv`.
- **Create Opportunity (1/2/3):** kritische Würfe in T-60m/T-0 oder beim finalen Durchbruch der Extended Tasks.
- **Keep the Initiative (2):** *Annahme:* in konfliktnahen, rundenbasierten Zuspitzungen (z. B. Eskalationsbeat mit T’Laru), wenn Handlungsreihenfolge narrativ/mechanisch relevant ist.
- **Extra Minor/Major Action:** schnelle Zusatzmaßnahme (Scan, Ruf, Sicherung) bei Parallelstress — Kosten/Nachteile beachten (Major: +1 Difficulty).

### 5.3 Threat-Ausgaben (SL, szenariokonsistent)

- **Complication (2) erzeugen:** punktgenaue Verschärfung (z. B. Puls kommt früher, Köder verliert Phase, Kolonie meldet neue Erschütterung).
- **Environmental/Narrative Change:** Resonanzwelle erschwert Bewegung/Kommunikation; temporärer Systemausfall; sichtbares tholianisches Macht-Signal ohne direkten Angriff.
- **NPC Momentum/Pressure:** T’Laru verstärkt Druck durch Präsenz, kurze Waffen-/Sensor-Geste oder harte ultimative Botschaft (*Annahme: im Rahmen „drohend auf Abstand“*).
- **Reinforcements (nur sparsam, falls passend):** zusätzliche tholianische Kontakte/Assets **nur** wenn Eskalationslogik es trägt; Standardfall der Episode ist Distanzdruck, kein Großgefecht (*Annahme*).

---

## 6) Kurze NSC-Stat-Hilfen für Jateran-Kontakte (Vorlagen)

> Vorlagen nach Kernkategorien aus `sta2ecore_ch11.md` (Minor/Notable). Werte sind **Startpunkte** zur schnellen Anpassung; Feintuning nach Szene/Ton empfohlen.

### 6.1 Minor-NPC-Vorlage: Jateran-Kolonist:in (Comms/Bevölkerung)

- **Kategorie:** Minor NPC  
- **Traits:** *Human/Jateran-Kolonist:in* (*Annahme: Spezies nach Bedarf*), `Zivile:r Siedler:in unter Stress`
- **Personal Threat:** 0 | **Protection:** 0  
- **Attribute (Basis, vor Speziesmodifikatoren):** Control 9, Daring 8, Fitness 8, Insight 9, Presence 9, Reason 8  
- **Departments:** Command 1, Conn 1, Engineering 1, Medicine 0, Science 1, Security 0 (*Annahme: anpassbar, z. B. mehr Engineering bei Techniker:in*)  
- **Focuses/Values:** keine (Minor-Standard)  
- **Ausrüstung (optional):** Kommunikator, lokales Datentool  
- **Einsatz:** liefert Lageberichte (Bebenrhythmus, Angst, Evakuierungsstatus), keine taktische Eigenlösung. Bei direkter Gefahr schnell handlungsunfähig (Minor-Regel).

### 6.2 Minor-NPC-Vorlage: Minenarbeiter:in / Betriebspersonal (Hintergrund)

- **Kategorie:** Minor NPC  
- **Traits:** *Spezies nach Bedarf*, `Erfahrene:r Minenarbeiter:in`, `Erschöpft durch Stillstand`
- **Attribute (Basis):** Control 8, Daring 9, Fitness 9, Insight 8, Presence 8, Reason 9  
- **Departments:** Command 0, Conn 1, Engineering 2, Medicine 0, Science 1, Security 0  
- **Personal Threat:** 0  
- **Einsatz:** praktische Hinweise zu Schächten, Ausfällen, Materialwegen; unterstützt Atmosphäre, keine Spotlight-Rolle.

### 6.3 Notable-NPC-Vorlage: Bergbauleitung Jateran (Comms/Entscheidung vor Ort)

- **Kategorie:** Notable NPC  
- **Traits:** *Spezies nach Bedarf*, `Leitung Bergbaubetrieb Jateran`, `Verantwortung für Belegschaft`
- **Value (Beispiel):** *„Meine Leute gehen lebend nach Hause.“* (*Annahme: an Tisch anpassen*)  
- **Focuses (2):** *Industrial Operations*, *Crisis Coordination* (*Annahme*)  
- **Personal Threat:** 3 | **Protection:** 0  
- **Attribute (Vorschlag):** Control 10, Daring 8, Fitness 8, Insight 9, Presence 10, Reason 9 (danach Speziesmodifikatoren)  
- **Departments (Vorschlag):** Command 3, Conn 1, Engineering 2, Medicine 1, Science 1, Security 1  
- **Ausrüstung (optional):** Betriebsdatenzugang, Kommunikationsfreigaben, Lagekarten  
- **Besondere Nutzung:** kann 1×/Szene Verletzung/Konsequenz durch Threat vermeiden (Notable-Regel); geeignet für Verhandlungen über Sperrzonen, Ressourcenfreigabe, Evakuierungstempo.

### 6.4 Notable-NPC-Vorlage: Kolonie-Sicherheits- oder Einsatzkoordinator:in

- **Kategorie:** Notable NPC  
- **Traits:** *Spezies nach Bedarf*, `Koordination ziviler Sicherheit`, `Pragmatisch unter Druck`
- **Value (Beispiel):** *„Ordnung rettet Leben, wenn Panik tötet.“* (*Annahme*)  
- **Focuses (2):** *Emergency Response*, *Crowd Control* (*Annahme*)  
- **Personal Threat:** 3 | **Protection:** 0 (oder 1 bei Schutzausrüstung, *Annahme*)  
- **Attribute (Vorschlag):** Control 9, Daring 9, Fitness 9, Insight 10, Presence 9, Reason 8  
- **Departments (Vorschlag):** Command 2, Conn 1, Engineering 1, Medicine 1, Science 1, Security 3  
- **Einsatz:** unterstützt Ködersignal-/Evakuierungspläne, liefert bodennahe Risikobilder, kann bei Fehlkoordination Konfliktquelle sein.

---

## 7) Kurze SL-Annahmen (transparent)

- *Annahme:* Konkrete Fokusnamen sind teils frei gewählt, solange sie zum Ansatz passen (Regel: Focus beeinflusst kritische Erfolge bei passender Anwendung).
- *Annahme:* Intervalldauern und exakte Impact-Handhabung pro Versuch werden vom SL szenisch konsistent festgelegt; Leitfaden-Vorgaben (Tracks/D/R/Breakpoints, Countdown) haben Vorrang.
- *Annahme:* T’Laru-Druck wird primär über Threat/Narrativ abgebildet („drohend auf Abstand“), kein standardmäßiger Raumkampf.
- *Annahme:* Jateran-NSC-Spezies/Detailwerte sind offen; Vorlagen oben sind bewusst generisch und tischfertig anpassbar.

*Ausgelassen/geändert:* Keine Scientific-Method-Erweiterung; keine neuen Canon-Fakten über Nursery-Herkunft, tholianische Theologie oder Vozrax’ Geheimwissen hinaus.  
*Risiko:* Feingranulare Extended-Task-Mathematik (exakte Impact-Modifikatoren pro Talent/Ausrüstung) hängt von Tischkonventionen ab; Breakthrough-Effekte daher als regelnahe, erprobbare Optionen formuliert.