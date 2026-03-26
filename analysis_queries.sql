/*
=============================================================================
Gamezone Strategic Data Analysis - Q1 2026
Author: J. Favreau
Platform: SQL 
Description: 
    This script handles data integrity validation, privacy masking for 
    executive reporting, and core revenue analysis.
=============================================================================
*/

-- ==========================================================================
-- SECTION 0: INDEX SETUP
-- ==========================================================================
-- Recommended indexes:
CREATE INDEX idx_orders_user_id ON orders(USER_ID);
CREATE INDEX idx_orders_purchase_ts ON orders(PURCHASE_TS);
CREATE INDEX idx_orders_country ON orders(COUNTRY_CODE);
CREATE INDEX idx_orders_ship_ts ON orders(SHIP_TS);

-- ==========================================================================
-- SECTION 1: DATA INTEGRITY & QUALITY CHECKS
-- ==========================================================================

/* Logic Check: "Time Travel" Detection
   Identifies rows where Shipment Date is recorded BEFORE Purchase Date.
   These likely indicate logging errors in the warehouse timestamp system.
*/
SELECT 
    ORDER_ID, 
    PURCHASE_TS, 
    SHIP_TS,
    (SHIP_TS - PURCHASE_TS) as shipping_latency_days
FROM orders
WHERE SHIP_TS < PURCHASE_TS
ORDER BY shipping_latency_days ASC;

-- ==========================================================================
-- SECTION 2: PRIVACY & SECURITY (BOARD READY VIEWS)
-- ==========================================================================

/*
   View: board_ready_sales
   Purpose: Masks Personally Identifiable Information (PII) for board presentations.
   Uses concatenation to hide the full USER_ID while keeping it unique for counting.
*/
CREATE OR REPLACE VIEW board_ready_sales AS
SELECT 
    -- Masking USER_ID for Privacy (GDPR/CCPA Compliance)
    MD5(USER_ID) as masked_user_id,
    COUNTRY_CODE,
    SUM(USD_PRICE) as total_spend,
    COUNT(ORDER_ID) as order_volume,
    -- Segmentation for Strategy
    CASE 
        WHEN SUM(USD_PRICE) > 2000 THEN 'Whale (VIP)'
        WHEN SUM(USD_PRICE) BETWEEN 500 AND 2000 THEN 'High Value'
        ELSE 'Standard'
    END as customer_tier
FROM orders
GROUP BY USER_ID, COUNTRY_CODE;

-- ==========================================================================
-- SECTION 3: STRATEGIC REVENUE INSIGHTS
-- ==========================================================================

-- INSIGHT A: The "Whales" (Top 10 Customers by Revenue)
-- Focus: These customers drive the "Predictive Bundling" strategy.

SELECT 
    USER_ID,
    COUNTRY_CODE,
    SUM(USD_PRICE) AS lifetime_revenue,
    COUNT(ORDER_ID) AS frequency,
    FIRST_VALUE(PRODUCT_NAME) OVER (PARTITION BY USER_ID ORDER BY PURCHASE_TS DESC) AS last_item_purchased
FROM orders
GROUP BY USER_ID, COUNTRY_CODE
ORDER BY lifetime_revenue DESC
LIMIT 10;

-- INSIGHT B: Retention Analysis (The "One-and-Done" Problem)
-- Uses a CTE (Common Table Expression) to categorize buyer loyalty.
WITH UserOrderCounts AS (
    SELECT USER_ID, COUNT(ORDER_ID) as total_orders
    FROM orders
    GROUP BY USER_ID
)
SELECT 
    CASE 
        WHEN total_orders = 1 THEN 'One-Time Buyer'
        WHEN total_orders BETWEEN 2 AND 4 THEN 'Repeat Buyer'
        ELSE 'Super User (5+)' 
    END AS retention_category,
    COUNT(USER_ID) as user_count,
    ROUND(COUNT(USER_ID) * 100.0 / (SELECT COUNT(*) FROM UserOrderCounts), 1) as pct_of_base
FROM UserOrderCounts
GROUP BY 1
ORDER BY user_count DESC;

-- INSIGHT C: Regional Opportunity (Under-Monetized Markets)
-- Identifies countries with high order volume but low Average Order Value (AOV).
SELECT 
    COUNTRY_CODE,
    COUNT(ORDER_ID) as total_orders,
    SUM(USD_PRICE) as total_revenue,
    ROUND(AVG(USD_PRICE), 2) as avg_order_value
FROM orders
GROUP BY COUNTRY_CODE
HAVING COUNT(ORDER_ID) > 50  -- Filter for significant markets only
ORDER BY avg_order_value DESC;

-- INSIGHT D: Monthly Revenue Trends (Seasonality)
-- Aggregates sales by month to identify the "Summer Slump" vs "Holiday Spike".
SELECT 
    DATE_TRUNC(MONTH, PURCHASE_TS) AS sales_month,
    SUM(USD_PRICE) AS total_revenue
FROM orders
GROUP BY 1
ORDER BY 1 DESC;
