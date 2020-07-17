import os
import glob
import pandas as pd

def combine(year, dir):
    os.chdir(dir)

    extension = 'csv'
    all_filenames = [i for i in glob.glob('*.{}'.format(extension))]

    #combine all files in the list
    combined_csv = pd.concat([pd.read_csv(f) for f in all_filenames ])
    #export to csv
    combined_csv.to_csv('{}.csv'.format(year), index=False, encoding='utf-8-sig')

    print('{} done'.format(year))

#combine('2014', '/Users/perezs4/Desktop/Bikes Data/Months/2014')
#combine('2015', '/Users/perezs4/Desktop/Bikes Data/Months/2015')
#combine('2016', '/Users/perezs4/Desktop/Bikes Data/Months/2016')
#combine('2017', '/Users/perezs4/Desktop/Bikes Data/Months/2017')
#combine('2018', '/Users/perezs4/Desktop/Bikes Data/Months/2018')
#combine('2019', '/Users/perezs4/Desktop/Bikes Data/Months/2019')
#combine('2020', '/Users/perezs4/Desktop/Bikes Data/Months/2020')
#combine('2011-2020', '/Users/perezs4/Desktop/Bikes Data/Years')