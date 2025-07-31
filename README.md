# M&A Template System 🏢
## Automatisierte CIM-Erstellung für Tech- und Software-Mittelstandsunternehmen

Dieses System automatisiert die Erstellung von **Company Information Memoranda (CIM)** für Mergers & Acquisitions im Tech- und Software-Mittelstandssegment. Das Template nutzt KI-basierte Dokumentenanalyse und strukturierte Workflows, um professionelle, investoren-bereite CIMs zu generieren.

---

## 📋 Inhaltsverzeichnis

- [Überblick](#überblick)
- [Features](#features)
- [Projektstruktur](#projektstruktur)
- [Installation & Setup](#installation--setup)
- [Verwendung](#verwendung)
- [CIM-Erstellungsprozess](#cim-erstellungsprozess)
- [Ausgabeformate](#ausgabeformate)
- [Best Practices](#best-practices)
- [Konfiguration](#konfiguration)
- [Troubleshooting](#troubleshooting)
- [Roadmap](#roadmap)

---

## 🎯 Überblick

Das M&A Template System ist darauf spezialisiert, hochwertige Company Information Memoranda für Technologieunternehmen zu erstellen. Es kombiniert:

- **Automatisierte Dokumentenkonvertierung** mit LlamaParse API
- **KI-gestützte Content-Analyse** und -Strukturierung  
- **Branchenspezifische CIM-Templates** für Tech-/Software-Unternehmen
- **Multi-Language-Support** (Deutsch/Englisch)
- **Qualitätssicherung** durch automatische Fact-Checking

### Zielgruppe
- M&A-Berater und Investment-Banken
- Corporate Development Teams
- Private Equity / Venture Capital Funds
- Technologieunternehmen beim Exit-Prozess

---

## ✨ Features

### 🔄 Intelligente Dokumentenverarbeitung
- **Multi-Format-Support**: PDF, Word, PowerPoint, Excel, Bilder, Audio (20+ Dateiformate)
- **Premium-Parsing**: Erweiterte Analyse für komplexe Layouts (Dateien mit "DIFFICULT" Präfix)
- **Struktur-Erhaltung**: Beibehaltung der ursprünglichen Ordnerstruktur
- **Smart-Processing**: Automatisches Überspringen bereits konvertierter Dateien

### 📊 CIM-Generierung
- **Branchenspezifische Templates**: Optimiert für Tech-/Software-Unternehmen  
- **Umsatzbasierte Anpassung**: 
  - < 5 Mio. € → Fokus auf Tech/IP, Make-or-Buy-Argumente
  - ≥ 5 Mio. € → PE-orientiert, Finanzkennzahlen im Vordergrund
- **Strategische Käufer-Personas**: Automatische Identifikation potentieller Acquirer
- **Growth-Story-Szenarien**: 2-3 konkrete Wachstumspfade

### 🎨 Output-Optimierung
- **Multi-Format-Export**: Markdown + HTML mit interaktiven Charts
- **Professionelles Layout**: DTP-ready mit Platzhalter-Grafiken
- **Mehrsprachiger Output**: Identische Struktur für DE/EN
- **Qualitätssicherung**: Automatisches Fact-Checking und Fragenkatalog

---

## 📁 Projektstruktur

```
m-a-template/
├── 📂 code/                           # Kernfunktionalität
│   ├── llamaparse.py                  # Dokumentenkonverter
│   ├── README.md                      # Code-Dokumentation
│   └── .env                          # API-Konfiguration (nicht in Git)
│
├── 📂 input/                          # Eingabedateien
│   ├── projektkommentare.md           # Deal-spezifische Notizen
│   └── 📂 reference_documents/
│       ├── 📂 original/               # Rohdokumente (alle Formate)
│       │   ├── 📂 target_company/     # Zielunternehmen-Dokumente
│       │   └── 📂 past_cim_examples/  # Referenz-CIMs für Stil
│       └── 📂 plain_text/             # Konvertierte Markdown-Dateien
│           ├── 📂 target_company/     # → Konvertierte Zielunternehmen-Docs
│           └── 📂 past_cim_examples/  # → Konvertierte Referenz-CIMs
│
├── 📂 output/                         # Generierte CIMs
│   ├── draft_cim_DE.md # Aktueller CIM-Entwurf (Markdown)
│   ├── CIM_Company_Professional.html # HTML-Version mit Charts
│   ├── questions.md    # Fragenkatalog für DD
│   └── 📂 past/                      # Archiv vorheriger Versionen
│
├── requirements.txt                   # Python-Dependencies
├── README.md                         # Diese Datei
└── venv/                             # Python Virtual Environment
```

---

## 🚀 Installation & Setup

### Voraussetzungen
- Python 3.8+
- LlamaParse API Key ([LlamaCloud](https://cloud.llamaindex.ai/))

### 1. Repository klonen
```bash
git clone <repository-url>
cd m-a-template
```

### 2. Virtual Environment einrichten
```bash
python -m venv venv

# Aktivierung:
# macOS/Linux:
source venv/bin/activate
# Windows:
venv\Scripts\activate
```

### 3. Dependencies installieren
```bash
pip install -r requirements.txt
```

### 4. API-Konfiguration
```bash
# .env-Datei in code/ erstellen:
echo "LLAMAPARSE_API_KEY=your_actual_api_key_here" > code/.env
```

> **API Key erhalten:** Registrierung bei [LlamaCloud](https://cloud.llamaindex.ai/) → Dashboard → API Keys

---

## 💡 Verwendung

### Schritt 1: Dokumente vorbereiten
Dokumente in `input/reference_documents/original/target_company/` ablegen:

```
📁 target_company/
├── Unternehmenspräsentation.pdf
├── Jahresabschluss_2023.pdf
├── DIFFICULT_komplexe_Finanzdaten.xlsx    # Premium-Parsing
├── Produktdokumentation.docx
└── 📁 Finanzen/
    ├── Bilanz_2023.pdf
    └── GuV_2024.xlsx
```

### Schritt 2: Dokumente konvertieren
```bash
# Nur neue Dateien konvertieren
python code/llamaparse.py

# Alle Dateien neu konvertieren
python code/llamaparse.py --force
```

### Schritt 3: CIM generieren
Das System nutzt die workspace rules und generiert automatisch:
- Strukturiertes CIM nach Standard-ToC
- Fragenkatalog für Due Diligence
- Multi-Format-Output (MD + HTML)

---

## 📖 CIM-Erstellungsprozess

### Automatischer Workflow

1. **📄 Dokumentenanalyse**
   - Konvertierung aller Eingabedokumente zu strukturiertem Text
   - Extraktion von Finanzkennzahlen, Produktinformationen, Marktdaten

2. **🏗️ Strukturierung**
   - Clustering nach CIM-Kapiteln (Executive Summary → Transaktionsstruktur)
   - Umsatzbasierte Template-Anpassung (< 5 Mio. vs. ≥ 5 Mio. €)

3. **✍️ Content-Generierung**
   - Erstellung investment-ready Content
   - Integration von Referenz-CIM-Stil
   - Fact-Checking gegen Quelldokumente

4. **🔍 Qualitätssicherung**
   - Automatische Plausibilitätsprüfung
   - Generierung von Nachfragekatalogen
   - Multi-Language-Output

### Standard CIM-Struktur

```
1. Executive Summary              # Kompakte Investoren-Übersicht
2. Investment Highlights          # Key Value Propositions  
3. Unternehmen & Historie        # Background, Entwicklung
4. Produkte / Technologie        # Kernprodukte, IP, Tech-Stack
5. Markt & Wettbewerb           # TAM, Positionierung, Competitors
6. Wachstumschancen             # Growth Stories, Synergien
7. Finanzübersicht              # KPIs, Trends, Projections
8. Transaktionsstruktur & Kontakt # Deal-Parameter, Next Steps
```

---

## 📊 Ausgabeformate

### Markdown CIM (`draft_cim_DE.md`)
- **Zweck**: Content-Struktur für DTP-Team
- **Features**: Platzhalter-Grafiken, saubere Gliederung
- **Format**: `🖼️ Bild: Beschreibung 300 dpi`

### HTML Dashboard (`CIM.html`)
- **Zweck**: Interaktive Investoren-Präsentation
- **Features**: Chart.js-Visualisierungen, Responsive Design
- **Inhalte**: KPI-Dashboards, Umsatzcharts, Kundenanalysen

### Fragenkatalog (`questions.md`)
- **Zweck**: Due Diligence-Vorbereitung
- **Inhalte**: Offene Punkte, Datenabweichungen, Empfehlungen
- **Format**: Kategorisiert nach Dringlichkeit und Themenbereich

---

## ⚙️ Konfiguration

### JSON-Parameter für Deal-Anpassung

```json
{
  "lang": ["de"],                     # Ausgabesprachen  
  "emphasize_team": false,            # Team-Kapitel (ja/nein)
  "emphasize_financials": "auto",     # Finanz-Fokus (high/low/auto)
  "growth_stories": 3,                # Anzahl Growth-Szenarien
  "target_buyers": ["Sennheiser","Shure","Audio-Technica"]  # Potentielle Käufer
}
```

### Umsatzbasierte Auto-Anpassung

| Umsatz | Fokus | Team-Kapitel | Finanz-Detail | Seiten |
|--------|-------|--------------|---------------|---------|
| < 1 Mio. € | Tech/IP, Make-or-Buy | Minimal | Knapp | 7-10 |
| 1-5 Mio. € | Product-Market-Fit | Optional | Moderat | 10-15 |
| ≥ 5 Mio. € | PE-Kriterien | Ausführlich | Detailliert | 20-25 |

---

## 🛠️ Best Practices

### 📁 Dokumenten-Organisation
- **Namenskonvention**: `DIFFICULT_` Präfix für komplexe Layouts
- **Versionierung**: Jahres-/Quartalsdaten eindeutig kennzeichnen
- **Vollständigkeit**: Mindestens 3 Jahre Finanzdaten bereitstellen

### 🎯 Content-Qualität
- **Fact-Checking**: Immer Quellenangaben in Klammern
- **Konservative Projektionen**: Realistisch bleiben vs. zu optimistisch
- **Buyer-Perspektive**: Content aus Käufer-Sicht strukturieren

### 🔒 Vertraulichkeit
- **Sensitive Daten**: Kundennamen ggf. anonymisieren (Kunde A, B, C)
- **IP-Schutz**: Detailgrad an Verhandlungsphase anpassen
- **NDA-Management**: Template unterstützt schrittweise Information Disclosure

---

## 🐛 Troubleshooting

### Häufige Probleme

#### Dokumentenkonvertierung schlägt fehl
```bash
# Fehler: API Key nicht gefunden
→ Überprüfen: code/.env existiert und enthält LLAMAPARSE_API_KEY

# Fehler: Unsupported file format
→ Lösung: Nur unterstützte Formate verwenden (siehe code/README.md)

# Fehler: Rate Limiting
→ Lösung: Delays zwischen Konvertierungen erhöhen (im Code anpassbar)
```

#### CIM-Generierung unvollständig
```bash
# Problem: Fehlende Finanzdaten
→ Lösung: Mindestens Bilanz + GuV der letzten 2 Jahre bereitstellen

# Problem: Zu generischer Content  
→ Lösung: Mehr spezifische Dokumente (Pitch Decks, Produktsheets) hinzufügen

# Problem: Unstimmige Zahlen
→ Lösung: questions.md prüfen → Datenquellen verifizieren
```

#### Performance-Optimierung
```bash
# Große Dokumente (>50MB)
→ Aufteilen in kleinere Dateien oder PDF-Komprimierung

# Viele Dateien (>100)
→ Batch-Processing mit --force alle 24h

# Speicher-Issues
→ Virtual Environment mit mehr RAM oder Cloud-Ausführung
```

---

---

## 📞 Support & Kontakt

### Dokumentation
- **Code-Details**: `code/README.md`
- **API-Referenz**: [LlamaParse Docs](https://github.com/run-llama/llama_parse)
- **CIM-Standards**: Workspace Rules (siehe Cursor-Konfiguration)

### Community
- **Issues**: GitHub Issues für Bug-Reports
- **Features**: Diskussionen für neue Funktionen
- **Examples**: `input/reference_documents/plain_text/past_cim_examples/`

---

**Made with ❤️ for the M&A Community**

*Automatisiere den CIM-Prozess. Fokussiere auf den Deal.*