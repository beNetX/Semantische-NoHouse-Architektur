# SPDX-License-Identifier: LicenseRef-SinnZeit-1.0
# SPDX-FileCopyrightText: 2025 beNetX – Moritz Oliver Benatzky
# SPDX-Comment: An artifact of the NoHouse.DotMesh—born from the synthesis of human vision and machine logic.

<!-- SPDX-License-Identifier: LicenseRef-SinnZeit-1.0 -->
<!-- SPDX-FileCopyrightText: 2025 beNetX – Moritz Oliver Benatzky M.A. -->
<!-- SPDX-Comment: An artifact of the NoHouse.DotMesh—born from the synthesis of human vision and machine logic. -->

---
title: "beNetX Projektstruktur"
owner: "system"
purpose: "Übersicht der beNetX-Module und deren Funktionen"
created: "2024-03-20"
tags: ["documentation", "system", "architecture", "structure"]
status: "active"
---

# beNetX Projektstruktur
---

# beNetX Projektstruktur
---

# beNetX Projektstruktur
---
title: "beNetX Projektstruktur"
owner: "system"
purpose: "Übersicht der beNetX-Module und deren Funktionen"
created: "2024-03-20"
tags: ["documentation", "system", "architecture", "structure"]
status: "active"
---

# beNetX Projektstruktur

## Hauptmodule

### Core-Module
- `apps/benetx-dashboard/` - Web-basiertes Dashboard für Monitoring und Steuerung
- `apps/benetx-factory-builder/` - Factory Builder für Dot-Erstellung

### Packages
- `packages/benetx-control/` - Zentrale Steuerung und Orchestrierung
- `packages/benetx-dots/` - Dot-System für Datenverwaltung und -strukturierung
- `packages/benetx-llm/` - LLM-Integration (Mistral via Ollama)
- `packages/benetx-ml/` - Machine Learning Komponenten
- `packages/benetx-agents/` - Agent-System mit YAML-Konfiguration
- `packages/benetx-core/` - Core-Funktionalitäten

### Services
- `services/benetx-docs/` - Systemdokumentation und Wissensbasis
- `services/benetx-productmatrix/` - Echo & Resonanz Semilogie-Implementierung
- `services/benetx-front/` - Frontend-Anwendung
- `services/benetx-gateways/` - API-Gateways für externe Dienste
- `services/benetx-datajobs/` - Hintergrund-Jobs und Automatisierung
- `services/benetx-dataresults/` - Ergebnisverarbeitung und -speicherung
- `services/benetx-nodesync/` - Synchronisation zwischen Systemen

## Modul-Details

### benetx-control
- Zentrale Steuerung des Gesamtsystems
- Job-Orchestrierung
- System-Monitoring
- Konfigurationsmanagement

### apps/benetx-dashboard
- Web-basiertes Dashboard (Vue3 + FastAPI)
- Echtzeit-Monitoring
- System-Status
- Benutzer-Interface
- Typer CLI für Deployment

### benetx-docs
- Systemdokumentation
- API-Dokumentation
- Entwickler-Guides
- Architektur-Dokumentation

### benetx-dots
- Dot-System Implementierung
- Datenstruktur-Definitionen
- Dot-Verarbeitung
- Dot-Speicherung

### benetx-productmatrix
- Echo & Resonanz Semilogie
- Text-Generierung
- Semantische Analyse
- Empfehlungslogik

### benetx-front
- Frontend-Anwendung
- Benutzer-Interface
- Interaktive Komponenten
- API-Integration

### benetx-gateways
- Notion Gateway
- Airtable Gateway
- Google Services Gateway
- Weitere API-Integrationen

### benetx-datajobs
- Hintergrund-Jobs
- Automatisierte Tasks
- Batch-Verarbeitung
- Scheduling

### benetx-llm
- LLM-Integration
- Mistral via Ollama
- Text-Generierung
- Prompt-Engineering

### benetx-ml
- Machine Learning Modelle
- MatrixScore Berechnung
- Feature Engineering
- Modell-Training

### benetx-dataresults
- Ergebnisverarbeitung
- Daten-Export
- Berichtsgenerierung
- Ergebnis-Speicherung

### benetx-nodesync
- Daten-Synchronisation
- System-Integration
- Echtzeit-Updates
- Konflikt-Lösung

## Verzeichnisstruktur

```
beNetX/
├── apps/                   # Anwendungen
│   ├── benetx-dashboard/   # Web-Dashboard (Vue3 + FastAPI)
│   └── benetx-factory-builder/ # Factory Builder
├── packages/               # Pakete
│   ├── benetx-control/     # Zentrale Steuerung
│   ├── benetx-dots/        # Dot-System
│   ├── benetx-llm/         # LLM-Integration
│   ├── benetx-ml/          # Machine Learning
│   ├── benetx-agents/      # Agent-System
│   └── benetx-core/        # Core-Funktionalitäten
├── services/               # Services
│   ├── benetx-docs/        # Systemdokumentation
│   ├── benetx-productmatrix/ # Echo & Resonanz
│   ├── benetx-front/       # Frontend
│   ├── benetx-gateways/    # API-Gateways
│   ├── benetx-datajobs/    # Hintergrund-Jobs
│   ├── benetx-dataresults/ # Ergebnisse
│   └── benetx-nodesync/    # Synchronisation
```

## Entwicklungsumgebung

- **Lokale Entwicklung:** Mac Mini
- **Produktion:** be-hpworker
- **Version Control:** Git
- **Python Environment:** venv
- **Node.js Environment:** npm/yarn

## Wichtige Dateien

- `README.md` - Hauptdokumentation
- `.gitignore` - Git-Ausschlussregeln
- `requirements.txt` - Python-Abhängigkeiten
- `package.json` - Node.js-Abhängigkeiten
- `config_*.json` - Modulspezifische Konfigurationen 
