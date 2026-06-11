# Search Benchmark Results

| Round | N | Binary Search Time | Linear Search Time |
|---|---:|---:|---:|
| Round 1 | 100,000 | 0.000169 ms | 0.019064 ms |
| Round 2 | 5,000,000 | 0.001596 ms | 1.406991 ms |

Expected `O(n)` behavior for linear search. If `N` increases by 50x, the amount of work in the worst case also increases by about 50x because the method checks elements one by one until it finds the target or reaches the end.

Expected `O(log n)` behavior for binary search. Each comparison removes about half of the remaining search space, so increasing from `100,000` to `5,000,000` only adds a small number of extra loop iterations.

What I observed matches the overall expectation: linear search became much slower when `N` increased, while binary search stayed extremely fast. The measured linear search time rose from `0.019064 ms` to `1.406991 ms`, showing clear growth with input size. Binary search also increased slightly, from `0.000169 ms` to `0.001596 ms`, but the absolute time stayed tiny compared with linear search.

These timings still have caveats. JVM warmup, CPU cache effects, timer precision, background system activity, and constant factors can all affect small benchmark results, especially for very fast operations like binary search. Big-O still matters because it describes the growth trend as input size increases: constants can hide differences at small sizes, but the slower growth rate of `O(log n)` becomes much more important as data gets large.
