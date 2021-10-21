"""
Creates a statistics report on any CSV file.

*Note*: Need to install the pandas-profiling package for this to work (pip install pandas-profiling)

Goal: using the argparse package, make it so you can specify a filename to load and the filename name of the report

Example: `python profile_csv.py penguin.csv --out penguin_report.html`
"""

import pandas as pd
from pandas_profiling import ProfileReport
from argparse import ArgumentParser

parser = ArgumentParser(description='Creates a statistics report on any CSV file')
parser.add_argument('filename', help='name of the file')
parser.add_argument('report_filename', help='name of the report')
args = parser.parse_args()

df = pd.read_csv(args.filename)
report = ProfileReport(df)
report.to_file(args.report_filename)
