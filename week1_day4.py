import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# ── Load Clean Data ────────────────────────────────────────────
df = pd.read_csv("data/startup_clean.csv")

# ── Fix City Names ─────────────────────────────────────────────
df['city'] = df['city'].str.strip()
df['city'] = df['city'].replace({
    'Bangalore': 'Bengaluru',
    'bangalore': 'Bengaluru',
    'New Delhi': 'Delhi',
    'new delhi': 'Delhi',
    'Gurugram': 'Gurgaon',
    'Ahemadabad': 'Ahmedabad',
    'Ahemdabad': 'Ahmedabad',
})
print("✅ City names fixed!")

# ── Fix Industry Names ─────────────────────────────────────────
df['industry'] = df['industry'].str.strip()
df['industry'] = df['industry'].replace({
    'ECommerce': 'eCommerce',
    'E-Commerce': 'eCommerce',
    'E-commerce': 'eCommerce',
    'Ecommerce': 'eCommerce',
    'FinTech': 'Finance',
    'Fintech': 'Finance',
})
print("✅ Industry names fixed!")

# ── Fix Investment Types ───────────────────────────────────────
df['investment_type'] = df['investment_type'].str.strip()
df['investment_type'] = df['investment_type'].replace({
    'Seed/ Angel Funding': 'Seed/Angel Funding',
    'Seed / Angel Funding': 'Seed/Angel Funding',
    'Seed\\nFunding': 'Seed Funding',
    'Seed  Funding': 'Seed Funding',
    'Series A': 'Series Funding',
    'Series B': 'Series Funding',
    'Series C': 'Series Funding',
    'Series D': 'Series Funding',
    'Series E': 'Series Funding',
    'Series F': 'Series Funding',
    'Series G': 'Series Funding',
    'Series H': 'Series Funding',
    'Series J': 'Series Funding',
})
print("✅ Investment types fixed!")

# ── Fix Investor Names ─────────────────────────────────────────
df['investors'] = df['investors'].str.replace(
    r'(?i)softbank.*', 'SoftBank', regex=True
)
print("✅ Investor names fixed!")

# ═══════════════════════════════════════════════════════════════
# BUSINESS QUESTION 5: Top 10 highest funded startups
# ═══════════════════════════════════════════════════════════════
top_startups = df.groupby('startup_name')['amount_usd'].sum().sort_values(ascending=False).head(10)

plt.figure(figsize=(12, 6))
sns.barplot(x=top_startups.values, y=top_startups.index, palette='Reds_r')
plt.title('Top 10 Highest Funded Startups', fontsize=16, fontweight='bold')
plt.xlabel('Total Funding (USD)')
plt.ylabel('Startup')
plt.tight_layout()
df.to_csv("startup_final.csv", index=False)
plt.show()
print("✅ Q5 Done!")

# ═══════════════════════════════════════════════════════════════
# BUSINESS QUESTION 6: Which month sees highest funding?
# ═══════════════════════════════════════════════════════════════
months = ['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec']
monthly = df.groupby('month')['amount_usd'].sum()
monthly.index = [months[int(m)-1] for m in monthly.index]

plt.figure(figsize=(12, 6))
sns.barplot(x=monthly.index, y=monthly.values, palette='coolwarm')
plt.title('Which Month Gets Most Startup Funding?', fontsize=16, fontweight='bold')
plt.xlabel('Month')
plt.ylabel('Total Funding (USD)')
plt.tight_layout()
plt.savefig("reports/q6_monthly_seasonality.png")
plt.show()
print("✅ Q6 Done!")

# ═══════════════════════════════════════════════════════════════
# BUSINESS QUESTION 7: Most active investors
# ═══════════════════════════════════════════════════════════════
top_investors = df['investors'].value_counts().head(10)

plt.figure(figsize=(12, 6))
sns.barplot(x=top_investors.values, y=top_investors.index, palette='Purples_r')
plt.title('Top 10 Most Active Investors in India', fontsize=16, fontweight='bold')
plt.xlabel('Number of Deals')
plt.ylabel('Investor')
plt.tight_layout()
plt.savefig("reports/q7_top_investors.png")
plt.show()
print("✅ Q7 Done!")

# ── Save Final Data ────────────────────────────────────────────
df.to_csv("data/startup_final.csv", index=False)
print("\n✅ startup_final.csv saved with ALL fixes!")
print("\nCity counts (top 10):")
print(df['city'].value_counts().head(10))
print("\nIndustry counts (top 10):")
print(df['industry'].value_counts().head(10))
print("\nInvestment type counts:")
print(df['investment_type'].value_counts())