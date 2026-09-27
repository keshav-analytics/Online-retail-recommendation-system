# Online-retail-recommendation-system
# Online Retail Recommendation System

A product recommendation engine built on real-world e-commerce transaction data. The system uses **item-based collaborative filtering** (cosine similarity) to recommend products that are frequently purchased together, based on customer purchase history.

## 📌 Overview

This project analyzes the **Online Retail dataset** (UK-based e-commerce transactions) to:
- Clean and preprocess raw transactional data
- Build a customer–product purchase matrix
- Compute item-to-item similarity using cosine similarity
- Generate top-N product recommendations for any given item
- Visualize the top 10 best-selling products

## 🛠️ Tech Stack

- **Python 3**
- **pandas** – data cleaning and manipulation
- **scikit-learn** – cosine similarity computation
- **matplotlib / seaborn** – data visualization

## 📂 Dataset

The dataset (`OnlineRetail.csv`) contains transactional records with the following key columns:
- `CustomerID` – unique customer identifier
- `StockCode` – unique product code
- `Description` – product name
- `Quantity` – units purchased
- `InvoiceDate` – date of transaction

## ⚙️ How It Works

1. **Data Cleaning** – Removes missing customer IDs, invalid quantities, and invalid dates.
2. **User-Item Matrix** – Pivots data into a matrix of customers vs. products (quantity purchased).
3. **Similarity Computation** – Uses cosine similarity to find products that behave similarly across customers.
4. **Recommendation Function** – Given a product code, returns the top N most similar products.
5. **Visualization** – Plots the top 10 best-selling products by quantity sold.

## 🚀 How to Run

```bash
# 1. Clone the repository
git clone <your-repo-url>
cd Retail_project2

# 2. Install dependencies
pip install -r requirements.txt

# 3. Run the script
python main.py
```

## 📊 Sample Output

The script prints top-5 recommended products for a sample item and saves results to `sample_recommendations.csv`. It also displays a bar chart of the top 10 best-selling products.

## 📈 Future Improvements

- Add a popularity-based fallback for new customers
- Add evaluation metrics (e.g., precision@k)
- Build a simple web interface for interactive recommendations

## 👤 Author

Keshav Choudhary
