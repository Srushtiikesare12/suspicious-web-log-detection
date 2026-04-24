import pandas as pd

# Load data
df = pd.read_csv("../data/logs.csv")

print("\n=== LOG DATA ===")
print(df.head())

# Step 1: Failed login detection
failed_logins = df[df['status'] == 401]

ip_counts = failed_logins['ip'].value_counts()

print("\n=== FAILED LOGIN COUNTS ===")
print(ip_counts)

# Step 2: Suspicious IP detection (rule-based)
suspicious_ips = ip_counts[ip_counts >= 3].index

# Step 3: Mark suspicious logs
df['suspicious'] = df['ip'].apply(lambda x: x in suspicious_ips)

print("\n=== SUSPICIOUS ACTIVITY ===")
print(df[df['suspicious'] == True])

# Step 4: Save result
df.to_csv("../data/processed_logs.csv", index=False)

print("\nReport saved successfully!")