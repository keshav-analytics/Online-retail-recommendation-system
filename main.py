import os
import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
file_csv = "OnlineRetail.csv"
if os.path.exists(file_csv):
    df = pd.read_csv(file_csv, encoding="ISO-8859-1")
    print(f"Loaded {file_csv}")
else:
    raise FileNotFoundError("CSV file not found.")

# Data cleaning
df = df.dropna(subset=["CustomerID"])
df = df[df["Quantity"] > 0]
df["InvoiceDate"] = pd.to_datetime(df["InvoiceDate"], errors="coerce")
df = df.dropna(subset=["InvoiceDate"])

# User-Item matrix
user_item = df.pivot_table(
    index="CustomerID",
    columns="StockCode",
    values="Quantity",
    aggfunc="sum"
).fillna(0)

# Item-item similarity
item_sim = cosine_similarity(user_item.T)
item_sim_df = pd.DataFrame(item_sim, index=user_item.columns, columns=user_item.columns)

# Recommendation function
def recommend_items(item_code, top_n=5):
    if item_code not in item_sim_df.index:
        print(f"Item {item_code} not found.")
        return None
    sims = item_sim_df[item_code].sort_values(ascending=False)
    return sims.iloc[1:top_n+1]

# Example usage
example_item = user_item.columns[0]
print(f"\nRecommendations for item {example_item}:")
print(recommend_items(example_item, top_n=5))

# Save sample recommendations
results = []
for item in user_item.columns[:10]:
    recs = recommend_items(item, top_n=5)
    if recs is not None:
        for related_item, score in recs.items():
            results.append({
                "BaseItem": item,
                "RecommendedItem": related_item,
                "Score": score
            })
out_df = pd.DataFrame(results)
out_df.to_csv("sample_recommendations.csv", index=False)
print("Sample recommendations saved to sample_recommendations.csv")

# Visualization
top_products = df.groupby("Description")["Quantity"].sum().sort_values(ascending=False).head(10)
plt.figure(figsize=(8,5))
sns.barplot(x=top_products.values, y=top_products.index)
plt.title("Top 10 Best-Selling Products")
plt.xlabel("Quantity Sold")
plt.tight_layout()
plt.show()
