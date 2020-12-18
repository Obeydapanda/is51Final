

def main():
    infile = open("final.txt", "r")
    grades = [int(word) for word  in infile]
    infile.close()

    above_average = calculate_percent_above_avereage(grades) * 100

    

    print("Number of Grades:", len(grades))
    print("Average Grade:", calculate_average(grades), "%")
    print("Percentage of Grades Above Average:", round(above_average, 2), "%")



def calculate_percent_above_avereage(grades):
    avg = calculate_average(grades)
    counter = 0
    for grade in grades:
        if grade > avg:
            counter += 1 

    return (counter/len(grades))

def calculate_average(grades):
    if len(grades) == 0:
        return 0

    avg = sum(grades)/len(grades)
    return avg


main()
