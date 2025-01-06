import yfinance as yf
import pandas as pd

# Étape 1 : Récupérer les données de l'indice S&P 500
def get_sp500_data(start_date, end_date):
    sp500 = yf.Ticker("^GSPC")  # ^GSPC correspond au S&P 500
    sp500_data = sp500.history(start=start_date, end=end_date)
    sp500_data['Daily_Return'] = sp500_data['Close'].pct_change()  # Rendement quotidien
    return sp500_data

# Exécution pour récupérer les données
start_date = "2010-01-01"
end_date = "2023-01-01"
sp500_data = get_sp500_data(start_date, end_date)
