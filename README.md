# 📈 Stock Market Forecasting on EGX30
### Using LSTM & Arabic Sentiment Analysis

> A dual-model AI framework for forecasting the Egyptian EGX-30 stock market index — combining technical analysis with Arabic NLP.

**Helwan University — Faculty of Computing and Artificial Intelligence**  
Ziad Hany · Ziad Mohamed Hassan · Mazen Mohamed · Yasmeen Elsayed · Tasneem Ahmed · Ziad Abdelalem

---

## 🧠 Overview

This project presents two independent yet complementary AI-driven models:

| Model | Purpose | Output |
|---|---|---|
| **LSTM Classifier** | Technical analysis on historical price data | Buy / Hold / Sell signals |
| **CAMeL BERT** | Arabic financial news sentiment analysis | Positive / Neutral / Negative |

---

## 🏗️ System Architecture

### Model 1 — LSTM-Based Trading Signal Classification

- **Data:** EGX-30 historical data from Investing.com & Yahoo Finance (2008–2025)
- **Features:** RSI, MACD, ADX, ATR, ROC computed via sliding windows
- **Input:** 10-day sequences of technical indicators
- **Architecture:** LSTM (50 units) → Dropout → Dense (Softmax)
- **Training:** Adam optimizer, Categorical Cross-Entropy, 25 epochs, 80/20 split

**Signal Labeling Rules:**
- RSI < 30 → **Buy**
- RSI > 70 → **Sell**
- ADX < 20 → **Hold**

### Model 2 — CAMeL BERT Sentiment Analysis

- **Data:** Arabic financial news scraped from Mubasher Misr, manually labeled
- **Model Base:** `CAMeL-Lab/bert-base-arabic-camelbert-mix`
- **Preprocessing:** Arabic normalization, punctuation/URL removal, CAMeL BERT tokenization
- **Training:** 3 epochs, lr = 2e-5, batch size = 16, Hugging Face Transformers on Google Colab

---

## 📊 Results

### LSTM Classifier
| Metric | Value |
|---|---|
| Accuracy | 64.71% |
| Precision (macro) | 0.70 |
| Recall (macro) | 0.80 |
| F1-score (macro) | 0.67 |

### CAMeL BERT Sentiment Model
| Metric | Value |
|---|---|
| Accuracy | 82% |
| Precision (macro) | 0.80 |
| Recall (macro) | 0.84 |
| F1-score (macro) | 0.80 |

---

## 🔬 Experiments & Model Comparisons

Several approaches were explored before settling on the final architecture:

| Model | RMSE | MAPE (%) | Notes |
|---|---|---|---|
| CNN Regression | High | High | Overfitting — discarded |
| LSTM Regression | 10,047.84 | 28.17 | Poor volatility generalization |
| ARIMA (Tuned 3,2,3) | 2,909.38 | 8.54 | Decent baseline, fails on volatility |
| Hybrid ARIMA–LSTM | 2,945.41 | 8.69 | Strong signal |
| **LSTM Classification** | **0.8402** | **13.77** | ✅ Best practical performance |

---

## 🗂️ Data Sources

- [Investing.com](https://www.investing.com/indices/egx30-historical-data) — EGX-30 historical OHLCV data (2008–2025)
- [Yahoo Finance](https://finance.yahoo.com/) — Cross-validation of prices
- [Mubasher Misr](https://www.mubasher.info) — Arabic financial news articles

---

## 🛠️ Tech Stack

- **Deep Learning:** TensorFlow / Keras
- **NLP:** Hugging Face Transformers, CAMeL BERT
- **Statistical:** ARIMA / SARIMA (statsmodels)
- **Data:** Pandas, NumPy, Scikit-learn
- **Environment:** Google Colab

---

## 🚀 Future Work

- Integrate both models into a **real-time decision-support dashboard**
- Extend sentiment analysis to **English sources and social media**
- Apply the framework to **EGX-70 and EGX-100** indices

---
