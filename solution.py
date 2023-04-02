import pandas as pd
import numpy as np

from scipy.stats import expon


chat_id = 392609262

def solution(p: float, x: np.array) -> tuple:
    alpha = 1 - p
    errors = x - x.mean()
    a_errors_exp = expon.ppf(alpha / 2) / (len(x) * min(errors))
    b_errors_exp = expon.ppf(1 - alpha / 2) / (len(x) * min(errors))
    a_errors_final = 0.5 - b_errors_exp
    b_errors_final = 0.5 - a_errors_exp
    return (min(a_errors_exp, b_errors_final) + x.mean()) / 53**2, (max(a_errors_exp, b_errors_final) + x.mean()) / 53**2
