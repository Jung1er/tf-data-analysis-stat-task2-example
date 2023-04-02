import pandas as pd
import numpy as np

from scipy.stats import expon


chat_id = 392609262

def solution(p: float, x: np.array) -> tuple:
    alpha = 1 - p
    return 0.5 - expon.ppf(1 - alpha / 2) / (len(x) * min(x) / 53**2), 0.5 - expon.ppf(alpha / 2) / (len(x) * min(x) / 53**2)
