import pandas as pd

df = pd.read_csv("../data/logs.csv")

print("\nTop Active IPs:")
print(df['ip'].value_counts())

print("\nStatus Code Distribution:")
print(df['status'].value_counts())