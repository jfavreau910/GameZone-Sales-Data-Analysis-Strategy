# GameZone Strategic Analysis 2026: Turning Latency into Currency

## 🎯 Executive Summary
This repository contains a professional-grade technical suite designed for the GameZone Board of Directors. The project transitions our data operations from retrospective reporting to a forward-looking roadmap centered on "Whale" retention, warehouse efficiency, and accessible market expansion.

### Key Strategic Pillars
* **The Whale Strategy**: Identification and white-glove targeting of the Top 10 customers (LTV > $2,000). While US volume is high, our highest margin growth is currently situated in the EU (DE, GB, FR).
* **Operational Alpha**: Reducing warehouse overhead by 20% through "Predictive Bundling"—pre-packaging high-probability item pairs (e.g., PS5 + 4K Monitors) before peak demand cycles.
* **Accessible Market Expansion**: By implementing WCAG 2.1 (ADA) compliance across our data visuals and store-fronts, we are positioning GameZone to capture the 25% of the market often ignored by competitors.
* **Ethical Data Framework**: Utilizing Zero-Party data for marketing and cloud-native field-level encryption (AWS/Azure) to ensure 100% GDPR and CCPA compliance.



---

## 🛠 Technical Stack & Methodology
This project utilizes a multi-disciplinary approach to ensure data integrity and actionable insights:

* **Python (ETL & Modeling)**: Handles complex data scrubbing, "Time Travel" error correction (Ship Date < Purchase Date), and probability-of-purchase scoring for subscription targeting.
* **SQL (Cloud-Ready Analysis)**: Features Common Table Expressions (CTEs) optimized for AWS Redshift/Azure Synapse, including automated PII masking views for executive security.
* **Tableau (Strategic Visualization)**: High-contrast, interactive dashboards built for rapid executive decision-making.
* **ADA Compliance**: Visualizations utilize the Okabe-Ito colorblind-friendly palette and direct-labeling standards to ensure accessibility for visually impaired board members.



---

## 📂 Repository Structure
* `analysis_script.py`: The core Python engine for data cleaning and probability modeling.
* `analysis_queries.sql`: The cloud-optimized SQL script for revenue aggregation and privacy-first views.
* `/visuals/`: Contains high-resolution, ADA-compliant PNG charts for presentations.
* `Gamezone_Board_Presentation.pptx`: The final slidedeck generated for the Board of Directors.
* `gz-orders-cleaned.csv`: The source dataset 
---

## 📈 Key Findings
1.  **Retention Gap**: 82% of our customers are one-time buyers. The "GameZone Pro" initiative targets the 18% repeat-buyer segment which currently drives 45% of our profit margins.
2.  **Seasonality**: Revenue analysis identifies a significant "Summer Valley." Predictive bundling of accessories is recommended to smooth cash flow during non-holiday quarters.
3.  **Privacy Priority**: All board-facing data uses masked User IDs. Data is protected via field-level encryption on our cloud-hosted (AWS/Azure) database.

---

## 🚀 Getting Started
1.  **Requirements**: Install Python 3.x and libraries (`pandas`, `matplotlib`, `seaborn`).
2.  **Data Processing**: Run `analysis_script.py` to generate the clean outputs and accessibility-optimized visuals.
3.  **Database Migration**: Execute `analysis_queries.sql` in your SQL environment to build the `board_ready_sales` view.

**Note on ADA Compliance**: This project follows Americans with Disabilities Act standards for data presentation. All charts are rendered with high contrast and pattern-based markers to ensure they are fully interpretable by colorblind and visually impaired viewers.

---
*Developed by J. Favreau, Data Analytics Team*