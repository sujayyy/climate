# src/app_streamlit.py
import streamlit as st
import pandas as pd
from src.emissions_model import baseline_emissions, apply_policies
from src.econ_model import damage_from_temp

st.set_page_config(layout='centered')
st.title('Generative Climate Policy Simulator - Demo')

country = st.selectbox('Country', ['World', 'India', 'United States'])
tax = st.slider('Carbon tax (USD per tCO2)', 0, 200, 50)
renew = st.slider('Renewable subsidy (%)', 0, 50, 10)
afforest = st.slider('Afforestation (million ha)', 0.0, 10.0, 0.5)

policies = {'carbon_tax_usd_per_t': tax, 'renewable_subsidy_pct': renew, 'afforestation_million_ha': afforest}
base = baseline_emissions(country, base_co2=10.0 if country == 'World' else 1.0)
adj = apply_policies(base, policies)

df = pd.DataFrame({'year': base.index, 'baseline': base.values, 'policy_adj': adj.values}).set_index('year')
st.subheader('Emissions trajectories')
st.line_chart(df)

cumulative = df['policy_adj'].sum()
st.write('Cumulative emissions over timeframe (arbitrary units):', float(cumulative))

# toy temperature mapping: cumulative emissions -> delta temp
delta_temp = (cumulative / 10000.0)  # toy scaling
st.write('Estimated global mean temperature increase (toy):', round(delta_temp,3), '°C')

gdp_after = damage_from_temp(delta_temp, gdp_base=1.0)
st.write('Estimated GDP multiplier after damages (toy):', round(gdp_after,3))

st.info('This demo is a simplified educational scaffold. Replace surrogate models and parameters with CMIP/ClimSim-trained emulators for realism.')
