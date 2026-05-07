# GameZone Strategic Full Stack Analysis: Turning Latency into Currency


## Executive Summary
This repository contains a full stack technical suite designed for the GameZone Board of Directors.  This proposal and analysis identifies three growth opportunities: retaining high-value customers, optimizing warehouse costs, and expanding into underserved accessible markets. 
Included are ADA, colorblind-friendly, high-contrast visualizations, a pipeline transformation, and a slide-deck. These are built for quick understanding and rapid executive decision-making.

## Key Findings
1.  **Retention Gap**: 82% of our new customers in Year 1 are one-time buyers. The "GameZone Pro" initiative I'm proposing, targets the 18% repeat-buyer segment which currently drives 45% of our profit margins. 
3.  **Seasonality**: Revenue analysis identifies a significant "Summer Valley." Predictive bundling of accessories is recommended to smooth cash flow during non-holiday quarters.
4.  **Privacy Priority**: All board-facing data uses masked User IDs. Data is protected via encryption on our cloud-hosted database.
   
## Key Strategic Pillars
* **The Whale Strategy**: Identification and white-glove targeting of the Top 10 customers with a lifetime value (LTV) > $2,000. While US volume is high, our highest margin growth is currently situated in the EU (DE, GB, FR).
* **Predictive Bundling**: Reducing warehouse overhead by 20% through "Predictive Bundling" pre-packaging high-probability item pairs (e.g., PS5 + 4K Monitors) before peak demand cycles.
* **Accessible Market Expansion**: By implementing WCAG 2.1 (ADA) compliance across our data visuals and store-fronts, we are positioning GameZone to capture the 25% of the market often ignored by competitors.
* **Ethical Data Framework**: Utilizing Zero-Party data for marketing, and cloud-native field-level encryption (AWS/Azure) to ensure 100% GDPR and CCPA compliance.

---

##For Developers:
## Technical Stack & Methodology
We're utilizing a multi-disciplinary approach to ensure data integrity and actionable insights:

* **Python 3.10+ & (ETL & Modeling)**: Handles complex data scrubbing, identifying and correcting records where Ship Date < Purchase Date by clipping negative values to 0, and probability-of-purchase scoring for subscription targeting.
* **SQL (Cloud-Ready Analysis)**: Features Common Table Expressions (CTEs) optimized for AWS Redshift/Azure Synapse, including automated PII masking views for executive security.
* **Gemini (Strategic Visualization)**: Utilizes high-contrast visualizations and a pipeline transformation,  built for quick understanding and rapid executive decision-making.
* **ADA Compliance**: Visualizations utilize the Okabe-Ito colorblind-friendly palette and direct-labeling standards to ensure accessibility for visually impaired viewers.
---

## Repository Structure
* `analysis_script.py`: The core Python engine for data cleaning and probability modeling.
* `analysis_queries.sql`: The cloud-optimized SQL script for revenue aggregation and privacy-first views.
* `/visuals/`: Contains high-resolution, ADA-compliant PNG charts for presentations.
* `Gamezone_Board_Presentation.pptx`: The final slidedeck generated for the Board of Directors.
* `gz-orders-cleaned.csv`, `gz-region-cleaned.csv`: The source datasets, containing over 20k rows of excel data.
---

## Getting Started
1.  **Requirements**: Install Python 3.10+ and libraries (`pandas`, `matplotlib`, `seaborn`).
2.  **Data Processing**: Run `analysis_script.py` to generate the clean outputs and accessibility-optimized visuals.
3.  **Database Migration**: Execute `analysis_queries.sql` in SQL to build the `board_ready_sales` view.

**Note on ADA Compliance**: This project follows Americans with Disabilities Act standards for data presentation. All charts are rendered with high contrast and pattern-based markers to ensure they are fully interpretable by colorblind and visually impaired viewers.

## Assumptions / Limitations
** The dataset used for analysis is representative of the last 2 years. If the BOD approves the proposal, we will gather and analyze more granular data.

## Ownership & Contact
**Project Owner: Julie Favreau, Data Analyst
**Executive Sponsor: Anne Hryunak, VP of Marketing
**Implementation Lead: Dave Palpatine, Senior Data Engineer
**Last Updated: 2026/03/31
**Contact: jfavreau@gamezone.com
---
*Developed by J. Favreau*
