import numpy as np
from scipy.optimize import minimize

# Funkcja celu - maksymalizacja zysku
# Przekształcamy problem w minimalizację -f(p1, p2, p3), ponieważ scipy.optimize.minimize minimalizuje funkcję
def profit_function(prices):
    p1, p2, p3 = prices
    profit = (
        (6000 - 0.3 * p1 + 0.05 * p2) * (p1 - 300) +
        (25000 - 1.5 * p2 + 0.15 * p1 + 0.25 * p3) * (p2 - 140) +
        (30000 - 4 * p3 + 0.5 * p2) * (p3 - 60)
    )
    return -profit  # Negacja, aby zmienić maksymalizację w minimalizację

# Ograniczenia wynikające z maksymalnej produkcji
def constraint_1(prices):
    p1, p2, p3 = prices
    return 4000 - (6000 - 0.3 * p1 + 0.05 * p2)  # Popyt na produkt 1 ≤ 4000

def constraint_2(prices):
    p1, p2, p3 = prices
    return 10000 - (25000 - 1.5 * p2 + 0.15 * p1 + 0.25 * p3)  # Popyt na produkt 2 ≤ 10000

def constraint_3(prices):
    p1, p2, p3 = prices
    return 16000 - (30000 - 4 * p3 + 0.5 * p2)  # Popyt na produkt 3 ≤ 16000

# Początkowe wartości cen
initial_prices = [500, 500, 500]

# Definicja ograniczeń
constraints = (
    {'type': 'ineq', 'fun': constraint_1},
    {'type': 'ineq', 'fun': constraint_2},
    {'type': 'ineq', 'fun': constraint_3}
)

# Rozwiązanie problemu optymalizacyjnego
result = minimize(profit_function, initial_prices, constraints=constraints, method='SLSQP')

# Wynik optymalizacji
if result.success:
    optimal_prices = result.x
    print(f"Optymalne ceny: p1 = {optimal_prices[0]:.2f}, p2 = {optimal_prices[1]:.2f}, p3 = {optimal_prices[2]:.2f}")
    print(f"Maksymalny zysk: {-result.fun:.2f}")
else:
    print("Nie udało się znaleźć optymalnego rozwiązania.")
