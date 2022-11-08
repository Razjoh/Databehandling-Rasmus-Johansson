import pandas as pd
import os


class StockData:
    def __init__(self, data_folder_path: str) -> None:
        self._data_folder_path = data_folder_path

    def stock_dataframe(self, stockname: str) -> list:
        stock_df_list = []

        for path_ending in [
            "_TIME_SERIES_DAILY_ADJUSTED.csv",
            "_TIME_SERIES_INTRADAY_EXTENDED.csv",
        ]:
            # data_folder_path: /c/Users/Rasmus/Documents/Github/Databehandling-Rasmus-Johansson
            # stockname: AAPL, IBM, NVDA, TSLA
            # path_ending: _TIME_SERIES_DAILY_ADJUSTED, _TIME_SERIES_INTRADAY_EXTENDED
            # example results: /c/Users/Rasmus/Documents/Github/Databehandling-Rasmus-Johansson/AAPL_TIME_SERIES_DAILY_ADJUSTED
            path = os.path.join(self._data_folder_path, stockname + path_ending)

            stock = pd.read_csv(path, index_col=0, parse_dates=True)
            stock.index.rename("Date", inplace=True)

            stock_df_list.append(stock)

        return stock_df_list