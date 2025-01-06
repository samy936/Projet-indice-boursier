import yfinance as yf
import pandas as pd

#1 Étape 1 : Récupérer les données de l'indice S&P 500
def get_sp500_data(start_date, end_date):
    sp500 = yf.Ticker("^GSPC")  # ^GSPC correspond au S&P 500
    sp500_data = sp500.history(start=start_date, end=end_date)
    sp500_data['Daily_Return'] = sp500_data['Close'].pct_change()  # Rendement quotidien
    return sp500_data

# Exécution pour récupérer les données
start_date = "2010-01-01"
end_date = "2023-01-01"
sp500_data = get_sp500_data(start_date, end_date)

#2 Visualisation données
import matplotlib.pyplot as plt

# Étape 2 : Visualiser les données du S&P 500
def visualize_sp500(sp500_data):
    plt.figure(figsize=(10, 6))
    plt.plot(sp500_data['Close'], label="S&P 500 (Clôture)", color="blue")
    plt.title("Évolution de l'indice S&P 500")
    plt.xlabel("Date")
    plt.ylabel("Prix de clôture")
    plt.legend()
    plt.show()

# Visualisation
visualize_sp500(sp500_data)
 
# 3 Analyse rendements
# Étape 3 : Analyser les rendements quotidiens
def analyze_returns(sp500_data):
    mean_return = sp500_data['Daily_Return'].mean()
    volatility = sp500_data['Daily_Return'].std()

    print(f"Rendement moyen quotidien : {mean_return:.5f}")
    print(f"Volatilité quotidienne : {volatility:.5f}")

    # Histogramme des rendements quotidiens
    plt.figure(figsize=(10, 6))
    plt.hist(sp500_data['Daily_Return'].dropna(), bins=50, alpha=0.7, color="orange")
    plt.title("Distribution des rendements quotidiens du S&P 500")
    plt.xlabel("Rendement quotidien")
    plt.ylabel("Fréquence")
    plt.show()

# Analyse des rendements
analyze_returns(sp500_data)

#4
# Étape 4 : Backtesting d'une stratégie simple
def backtest_strategy(sp500_data):
    """
    Stratégie : Acheter les jours où le S&P 500 a baissé de plus de 1% la veille.
    """
    sp500_data['Signal'] = sp500_data['Daily_Return'].shift(1).apply(lambda x: 1 if x < -0.01 else 0)
    sp500_data['Strategy_Return'] = sp500_data['Daily_Return'] * sp500_data['Signal']

    # Calcul des rendements cumulés
    cumulative_strategy_return = (1 + sp500_data['Strategy_Return']).cumprod()
    cumulative_market_return = (1 + sp500_data['Daily_Return']).cumprod()

    # Visualisation des performances
    plt.figure(figsize=(10, 6))
    plt.plot(cumulative_strategy_return, label="Rendement de la stratégie", color="green")
    plt.plot(cumulative_market_return, label="Rendement du marché (Buy & Hold)", color="blue")
    plt.title("Comparaison des rendements")
    plt.legend()
    plt.show()

    print("Performance finale :")
    print(f"Stratégie : {cumulative_strategy_return.iloc[-1]:.2f}")
    print(f"Marché : {cumulative_market_return.iloc[-1]:.2f}")

# Backtesting
backtest_strategy(sp500_data)
