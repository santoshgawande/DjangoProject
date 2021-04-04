import pandas as pd
from stock.models import Equity
import os

# CACHE_TTL = getattr(settings, 'CACHE_TTL', DEFAULT_TIMEOUT)

# # connect to our Redis instance
# redis_instance = redis.StrictRedis(host=settings.REDIS_HOST,
#                                    port=settings.REDIS_PORT, db=0)

# @cache_page(CACHE_TTL)
def import_data():
    row = []
    data = []
    print("os :",os.getcwd())
    df = pd.read_csv((os.getcwd())+"/stock/scrapping/EQ250321.CSV")
    print(df)
    code = df["SC_CODE"]
    name = df["SC_NAME"]
    open =df["OPEN"]
    high = df["HIGH"]
    low = df["LOW"]
    close = df["CLOSE"]
    for i in range(0, len(code)):
        row.append(code[i])
        row.append(name[i])
        row.append(open[i])
        row.append(high[i])
        row.append(low[i])
        row.append(close[i])

        st = Equity.objects.create(
            code = df["SC_CODE"][i],
            name = df["SC_NAME"][i],
            open = df["OPEN"][i],
            high = df["HIGH"][i],
            low =  df["LOW"][i],
            close = df["CLOSE"][i]
        )
        st.save()
        data.append(row)
        row =[]
    
  
    # print(df, df["SC_CODE"], type(df["SC_CODE"]))
    # print(df, type(df.head()))
    # code = df["SC_CODE"]
    # print("code :", code)
    # for row in df:
    #     print("row :", row)

    # st = Equity.objects.create(
    #     code = 1,
    #     name = "ABS",
    #     open = 233,
    #     high = 344,
    #     low = 343,
    #     close = 534
    # )
    # st.save()