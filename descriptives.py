import pandas as pd

df = pd.read_csv('https://health.data.ny.gov/resource/5dtw-tffi.csv')

df.sample(25)