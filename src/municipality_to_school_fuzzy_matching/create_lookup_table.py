import pandas as pd
import numpy as np
import chardet as ch
from thefuzz import process as fuzzProcess
from thefuzz import fuzz
import time

with open("data/schools.txt", "r") as read_file:
    # Count unique schools
    schools = set()
    for line in read_file:
        schools.add(line.strip())

df = pd.read_parquet('new_friends.parquet')

unique = df["evaluationName"].unique()

print("STARTED")
# start_time = time.time()
result = [(eName, fuzzProcess.extractOne(str(eName), schools, scorer=fuzz.partial_ratio)[0]) for eName in unique[:10]]

# end_time = time.time()
# print("Time elapsed: ", end_time - start_time)

