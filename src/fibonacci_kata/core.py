def fibonacci(n: int) -> int:
    """
    Compute the n-th term of the Fibonacci sequence (recursively)

    Args:
        n (int): Index of the desired term (must be a positive integer or zero)

    Returns: 
        int: Value of F(n)

    Raises:
        TypeError: If n is not an integer or a boolean
        ValueError: If n is negative
    """

    if not isinstance(n, int) or isinstance(n, bool):
        raise TypeError("n must be an int")
    if n < 0:
        raise ValueError("n must be positive or null")

    if n == 0:
        return 0
    if n == 1:
        return 1
    
    return fibonacci(n-1) + fibonacci(n-2)

    