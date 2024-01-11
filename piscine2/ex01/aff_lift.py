from load_csv import load
import matplotlib.pyplot as plt


def main():
    try:
        data = load('../../assets/life_expectancy_years.csv')
        south_korea_data = data[data['country'] == 'South Korea']
        # Transpose the data for plotting and remove the 'country' row
        south_korea_data_transposed = south_korea_data.drop(
            'country', axis=1).transpose()
        south_korea_data_transposed.columns = ['Life Expectancy']

        # Plot the data
        plt.figure(figsize=(10, 6))
        plt.plot(south_korea_data_transposed,
                 label='South Korea', color='blue', linewidth=2)
        plt.title('South Korea Life Expectancy Projections')
        plt.xlabel('Year')
        plt.ylabel('Life Expectancy')
        plt.xticks(range(0, len(south_korea_data_transposed.index), 40))
        plt.legend()
        plt.grid(False)
        plt.tight_layout()  # Adjust the plot to ensure everything fits without overlapping

        plt.show()

    except Exception as e:
        print(f'Error: {e}')
        return


if __name__ == "__main__":
    main()
