from ydata_quality import DataQuality
import pandas as pd


if __name__ == '__main__':
    df = pd.read_csv('datamovie_short.csv', header=None, dtype=str)
    print(df)
    dq = DataQuality(df=df)
    
    results = dq.evaluate()
    dq.get_warnings(test='Duplicate Columns')[0].df


