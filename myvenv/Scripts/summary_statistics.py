from src.data_analysis import load_data, summary_statistics

if __name__ == "__main__":
    data = load_data('path/to/your/solar_farm_data.csv')
    stats = summary_statistics(data)
    print(stats)
