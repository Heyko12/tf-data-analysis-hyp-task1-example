import pandas as pd
import numpy as np


chat_id = 1012233839

def solution(x_success: int, 
             x_cnt: int, 
             y_success: int, 
             y_cnt: int) -> bool:
    return (y_success/y_cnt - x_success/x_cnt < 0.05)

