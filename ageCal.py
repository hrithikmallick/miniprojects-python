import datetime
import math
current_time = datetime.datetime.now()

# check the format is right or wrong


def checkFormat(dob):
    try:
        dt, mnth, yr = dob.split('/')
    except:
        print("invalid format")
        exit()
    if len(dt) > 2 or len(mnth) > 2 or len(yr) > 4:
        print("Please check the format again")
        return False

    tmp = 0
# Type cast in int
    try:
        dt = int(dt)
        mnth = int(mnth)
        yr = int(yr)
    except:
        print("please use number in DOB")
        return False

    if dt > 31 or dt == 0:
        print("Date is invalid")
        tmp += 1

    if mnth > 12 or mnth == 0:
        print("Month is invalid")
        tmp += 1

    if yr > current_time.year or yr == 0:
        print("Check the year")
        tmp += 1
    if tmp == 0:
        # print("Format is valid")
        return [dt, mnth, yr]
    else:
        return False
    # print(date, month, year)

# checking  the calculations here


def ageCalculator(dt, mnth, yr):
    # calculate the age
    cur_dt = current_time.day
    cur_mnth = current_time.month
    cur_yr = current_time.year
    cur_total = int(cur_yr*365+cur_mnth*30+cur_dt)
    age_total = int(yr*365+mnth*30+dt)
    # print(cur_total, age_total, cur_total-age_total)
    if age_total > cur_total:
        print("DOB is in future check again")
        exit()

    return cur_total-age_total

# main method


def ageCal(dob):
    if checkFormat(dob) != False:
        dt, mnth, yr = checkFormat(dob)
        age = ageCalculator(dt, mnth, yr)
        age_yr = age/365
        frac, whole = math.modf(age_yr)
        age_yr = int(age_yr)
        age = age % 365
        age_mnth = age/30+int(frac*10)
        frac, whole = math.modf(age_mnth)
        age_mnth = int(age_mnth)
        age = age % 30+int(frac*10)
        age_dt = age
        if age_mnth >= 12:
            age_yr += 1
            age_mnth = age_mnth-12
        if age_dt >= 30:
            age_mnth += 1
            age_dt = age_dt-30
        var1 = "year"
        var2 = "month"
        var3 = "day"
        if age_yr > 1:
            var1 = "years"
        if age_mnth > 1:
            var2 = "months"
        if age_dt > 1:
            var3 = "days"

        print("Your age is", age_yr, var1, age_mnth, var2, age_dt, var3,)
    else:
        print("Invalid format")


# getting input from users
dob = input("Enter your Date of Birth in this format 'dd/mm/yyyy':- ")
# call the function
ageCal(dob)
