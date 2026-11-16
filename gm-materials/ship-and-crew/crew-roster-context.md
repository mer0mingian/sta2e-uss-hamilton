# Crew- und Offizierskontext (USS Hamilton)

**Quellen:** [`../../Player Character Data.csv`](../../Player Character Data.csv), [`../../senior_officers.html`](../../senior_officers.html), [`../../crew_manifest.html`](../../crew_manifest.html), [`../../personal_logs.html`](../../personal_logs.html), `pages/personal_logs/*`, [`../../clear-skies-source/Crew & NPC Overview - NPC Data.csv`](../../clear-skies-source/Crew & NPC Overview - NPC Data.csv).

## Datenlage im Repo
- **Dynamische Roster-Seiten:** `senior_officers.html` und `crew_manifest.html` rendern Daten aus `_data/*.json` (im Repo nicht vorhanden). Konkrete, aktuelle Besetzungslisten sind daher **nicht direkt aus dem Repo ableitbar**.
- **Verlässliche Crew-Hinweise:** `Player Character Data.csv` (Main/Support/Holo), Personal Logs (erwähnte Offiziere/Crew), NPC-CSV (Scenario „Crew“/andere).

## Senior Officers / Kernrollen (aus Quellen ableitbar)
| Rolle | Person (belegt) | Anmerkung |
|---|---|---|
| Commanding Officer | **Malax** | Main-PC, Captain |
| Chief Medical Officer | **Dr. T'Laar** | Main-PC |
| Chief of Operations / Science Officer | **Yorin Jaela** | Main-PC |
| Chief Engineer | **T'Muk** | Main-PC |
| Chief of Security | **Mendox** | Main-PC, **pausiert** (Prinzip 5) |
| First Officer / XO | **offen / SL-Option**; **Cmdr. Robert Knox** als Kandidat/Hook in Logs erwähnt | Keine eindeutige dauerhafte XO-Besetzung in CSV; Knox-Extraktion/Rückkehr in Logs dokumentiert |
| Counselor (wachsend) | **Dr. Zenn'dikaar Iral** (Support/Logs) | Entwicklung zum Counselor in Logs erwähnt |

## Erwähnte Crew-Mitglieder in Personal Logs (Auswahl, belegte Namen)
Diese Personen tauchen in Ereignissen auf und eignen sich als wiederkehrende NSCs/Offscreen-Crew:
- **Lt. Cmdr. Dr. Zenn Iral** – Counselor/Brückenoffizier (β-Schicht), Erstkontakt-/Krisenbewältigung während Vashti-Abwesenheit; medizinische/psychologische Arbeit. (Logs: dr_iral, tlaar, yorin_jaela)
- **Zhara ch'Thari** – Brücken-/Operations-Aufgaben, Notfallprotokolle (dr_iral).
- **Lt. Carter (Dr. Ethan Carter)** – Wissenschaft/Analyse, Subraumbeobachtungen (dr_iral; Support in CSV).
- **Ozyrrian 'Ozzy' th'Arilith** – Security/CPO-Kontext, Ermittlungen/Holodeck-Einsatz (dr_iral).
- **Vrok zh'Daar** – Security/Brückenkommando temporär (dr_iral).
- **Ensign Patel**, **CPO Markus Chen**, **Ensign McLaren**, **Ensign Peterson** (†) – beteiligt an Subraum-/„Wesen“-Übernahme und Torpedoraum-Vorfall (dr_iral, tlaar, yorin_jaela).
- **Ensign Katrina Johnson** – Security, Stellvertretung/Expertise (mendox Log).
- **Chief th’Arilith** – Sicherheit/Anlagensicherheit (mendox Log).
- **Lt. Vionn (Marlin Vionn)** – Science-Unterstützung (yorin_jaela Log; Support in CSV).
- **Kendraal** (Cardassianer, Crewkontext) – Konflikt/medizinisch-psychologische Nachsorge (tlaar, mendox, yorin_jaela).
- **James Hawkins** – Flight Controller (NPC-CSV „Crew“; in Logs nicht prominent, aber als Crew-NPC vorhanden).
- **Janice Randall** – Yeoman/Adjutant (NPC-CSV „Crew“).
- **Cmdr. Robert Knox** – Astrophysiker, XO-Kandidat; Extraktion von Narasa Station, Rückkehr (mendox/yorin_jaela Logs).
- **Lt. Larling** (Benzit, temporär zugeteilt) – Engineering/Sicherheitssupport, Konfliktquelle, auffällige Berichtslinien/Subraumaktivität (tlaar, yorin_jaela, tmuk Logs).
- **Weitere in Logs:** Hiren/Altor/Jarok/Vestra/Prelena (Vashti, missionsspezifisch), Grog (Händler), Admiral Blackwater, Dr. K'Vor, Prof. T'Venna (Auftraggeber/Wissenschaft, Xar'Thai), Gi'ral (klingonische Botschafterin, tmuk Log), EEH/EMH/Diplomat-Hologramme.

## Personal Logs (vorhandene Dateien)
| Datei | Figur | Fokus |
|---|---|---|
| `pages/personal_logs/dr_iral.html` | Dr. Zenn Iral | β-Schicht-Kommando, Romulaner-Kontakt im Orbit, Subraum-/Wesen-Krise, Folgen |
| `pages/personal_logs/mendox.html` | Mendox | Ankunft, Vashti, Knox-Extraktion (Narasa Station), Nachwirkungen |
| `pages/personal_logs/tlaar.html` | Dr. T'Laar | Vashti (Infektion/Heilung), Crew-Fürsorge, Larling, Vorbereitungen |
| `pages/personal_logs/tmuk.html` | T'Muk | Larling, Besuch Gi'ral |
| `pages/personal_logs/yorin_jaela.html` | Yorin Jaela | Ankunft, Vashti (RRSS), Rückkehr/Repairs, Sternenbasis, Xar'Thai-Briefing, Larling |

## Lücken
- Kein vollständiges offizielles Crew-Manifest als Daten im Repo (`_data/` fehlt).
- Exakte aktuelle Dienstposten/Abteilungen aller genannten Nebenfiguren teils nur aus Kontext/CSV ableitbar.
- Cetacean Ops officer: **Bedarf laut Prinzip 6**, im Hamilton-Material nicht namentlich belegt → neu zu definieren (siehe [../npcs/known-npcs.md](../npcs/known-npcs.md)).
