import pandas as pd
df = pd.read_csv("train.csv")


# First 2 rows
print("First 2 rows:")
print(df.head(2))


# First row
print("\nFirst row:")
print(df.iloc[0])


# Rows 10-19
print("\nRows 10-19:")
print(df.iloc[10:20])


# Column names
print("\nColumn names:")
print(df.columns)


# First 10 values of one column
print("\nFirst 10 popularity values:")
print(df["popularity"].head(10))


# First 10 rows of three columns
print("\nFirst 10 rows of track name, genre, and popularity:")
print(df[["track_name", "track_genre", "popularity"]].head(10))


# Question 1
print(df.groupby("track_genre")["popularity"].mean().sort_values(ascending=False).head(1))

# Question 2
print(df.groupby("explicit")["popularity"].mean())

# Question 3
print(df[(df["explicit"] == True) & (df["popularity"] >= 80)]["track_genre"].value_counts().head(1))

