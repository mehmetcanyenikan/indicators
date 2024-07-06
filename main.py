from data_read import excel_file_reader, csv_file_reader
from RSI import change, gain, loss, avg_gain, avg_loss, RSI


def main():
    name = 'deneme.xlsx'
    path = 'C:/Users/Can/Desktop/technical_indicators/'
    l1 = excel_file_reader(path, name)
    print(l1.data_read_excel)
    l2 = avg_gain(l1.data_read_excel, 14)
    l3 = avg_loss(l1.data_read_excel, 14)
    l4 = RSI(l2.avg_gain_positive, l3.avg_gain_negative)
    print(l4.RSi)


if __name__ == '__main__':
    main()


"""
--- Talib library RSI Output ---
0           NaN
1           NaN
2           NaN
3           NaN
4           NaN
5           NaN
6           NaN
7           NaN
8           NaN
9           NaN
10          NaN
11          NaN
12          NaN
13          NaN
14    55.374511
15    50.068964
16    51.545122
17    50.197093
18    45.138192
19    50.478143
20    44.688396
21    47.467390
22    46.707972
23    47.450106
24    51.054241
25    56.288350
26    51.118753
27    55.575467
28    58.409289
29    54.166397

-- My Output --

0           NaN
1           NaN
2           NaN
3           NaN
4           NaN
5           NaN
6           NaN
7           NaN
8           NaN
9           NaN
10          NaN
11          NaN
12          NaN
13          NaN
14    55.374511
15    50.068964
16    51.545122
17    50.197093
18    45.138192
19    50.478143
20    44.688396
21    47.467390
22    46.707972
23    47.450106
24    51.054241
25    56.288350
26    51.118753
27    55.575467
28    58.409289
29    54.166397
"""

