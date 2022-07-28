if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()

sum = 0
for x in student_marks:
    if x == query_name:
        for y in student_marks[x]:
            sum += y
        print(format(sum/len(student_marks[x]), '.2f')) # for displaying 2 decimal places even if they are .00
