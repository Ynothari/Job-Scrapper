import pandas as pd

# Load scraped jobs
df = pd.read_csv("jobs.csv")

# Filter by keywords in title or description
keywords = ["intern", "cloud", "devops", "aws", "ai"]
mask = df["title"].str.contains('|'.join(keywords), case=False, na=False) | \
       df["description"].str.contains('|'.join(keywords), case=False, na=False)

filtered_jobs = df[mask]

# Save filtered results
filtered_jobs.to_csv("filtered_jobs.csv", index=False)
print(f"✅ Found {len(filtered_jobs)} matching jobs.")
