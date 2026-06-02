import pandas as pd
import os

df = pd.read_csv("test_data.csv")

print("══════════════════════════════════════")
print("  Test Results Analysis")
print("══════════════════════════════════════\n")

print(f"  Total Tests:    {len(df)}")
print(f"  Column names and dtypes:\n{df.dtypes}\n")
print("  First 5 rows:")
print(df.head(), "\n")

pass_rate = (df["status"] == "pass").mean() * 100
avg_ms = df["duration_ms"].mean()
slowest = df.loc[df["duration_ms"].idxmax()]
fastest = df.loc[df["duration_ms"].idxmin()]

print(f"  Pass Rate:      {pass_rate:.1f}%")
print(f"  Avg Duration:   {avg_ms:,.0f}ms ({avg_ms/1000:.2f}s)")
print(f"  Slowest:        {slowest['test_name']} ({slowest['duration_ms']:,}ms)")
print(f"  Fastest:        {fastest['test_name']} ({fastest['duration_ms']:,}ms)")

print("\n  ── By Module ──")
module_stats = df.groupby("module").agg(
    Tests=("test_name", "count"),
    Pass_Rate=("status", lambda x: (x == "pass").mean() * 100),
    Avg_Duration=("duration_ms", "mean"),
).reset_index()

print(f"  {'Module':<12} {'Tests':>5}  {'Pass Rate':>9}  {'Avg Duration':>12}")
for _, row in module_stats.iterrows():
    print(f"  {row['module']:<12} {int(row['Tests']):>5}    {row['Pass_Rate']:>5.1f}%      {row['Avg_Duration']:>7,.0f}ms")

print("\n  ── Failed Tests ──")
failed = df[df["status"] == "fail"][["test_name", "module", "duration_ms"]]
for _, row in failed.iterrows():
    print(f"  {row['test_name']:<24} {row['module']:<10} {row['duration_ms']:>5,}ms")

print("\n  ── Tests Slower Than 1500ms ──")
slow = df[df["duration_ms"] > 1500][["test_name", "module", "duration_ms"]]
print(slow.to_string(index=False))

print("\n  ── Auth Module ──")
auth = df[df["module"] == "auth"]
print(auth.to_string(index=False))

df["duration_sec"] = df["duration_ms"] / 1000

os.makedirs("output", exist_ok=True)
df_sorted = df.sort_values("duration_ms", ascending=False)
df_sorted.to_csv("output/results_sorted.csv", index=False)
print("\n  Saved: output/results_sorted.csv")
