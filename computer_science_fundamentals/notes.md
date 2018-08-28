# Computer Science Fundamentals - Brilliant Course

Note: base-2 is implied for `log`.

## Searching (ordered and unordered lists, length `n`)

| Algorithm | Operates on | Worst case | Average case | Best case |
| :-------- | :---------- | ---------- | ------------ | --------- |
| Linear search | Unordered list | `O(n)` | `O(n)` | `O(1)` |
| Binary search | Ordered list | `O(log(n))` | `O(log(n))` | `O(1)` |

## Sorting (unordered lists, length `n`)

| Algorithm | Operates on | Worst case | Average case | Best case | Extra info |
| :-------- | :---------- | ---------- | ------------ | --------- | :--------- |
| Insertion sort | Unordered list | `O(n^2)` | `O(n^2)` | `O(n)` |
| Mergesort | Unordered list | `O(nlog(n))` | `O(nlog(n))` | `O(nlog(n))` |
| Quicksort | Unordered list | `O(n^2)` (for a pre-sorted list, ironically) | `O(nlog(n))` (but ~ 2 - 3 times faster than mergesort in practice) | `O(nlog(n))` (for a randomly-ordered list) | More sensitive to initial ordering of list than mergesort |

## Recursion
**Fibonacci sequence**
* Iterative algorithm much faster, but longer and less beautiful
* Recursive algorithm more appealing but much slower (exponentially increasing calls to itself with increasing `n`)

See my [comparison of Fibonacci sequence recursion and iteration methods](/computer_science_fundamentals/recursion/comparison_of_fibonacci_sequence_recursion_and_iteration_methods.ipynb).
