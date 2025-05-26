total = int(float(input("Enter Total Questions in ALL: ")))
correct = int(float(input("Enter Total Questions Correct: ")))
if total < correct:
	exit("BadInput")
score = round(((correct / total) * 100),2)
if score > 100:
	score = 100
if score >= 97.5:
	grade = "A+"
elif score >= 92.5:
	grade = "A"
elif score >= 90.0:
	grade = "A-"
elif score >= 87.5:
	grade = "B+"
elif score >= 82.5:
	grade = "B"
elif score >= 80.0:
	grade = "B-"
elif score >= 77.5:
	grade = "C+"
elif score >= 72.5:
	grade = "C"
elif score >= 70.0:
	grade = "C-"
elif score >= 67.5:
	grade = "D+"
elif score >= 62.5:
	grade = "D"
elif score >= 60:
	grade = "D-"
elif score < 60:
	grade = "E *Failing*"
grade_view = ("You Got an " + grade + "! (" + str(score)+"%)")
grade_view_len = len(grade_view)
times = 35-grade_view_len
addto = ""
for i in range(1,times):
	addto = addto + "-"
grade_view = grade_view+addto
print("""
----------------------------------
REPORT CARD-----------------------
"""+grade_view+"\n----------------------------------")
