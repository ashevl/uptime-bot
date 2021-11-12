from twitter import tweet

f = open('uptime.txt', 'r')
tweet(f.read())
f.close
