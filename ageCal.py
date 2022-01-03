import datetime
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


# dob = input("Enter your Date of Birth in this format 'dd/mm/yyyy':- ")
dob = "18/07/2000"
# print(checkFormat(dob))
if checkFormat(dob) != False:
    dt, mnth, yr = checkFormat(dob)
    cur_dt = current_time.date
    cur_mnth = current_time.month
    cur_yr = current_time.year
    print(dt, mnth, yr)
    print("You are ", cur_yr-yr, "years age")
