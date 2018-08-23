# Computer Science Fundamentals - Brilliant Course
## Searching (ordered and unordered lists, length `n`)
**Linear search (unordered list)**
* Best case - 1 comparison
* Worst case - `n` comparisons
* Average case - `(n + 1) / 2` comparisons

**Binary search (ordered list)**
* Best case - `O(1)`
* Worst case - `O(log(n))`
* Average case - `O(log(n))`

## Sorting (unordered lists, length `n`)
**Insertion sort**
* Best case - `O(n)`
* Average case - `O(n^2)`
* Worst case - `O(n^2)`

**Mergesort**
* Best case - `nlog(n)`
* Average case - `nlog(n)`
* Worse case - `nlog(n)`

**Quicksort**
* Best case - `nlog(n)` (for a randomly-ordered list)
* Average case - `nlog(n)` (but ~ 2 - 3 times faster than mergesort in practice)
* Worse case - `n^2` (for a pre-sorted list, ironically)
* More sensitive to initial ordering of list than mergesort

## Recursion
**Fibonacci sequence**
* Iterative algorithm faster, but longer and less beautiful
* Recursive algorithm more appealing but much slower (exponentially increasing calls to itself with increasing `n`)


Note: base-2 is implied for `log` here
