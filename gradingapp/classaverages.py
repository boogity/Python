willy = {
	"name": "Willy",
	'homework': [100.0, 95.0, 97.5, 87.0, 83.5],
	'quizzes': [65.0, 70.0, 85.0, 88.0],
	'tests': [100.0, 72.0]
}

def Average(numbers):				#takes list of test scores for a student, then averages together assuming equal weight
	total = float(sum(numbers))
	total /= len(numbers)
	return total

def GetAverage(student):			#calls average() then weights according to grade grouping
	homework = Average(student['homework'])
	quizzes = Average(student['quizzes'])
	tests = Average(student['tests'])
	total = homework * .1 + quizzes * .3 + tests * .6
	return total
def GetLetterGrade(score):			#Converts numerical grade to letter grade
	if score >= 90:	
		return "A"
	elif 90 > score >= 80:
		return "B"
	elif 80 > score >= 70:
		return "C"
	elif 70 > score >= 60:
		return "D"
	else: 
		return "F"

print GetAverage(willy)
print GetLetterGrade(GetAverage(willy))
