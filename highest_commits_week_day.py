#!/usr/bin/python2.7

# Martha Cassetti's Exploratory Data Analysis 2-2b
from datetime import datetime,timedelta
import shlex
import os
import numpy as np
import matplotlib.pyplot as plt
# Main Script
def main():
    """ Takes Question 1 output uploaded to hackerspace servor, and parses out date"""
    geep_str = 'grep -w date d3_commits_1yrfromtoday.txt > date_in_year'
    grep_str = 'grep -n2 message d3_commits_1yrfromtoday.txt > tmp.txt'
    os.system(grep_str)
    grep_str = 'grep -w date tmp.txt > dates_in_year'
    os.system(grep_str)
    commit_dates = []
    # open new file and append commit dates to new list
    fp = open('dates_in_year')
    # readlines in input, should contain dates from the github api d3.js curl output
    for line in fp.readlines():
        c = shlex.split(line)
        commit_date = translate_commit_date(c[-1])
        commit_dates.append(commit_date)
    fp.close()
    # Call the date histogram function and term hist values and date ranges
    week_array = create_date_hist(commit_dates)
    week_days= ['Mon','Tues','Wed','Thurs','Fri','Sat','Sun']
    # Find the day with max commits
    max_freq = max(week_array)
    max_bin_indicies = [i for i, freq in enumerate(week_array) if freq == max_freq]
    for bin in max_bin_indicies:
        print "most frequent commit day in week"
        print week_days[bin]
    x = range(0,7)
    plot_hist_data(x,week_array,xlabel = 'days of week',ylabel = '# commits per day of week', LABELS = week_days, title = 'Commits Per Day of Week - Year Summary', savestr = 'commits_per_weekday.png')

def translate_commit_date(timestamp):
    """ translate date to time
        takes timestamp input from git api, which uses ISO 8601 time date format"""
    conformed_timestamp = timestamp.translate(None,':-')
    commit_date_format = datetime.strptime(conformed_timestamp, "%Y%m%dT%H%M%S%fZ" )
    return commit_date_format

def format_date(timestamp_str):
    """ Format timestamp with month:day:year """
    time_str = timestamp_str.strftime('%m:%d:%Y')
    return time_str


def set_new_current(current_date, day_offset):
    """ Create new date range window"""
    new_current_date = current_date - timedelta(days = day_offset)
    return new_current_date

def plot_hist_data(x,freq,xlabel,ylabel,LABELS,title,savestr):
    """plot hist data as bar graph, could be made more modular """
    fig = plt.figure()
    plt.bar(x,freq)
    plt.ylabel(ylabel)
    plt.xlabel(xlabel)
    plt.xticks(x, LABELS)
    plt.title(title)
    fig.savefig(savestr)
def create_date_hist(commit_timestamps):
    """ Histogram the number of commits into weekly bins"""
    days_in_week = 7
    week_array = np.zeros(days_in_week)
    current_date = datetime.today()
    # use the strftime('%s') to compare integer numbers
    current_time = current_date.strftime('%s')
    end_time = commit_timestamps[-1].strftime('%s')
    while int(current_time) >= int(end_time):
        freq_count = 0
        for x in range(0, days_in_week):
            date_in_range = current_date - timedelta(days = x)
            week_index = date_in_range.weekday()
            date_str = format_date(date_in_range)
            for dt in range(0,len(commit_timestamps)):
                tmp = commit_timestamps[dt]
                if date_str==format_date(tmp):
                    week_array[week_index] += 1
        current_date_start = current_date
        # decrement time window and update the date_hist and date_list
        current_date = set_new_current(current_date_start, days_in_week)
        current_date_end = current_date
        current_time = current_date.strftime('%s')

    return week_array

if __name__ == "__main__":
    main()
