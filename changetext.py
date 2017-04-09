import random

def changeText(f, listRanks):
	f = open("test.txt", "w")
	f.write('<table id ="leadertable">')
	f.write('<tr>')
	f.write('<th>Rank</th>')
	f.write('<th>User</th>')
	f.write('<th>Score</th>')
	f.write('</tr>')

	for i in range(1,11):
		s = '<tr id = "rank' + str(i) +'">'
		f.write(s)
		r = '<td>' + str(i) + '</td>'
		f.write(r)
		q = '<td>' + str(random.random()) + '</td>'
		f.write(q)
		score = '<td>' + str(random.randrange(100)) + '</td>'
		f.write(score)
		f.write('</tr>')

	f.write('</table>')

def changePath(f, path):
	f.write(path)
