import pandas as pd
import google.generativeai as genai
import time

# --- STEP 1: SETUP ---
# Paste your API Key inside the quotes below
API_KEY = 'AIzaSyAXxg6h0LRHBBL88zkMwr1BHH-4JIpHWDg' 

# Configure Gemini
genai.configure(api_key=API_KEY)
model = genai.GenerativeModel('gemini-pro') # Using the standard Gemini Pro model

# --- STEP 2: LOAD DATA ---
print("Loading Gamezone Data...")
# We are loading the cleaned CSV you already have
df = pd.read_csv('gz-orders-cleaned.csv')

# Let's just look at the Top 5 customers to save time/cost for this demo
# We group by User to get our "Whales"
whales = df.groupby('USER ID')['USD_PRICE'].sum().sort_values(ascending=False).head(5).reset_index()

print("Found Top 5 Whales. Asking Gemini for strategy...")

# --- STEP 3: ASK GEMINI ---
def ask_gemini(user_id, total_spend):
    # This is the prompt we send to the AI
    prompt = f"""
    You are a data analyst for Gamezone. 
    Customer {user_id} has spent ${total_spend} on gaming gear.
    Write a ONE sentence VIP marketing email subject line for them.
    Then, write a ONE sentence strategy on what to sell them next.
    Separate the two sentences with a pipe symbol '|'.
    """
    try:
        response = model.generate_content(prompt)
        return response.text.strip()
    except Exception as e:
        return "Error | Error"

# Create a list to store results
gemini_results = []

# Loop through the whales and ask Gemini
for index, row in whales.iterrows():
    print(f"Analyzing Customer {index + 1}...")
    result = ask_gemini(row['USER ID'], row['USD_PRICE'])
    gemini_results.append(result)
    time.sleep(1) # Pause specifically to be nice to the API

# --- STEP 4: SAVE RESULTS ---
whales['Gemini_Output'] = gemini_results

# Split the output into two columns for Tableau
whales[['Email_Subject', 'Next_Strategy']] = whales['Gemini_Output'].str.split('|', expand=True)

# Save to a new file for Tableau
whales.to_csv('gamezone_ai_enriched.csv', index=False)
print("Success! Created 'gamezone_ai_enriched.csv' for Tableau.")