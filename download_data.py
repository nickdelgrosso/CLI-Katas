"""
Data download program.

Requires seaborn: pip install seaborn

Get help:  python download_data.py --help
"""

from argparse import ArgumentParser
import seaborn as sns

###  Build the User Interface ###
# Make command-line user interface (i.e. so we can parse arguments from the terminal).
parser = ArgumentParser(description="Seaborn CSV Dataset Downloader")

# Add an argument (i.e. an input) to the program
# in this case, the name of the dataset to download.
parser.add_argument('dataset', help="Name of the dataset to download.", choices=sns.get_dataset_names())

# Add an optional argument to the program, with a default value
parser.add_argument('--output', default="data.csv", help="Filename to save dataset to.")

### Run the User Interface ###

args = parser.parse_args()

### Okay, we have the inputs, now run the script!

dataset_name = args.dataset

print('downloading data...')
df = sns.load_dataset(dataset_name)

print('saving data to {}...'.format(dataset_name))
df.to_csv(args.output)

print('done!')
