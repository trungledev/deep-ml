def empirical_pmf(samples):
    """
    Given an iterable of integer samples, return a list of (value, probability)
    pairs sorted by value ascending.
    """
    # TODO: Implement the function
    values = list(set(samples))
    return [(i, (samples.count(i) / len(samples))) for i in values]
