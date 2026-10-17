import numpy as np

def quotient_rule_derivative(g_coeffs: list, h_coeffs: list, x: float) -> float:
    """
    Compute the derivative of f(x) = g(x)/h(x) at point x using the quotient rule.
    
    Args:
        g_coeffs: Coefficients of numerator polynomial in descending order
        h_coeffs: Coefficients of denominator polynomial in descending order
        x: Point at which to evaluate the derivative
        
    Returns:
        The derivative value f'(x)
    """
    # Your code here

    if x == 0: 
        return -1
    m = len(g_coeffs)
    n = len(h_coeffs)
    gx = 0.0
    df_gx = 0.0
    hx = 0.0
    df_hx = 0.0
    gx, df_gx = calc(g_coeffs[:m], x)
    hx, df_hx = calc(h_coeffs[:n], x)

    return (df_gx * hx - gx * df_hx)/hx **2
def calc(coeffs, x):
    p = dp = 0
    for a in coeffs:
        dp = dp * x + p
        p = p * x + a
    return p * x, dp * x + p