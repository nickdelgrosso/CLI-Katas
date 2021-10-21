"""
Creates a statistics report on any CSV file.

*Note*: Need to install the pandas-profiling package for this to work (pip install pandas-profiling)

Goal: using the argparse package, make it so you can specify a filename to load and the filename name of the report

Example: `python profile_csv.py penguin.csv --out penguin_report.html`
"""

import pandas as pd
from pandas_profiling import ProfileReport

filename = "penguins.csv"
report_filename = 'penguin_report.html'

df = pd.read_csv(filename)
report = ProfileReport(df)
report.to_file(report_filename)