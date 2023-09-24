N, X = map(int, input().split())
student_sums = [0] * N

# read the marks in every subject and update student_sums
for _ in range(X):
    subject_marks = list(map(float, input().split()))
    for i in range(N):
        student_sums[i] += subject_marks[i]

for i in range(N):
    average_score = student_sums[i] / X
    print("{:.1f}".format(average_score))
