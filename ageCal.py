import datetime
import math
current_time = datetime.datetime.now()


def checkFormat(dob):
    dt, mnth, yr = dob.split('/')
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

    if dt > 31:
        print("Date is invalid")
        tmp += 1

    if mnth > 12:
        print("Month is invalid")
        tmp += 1

    if yr > current_time.year:
        print("Check the year")
        tmp += 1
    if tmp == 0:
        # print("Format is valid")
        return [dt, mnth, yr]
    else:
        return False
    # print(date, month, year)


def ageCalculator(dt, mnth, yr):
    # calculate the age
    cur_dt = current_time.day
    cur_mnth = current_time.month
    cur_yr = current_time.year
    cur_total = int(cur_yr*365+cur_mnth*30+cur_dt)
    age_total = int(yr*365+mnth*30+dt)
    # print(cur_total, age_total, cur_total-age_total)
    return cur_total-age_total


# dob = input("Enter your Date of Birth in this format 'dd/mm/yyyy':- ")
dob = "18/07/2000"
if checkFormat(dob) != False:
    dt, mnth, yr = checkFormat(dob)
    age = ageCalculator(dt, mnth, yr)
    age_yr = int(age/365)
    age = age % 365
    age_mnth = int(age/30)
    age = age % 30
    age_dt = age
    print("Your age is ", age_yr, "years", age_mnth, "month", age_dt, "days")
