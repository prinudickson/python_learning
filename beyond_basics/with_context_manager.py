#usual way of writing data into a file
myfile = open("example.txt", "w")
myfile.write("Something")
myfile.close()

#Best practice

with open("example.txt", "w") as myfile:
    myfile.write("Something2")
    myfile.close()