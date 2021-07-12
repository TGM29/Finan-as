import pandas as pd
import pandas_datareader as data

ibov = data.get_data_yahoo('^BVSP')
