import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("weather_tokyo_data.csv")

# Clean column names
df.columns = df.columns.str.strip()

# Clean temperature
df['temperature'] = df['temperature'].astype(str)
df['temperature'] = df['temperature'].str.replace(r"\(.*?\)", "", regex=True)
df['temperature'] = pd.to_numeric(df['temperature'], errors='coerce')

# Extract month (NO datetime needed)
df['month'] = df['day'].str.split('/').str[0].astype(int)

# Average temperature
avg_temp = df['temperature'].mean()
print(f"Average Temperature: {avg_temp:.2f}")

# Monthly average
monthly_avg = df.groupby('month')['temperature'].mean()

# Plot monthly averages
plt.figure(figsize=(10,6))
bars = plt.bar(monthly_avg.index, monthly_avg.values, color="black")

plt.title("Average Monthly Temperature")
plt.xlabel("Month")
plt.ylabel("Temperature")

plt.grid(axis="y", linestyle="--", alpha=0.7)

plt.bar_label(bars, fmt="%.2f")

plt.show()

hottest_per_year = df.sort_values('temperature', ascending=False).groupby('year').head(1)
coldest_per_year = df.sort_values('temperature', ascending=True).groupby('year').head(1)

# Plot yearly extremes
plt.figure(figsize=(10,6))

plt.bar(hottest_per_year['year'], hottest_per_year['temperature'], color='red', label='Hottest')
plt.bar(coldest_per_year['year'], coldest_per_year['temperature'], color='blue', label='Coldest')

plt.title("Hottest and Coldest Days per Year")
plt.xlabel("Year")
plt.ylabel("Temperature")
plt.legend()

plt.show()

def get_season(month):
    if month in [12, 1, 2]:
        return "Winter"
    elif month in [3, 4, 5]:
        return "Spring"
    elif month in [6, 7, 8]:
        return "Summer"
    else:
        return "Fall"

# Extract month from "day"
df['month'] = df['day'].str.split('/').str[0].astype(int)

# Create season column (FIXED)
df['season'] = df['month'].apply(get_season)

# Seasonal average temperature
seasonal_temperature = df.groupby('season')['temperature'].mean()

# Plot
import matplotlib.pyplot as plt

plt.figure(figsize=(10,6))
plt.plot(seasonal_temperature.index, seasonal_temperature.values, marker='o')

plt.title("Average Temperature by Season")
plt.xlabel("Season")
plt.ylabel("Temperature")
plt.grid(True)

plt.show()