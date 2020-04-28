import os 
  
os.chdir(' ') #paste location of your ct-scan images folder 
print(os.getcwd()) 
COUNT = 0
  
# Function to increment count  
# to make the files sorted. 
def increment(): 
    global COUNT 
    COUNT = COUNT + 1
  
  
for f in os.listdir(): 
    f_name, f_ext = os.path.splitext(f) 
    f_name = str(COUNT) 
    increment() 
  
    new_name = '{}{}'.format(f_name, ".png") #makes all images in .png extension if there/any
    os.rename(f, new_name)