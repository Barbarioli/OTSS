# OTSS
Online Time Series Subsampling
    
## Documentation

### Pipeline

The subsampler algorithm works in an online fashion by having a pipeline delimiting the piecewise stationary time series, and subsequently choosing the optimal subsample from each piece.

Essentially there are two main algorithms working simultaneously:
Breakpoint detection
Subsampler

#### Subsampler

Uses a modification of the Empirical Bernstein to a time series block sample.

```python
online_subsampler(epsilon, delta, variable_range, block_size, data, queue, return_queue, index_queue, max_iteration)
```

**epsilon:**

