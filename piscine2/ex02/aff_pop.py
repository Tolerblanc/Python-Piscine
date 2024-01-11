from load_csv import load
import matplotlib.pyplot as plt


def parse_population(value):
    if 'B' in value:
        return float(value.replace('B', '')) * 1e9
    elif 'M' in value:
        return float(value.replace('M', '')) * 1e6
    elif 'k' in value:
        return float(value.replace('k', '')) * 1e3
    return float(value)


def main():
    try:
        data = load('../../assets/population_total.csv')
        population_data_numeric = data.set_index(
            'country').applymap(parse_population)

        # Extract data for South Korea and France again
        south_korea_population = population_data_numeric.loc['South Korea']
        france_population = population_data_numeric.loc['France']

        # Select the range from 1800 to 2050 for plotting again
        years = list(map(str, range(1800, 2051)))
        south_korea_population = south_korea_population[years]
        france_population = france_population[years]

        # Create the plot again
        plt.figure(figsize=(10, 6))
        plt.plot(years, south_korea_population,
                 label='South Korea', color='blue')
        plt.plot(years, france_population, label='France', color='green')
        plt.xticks(range(0, len(years), 40))

        # Add title and labels with font sizes for better visibility
        plt.title('Population Projections', fontsize=14)
        plt.xlabel('Year', fontsize=12)
        plt.ylabel('Population', fontsize=12)

        # Convert y-axis labels to millions
        plt.gca().get_yaxis().set_major_formatter(
            plt.FuncFormatter(lambda x, loc: "{:,}M".format(int(x/1e6))))

        # Ensure the legend is displayed
        plt.legend()

        plt.show()

    except Exception as e:
        print(f'Error: {e}')
        return


if __name__ == "__main__":
    main()
