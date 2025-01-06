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
