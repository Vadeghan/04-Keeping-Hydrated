#Made by Marika Colby (12.10)
#From your examples in the ReadMe file, I'm assuming that we output the input divided by two and rounded down as an integer (w = int(floor(t/2)))
#I disagree with this but thats what I worked out and it answers the examples correctly, so I'm going with it.
#I'm using truncation because it sounds more complicated and therefore more creative that flooring. I don't actually know what it means to be creative.

def needed_water(hours):
    EveryHour     = []
    NeededWater   = 0
    #Truncate the decimal out of the input.
    hours = int(hours)
    #Make a note of each time an hour passed.
    EveryHour += ["An hour has passed."] * hours
    #For each hour, add 0.5L to the water tally.
    for EachHour in EveryHour:
        NeededWater += 0.5

    return NeededWater

def inputPositiveFloat(statement):
    output = input("%s\n  > " % (statement))
    while (not isFloat(output)) and ((output < 0) if isFloat(output) else True):
        #If it is not a float, or if it is a float but less that zero, then:
        print("invalid input\n")
        output = input("%s\n  > " % (statement))
    return float(output)


def isFloat(test):
    #Decided to put this in a seperate function to save on confusion.
    try:
        float(test)
        return True
    except:
        return False

while True:
    #Find out how many litres of water is needed.
    NeededWater = needed_water(inputPositiveFloat("How many hours have you been cycling?"))
    #Truncate this to the lower integer.
    NeededWater = int(NeededWater)
    #Print results.
    print("You should drink %i %s of water.%s\n\n" % (NeededWater, "litre" if (NeededWater == 1) else "litres", " Cycling for that many hours is the answer to Life, The Universe, and Everything!!!" if (NeededWater == 42) else ""))
