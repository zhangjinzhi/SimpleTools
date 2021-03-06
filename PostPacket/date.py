# coding:utf-8
import datetime
import calendar
from datetime import date, timedelta as td

def get_date_list(begin_date,end_date):
    begin_date = begin_date.split('-')
    end_date = end_date.split('-')
    date_list = []
    begin_year = int(begin_date[0])
    begin_month = int(begin_date[1])
    begin_day = int(begin_date[2])
    end_year = int(end_date[0])
    end_month = int(end_date[1])
    end_day = int(end_date[2])
    #法定节假日,不可以交易,应排除
    exclude_date = ['2016-04-02','2016-04-03','2016-04-04','2016-04-30','2016-05-01','2016-05-02','2016-06-09','2016-06-10','2016-06-11','2016-06-12','2016-09-15','2016-09-16','2016-09-17','2016-09-18']
    d_begin = date(begin_year,begin_month,begin_day)
    d_end = date(end_year,end_month,end_day)
    delta = d_end - d_begin
    date_list = []
    for i in range(delta.days + 1):
        date_temp = str(d_begin + td(days=i))
        if date_temp not in exclude_date:
            date_list.append(date_temp)
    date_list = tick_weekend(date_list)
    return date_list

def tick_weekend(date_list):
    date_without_weekend = []
    for date in date_list:
        date_temp = date.split("-")
        weekday = calendar.weekday(int(date_temp[0]),int(date_temp[1]),int(date_temp[2]))
        if weekday != 5 and weekday != 6:
            date_without_weekend.append(date)
    return date_without_weekend

if __name__ == "__main__":
    #仅供测试
    # begin_date = str(input("begin_date:  "))  #python3
    # end_date = str(input("end_date:   "))
    # begin_date = raw_input("begin_date:  ")
    # end_date = raw_input("begin_date:  ")
    begin_date = "2016-04-11"
    end_date = "2016-05-14"
    result_list = get_date_list(begin_date,end_date)
    print result_list
