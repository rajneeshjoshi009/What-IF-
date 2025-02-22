import numpy as np
import pandas as pd

class Simulator:
    def __init__(self):
        self.reset()
    
    def reset(self):
        """Reset simulation parameters"""
        self.results = None
        
    def run_simulation(self, initial_investment, growth_rate, years, volatility):
        """
        Run a Monte Carlo simulation for investment scenarios
        
        Parameters:
        -----------
        initial_investment : float
            Starting investment amount
        growth_rate : float
            Expected annual growth rate (as decimal)
        years : int
            Number of years to simulate
        volatility : float
            Annual volatility/risk factor (as decimal)
        """
        try:
            # Number of simulations
            num_simulations = 1000
            
            # Generate random walks
            returns = np.random.normal(
                loc=(1 + growth_rate),
                scale=volatility,
                size=(num_simulations, years)
            )
            
            # Calculate cumulative returns
            cumulative_returns = np.cumprod(returns, axis=1)
            
            # Calculate investment values over time
            investment_values = initial_investment * cumulative_returns
            
            # Create results dictionary
            self.results = {
                'mean_values': np.mean(investment_values, axis=0),
                'percentile_25': np.percentile(investment_values, 25, axis=0),
                'percentile_75': np.percentile(investment_values, 75, axis=0),
                'worst_case': np.min(investment_values, axis=0),
                'best_case': np.max(investment_values, axis=0),
                'years': list(range(1, years + 1))
            }
            
            return True
            
        except Exception as e:
            print(f"Simulation error: {str(e)}")
            return False
