# 📈 Trading Strategy Backtest

This is a simple web application that allows users to upload historical stock price data (CSV), run a trading strategy backtest, and visualize the results.

---

## 🛠️ Tech Stack

- **Frontend**: HTML, JavaScript, [Chart.js](https://www.chartjs.org/)
- **Backend**: Python, [FastAPI](https://fastapi.tiangolo.com/), Pandas
- **Server**: Uvicorn (ASGI server for FastAPI)

---

## 🚀 Features

- 📤 Upload historical stock data as CSV
- ⚙️ Run backtest with a simple strategy (Close > 5-day SMA)
- 📊 Display results in a clean table
- 📈 Plot stock prices with buy signals using Chart.js
- 💹 Display:
  - Total return

---

## Setup & Demonstration

- CD Backend 
- In Terminal Run, **uvicorn main:app --reload**
- Run the Live Server of the index.html file located in Frontend dir.
- Upload CSV
- Run Testing Strategies