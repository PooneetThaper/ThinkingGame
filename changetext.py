import random

def changeText(listRanks):
	f = open("test.txt", "w")
	f.write('<table id ="leadertable">')
	f.write('<tr>')
	f.write('<th>Rank</th>')
	f.write('<th>User</th>')
	f.write('<th>Score</th>')
	f.write('</tr>')

	count = 1

	for i in listRanks.keys():
		s = '<tr id = "rank' + count +'">'
		f.write(s)
		r = '<td>' + count + '</td>'
		f.write(r)
		q = '<td>' + i + '</td>'
		f.write(q)
		score = '<td>' + listRanks[i] + '</td>'
		f.write(score)
		f.write('</tr>')
		count +=1

	f.write('</table>')

def changePath(path):
	f = open("path.txt", "w")
	f.write(path)
	f.write('<br>')
	f.write('Current Photograph')
