import math
import time
import numpy as np
import time

t0 = time.time()
def readFileHistory(filename):
    file_object = open(filename, "r") #File made into list
    file_object = file_object.read()
    file_object = file_object.split("\n")
    first_line = file_object[0].split(" ")
    No_of_Customers = int(first_line[0])
    No_of_Items = int(first_line[1])
    No_of_Transactions = int(first_line[2])
    matrix = []
    #make a 2d matrix of size No_of_Items with each item inside having a list of size No_of_Customers
    for i in range(No_of_Items):
        list1 = []
        for i in range(No_of_Customers):
            list1.append(0)
        matrix.append(list1)
    
    for i in range(1, No_of_Transactions+1):
        Transaction = file_object[i].split(" ")
        #print(Transaction)
        if matrix[int(Transaction[1])-1][int(Transaction[0])-1] == 0:
            matrix[int(Transaction[1])-1][int(Transaction[0])-1] = 1
    return matrix


history = readFileHistory("history.txt") #Created a matrix of the history of items that have been purchased by customers
#Create a funciton that takes the matrix and calculates the queries to then output them in the right format


def checkPositiveEntries(history):
    positiveEntries = 0
    for i in history:
        for j in i:
            if j == 1:
                positiveEntries += 1
    print("Positive entries: " + str(positiveEntries))

def calculateAngle(i, j):
    norm1 = np.linalg.norm(i)
    norm2 = np.linalg.norm(j)
    cos_theta = np.dot(i, j)/(norm1*norm2)
    theta = math.degrees(math.acos(cos_theta))
    return theta

def calculateAverageAngle(history):
    #for each item in the list. Find the angle between itself and every other angle
    sum1 = 0
    angles = []
    for i in range(len(history)):
        list1 = []
        for j in range(len(history)):
            if i == j:
                angle = 0
            else:
                angle = calculateAngle(history[i], history[j])
                sum1 += angle
            list1.append(angle)
        angles.append(list1)
    average = round(sum1/((len(history)*len(history))-len(history)), 2)
    return average, angles

def readQueries(filename):
    file_object = open(filename, "r") #Reads the queries
    file_object = file_object.read() #Converts it to a python format
    file_object = file_object.split("\n") #Splits the query by the new line
    averageAngle, angles = calculateAverageAngle(history)
    print("Average angle: " + str(averageAngle))
    result = ""
    for i in range(len(file_object)): #For i in range queries
        recommend = "Recommend: "
        recommendations = []
        angles1 = []
        matches = []
        result += "Shopping cart: " + file_object[i] + "\n"
        list1 = file_object[i].split(" ") #Split each query by spaces
        for j in list1: #In each query
            min_angle, match = calculateMinAngle(int(j)-1, angles, file_object[i]) #Calculate the min angle of the item
            if min_angle != 90:
                recommendations.append([min_angle, match])
                result += "Item: " + str(j) + "; match: " + str(match) + "; angle: " + str("{:.2f}".format(min_angle)) + "\n"
            else:
                result += "Item: " + str(j) + " no match \n"
        recommendations = sorted(recommendations, key=lambda x:x[0])
        for i in recommendations:
            if str(i[1]) not in matches:
                matches.append(str(i[1]))
                recommend += str(i[1]) + " "
        result += recommend + "\n" 
    print(result)
def calculateMinAngle(item, angles, shoppingCart):
    min_angle = 90
    index = 0
    shoppingCart = shoppingCart.split(" ")
    #print(shoppingCart)
    #compare only with items that are not in the cart
    for i in range(len(angles[item])):
        if angles[item][i] != 0:
            if not str(i+1) in shoppingCart:
                #print("Got here with " + str(i+1))
                #time.sleep(2)
                if angles[item][i] < min_angle:
                    min_angle = angles[item][i]
                    index = i
                    
            #print("New min angle with item" + str(index+1))
    return round(min_angle, 2), index+1


checkPositiveEntries(history)

readQueries("queries.txt")
t1 = time.time()
t2 = t1-t0
print("The program took:", t2, "s to execute")
