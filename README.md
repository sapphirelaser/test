# test
# pull data from git api
curl "https://api.github.com/repos/d3/d3/commits?since=2017-05-12T00:00:00Z&until=2018-05-12T23:59:59Z&page=1" > d3_commits_pg1.txt
curl "https://api.github.com/repos/d3/d3/commits?since=2017-05-12T00:00:00Z&until=2018-05-12T23:59:59Z&page=2" > d3_commits_pg2.txt
cat d3_commits_pg1.txt d3_commits_pg1 > d3_commits_1yrfromtoday.txt
