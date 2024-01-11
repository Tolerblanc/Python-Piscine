from load_csv import load
import matplotlib.pyplot as plt
import pandas as pd


def main():
    income_df = load(
        '../../assets/income_per_person_gdppercapita_ppp_inflation_adjusted.csv')
    life_expectancy_df = load('../../assets/life_expectancy_years.csv')

    income_1900 = income_df[['country', '1900']].rename(
        columns={'1900': 'Income'})
    life_expectancy_1900 = life_expectancy_df[['country', '1900']].rename(
        columns={'1900': 'Life Expectancy'})

    # Merge the two datasets on the country column
    merged_data_1900 = pd.merge(
        income_1900, life_expectancy_1900, on='country')

    # Convert income to numeric, as it may contain strings like 'k' for thousands
    merged_data_1900['Income'] = pd.to_numeric(
        merged_data_1900['Income'].replace('k', 'e3', regex=True))

    # Drop any rows with NaN values to avoid errors during plotting
    merged_data_1900.dropna(inplace=True)

    plt.figure(figsize=(10, 6))
    plt.scatter(x=merged_data_1900['Income'],
                y=merged_data_1900['Life Expectancy'], alpha=0.6, color='blue', marker='.')

    # Adding title and labels
    plt.title('Life Expectancy vs Gross Domestic Product in 1900')
    plt.xlabel('Gross domestic product')
    plt.ylabel('Life Expectancy')

    # Set the x-axis scale to logarithmic and customize the ticks as requested
    plt.xscale('log')
    plt.xticks([300, 1000, 10000], ['300', '1k', '10k'])

    # Adding grid lines for better readability
    # plt.grid(True, which="both", ls="--", linewidth=0.5)
    plt.grid(False)

    # Display the plot
    plt.show()


if __name__ == "__main__":
    main()
