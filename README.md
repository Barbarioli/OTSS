# Online Time Series Subsampling (OTSS)
OTSS is an algorithm to subsample time series while retaining their statistical properties.
    
## Documentation

- [Online Time Series Subsampler](#Online-Time-Series-Subsampler)
- [Breakpoint Detection](#Breakpoint-Detection)
- [Competing Subsamplers](#Competing-Subsamplers)
  + [Empirical Bernstein](#Empirical-Bernstein)
  + [Uniform Subsampler](#Uniform-Subsampler)

The pipeline works by simultaneously delimiting the piecewise stationary time series. and subsampling from them an optimal size subsample. Multiprocessing is leveraged to ensure scalability.

### Online Time Series Subsampler

Uses a modification of the Empirical Bernstein to a time series block sample.

```python
online_subsampler(epsilon, delta, variable_range, block_size, data, queue, return_queue, index_queue, max_iteration)
```
**epsilon:**

### Breakpoint Detection

### Competing Subsamplers

#### Empirical Bernstein

#### Uniform Subsampler

## License
[MIT](https://choosealicense.com/licenses/mit/)
