
from datetime import date

if __name__ == '__main__':
    start = date(1901, 1, 1)
    end = date(2000, 12, 31)

    start_ord = start.toordinal()
    end_ord = end.toordinal()

    cnt = 0

    for date_ord in range(start_ord, end_ord):
        d = date.fromordinal(date_ord)
        if d.weekday() == 6 and d.day == 1:
            cnt += 1

    print(cnt)
