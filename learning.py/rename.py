# # from  os import  *

# # # # Get current directory
# # # print(getcwd())

# # # # List files in the current directory
# # # print(listdir("."))

# # # Create a directory 
# # # mkdir("test")

# # # Get environment variables
# # # print(environ.get("PATH"))

# # #Remov the dirrectory



# # # Get current directory

# # # List files in current directory
# # # print(listdir("." ))
 

# # # Get enviroment variables 
# # print(os.environ.get('PATH'))
# # import os

# # # Get current directory
# # print(os.getcwd())

# # # List files in current directory
# # print(os.listdir('.'))

# # # Create a directory
# # os.mkdir('test_dir')

# # # Get environment variable
# # print(os.environ.get('PATH'))


# import os

# # for i in range(1,52):
# #     print(os.rename(f"data/Day{i+1}" , f"data/tutorial{i+1}"))

# folders = os.listdir("data")
# print(folders)

# for folder in folders:
#     print(folders)
#     print(os.listdir(f"data/{folder}"))
# importing os module 
import os 

# Command to execute
# Using Windows OS command
cmd = 'date'

# Using os.system() method
os.system(cmd)
print(os.getcwd())
