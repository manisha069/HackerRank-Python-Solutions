if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    ls=list()
    ls=student_marks[query_name]
    sum=0
    for i in range(3):
        sum += ls[i]
    print("{:.2f}".format(sum/3))
