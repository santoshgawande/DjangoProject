import pandas as pd
from stock.models import Equity
import os
def import_data():
    print("os :",os.getcwd())
    df = pd.read_csv((os.getcwd())+"/stock/scrapping/EQ250321.CSV")
    print(df)
    st = Equity.objects.create(
        code = 1,
        name = "ABS",
        open = 233,
        high = 344,
        low = 343,
        close = 534
    )
    st.save()