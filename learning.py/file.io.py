# # # # # with open("myfile.txt", "r") as file:
# # # # #     line = file.readline()
# # # # #     print(line.strip())

# # # # with open("myfile.txt", "r") as file:
# # # #     line1 = file.readline() 
# # # #     line2 = file.readline()
# # # #     line3 = file.readline()
# # # #     line4 = file.readline()
# # # #     line5 = file.readline()
# # # #     print(line1.strip())
# # # #     print(line2.strip())
# # # #     print(line3.strip())
# # # #     print(line4.strip())
# # # #     print(line5.strip())

# # # # loop until End of File EOF
# # # with open("myfile.txt", "r") as file:
# # #     while True: 
# # #         line = file.readline()
# # #         if not line:
# # #             break
# # #     print(line.strip())


# # with open('myfile.txt', 'r') as file:
# #     while True:
# #         line = file.readline()
# #         if not line:  # Empty string means end of file
# #             break
# #         print(line.strip())


# f = open("myfile.txt", "r" )
# i = 0 
# while True:
#     i = i + 1 
#     line = f.readline()
#     if not line:
#         break
#     m1 = line.split(",")[0]
#     m2 = line.split(",")[1]
#     m3 = line.split(",")[3]
#     print(f"marks of student {i} in subject 1 is {m1} ")
#     print(f"marks of student {i} in subject 2 is {m2} ")
#     print(f"marks of student {i} in subject 3 is {m3} ")

# line.close()


f = open("myfile.txt", "r")
i = 0 
while True:
    i = i + 1 
    line = f.readline()
    if not line:
        break
    parts = line.strip().split(",")
    m1 = parts[0]
    m2 = parts[1]
    m3 = parts[2]  # Changed from [3] to [2]
    print(f"marks of student {i} in subject 1 is {m1}")
    print(f"marks of student {i} in subject 2 is {m2}")
    print(f"marks of student {i} in subject 3 is {m3}")
f.close()


    