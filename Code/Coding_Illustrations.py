import pandas as pd
import matplotlib.pyplot as plt

# Data for TSMC
data = pd.read_excel("df.xlsx")
data.columns = data.columns.str.strip()

data["Current Ratio"] = data["Current Assets"] / data["Current Liabilities"]
data["Capex Revenue Ratio"] = data["Capex"] / data["Revenue"] * 100
data["Net Profit Margin"] = data["Net Income"] / data["Revenue"] * 100

# Illustrations

# 3.1.1

plt.figure(figsize=(9,5))
plt.bar(data["Year"] - 0.2, data["Current Assets"], width=0.4, label="Current Assets")
plt.bar(data["Year"] + 0.2, data["Current Liabilities"], width=0.4, label="Current Liabilities")
plt.title("TSMC Current Assets and Current Liabilities")
plt.xlabel("Year")
plt.ylabel("NT$ millions")
plt.xticks(data["Year"])
plt.legend()
plt.tight_layout()
plt.savefig("3_1_1.png", dpi=300)
#plt.show()

# 3.1.2

plt.figure(figsize=(9,5))
plt.plot(data["Year"], data["Current Ratio"], marker="o")
plt.title("TSMC Current Ratio")
plt.xlabel("Year")
plt.ylabel("Current Ratio")
plt.xticks(data["Year"])
plt.tight_layout()
plt.savefig("3_1_2", dpi=300)
#plt.show()

# 3.1.3

plt.figure(figsize=(9,5))
plt.plot(data["Year"], data["Revenue"], marker="o", label="Revenue")
plt.plot(data["Year"], data["Net Income"], marker="o", label="Net Income")
plt.title("TSMC Revenue and Net Income")
plt.xlabel("Year")
plt.ylabel("NT$ millions")
plt.xticks(data["Year"])
plt.legend()
plt.tight_layout()
plt.savefig("3_1_3.png", dpi=300)
#plt.show()

# 3.1.4

plt.figure(figsize=(9,5))
plt.bar(data["Year"], data["Capex"])
plt.title("TSMC Capital Expenditure")
plt.xlabel("Year")
plt.ylabel("NT$ millions")
plt.xticks(data["Year"])
plt.tight_layout()
plt.savefig("3_1_4.png", dpi=300)
#plt.show()

# 3.1.5

plt.figure(figsize=(9,5))
plt.plot(data["Year"],data["Cash"],marker="o",label="Cash")
plt.plot(data["Year"],data["Total Liabilities"],marker="o",label="Total Liabilities")
plt.title("TSMC Cash and Total Liabilities")
plt.xlabel("Year")
plt.ylabel("NT$ millions")
plt.xticks(data["Year"])
plt.legend()
plt.tight_layout()
plt.savefig("3_1_5.png", dpi=300)
#plt.show()

# 3.1.6

plt.figure(figsize=(9,5))
plt.plot(data["Year"],data["Net Profit Margin"],marker="o")
plt.title("TSMC Net Profit Margin")
plt.xlabel("Year")
plt.ylabel("Net Income / Revenue (%)")
plt.xticks(data["Year"])
plt.tight_layout()
plt.savefig("3_1_6.png", dpi=300)
#plt.show()


# 3.2.1

plt.figure(figsize=(9,5))
plt.plot(data["Year"], data["Interest Expense"], marker="o")
plt.title("TSMC Interest Expense Over Time")
plt.xlabel("Year")
plt.ylabel("NT$ millions")
plt.xticks(data["Year"])
plt.tight_layout()
plt.savefig("3_2_1.png", dpi=300)
#plt.show()

# 3.2.2

plt.figure(figsize=(9,5))
plt.plot(data["Year"],data["Capex Revenue Ratio"],marker="o")
plt.title("TSMC CapEx as a Percentage of Revenue")
plt.xlabel("Year")
plt.ylabel("CapEx/Revenue (%)")
plt.xticks(data["Year"])
plt.tight_layout()
plt.savefig("3_2_2.png", dpi=300)
#plt.show()

# 3.3

plt.figure(figsize=(9,5))
plt.plot(data["Year"], data["USD/TWD"], marker="o")
plt.title("USD/TWD Exchange Rate")
plt.xlabel("Year")
plt.ylabel("NTD per USD")
plt.xticks(data["Year"])
plt.tight_layout()
plt.savefig("3_3.png", dpi=300)
#plt.show()

# 3.4.1

plt.figure(figsize=(9,5))
plt.plot(data["Year"], data["Inflation Rate"], marker="o", label="Inflation Rate")
plt.title("Taiwan Inflation Rate")
plt.xlabel("Year")
plt.ylabel("Inflation Rate (%)")
plt.xticks(data["Year"])
plt.tight_layout()
plt.savefig("3_4_1.png", dpi=300)
#plt.show()

# 3.4.2

plt.figure(figsize=(9,5))
plt.plot(data["Year"],data["Energy Consumption"],marker="o")
plt.title("TSMC Energy Consumption Over Time")
plt.xlabel("Year")
plt.ylabel("Energy Consumption")
plt.xticks(data["Year"])
plt.tight_layout()
plt.savefig("3_4_2.png", dpi=300)
#plt.show()

print("Thanks for running my code KÖSZIKE (:")