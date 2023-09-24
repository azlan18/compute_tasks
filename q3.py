if __name__ == '__main__':
    n = int(input())
    student_marks = {}

    # Read the names and marks for each student and store them in the dictionary
    for _ in range(n):
        line = input().split()
        name = line[0]
        marks = list(map(float, line[1:]))
        student_marks[name] = marks

    query_name = input()

    # calculating the average marks for the specified student
    average_marks = sum(student_marks[query_name]) / len(student_marks[query_name])

    # display result 
    print("{:.2f}".format(average_marks))
