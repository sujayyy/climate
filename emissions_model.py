# src/emissions_model.py
import numpy as np
import pandas as pd

def baseline_emissions(country='World', start_year=2020, years=50, base_co2=1.0):
    t = np.arange(years)
    # simple baseline: slight growth
    return pd.Series(base_co2 * (1 + 0.005 * t), index=np.arange(start_year, start_year+years))

def apply_policies(baseline, policies):
    out = baseline.copy().astype(float)
    years = len(out)
    tax_effect = min(policies.get('carbon_tax_usd_per_t', 0) / 200, 0.5)
    renew_effect = policies.get('renewable_subsidy_pct', 0) / 100 * 0.3
    afforest_effect = min(policies.get('afforestation_million_ha', 0) * 0.02, 0.2)
    total_reduction = tax_effect + renew_effect + afforest_effect
    total_reduction = min(total_reduction, 0.9)
    # apply a gradual adoption curve (1 - exp decay)
    decay = (1 - np.exp(-0.05 * np.arange(years)))
    out = out * (1 - total_reduction * decay)
    return out

if __name__ == '__main__':
    base = baseline_emissions('World', base_co2=10.0)
    policies = {'carbon_tax_usd_per_t': 50, 'renewable_subsidy_pct': 10, 'afforestation_million_ha': 0.5}
    adj = apply_policies(base, policies)
    print(adj.head())
