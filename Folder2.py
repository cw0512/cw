import os 


# 1 ~ 3 까지 
#os.mkdir("/Users/My_Home/Desktop/project/WordTest/Second/Day1") 
#os.mkdir("/Users/My_Home/Desktop/project/WordTest/Second/Day2") 
#os.mkdir("/Users/My_Home/Desktop/project/WordTest/Second/Day3") 

dir_path = "/Users/My_Home/Desktop/project/WordTest/Second" 
dir_name = "/Day" # 맨 앞에 / 존재 
num = 1 while num < 31: 
num += 1
# 4 ~ 9 까지 
os.mkdir(dir_path + dir_name + str(num)) 

