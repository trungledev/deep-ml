import numpy as np

def descriptive_statistics(data: list | np.ndarray) -> dict:
    """
    Calculate various descriptive statistics metrics for a given dataset.
    
    Args:
        data: List or numpy array of numerical values
    
    Returns:
        Dictionary containing mean, median, mode, variance, standard deviation,
        percentiles (25th, 50th, 75th), and interquartile range (IQR)
    """
    # Your code here
    n = len(data)

    mean = 0
    median = 0
    mode = 0
    variance = 0
    standard_deviation = 0
    x_25th_percentile, x_50th_percentile, x_75th_percentile = 0, 0, 0
    interquartile_range = 0
    
    mean = np.mean(data)
    median = np.median(data)

    values, counts = np.unique(data, return_counts=True)
    mode = values[np.argmax(counts)]

    variance = np.var(data, ddof=0)
    standard_deviation = np.std(data, ddof=0)
    
    q1, q2, q3 = np.percentile(data, [25, 50, 75])
    interquartile_range = q3 - q1   

    return {"mean": mean, "median": median, "mode": mode,"variance": variance, "standard_deviation": standard_deviation,"25th_percentile":q1, "50th_percentile":q2, "75th_percentile": q3, "interquartile_range":interquartile_range}
