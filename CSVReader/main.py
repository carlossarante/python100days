import pandas

if __name__ == '__main__':
    data = pandas.read_csv('2018-squirrel-census-data.csv')
    parsedData = data[['Primary Fur Color']]
    print(parsedData)