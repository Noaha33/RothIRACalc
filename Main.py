import Calculator

# Annual return rate of the Roth IRA 
return_rate = 0.1

# Age when you start investing
startinvest_age = 18

# Age when you stop contributing 
endinvest_age = 35

# Age when you take the money out of the Roth IRA
cashin_age = 65

# Starting amount already in the Roth IRA
starting_amount = 10000

# How much you contribute each year
annual_contribution = 7000

# How much more you can contribute each year 
annual_contribution_growth = 0.03

# Whether to adjust the final balance for inflation (True or False)
adjust_for_inflation = True

# Annual inflation rate 
inflation_rate = 0.025

# Choose to plot output (True or False)
plot = False

def main():
    my_roth = Calculator.ROTH(
        return_rate=return_rate,
        startinvest_age=startinvest_age,
        endinvest_age=endinvest_age,
        cashin_age=cashin_age,
        starting_amount=starting_amount,
        annual_contribution=annual_contribution,
        annual_contribution_growth = annual_contribution_growth,
        inflation_rate=inflation_rate
    )

    if adjust_for_inflation:
        final_balance, amount_invested, balance_no_inflation, amount_invested_no_inflation = my_roth.calculate_balance(adjust_for_inflation=True, plot=plot)
        print(f"Final Balance: ${final_balance:,.2f} (Inflation-Adjusted) | ${balance_no_inflation:,.2f} (No Inflation)")
        print(f"Total Amount Invested: ${amount_invested:,.2f} (Inflation-Adjusted) | ${amount_invested_no_inflation:,.2f} (No Inflation)")

    else:
        final_balance, amount_invested = my_roth.calculate_balance(adjust_for_inflation=False, plot=plot)
        print(f"Final Balance: ${final_balance:,.2f}")
        print(f"Total Amount Invested: ${amount_invested:,.2f}")

if __name__ == "__main__":
    main()