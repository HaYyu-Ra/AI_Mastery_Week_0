from src.data_analysis import load_data, data_quality_check

if __name__ == "__main__":
    data = load_data('C:/Users/hayyu.ragea/AppData/Local/Programs/Python/Python312/pythonapp/path/to/your/solar_farm_data.csv')
    missing_values, outliers = data_quality_check(data)
