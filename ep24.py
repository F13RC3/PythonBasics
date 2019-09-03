#import urllib.request
from urllib import request
#http://real-chart.finance.yahoo.com/table.csv?s=GOOG&d=8&e=2&f=2014&g=d&a=2&b=27&c=2014&ignore=.csv

goog_url='http://insight.dev.schoolwires.com/HelpAssets/C2Assets/C2Files/C2ImportCalEventSample.csv'

def  download_stock_data(csv_url):
    response = request.urlopen(csv_url)
    csv = response.read()
    csv_str = str(csv)
    lines = csv_str.split("\\n")
    dest_url = r'goog.csv'
    fx=open(dest_url,"w")
    for line in lines:
        fx.write(line+"\n")
    fx.close()
download_stock_data(goog_url)