def CgpaCalc(marks, n):
    grade = [0] * n
    Sum = 0
    for i in range(n):
        grade[i] = (marks[i] / 10)
        for i in range(n):
            Sum += grade[i]
            cgpa = Sum / n
            return cgpa
n = 5
marks = [ 90, 80, 70, 80, 90 ]
cgpa = CgpaCalc(marks, n)
print("CGPA = ", '%.1f' % cgpa)
print("CGPA Percentage = ", '%.2f' % (cgpa * 9.5))