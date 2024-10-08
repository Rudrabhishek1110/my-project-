import time
from PIL import Image
from numpy import array
import winsound

duration = 1500  # milliseconds
freq = 540  # Hz

name = str(input("Enter the path of the jpg file with extension: "))
img = Image.open(name)      # reading the Image file in RGB 
arr = array(img)  # Array of RGB value ready
print("Pls wait while the code is working on the image", end='')
print('..', end='')
time.sleep(1)
print("\nSelect the right option from the below list")
print("Enter 1 for Reddish effect.\nEnter 2 for Greenish effect.\nEnter 3 for Bluish effect.\nEnter 4 for Grayscale effect.\n")

while(True):
    option = input("Enter your option: ")
    try:
        option = int(option)
    except:
        print("Enter a valid integer value among [1,2,3,4]")
        continue
    if(option in [1,2,3,4]):
        break
    else:
        print("Your entered value don't match with any option. Try once again...")
        continue
print("You have chosen option:",option)
print("The code is  working on it..")
if(option == 1):
    print("\nWorking on Red value...")
    for i in range(len(arr)):  # Manipulating RGB for Reddish Image output
        for j in range(len(arr[0])):
            arr[i][j][1] = 0
            arr[i][j][2] = 0
    imgr = Image.fromarray(arr, 'RGB')
    imgr = imgr.save("Redimg.jpg")
    arr = array(img)                   
elif(option==2):
    print("\nWorking on Green value...")
    for i in range(len(arr)):           # Manipulating RGB for Green Image output
        for j in range(len(arr[0])):
            arr[i][j][0] = 0
            arr[i][j][2] = 0

    imgg = Image.fromarray(arr, 'RGB')
    imgr = imgg.save("Greenimg.jpg")
    arr = array(img)
elif(option==3):
    print("\nWorking on Blue value...")
    for i in range(len(arr)):  # Manipulating RGB for Blue Image output
        for j in range(len(arr[0])):
            arr[i][j][1] = 0
            arr[i][j][0] = 0

    imgb = Image.fromarray(arr, 'RGB')
    imgr = imgb.save("Blueimg.jpg")
    arr = array(img)
elif (option == 4):
    print("\nWorking on grayscale...")
    for i in range(len(arr)):  # Manipulating RGB for Grayscale Image output
        for j in range(len(arr[0])):
            Y = 0.2989*(arr[i][j][0]) + 0.5870 * \
                (arr[i][j][1]) + 0.1140*(arr[i][j][2])
            arr[i][j][0] = Y
            arr[i][j][1] = Y
            arr[i][j][2] = Y
    imggrey = Image.fromarray(arr, 'RGB')
    image = imggrey.save("Greyimg.jpg")
    #print("Formula used for grayscale conversion : Y' = 0.2989*R + 0.5870*G + 0.1140*B")
winsound.Beep(freq, duration)
print("!!!!!!!!!!!!!!!Job done on image check out the current directory of your terminal!!!!!!!!!!!!!\n")
