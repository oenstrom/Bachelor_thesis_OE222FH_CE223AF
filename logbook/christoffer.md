# Logbook Christoffer

## 2023-03-23

![SQL Query](img/2023-03-23-christoffer.png)

Did an SQL Query from the MSSQL database. This to export the data to a CSV file. The csv file is to be used to import the data into NEO4J.

## 2023-03-24

```python
import os
import pandas as pd

DATA_PATH = 'data/new_friends'

if os.path.exists(f'{DATA_PATH}.parquet'):
    print('Reading data from parquet file')
    data = pd.read_parquet(f'{DATA_PATH}.parquet')
elif os.path.exists(f'{DATA_PATH}.csv'):
    print('Reading data from csv file')
    with open(f'{DATA_PATH}.csv', 'r', encoding='utf-16', errors='ignore') as f:
        chunks = pd.read_csv(f, sep='®', engine='python', iterator=True, chunksize=1000000)
        data = pd.concat(chunk for chunk in chunks)
else:
    raise FileNotFoundError('No data file found')


print(data.head())
print(data.shape)

data.to_parquet(f'{DATA_PATH}.parquet')
```

Used the data from the CSV file to create a parquet file. This is to be used to import the data into NEO4J.

Had to clean up the data a whole ton. 20k rows where somehow added during the export from MSSQL to CSV.

Found a suitable delimiter for the CSV file: ®. This is a character that is not used in the data.
