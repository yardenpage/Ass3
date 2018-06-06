import sys, csv, re
import numpy as np


def main():
    readFile()
    findRatesOfUser()

def readFile():
    try:
        # read csv file
        global data
        data = np.loadtxt("ratings.csv", delimiter=',', skiprows=1, usecols=range(0,3))
        #print data
    except IOError:
        print "The file ratings.csv doesn't exist"

def findRatesOfUser():
    #usersValues = set(map(lambda line: line[0], data))
    #result = map(lambda user : filter(lambda line: line[0] == user , data), usersValues)
    user = data[0][0]
    a = np.array(user)
    #a[0][0]= user
    i=0
    for line in data:
        if line[0] == user:
            np.append(a[i][1], line[1])
        else:
            i = i +1
            a[i][0] = line[0]
            np.append(a[i][1], line[1])
    print a


if __name__ == '__main__':
    main()