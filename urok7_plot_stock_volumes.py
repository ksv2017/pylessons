"""
    matplotlib needs to be installed: 'python -m pip install matplotlib'

    This script reads 'GOOG.csv' file, calculates monthly volumes by the
    given year and plots a simple bar chart by using matplotlib library.
"""
from datetime import datetime
import calendar as cal
import numpy as np
import matplotlib.pyplot as plot
import matplotlib.ticker as tick


def get_stock_monthly_volumes_per_year(year):
    with open('GOOG.csv', newline='') as csvfilecursor:
        next(csvfilecursor, None).split(',')
        dict_yyyymm_volume = {}
        for line in csvfilecursor:
            tuple_day = tuple(line.split(','))
            dt = datetime.strptime(tuple_day[0], '%Y-%m-%d')
            if dt.year == year:
                if not dt.month in dict_yyyymm_volume.keys():
                    dict_yyyymm_volume[dt.month] = int(tuple_day[6])
                else:
                    dict_yyyymm_volume[dt.month] += int(tuple_day[6])
    return dict_yyyymm_volume


def plot_the_data_using_pylab(dict_yyyymm_volume):
    # initialize the two lists to hold the associated months and volumes
    list_of_x_values = []   # months
    list_of_y_values = []   # volumes
    for key, value in dict_yyyymm_volume.items():
        # convert int month into a name (Jan, Feb, etc)
        month = cal.month_abbr[key]
        list_of_x_values.append(month)
        list_of_y_values.append(value)

    # return <class 'numpy.ndarray'> [0 1 2 3 4 5 6 7 8 9 etc]
    ind = np.arange(len(dict_yyyymm_volume))

    # return a tuple containing a figure and axes object(s)
    fig, ax = plot.subplots()
    ax.set_title('This table shows monthly volumes')
    fig.subplots_adjust(left=0.15)
    # choose the format we want the volumes to be displayed
    ax.yaxis.set_major_formatter(tick.StrMethodFormatter('{x:,.0f}'))
    plot.bar(ind, list_of_y_values, width=0.55)
    plot.xticks(ind, list_of_x_values)
    plot.show()


if __name__ == "__main__":
    plot_the_data_using_pylab(get_stock_monthly_volumes_per_year(2016))
