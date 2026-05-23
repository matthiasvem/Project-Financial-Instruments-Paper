import pandas as pd
import matplotlib.pyplot as plt

# Data for TSMC 
# everything in NT$ millions

years = [2021, 2022, 2023, 2024, 2025]

data = pd.DataFrame({
    "Year": years,
    "Current Assets": [2060000, 2400000, 2500000, 2850000, 3100000],
    "Current Liabilities": [810000, 950000, 1050000, 1250000, 1458000],
    "Cash": [1200000, 1350000, 1500000, 1700000, 1850000],
    "Total Liabilities": [1350000, 1550000, 1700000, 1950000, 2200000],
    "Revenue": [1587000, 2263000, 2162000, 2894000, 3200000],
    "Net Income": [596000, 1016000, 838000, 1173000, 1300000],
    "Capex": [850000, 1100000, 950000, 1000000, 1200000],
    "Interest Expense": [10000, 18000, 25000, 32000, 40000],
    "USD_TWD": [27.9, 29.8, 31.1, 32.0, 32.5],
    "Inflation Rate": [1.96, 2.95, 2.49, 2.18, 2.00],
    "Energy Consumption": [18000, 22400, 25000, 27456, 30000]
})

data["Current Ratio"] = data["Current Assets"] / data["Current Liabilities"]

# Illustrations

# 3.1.1

plt.figure(figsize=(9,5))
plt.bar(data["Year"] - 0.2, data["Current Assets"], width=0.4, label="Current Assets")
plt.bar(data["Year"] + 0.2, data["Current Liabilities"], width=0.4, label="Current Liabilities")
plt.title("TSMC Current Assets and Current Liabilities")
plt.xlabel("Year")
plt.ylabel("NT$ millions")
plt.legend()
plt.tight_layout()
plt.savefig("3_1_1.png", dpi=300)
plt.show()

# 3.1.2

plt.figure(figsize=(9,5))
plt.plot(data["Year"], data["Current Ratio"], marker="o")
plt.title("TSMC Current Ratio")
plt.xlabel("Year")
plt.ylabel("Current Ratio")
plt.tight_layout()
plt.savefig("3_1_2.png", dpi=300)
plt.show()


# 3.1.3

plt.figure(figsize=(9,5))
plt.plot(data["Year"], data["Revenue"], marker="o", label="Revenue")
plt.plot(data["Year"], data["Net Income"], marker="o", label="Net Income")
plt.title("TSMC Revenue and Net Income")
plt.xlabel("Year")
plt.ylabel("NT$ millions")
plt.legend()
plt.tight_layout()
plt.savefig("3_1_3.png", dpi=300)
plt.show()

# 3.1.4

plt.figure(figsize=(9,5))
plt.bar(data["Year"], data["Capex"])
plt.title("TSMC Capital Expenditure")
plt.xlabel("Year")
plt.ylabel("NT$ millions")
plt.tight_layout()
plt.savefig("3_1_4.png", dpi=300)
plt.show()

# 3.2

plt.figure(figsize=(9,5))
plt.plot(data["Year"], data["Interest Expense"], marker="o")
plt.title("TSMC Interest Expense Over Time")
plt.xlabel("Year")
plt.ylabel("NT$ millions")
plt.tight_layout()
plt.savefig("3_2.png", dpi=300)
plt.show()

# 3.3

plt.figure(figsize=(9,5))
plt.plot(data["Year"], data["USD_TWD"], marker="o")
plt.title("USD/TWD Exchange Rate")
plt.xlabel("Year")
plt.ylabel("NTD per USD")
plt.tight_layout()
plt.savefig("3_3.png", dpi=300)
plt.show()

# 3.4

plt.figure(figsize=(9,5))
plt.plot(data["Year"], data["Inflation Rate"], marker="o", label="Inflation Rate")
plt.title("Taiwan Inflation Rate")
plt.xlabel("Year")
plt.ylabel("Inflation Rate (%)")
plt.tight_layout()
plt.savefig("3_4.png", dpi=300)
plt.show()

