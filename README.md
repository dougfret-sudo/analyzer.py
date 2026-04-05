# Fleet Cost & Maintenance Analyzer 📊

A Python-based **Business Intelligence (BI) Engine** designed to transform raw service logs into actionable financial insights. This tool bridges the gap between field operations (SSR Data) and the CFO’s desk.

### 🛠️ Core Analytical Logic
*   **Maintenance Burn Rate:** Calculates real-time maintenance expenditure against revenue targets (e.g., $21M/year goals).
*   **Predictive Service Forecasting:** Analyzes odometer trends to identify assets approaching "Critical Service Windows" before they fail in the field.
*   **Utilization Analytics:** Designed to support a **93% Fleet Utilization** target by minimizing unscheduled downtime through data-driven scheduling.

### 🚀 Key Technical Features
*   **Object-Oriented Architecture:** Built using Python Classes for modularity and easy integration into existing SaaS backends.
*   **Data Ingestion:** Optimized for processing CSV and JSON payloads exported from the **Simple Service Recorder (SSR)**.
*   **Financial Governance:** Provides high-level summaries for EBITDA alignment and operational budgeting.

### 📁 File Structure
*   `analyzer.py`: The core BI engine containing the `FleetCostAnalyzer` class.
*   `ssr_data_sample.csv`: (Optional) Sample data to demonstrate the forecasting logic.

### 🛡️ Verified Integrity
Tested in a **hardware-isolated iMac sandbox** to ensure the logic handles "dirty data" and high-volume CSV exports without losing calculation accuracy.
