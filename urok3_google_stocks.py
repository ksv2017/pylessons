# https://finance.yahoo.com/quote/GOOG/history?p=GOOG
def get_dict_yyyymm_volume(csvfilename):
    with open(csvfilename, newline='') as csvfilecursor:
        next(csvfilecursor, None).split(',')
        # Date, Open, High, Low, Close, Adj Close, Volume
        dict_yyyymm_volume = {}
        for line in csvfilecursor:
            tuple_day = tuple(line.split(','))
            # 2012-10-17, 369.571289, 375.726257, 367.738220, 375.304016, 375.304016, 4615500
            yyyymm = tuple_day[0][0:7]
            # 2012-10
            if not dict_yyyymm_volume.__contains__(yyyymm):
                dict_yyyymm_volume[yyyymm] = int(tuple_day[6])
            else:
                dict_yyyymm_volume[yyyymm] += int(tuple_day[6])
    return dict_yyyymm_volume


def get_the_best_yyyymm(dict_yyyymm_volume):
    max_volume = 0
    best_month = None
    for key, value in dict_yyyymm_volume.items():
        if value > max_volume:
            max_volume = value
            best_month = key

    print('The best year-month was:', best_month, ', where volume was:', max_volume)


dict_yyyymm_volume = get_dict_yyyymm_volume('GOOG.csv')
get_the_best_yyyymm(dict_yyyymm_volume)
