import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# ── Load Data ──────────────────────────────────────────────────
df = pd.read_csv("data/startup_funding.csv")

# ── Step 1: Rename Columns (clean names) ───────────────────────
df.columns = ['sr_no', 'date', 'startup_name', 'industry', 
              'sub_vertical', 'city', 'investors', 
              'investment_type', 'amount_usd', 'remarks']

# ── Step 2: Drop Useless Columns ───────────────────────────────
df.drop(columns=['sr_no', 'sub_vertical', 'remarks'], inplace=True)
print("✅ Dropped useless columns")

# ── Step 3: Fix Date Column ────────────────────────────────────
df['date'] = pd.to_datetime(df['date'], dayfirst=True, errors='coerce')
df['year'] = df['date'].dt.year
df['month'] = df['date'].dt.month
print("✅ Date column fixed")

# ── Step 4: Clean Amount Column ────────────────────────────────
df['amount_usd'] = df['amount_usd'].astype(str)
df['amount_usd'] = df['amount_usd'].str.replace(',', '', regex=False)
df['amount_usd'] = pd.to_numeric(df['amount_usd'], errors='coerce')
print("✅ Amount column cleaned")

# ── Step 5: Fix City Names ─────────────────────────────────────
df['city'] = df['city'].str.strip()
df['city'] = df['city'].replace({
    'Bangalore': 'Bengaluru',
    'bangalore': 'Bengaluru',
    'New Delhi': 'Delhi',
    'new delhi': 'Delhi',
    'Gurugram': 'Gurgaon'
})
df['city'].fillna('Unknown', inplace=True)
print("✅ City names fixed")

# ── Step 6: Fix Industry Column ────────────────────────────────
df['industry'].fillna('Unknown', inplace=True)
df['industry'] = df['industry'].str.strip()
print("✅ Industry column fixed")

# ── Step 7: Remove URL rows in Startup Name ────────────────────
df = df[~df['startup_name'].str.contains('http', na=False)]
print("✅ Removed URL rows")

# ── Step 8: Drop rows with no Amount ──────────────────────────
df_clean = df.dropna(subset=['amount_usd'])
print(f"✅ Removed rows with no amount")

# ── Final Check ────────────────────────────────────────────────
print("\n📊 Clean Data Shape:", df_clean.shape)
print("\n📊 Missing Values After Cleaning:")
print(df_clean.isnull().sum())
print("\n📊 Sample Clean Data:")
print(df_clean.head())

# ── Save Clean Data
df_clean.to_csv("data/startup_clean.csv", index=False)