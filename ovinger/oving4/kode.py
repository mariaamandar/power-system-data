import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("ovinger/oving4/load_data.csv")
df["Time(Local)"] = pd.to_datetime(df["Time(Local)"],format="%d.%m.%Y %H:%M:%S %z", utc=True) # %z representerer tidssoneforskyvningen
df = df.set_index("Time(Local)")
df =df.tz_convert("Europe/Oslo")

df["Production"] = df["Production"].str.replace(",", ".").astype(float)
df["Consumption"] = df["Consumption"].str.replace(",", ".").astype(float)

print(df.head())

print(df.index[0])

