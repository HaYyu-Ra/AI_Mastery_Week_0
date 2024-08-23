import matplotlib.pyplot as plt
import seaborn as sns

def plot_time_series(data):
    data.plot(x='Time', y=['GHI', 'DNI', 'DHI', 'Tamb'], kind='line')
    plt.show()

def plot_histograms(data):
    data[['GHI', 'DNI', 'DHI', 'WS', 'Tamb']].hist(bins=30)
    plt.show()

def plot_correlation_heatmap(data):
    sns.heatmap(data[['GHI', 'DNI', 'DHI', 'TModA', 'TModB']].corr(), annot=True)
    plt.show()
