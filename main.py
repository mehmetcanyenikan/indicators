from data_read import data_read
from RSI import RSI


def main():
    name = 'BTCUSDT-1m-2024-06.csv'
    path = 'C:/Users/Can/Desktop/technical_indicators/'

    l1 = data_read(path, name)
    l2 = RSI(l1.data_read_csv, 10)
    print(l2.I)


if __name__ == '__main__':
    main()
