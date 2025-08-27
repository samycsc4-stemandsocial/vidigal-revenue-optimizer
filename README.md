# Vidigal Revenue Optimizer: Quantifying the 'Trust Tax'
**Author:** Samuel [Your Last Name]  
**Context:** Fieldwork in Vidigal, Rio de Janeiro (2025)  
**Status:** Proof of Concept / Working Prototype

## Project Overview
This repository contains the source code used to analyze the **"Digital Exclusion Tax"** in informal hospitality markets. Developed during participant-action research in the Vidigal favela, this tool models the revenue delta between "Analog" micro-enterprises (cash-based, walk-in only) and "Digitally Integrated" enterprises.

It addresses a core engineering problem in development economics: **How do we optimize revenue in high-friction, low-trust environments without high-bandwidth infrastructure?**

## The "Digital Exclusion" Algorithm
The core script (`vidigal_optimizer.py`) calculates lost revenue based on three variables identified during fieldwork:
1.  **Verification Latency:** The time cost of manual vetting vs. platform verification.
2.  **Inventory Volatility:** The cost of holding empty beds due to lack of predictive data.
3.  **The Trust Tax:** The differential in No-Show rates between verbal reservations (30% observed) and secured digital bookings (8% observed).

##  Key Features
- **Exclusion Calculator:** Quantifies the financial cost of invisibility for informal stakeholders.
- **Dynamic Pricing Logic:** A simple, rule-based algorithm designed to generate pricing alerts for operators via WhatsApp (Low Bandwidth).
- **Scenario Modeling:** Compares pre-intervention (Analog) vs. post-intervention (Digital) efficiency.

##  Tech Stack
- **Python 3.9+**
- **Pandas:** For handling transaction logs from the "Digital Twin" Excel sheets.
- **NumPy:** For occupancy probability modeling.

##  Findings
Early deployment of this logic in Vidigal suggested a potential **60% reduction in transaction friction** and a **20% increase in revenue stability** by bridging the gap to global supply chains.

---
*This code supports the working paper: "The Algorithm of the Street: Quantifying Trust in Vidigal's Informal Sector".*