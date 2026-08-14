import pandas as pd
import matplotlib.pyplot as plt


# --------------------------------------------------
# Load IPL dataset
# --------------------------------------------------

FILE_NAME = "matches.csv"

try:
    df = pd.read_csv(FILE_NAME)
except FileNotFoundError:
    print("ERROR: matches.csv was not found.")
    print("Place matches.csv in the same folder as this Python file.")
    exit()


print("\n========== IPL DATA ANALYSIS ==========\n")

print("Total matches:", len(df))

print("\nDataset columns:")
print(df.columns.tolist())


# --------------------------------------------------
# Clean column names
# --------------------------------------------------

df.columns = df.columns.str.strip().str.lower()


# --------------------------------------------------
# Check required columns
# --------------------------------------------------

required_columns = [
    "team1",
    "team2",
    "winner",
    "toss_winner",
    "toss_decision"
]

missing_columns = [
    column for column in required_columns
    if column not in df.columns
]

if missing_columns:
    print("\nMissing columns:")
    print(missing_columns)
    exit()


# --------------------------------------------------
# Remove rows with missing important values
# --------------------------------------------------

df = df.dropna(
    subset=[
        "team1",
        "team2",
        "winner"
    ]
)


# --------------------------------------------------
# Team win count
# --------------------------------------------------

win_counts = df["winner"].value_counts()

print("\n========== TEAM WIN COUNTS ==========\n")

print(win_counts)


# --------------------------------------------------
# Total matches played by each team
# --------------------------------------------------

teams = pd.unique(
    pd.concat(
        [
            df["team1"],
            df["team2"]
        ]
    )
)

matches_played = {}

for team in teams:

    count = (
        (df["team1"] == team) |
        (df["team2"] == team)
    ).sum()

    matches_played[team] = count


matches_played = pd.Series(
    matches_played
)


# --------------------------------------------------
# Calculate win rate
# --------------------------------------------------

win_rate = (
    win_counts
    .div(matches_played)
    .mul(100)
    .sort_values(
        ascending=False
    )
)


print("\n========== TEAM WIN RATES ==========\n")

for team, rate in win_rate.items():

    print(
        f"{team}: {rate:.2f}%"
    )


# --------------------------------------------------
# KKR analysis
# --------------------------------------------------

KKR = "Kolkata Knight Riders"

kkr_data = df[
    (df["team1"] == KKR) |
    (df["team2"] == KKR)
].copy()


print("\n========== KKR ANALYSIS ==========\n")

print(
    "KKR matches:",
    len(kkr_data)
)


# --------------------------------------------------
# KKR wins
# --------------------------------------------------

kkr_wins = (
    kkr_data["winner"] == KKR
).sum()

print(
    "KKR wins:",
    kkr_wins
)


if len(kkr_data) > 0:

    kkr_win_rate = (
        kkr_wins /
        len(kkr_data)
    ) * 100

else:

    kkr_win_rate = 0


print(
    f"KKR win rate: {kkr_win_rate:.2f}%"
)


# --------------------------------------------------
# KKR toss decisions
# --------------------------------------------------

print(
    "\n========== KKR TOSS DECISIONS ==========\n"
)


kkr_toss = kkr_data[
    kkr_data["toss_winner"] == KKR
]


toss_decisions = (
    kkr_toss["toss_decision"]
    .value_counts()
)


print(toss_decisions)


# --------------------------------------------------
# KKR toss decision percentages
# --------------------------------------------------

if len(kkr_toss) > 0:

    toss_percentage = (
        kkr_toss["toss_decision"]
        .value_counts(
            normalize=True
        )
        .mul(100)
    )

    print(
        "\nKKR toss decision percentage:"
    )

    print(
        toss_percentage
        .round(2)
    )


# --------------------------------------------------
# Save KKR analysis
# --------------------------------------------------

kkr_data.to_csv(
    "kkr_analysis.csv",
    index=False
)

print(
    "\nKKR data saved to kkr_analysis.csv"
)


# ==================================================
# VISUALIZATION 1
# Team Win Rates
# ==================================================

plt.figure(
    figsize=(12, 6)
)

win_rate.plot(
    kind="bar"
)

plt.title(
    "IPL Team Win Rates"
)

plt.xlabel(
    "Team"
)

plt.ylabel(
    "Win Rate (%)"
)

plt.xticks(
    rotation=75
)

plt.tight_layout()

plt.savefig(
    "team_win_rates.png"
)

plt.show()


# ==================================================
# VISUALIZATION 2
# KKR Toss Decisions
# ==================================================

plt.figure(
    figsize=(7, 5)
)

toss_decisions.plot(
    kind="bar"
)

plt.title(
    "KKR Toss Decision Outcomes"
)

plt.xlabel(
    "Toss Decision"
)

plt.ylabel(
    "Number of Matches"
)

plt.xticks(
    rotation=0
)

plt.tight_layout()

plt.savefig(
    "kkr_toss_decisions.png"
)

plt.show()


# ==================================================
# VISUALIZATION 3
# KKR Wins vs Losses
# ==================================================

kkr_losses = (
    len(kkr_data) -
    kkr_wins
)

kkr_results = pd.Series(
    {
        "Wins": kkr_wins,
        "Losses": kkr_losses
    }
)


plt.figure(
    figsize=(7, 5)
)

kkr_results.plot(
    kind="bar"
)

plt.title(
    "Kolkata Knight Riders: Wins vs Losses"
)

plt.xlabel(
    "Result"
)

plt.ylabel(
    "Number of Matches"
)

plt.xticks(
    rotation=0
)

plt.tight_layout()

plt.savefig(
    "kkr_wins_losses.png"
)

plt.show()


print(
    "\n========== ANALYSIS COMPLETE =========="
)

print(
    "Generated files:"
)

print("1. kkr_analysis.csv")
print("2. team_win_rates.png")
print("3. kkr_toss_decisions.png")
print("4. kkr_wins_losses.png")
