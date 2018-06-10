import sys, csv, os
import numpy as np


def writeCsv(dict, outputFolder, filename):
    filepath = outputFolder + "/" + filename + ".csv"
    with open(filepath, 'wb') as csvfile:
        dictWriter = csv.writer(csvfile)
        # iterate on each row in the dict and write it to the csv file
        for key, value in dict.iteritems():
            dictWriter.writerow([key, np.array2string(value[0],separator=","),np.array2string(value[1],separator=",")])


def extractProfiles(inputFile, userProfileOutput, itemProfileOutput):
    userDict = {}
    itemsDict = {}

    # read the input file
    with open(inputFile, 'rb') as csvfile:
        ratingReader = csv.reader(csvfile)
        firstline = True
        for row in ratingReader:
            if firstline:
                firstline = False
                continue

            userId = row[0]
            movieId = row[1]
            rating = row[2]
            userValue = userDict.get(userId, [np.array([]), np.array([])])
            itemValue = itemsDict.get(movieId, [np.array([]), np.array([])])

            # append the movie id and rating
            userValue[0] = np.append(userValue[0], [movieId])
            userValue[1] = np.append(userValue[1], [rating])

            itemValue[0] = np.append(itemValue[0], [userId])
            itemValue[1] = np.append(itemValue[0], [rating])

            userDict[userId] = userValue
            itemsDict[movieId] = itemValue

            # write the userDict and itemsDict to the output folders
            writeCsv(userDict, userProfileOutput, 'user profiles')
            writeCsv(itemsDict, itemProfileOutput, 'item profiles')


def main(args):
    # Check if there is the function name argument
    if (len(args) > 0):
        command = args[0].lower()
        if command == "extractedprofiles":
            # extract the arguments
            if len(args) > 3:
                inputFile = args[1]  # need to be csv file
                if not inputFile.endswith(".csv") or not os.path.isfile(inputFile):
                    print inputFile, "is not a valid input file"
                    return

                userProfileOutput = args[2]
                itemProfileOutput = args[3]

                # check if the user and item output folders are valid
                if not os.path.isdir(userProfileOutput):
                    os.makedirs(userProfileOutput)

                if not os.path.isdir(itemProfileOutput):
                    os.makedirs(itemProfileOutput)

                # call the extracted profiles function
                extractProfiles(inputFile, userProfileOutput, itemProfileOutput)
            else:
                print "There aren't enough parameters"
            pass
    else:
        print "Allowed command:" \
              "ExtractProfiles [rating input file][user profile csv output directory][item profile csv output directory]"
        # readFile()
        # findRatesOfUser()


if __name__ == '__main__':
    main(sys.argv[1:])
