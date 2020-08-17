# Adaptive Online Block Subsampling for Time Series Data (OTSS)
OTSS is an algorithm to subsample time series while retaining their statistical properties.
    
## Documentation

- [Subsampler](#Subsampler)
- [Breakpoint Detection](#Breakpoint-Detection)
- [Competing Subsamplers](#Competing-Subsamplers)
  + [Empirical Bernstein](#Empirical-Bernstein)
  + [Uniform Subsampler](#Uniform-Subsampler)

The pipeline works by simultaneously delimiting the piecewise stationary time series, and subsampling an optimal size subsample from the individual pieces. Multiprocessing is leveraged to ensure scalability.

### Subsampler

There are 4 typers of subsamplers:

```python
online_subsampler(data, queue, return_queue, index_queue,  block_size, epsilon, delta, variable_range, max_iteration = 1000)
```

### Breakpoint Detection

```python
breakpoint_detection(data, queue, threshold = 1, drift = 0, ending = False, show = True, ax = None)
```

### Competing Subsamplers

#### Empirical Bernstein

```python
empirical_bernstein(data, epsilon, delta, variable_range)
```

#### Uniform Subsampler

```python
uniform_sampler(data, rate = 2)
```

## Example

## License
[MIT](https://choosealicense.com/licenses/mit/)
