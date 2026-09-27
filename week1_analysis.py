import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# ── Load Clean Data ────────────────────────────────────────────
df = pd.read_csv("data/startup_clean.csv")

print("✅ Clean data loaded:", df.shape)

# ═══════════════════════════════════════════════════════════════
# BUSINESS QUESTION 1:
# Which industries are attracting the most funding?
# ═══════════════════════════════════════════════════════════════
industry_funding = df.groupby('industry')['amount_usd'].sum().sort_values(ascending=False).head(10)

plt.figure(figsize=(12, 6))
sns.barplot(x=industry_funding.values, y=industry_funding.index, palette='Blues_r')
plt.title('Top 10 Industries by Total Funding (USD)', fontsize=16, fontweight='bold')
plt.xlabel('Total Funding (USD)')
plt.ylabel('Industry')
plt.tight_layout()
plt.savefig("reports/q1_industry_funding.png")
plt.show()
print("\n✅ Q1 Done!")
print(industry_funding)

# ═══════════════════════════════════════════════════════════════
# BUSINESS QUESTION 2:
# Which cities are the startup hubs of India?
# ═══════════════════════════════════════════════════════════════
city_funding = df.groupby('city')['amount_usd'].sum().sort_values(ascending=False).head(10)

plt.figure(figsize=(12, 6))
sns.barplot(x=city_funding.values, y=city_funding.index, palette='Greens_r')
plt.title('Top 10 Cities by Total Funding (USD)', fontsize=16, fontweight='bold')
plt.xlabel('Total Funding (USD)')
plt.ylabel('City')
plt.tight_layout()
plt.savefig("reports/q2_city_funding.png")
plt.show()
print("\n✅ Q2 Done!")
print(city_funding)

# ═══════════════════════════════════════════════════════════════
# BUSINESS QUESTION 3:
# How has startup funding grown year over year?
# ═══════════════════════════════════════════════════════════════
yearly_funding = df.groupby('year')['amount_usd'].sum()

plt.figure(figsize=(12, 6))
sns.lineplot(x=yearly_funding.index, y=yearly_funding.values, marker='o', color='purple', linewidth=2.5)
plt.title('Startup Funding Growth Year Over Year', fontsize=16, fontweight='bold')
plt.xlabel('Year')
plt.ylabel('Total Funding (USD)')
plt.tight_layout()
plt.savefig("reports/q3_yearly_growth.png")
plt.show()
print("\n✅ Q3 Done!")
print(yearly_funding)

# ═══════════════════════════════════════════════════════════════
# BUSINESS QUESTION 4:
# What investment types are most common?
# ═══════════════════════════════════════════════════════════════
inv_type = df['investment_type'].value_counts().head(8)

plt.figure(figsize=(10, 6))
sns.barplot(x=inv_type.values, y=inv_type.index, palette='Oranges_r')
plt.title('Most Common Investment Types', fontsize=16, fontweight='bold')
plt.xlabel('Number of Deals')
plt.ylabel('Investment Type')
plt.tight_layout()
plt.savefig("reports/q4_investment_types.png")
plt.show()
print("\n✅ Q4 Done!")
print(inv_type)

print("\n🎉 All 4 Business Questions Answered!")
print("📁 Charts saved in reports folder!")