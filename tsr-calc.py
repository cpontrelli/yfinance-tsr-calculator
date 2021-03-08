import yfinance as yf
import pandas as pd
import csv


# open output file and write column headers
output_file = open('output.csv', 'w', newline='', encoding='utf-8')
csv_writer = csv.writer(output_file)
csv_writer.writerow(['Name',
                     'Ticker',
                     'FYE',
                     'TSR',
                     'Start Price',
                     'End Price',
                     'Dividends'])

with open('input.csv', newline='', encoding='utf8') as companies:
    stonks = csv.DictReader(companies)
    for stonk in stonks:
        print(stonk['Ticker'])
        try:
            # download data
            prices = yf.Ticker(stonk['Ticker'])
            # prices are adjusted for splits. auto_adjust=False excludes dividend adjustments
            fye = pd.to_datetime(stonk['FYE'])
            data = prices.history(start=fye - pd.DateOffset(days=370),
                                  end=fye + pd.DateOffset(days=5),
                                  auto_adjust=False)
            # calc end price
            end_price = data.Close[fye - pd.DateOffset(days=5):fye]
            stonk['End Price'] = end_price.iloc[len(end_price) - 1]

            # calc start price
            start_price = data.Close[:fye - pd.DateOffset(years=1)]
            stonk['Start Price'] = start_price.iloc[len(start_price) - 1]

            # calc dividends
            stonk['Dividends'] = data.Dividends[fye - pd.DateOffset(years=1):fye].sum()

            # calc TSR
            stonk['TSR'] = ((stonk['End Price'] + stonk['Dividends']) / stonk['Start Price']) - 1

        except:
            print('No data for', stonk['Ticker'])

        else:
            csv_writer.writerow([stonk['Name'],
                                 stonk['Ticker'],
                                 stonk['FYE'],
                                 stonk['TSR'],
                                 stonk['Start Price'],
                                 stonk['End Price'],
                                 stonk['Dividends']
                                 ])

    # close output file
    output_file.close()
