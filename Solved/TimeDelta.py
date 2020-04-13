
from datetime import datetime as dt

t1 = 'Sat 02 May 2015 19:54:36 +0530'
t2 = 'Fri 01 May 2015 13:54:36 -0000'


def time_delta(t1, t2):

    date_format = '%a %d %b %Y %H:%M:%S %z'
    return (int(abs((dt.strptime(t1, date_format) -
                    dt.strptime(t2, date_format)).total_seconds())))


if __name__ == '__main__':
    print(time_delta(t1, t2))

