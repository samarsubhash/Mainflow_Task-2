Python 3.12.4 (tags/v3.12.4:8e8a4ba, Jun  6 2024, 19:30:16) [MSC v.1940 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import pandas as pd
>>> data = pd.read_csv('C:\\Users\\Samar\\Downloads\\01.Data Cleaning and Preprocessing.csv')
>>> type(data)
<class 'pandas.core.frame.DataFrame'>
>>> data.info
<bound method DataFrame.info of     Observation  Y-Kappa  ...  T-Top-Chips-4   SulphidityL-4 
0      31-00:00    23.10  ...         252.077             NaN
1      31-01:00    27.60  ...         251.406           29.11
2      31-02:00    23.19  ...         251.335             NaN
3      31-03:00    23.60  ...         250.312           29.02
4      31-04:00    22.90  ...         249.916           29.01
..          ...      ...  ...             ...             ...
319    10-16:00    23.75  ...         252.947           30.86
320     9-19:00    19.80  ...         252.092           30.70
321     9-20:00    23.01  ...         252.438             NaN
322     9-21:00    24.32  ...         253.176           31.13
323     9-22:00    25.75  ...         253.216             NaN

[324 rows x 23 columns]>
>>> data.describe() #descriptive statistics
          Y-Kappa    ChipRate  ...  T-Top-Chips-4   SulphidityL-4 
count  324.000000  319.000000  ...      323.000000      173.000000
mean    20.635370   14.347937  ...      251.240087       30.411671
std      3.070036    1.499095  ...        1.283432        0.701317
min     12.170000    9.983000  ...      248.359000       29.010000
25%     18.382500   13.358000  ...      250.312000       29.970000
50%     20.845000   14.308000  ...      251.380000       30.370000
75%     23.032500   15.517000  ...      252.323500       30.820000
max     27.600000   16.958000  ...      254.122000       32.840000

[8 rows x 22 columns]
>>> data = data.drop_duplicates()
>>> data
    Observation  Y-Kappa  ...  T-Top-Chips-4   SulphidityL-4 
0      31-00:00    23.10  ...         252.077             NaN
1      31-01:00    27.60  ...         251.406           29.11
2      31-02:00    23.19  ...         251.335             NaN
3      31-03:00    23.60  ...         250.312           29.02
4      31-04:00    22.90  ...         249.916           29.01
..          ...      ...  ...             ...             ...
298    12-09:00    20.90  ...         251.833           30.29
299    12-10:00    24.98  ...         251.614           30.47
300    12-11:00    21.00  ...         251.197             NaN
301    12-12:00    21.40  ...         251.324           30.46
307    31-05:00    20.89  ...         250.084             NaN

[301 rows x 23 columns]
data.isnull()
     Observation  Y-Kappa  ...  T-Top-Chips-4   SulphidityL-4 
0          False    False  ...           False            True
1          False    False  ...           False           False
2          False    False  ...           False            True
3          False    False  ...           False           False
4          False    False  ...           False           False
..           ...      ...  ...             ...             ...
298        False    False  ...           False           False
299        False    False  ...           False           False
300        False    False  ...           False            True
301        False    False  ...           False           False
307        False    False  ...           False            True
