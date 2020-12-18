"""
def main():
    
    kickstart()
    calculate_average()
    calculate_percent_above_avereage()

    print("Number of Grades:", len(grades))
    print("Average Grade:", calculate_average(grades))
    print("Percentage of Grades Above Average:", calculate_percent_above_avereage(grades), "%")

def calculate_percent_above_avereage(grades):
    avg = calculate_average(grades)
    counter = 0
    for grades in grades:
        if grade > avg:
            counter += 1 

    return (counter/len(grades))

def calculate_average(grades)
    if len(grades) == 0:
        return 0

    avg = sum(grades)/len(grades)
    return avg

def kickstart()
    infile = open("final.txt", "r")
    grades = [word.strip() for word infile]
    infile.close()


main()



"""