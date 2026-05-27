"""
Black-Scholes pricing and implied volatility inversion.

Used as a baseline for comparison with Heston prices and to convert
between market option prices and implied volatility quotes.
"""


import numpy as np
from scipy import stats, optimize

def black_scholes_price(S: float, K: float, T: float, r: float, sigma: float, option_type: str = "call") -> float:
    """
    Return the Black-Scholes price of a European option.

    Parameters
    ----------
    S : float
        Spot price.
    K : float
        Strike price.
    T : float
        Time to maturity (years).
    r : float
        Continuously compounded risk-free rate.
    sigma : float
        Constant volatility.
    option_type : {"call", "put"}
    """
    raise NotImplementedError


def implied_vol(price: float, S: float, K: float, T: float, r: float, option_type: str = "call") -> float:
    """
    Invert Black-Scholes to find implied volatility via Brent's method.

    Parameters
    ----------
    price : float
        Observed market (or model) option price.
    """
    raise NotImplementedError