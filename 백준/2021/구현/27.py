date=input()

sep=date.index(".")
sep2=date.index(".",sep+1)
sep3=date.index(".",sep+2)

year=date[:sep]
month=date[sep+1:sep2]
day=date[sep2+1:]

print("{:0>2}-{:0>2}-{:0>4}".format(day,month,year))