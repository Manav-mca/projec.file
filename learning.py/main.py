# # Read entire file 
# f = open("myfile.txt", "r")
# # print(f)
# text = f.read()
# print(text)
# f.close()


# # Read line by line 
# f = open("myfile.txt", "r")
# line1  = f.readline()



# # write mode 
# f = open("myfile.txt" , "a")
# f.write("hello world \n")
# f.writ-("welcome to python programming \n")
# f.close()



# with open("myfile.txt" , "r") as f:
#     f.write("this is new line \n") 
    
# # Read file using with 
# with open("myfile.txt" , "r") as f:
#     text = f.read() 
#     print(text)

# Read lines using with 
with open("myfile.txt" , "r") as file:
    for line in file:
        print(line.strip())
        
# R ead all lines as list
with open("myfile.txt" , "r") as file:
    lines = file.readlines()
    print(lines)

    