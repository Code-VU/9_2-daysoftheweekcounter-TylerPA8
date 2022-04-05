
def countDayOfTheWeek():
    # This first line is provided for you
    file_name = input("Enter a file name: ")   
    file_open = open(file_name)
    fr = file_open.readlines()
    froms ={}
    for n in fr:
        if n.startswith("From "):
            n = n.strip()
            n = n.split(' ')
            if n[2] in froms:
                froms[n[2]] += 1
            else:
                froms[n[2]] = 1
    print(froms)
    # end assignment

## if you want to test locally before you try to sync
## uncomment calculateAbsolute() and run > python payCalculator.py
## ***IMPORTANT*** please recomment before you submit/sync your assignment.
## OR YOUR TEST WILL NOT RUN
##countDayOfTheWeek()