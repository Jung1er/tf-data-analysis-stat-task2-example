import pandas as pd
import numpy as np

from scipy.stats import expon


chat_id = 392609262

def solution(p: float, x: np.array) -> tuple:
    alpha = 1 - p
    a = expon.ppf(alpha / 2) / (len(x) * min(x - x.mean())) + x.mean()
    b = expon.ppf(1 - alpha / 2) / (len(x) * min(x - x.mean())) + x.mean()
    return min(a,b) / 53**2, max(a,b) / 53**2
