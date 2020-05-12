# Online Time Series Subsampler (OTSS)
OTSS is an algorithm to subsample time series while retaining their statistical properties.
    
## Documentation

- [Online Time Series Subsampler](#Online-Time-Series-Subsampler)
- [Breakpoint Detection](#Breakpoint-Detection)
- [Competing Subsamplers](#Competing-Subsamplers)
  + [Empirical Bernstein](#Empirical-Bernstein)
  + [Uniform Subsampler](#Uniform-Subsampler)

The pipeline works by simultaneously delimiting the piecewise stationary time series, and subsampling an optimal size subsample from the individual pieces. Multiprocessing is leveraged to ensure scalability.

### Online Time Series Subsampler

Uses a modification of the Empirical Bernstein to a time series block sample.

```python
online_subsampler(epsilon, delta, variable_range, block_size, data, queue, return_queue, index_queue, max_iteration)
```

### Breakpoint Detection

```python
breakpoint_detection(data, queue, threshold=1, drift=0, ending=False, show=True, ax=None)
```

### Competing Subsamplers

#### Empirical Bernstein

```python
empirical_bernstein(epsilon, delta, variable_range, sample)
```

#### Uniform Subsampler

```python
uniform_sampler(data, rate = 2)
```

## Example

## License
[MIT](https://choosealicense.com/licenses/mit/)
