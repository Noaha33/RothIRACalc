import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter

class ROTH:
    def __init__(
        self,
        return_rate: float,
        startinvest_age: int,
        endinvest_age: int,
        cashin_age: int,
        starting_amount: float,
        annual_contribution: float,
        annual_contribution_growth: float,
        inflation_rate: float = 0.0
    ):
        self.return_rate = return_rate
        self.startinvest_age = startinvest_age
        self.endinvest_age = endinvest_age
        self.cashin_age = cashin_age
        self.starting_amount = starting_amount
        self.annual_contribution = annual_contribution
        self.annual_contribution_growth = annual_contribution_growth
        self.inflation_rate = inflation_rate

    def calculate_balance(self, adjust_for_inflation: bool = False, plot: bool = False):
        growthYears = self.endinvest_age - self.startinvest_age
        stableYears = self.cashin_age - self.endinvest_age
        totalYears = growthYears + stableYears
        balance = self.starting_amount
        annual_contribution = self.annual_contribution
        balances = []
        amountInvested = [] 

        running_total = self.starting_amount
        for year in range(1, growthYears + 1):
            annual_contribution = annual_contribution + annual_contribution * self.annual_contribution_growth
            running_total += annual_contribution
            amountInvested.append(running_total)

        for year in range(growthYears + 1, totalYears + 1):
            amountInvested.append(running_total)
        
        for year in range(1, growthYears + 1):
            balance = balance * (1 + self.return_rate)
            balance += self.annual_contribution
            self.annual_contribution += self.annual_contribution*self.annual_contribution_growth
            balances.append(balance)
        
        for year in range(growthYears+1 , totalYears+1):
            balance = balance * (1 + self.return_rate)
            balances.append(balance)

        balancesNoInflation = balances.copy()
        amountInvestedNoInflation = amountInvested.copy()

        if adjust_for_inflation:
            inflation_factor = [(1 + self.inflation_rate) ** year for year in range(1, totalYears + 1)]
            balances = [b / f for b, f in zip(balances, inflation_factor)]
            amountInvested = [a / f for a, f in zip(amountInvested, inflation_factor)]
            balance = balances[-1]  

        if plot:
            def millions_formatter(x, pos):
                return f'{x * 1e-6:.1f}M'

            years = list(range(self.startinvest_age + 1, self.cashin_age + 1))

            # First figure: Inflation-Adjusted
            if adjust_for_inflation:
                fig1 = plt.figure(figsize=(10, 6))
                plt.plot(years, balances, marker='o', linewidth=2, color='blue', label='Balance (Inflation Adjusted)')
                plt.plot(years, amountInvested, marker='o', linewidth=2, color='red', label='Amount Invested (Inflation Adjusted)')
                plt.title("Roth IRA (Inflation-Adjusted)", fontsize=16, fontweight='bold')
                plt.xlabel("Age", fontsize=14)
                plt.ylabel("Amount ($ Millions)", fontsize=14)
                plt.grid(True, which='both', linestyle='--', linewidth=0.5, alpha=0.7)
                plt.minorticks_on()
                plt.gca().yaxis.set_major_formatter(FuncFormatter(millions_formatter))
                plt.legend()
                plt.tight_layout()

            # Second figure: No Inflation
            fig2 = plt.figure(figsize=(10, 6))
            plt.plot(years, balancesNoInflation, marker='o', linewidth=2, color='purple', label='Balance (No Inflation)')
            plt.plot(years, amountInvestedNoInflation, marker='o', linewidth=2, color='orange', label='Amount Invested (No Inflation)')
            plt.title("Roth IRA (No Inflation)", fontsize=16, fontweight='bold')
            plt.xlabel("Age", fontsize=14)
            plt.ylabel("Amount ($ Millions)", fontsize=14)
            plt.grid(True, which='both', linestyle='--', linewidth=0.5, alpha=0.7)
            plt.minorticks_on()
            plt.gca().yaxis.set_major_formatter(FuncFormatter(millions_formatter))
            plt.legend()
            plt.tight_layout()

            # Now show both figures
            plt.show()

        if adjust_for_inflation:
            return balance, amountInvested[-1], balancesNoInflation[-1], amountInvestedNoInflation[-1]
        else:
            return balance, amountInvested[-1]