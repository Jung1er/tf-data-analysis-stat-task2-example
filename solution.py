import pandas as pd
import numpy as np

from scipy.stats import gamma


chat_id = 392609262

def solution(p: float, x: np.array) -> tuple:
    alpha = 1 - p
    n = len(x)
    
    left_gamma = gamma.ppf(q = alpha / 2, a = n, scale = 1 / n)
    right_gamma = gamma.ppf(q = 1 - alpha / 2, a = n, scale = 1 / n)
    
    left = 2 * (left_gamma + x.mean() - 0.5) / (53 ** 2)
    right = 2 * (right_gamma + x.mean() - 0.5) / (53 ** 2)
    
    return (left, right)
