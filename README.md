# Generative Climate Policy Simulator - Starter Scaffold

This repository is a starter scaffold for the **Generative Climate Policy Simulator** final year project.
It includes:
- basic data fetcher (OWID CO2)
- simple policy -> emissions model
- surrogate model training skeleton (PyTorch)
- Streamlit demo app

## Quick start

1. Create a virtualenv:
   ```
   python -m venv .venv
   source .venv/bin/activate   # Linux / Mac
   .\.venv\Scripts\activate  # Windows (PowerShell)
   pip install -r requirements.txt
   ```

2. Fetch OWID sample:
   ```
   python -m src.data_fetch
   ```

3. Run demo:
   ```
   streamlit run src/app_streamlit.py
   ```

## Structure

- src/: source code
- data/: sample or downloaded datasets
- notebooks/: exploratory analysis

## License
MIT
