#fuelEconomy.py
#Rodas T Gebreslassie
#This program open two data files, carModelData_city and
#carModelData_hwy, and output the total number of vehicles
#tested, the average city mpg , the average highway mpg  and
#the number of gas guzzlers among the vehicle models tested.

def convertData(a):
    fob = open(a,"r")
    line = fob.read()
    aa = line.split()
    
    alist = []
    for i in aa:
        alist.append(float(i))
    return(alist)

def averageMPG(fa):
    sum = 0

    for i in fa:
        sum = sum + i
    avg = sum/len(fa)
    return (round(avg, 3))



def countGazGuzzlers(a,b):
    counter = 0
    for i in range(len(a)):
        if a[i] < 22 or b[i] < 27:
            counter = counter + 1
    return counter

def output(a,a2,b,alist):
    print("The total number of vehicles tested are {}.".format(len(alist)))
    print("The average for the city mpg for all the vehicles tested is {}.".format(a))
    print("The average for the highway mpg for all the vehicles tested is {}.".format(a2))
    print("The number of gas guzzlers among the vehicle models tested are {}.".format(b))




def main():

    floatValue = convertData("carModelData_city.txt")
    floatValue2 = convertData("carModelData_hwy.txt")

    averageValue = averageMPG(floatValue)
    averageValue2 = averageMPG(floatValue2)
    
    count = countGazGuzzlers(floatValue,floatValue2)
    output(averageValue,averageValue2,count,floatValue)


main()
