import numpy as np
import matplotlib.pyplot as plt

# Set simulation parameters
initial_investment = 100000  # starting amount
years = 10
simulations = 5000  # number of Monte Carlo runs
np.random.seed(42)

# Asset allocation (DIY portfolio)
allocation = {
    'US Stocks': {'weight': 0.40, 'mean_return': 0.07, 'volatility': 0.15},
    'Int’l Stocks': {'weight': 0.15, 'mean_return': 0.06, 'volatility': 0.17},
    'US Bonds': {'weight': 0.35, 'mean_return': 0.04, 'volatility': 0.06},
    'Short-Term Bonds/Cash': {'weight': 0.10, 'mean_return': 0.02, 'volatility': 0.01}
}

# Simulate portfolio growth over 10 years
portfolio_values = []

for sim in range(simulations):
    value = initial_investment
    for year in range(years):
        annual_return = sum(
            np.random.normal(asset['mean_return'], asset['volatility']) * asset['weight']
            for asset in allocation.values()
        )
        value *= (1 + annual_return)
    portfolio_values.append(value)

# Stats
median_ending_value = np.median(portfolio_values)
percentile_10 = np.percentile(portfolio_values, 10)
percentile_90 = np.percentile(portfolio_values, 90)

# Plot results
plt.figure(figsize=(10, 6))
plt.hist(portfolio_values, bins=75, color='steelblue', edgecolor='black', alpha=0.7)
plt.axvline(median_ending_value, color='red', linestyle='dashed', label=f'Median: ${median_ending_value:,.0f}')
plt.axvline(percentile_10, color='orange', linestyle='dotted', label=f'10th %ile: ${percentile_10:,.0f}')
plt.axvline(percentile_90, color='green', linestyle='dotted', label=f'90th %ile: ${percentile_90:,.0f}')
plt.title('10-Year Simulation of Suggested Portfolio (Starting at $100,000)')
plt.xlabel('Portfolio Value ($)')
plt.ylabel('Frequency')
plt.legend()
plt.grid(True)
plt.show()
