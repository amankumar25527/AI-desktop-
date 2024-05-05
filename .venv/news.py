from GoogleNews import GoogleNews
import pandas as pd

def news():
    news=GoogleNews(period='id')
    news.search("India")
    result=news.result()
    data=pd.DataFrame.from_dict(result)
    data=data.drop(columns=["img"])
    print(data.head())
    data.head()

    for i in result:
        print(i["title"])