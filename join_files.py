import re
import glob
import argparse
import pandas as pd


def main():
    parser = argparse.ArgumentParser(description='Joins data files into a single CSV file.')
    parser.add_argument('-o', '--output',
                        default='output.csv',
                        type=str,
                        help='Output filename.')

    args = parser.parse_args()
    args_dict = dict(vars(args).items())

    output = args_dict['output']
    if not output.endswith('.csv'):
        output = '{}.csv'.format(output)
    if not output.startswith('data/'):
        output = 'data/{}'.format(output)

    files = glob.glob('data/*.csv')

    # Combine all files in the list
    combined_csv = pd.concat([pd.read_csv(file, lineterminator='\n') for file in files if re.search(r'[0-9]+\.csv$', file)])
    combined_csv.drop_duplicates(subset=['id']) \
        .to_csv(output, index=False)


if __name__ == '__main__':
    main()
