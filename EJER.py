import pandaS as pd
from datetime import datetime

def get_month_format(number):
    if number < 10:
        return '0' + str(number)
    else:
        return str(number)


data = pd.DataFrame([[datetime(year=2019, month=8, day=3), 1],
                     [datetime(year=2019, month=8, day=4), 2],
                     [datetime(year=2019, month=9, day=3), 3]],
                    columns=['created_at', 'id'])

data['month'] = data['created_at'].apply(lambda date: '{y}-{m}'
                                         .format(y=date.year,
                                                 m=get_month_format(date.month)))

data.drop('created_at', axis=1, inplace=True)

data.sort_values(by=['month'], inplace=True)
gp = data.groupby(by='month').aggregate({'id': 'count'})
df = pd.DataFrame(gp)

print(df.loc['2019-08'], 'id')