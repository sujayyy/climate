# src/econ_model.py
import numpy as np

def damage_from_temp(delta_temp, gdp_base=1.0):
    # Very simple damage function: linear % GDP loss per degree
    loss_pct = 0.01 * delta_temp  # 1% GDP loss per degree C (toy)
    return gdp_base * (1 - loss_pct)

if __name__ == '__main__':
    print(damage_from_temp(1.5, 1.0))
