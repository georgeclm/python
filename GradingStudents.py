def gradingStudents(grades):
    # Write your code here
    resultt = []
    for i in grades:
        if i > 37:
            if (i + 1) % 5 == 0:
                resultt.append(i + 1)
            elif (i + 2) % 5 == 0:
                resultt.append(i + 2)
            else:
                resultt.append(i)
        else:
            resultt.append(i)
    return resultt
