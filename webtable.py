import requests
import pandas as pd
import numpy as np

url = 'https://en.wikipedia.org/wiki/List_of_colors:_A%E2%80%93F'

class Webtable:
    def showTable(self):
        colors_df = pd.read_html(url)
        shwtable = colors_df[0]
        print("Webtable display as follows :",shwtable)

        tbl = np.array(shwtable)
        print("Dimension in form of ROW and COLUMN are as follows: ", tbl.shape)

        print("Total rows present in webtable :",len(tbl))
        for i in range(len(tbl)):
            print("Data from  "+str(i)+" row are as follows:", tbl[i])

        print("Total column present in webtable :", len(tbl[0]))
        for i in range(len(tbl)):
            for j in range(len(tbl[i])):
                print(" "+str(i)+" ")
                print("Data from "+str(j)+" column are", tbl[i][j])
            print()

    def webHeader(self):
        webpage = requests.get(url)
        for key in webpage.headers:
            print(key, ": ", webpage.headers[key])
            #  OR ....print(webpage.request.headers)


obj = Webtable()
print(obj.showTable())
print(obj.webHeader())

    
# ========================================================================================
# url3 = 'https://ahdb.org.uk/cereals-oilseeds-markets'
# url2 = 'https://en.wikipedia.org/api/rest_v1/page/summary/Lists_of_colors'
# print("The columns present in that table are as follows: ", showtable.columns.values)
