"""
Gamezone Strategic Analysis - Q1 2026
Author: J. Favreau
Description: 
    This script processes sales data to identify VIP customers ("Whales"), 
    calculates purchase probability for subscription targeting, 
    and generates ADA-compliant visualizations for the Board of Directors.
    
    Optimized for GitHub Desktop and Cloud-Hosted Data Warehouses.
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# --- CONFIGURATION: ADA & ACCESSIBILITY SETTINGS ---
# Use a colorblind-friendly style
try:
    plt.style.use('seaborn-v0_8-colorblind')
except:
    plt.style.use('ggplot') # Fallback if specific style is missing

# --- PART 1: DATA LOADING & CLEANING ---
def load_and_clean_data(filename):
    print("Loading data...")
    try:
        df = pd.read_csv(filename)
    except FileNotFoundError:
        print(f"Error: '{filename}' not found. Please ensure the CSV is in this folder.")
        return None

    # 1. Deduplication (Consolidating Region and Order files)
    initial_count = len(df)
    df.drop_duplicates(inplace=True)
    print(f"Data Scrubbed: Removed {initial_count - len(df)} duplicate rows.")

    # 2. Date Standardization
    # Coerce errors to NaT (Not a Time) to handle messy formats
    df['PURCHASE_TS'] = pd.to_datetime(df['PURCHASE_TS'], errors='coerce')
    df['SHIP_TS'] = pd.to_datetime(df['SHIP_TS'], errors='coerce')

    # 3. Numeric Standardization
    df['USD_PRICE'] = pd.to_numeric(df['USD_PRICE'], errors='coerce')
    df.dropna(subset=['PURCHASE_TS', 'USD_PRICE'], inplace=True)

    # 4. Feature Engineering: Shipping Overhead
    # Calculate 'Days to Ship'. Logic handles 'Time Travel' errors (Ship < Purchase)
    # by clipping negative values to 0.
    df['Shipping_Lag'] = (df['SHIP_TS'] - df['PURCHASE_TS']).dt.days.clip(lower=0)
    
    # 5. Handle Null Shipping Dates (Assume Pending)
    df['Status'] = np.where(df['SHIP_TS'].isnull(), 'Pending', 'Shipped')

    return df

# --- PART 2: STRATEGIC ANALYSIS ---
def generate_insights(df):
    print("Generating strategic insights...")
    
    # --- INSIGHT A: Top 10 'Whale' Customers (Revenue Focus) ---
    # Group by User ID and Country to find high-value targets
    whales = df.groupby(['USER ID', 'COUNTRY_CODE'])['USD_PRICE'].sum().reset_index()
    whales.rename(columns={'USD_PRICE': 'Lifetime_Value'}, inplace=True)
    top_10_whales = whales.sort_values(by='Lifetime_Value', ascending=False).head(10)

    # --- INSIGHT B: Top 20 Subscribers (Probability Modeling) ---
    # Metric: 'Probability of Purchase' 
    # Formula: (Total Spend * 0.7) + (Order Frequency * 0.3)
    user_metrics = df.groupby('USER ID').agg({
        'USD_PRICE': 'sum', 
        'ORDER_ID': 'count'
    }).reset_index()
    
    # Normalize the data slightly for the score
    user_metrics['Prob_Score'] = (user_metrics['USD_PRICE'] * 0.7) + (user_metrics['ORDER_ID'] * 0.3)
    top_20_subscribers = user_metrics.sort_values('Prob_Score', ascending=False).head(20)

    # --- INSIGHT C: Revenue Trends (Monthly) ---
    df['Month_Year'] = df['PURCHASE_TS'].dt.to_period('M')
    revenue_trends = df.groupby('Month_Year')['USD_PRICE'].sum().reset_index()
    revenue_trends['Month_Year'] = revenue_trends['Month_Year'].astype(str)

    return top_10_whales, top_20_subscribers, revenue_trends

# --- PART 3: ADA-COMPLIANT VISUALIZATION ---
def create_visuals(top_10, trends):
    print("Generating ADA-compliant charts...")

    # 1. High-Contrast Bar Chart (Top 10 Customers)
    # We use horizontal bars for better readability of labels
    fig, ax = plt.subplots(figsize=(10, 6))
    
    # Create label: User ID + Country
    labels = top_10['USER ID'].str[:4] + "... (" + top_10['COUNTRY_CODE'] + ")"
    
    # Plot using a high-contrast blue
    bars = ax.barh(labels, top_10['Lifetime_Value'], color='#005AB5')
    
    # Direct Labeling (Accessibility Requirement: No Legend needed)
    ax.bar_label(bars, fmt='$%.0f', padding=3, fontsize=10, fontweight='bold')
    
    plt.title("Top 10 Customers: Lifetime Revenue (Whales)", fontsize=14, loc='left')
    plt.xlabel("Total Spend (USD)")
    plt.tight_layout()
    plt.savefig('visual_top_10_accessible.png', dpi=300)
    print("Saved: visual_top_10_accessible.png")

    # 2. Pattern-Based Line Chart (Revenue Trends)
    # Uses Markers AND Lines to aid colorblind viewers
    plt.figure(figsize=(12, 6))
    plt.plot(trends['Month_Year'], trends['USD_PRICE'], 
             color='black', marker='D', markersize=8, linewidth=2.5)
    
    plt.title("Revenue Volatility Trends (2019-2021)", fontsize=14, loc='left')
    plt.xlabel("Month")
    plt.ylabel("Revenue ($)")
    plt.xticks(rotation=45)
    plt.grid(True, linestyle='--', alpha=0.5)
    plt.tight_layout()
    plt.savefig('visual_revenue_trends.png', dpi=300)
    print("Saved: visual_revenue_trends.png")

# --- MAIN EXECUTION BLOCK ---
if __name__ == "__main__":
    # 1. Set File Path (Ensure this CSV matches your local file)
    FILE_NAME = 'gz-orders-cleaned.csv'
    
    # 2. Run Pipeline
    clean_df = load_and_clean_data(FILE_NAME)
    
    if clean_df is not None:
        whales, subscribers, trends = generate_insights(clean_df)
        
        # 3. Export Data for Tableau/Board Review
        whales.to_csv('output_top_10_whales.csv', index=False)
        subscribers.to_csv('output_top_20_subscribers.csv', index=False)
        trends.to_csv('output_revenue_trends.csv', index=False)
        print("CSV Exports Complete.")
        
        # 4. Create Images for Slide Deck
        create_visuals(whales, trends)
        
        print("\n--- ANALYSIS COMPLETE ---")
        print("Ready for GitHub Push.")