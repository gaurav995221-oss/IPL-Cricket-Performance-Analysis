import pandas as pd
import matplotlib.pyplot as plt

# Load IPL 2026 batting data (top 100 by runs)
df = pd.read_csv("ipl_2026_batting_top_100.csv")

print("\nFIRST FIVE ROWS")
print(df.head())
print("\nDATASET INFO")
df.info()
print("\nSUMMARY")
print(df[["Matches", "Runs", "Highest_Score", "Strike_Rate", "Fours", "Sixes"]].describe())

print("\nTOP 10 RUN SCORERS")
print(df.nlargest(10, "Runs")[["Player", "Team", "Runs", "Strike_Rate"]])

# Plot 1: Top 10 run scorers
top = df.nlargest(10, "Runs").sort_values("Runs")
plt.figure(figsize=(10, 6))
plt.barh(top["Player"], top["Runs"])
plt.title("IPL 2026 - Top 10 Run Scorers")
plt.xlabel("Runs")
plt.tight_layout()
plt.savefig("top_10_run_scorers.png", dpi=300)
plt.show()

# Plot 2: Runs vs strike rate
plt.figure(figsize=(9, 6))
plt.scatter(df["Strike_Rate"], df["Runs"])
plt.title("IPL 2026 - Runs vs Strike Rate (Top 100)")
plt.xlabel("Strike Rate")
plt.ylabel("Runs")
plt.tight_layout()
plt.savefig("runs_vs_strike_rate.png", dpi=300)
plt.show()

# Plot 3: Boundary runs among top 10 run scorers
top["Boundary_Runs"] = top["Fours"] * 4 + top["Sixes"] * 6
plt.figure(figsize=(10, 6))
plt.barh(top["Player"], top["Boundary_Runs"])
plt.title("Boundary Runs - Top 10 IPL 2026 Batters")
plt.xlabel("Runs from fours and sixes")
plt.tight_layout()
plt.savefig("boundary_runs_top10.png", dpi=300)
plt.show()

df.to_csv("ipl_2026_top100_cleaned.csv", index=False)
print("\nAnalysis complete.")
