from PIL import Image
import numpy as np, random

#-----------------------------------------------------------------
#Methods
#-----------------------------------------------------------------
#Input value
def input_value(question, error_message):
    while True:
        try:
            value = int(input(question))
            if value <= 0:
                raise ValueError
            return value
        except (TypeError, ValueError):
            print(error_message)

#Helper method to paste horizontal
def _paste_h(arr):
    new_image = Image.new("RGB", (total_w, img_h))
    curr_w = 0
    for pic in arr:
        new_image.paste(pic, (curr_w,0))
        curr_w += pic.width
    return new_image

#Helper method to paste vertical (Must use after paste_h)
def _paste_v(arr):
    new_image = Image.new("RGB", (total_w, total_h))
    curr_h = 0
    for pic in arr:
        new_image.paste(pic, (0,curr_h))
        curr_h += pic.height
    return new_image

#Return a collage of rows * columns randomly generated images
def collage(arr):
    result_array = []
    p_counter = 0
    lf_index = 0
    rt_index = img_per_col

    #Concatnate images horizontally and
    #append img_per_row of these images to the result_array 
    while p_counter < img_per_row:
        combine_pic = _paste_h(img_arr[lf_index : rt_index])
        result_array.append(combine_pic)
        lf_index += img_per_col
        rt_index += img_per_col
        p_counter += 1

    #Concatnate images in result_array vertically
    result = _paste_v(result_array)
    return result

#Random number generation
rand_color = lambda: random.randint(50,201)
rc = lambda: (rand_color(),rand_color(),rand_color())

#-----------------------------------------------------------------
#Shiba inu collage generation
#-----------------------------------------------------------------
while True:
    #Set up image width, height, image per row and column
    print("This program generates a collage of randomized shiba inu pixel art.")
    cont = input("Do you want to continue? (y/n) ").strip().lower()
    if(cont == "y"):
        row_q = "How many shiba inus do you want per row? "
        col_q = "How many shiba inus do you want per column? "
        err = "Please enter a positive integer. Try again!"
        img_per_row = input_value(row_q, err)
        img_per_col = input_value(col_q, err)
    else:
        print("See you!")
        break

    img_w = 150
    img_h = 150
    total_img = img_per_row * img_per_col
    total_w = img_w * img_per_col
    total_h = img_h * img_per_row

    #Stores individual images
    img_arr = []

    #Process images and append them to the image array
    counter = 0
    while counter < total_img:
        #Call on random number lambda functions to generate random colors
        bg = rc()
        do = rc()
        er = rc()
        cl = rc()
        gd = rc()
        
        #No change in eye and snout colors
        lt = (255,255,255)
        dk = (50,0,0)

        shibe = [
            [bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg],
            [bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg],
            [bg,bg,bg,bg,bg,do,bg,bg,bg,bg,bg,bg,bg,do,bg,bg,bg,bg,bg],
            [bg,bg,bg,bg,do,do,do,bg,bg,bg,bg,bg,do,do,do,bg,bg,bg,bg],
            [bg,bg,bg,bg,do,er,do,bg,bg,bg,bg,bg,do,er,do,bg,bg,bg,bg],
            [bg,bg,bg,do,do,er,do,do,bg,bg,bg,do,do,er,do,do,bg,bg,bg],
            [bg,bg,bg,do,do,do,do,do,do,do,do,do,do,do,do,do,bg,bg,bg],
            [bg,bg,bg,do,do,do,do,lt,do,do,do,lt,do,do,do,do,bg,bg,bg],
            [bg,bg,bg,do,do,do,dk,do,do,do,do,do,dk,do,do,do,bg,bg,bg],
            [bg,bg,bg,do,do,do,dk,do,do,do,do,do,dk,do,do,do,bg,bg,bg],
            [bg,bg,bg,do,do,do,do,do,lt,dk,lt,do,do,do,do,do,bg,bg,bg],
            [bg,bg,bg,do,do,do,do,do,do,er,do,do,do,do,do,do,bg,bg,bg],
            [bg,bg,bg,do,do,do,do,do,do,do,do,do,do,do,do,do,bg,bg,bg],
            [bg,bg,bg,do,do,do,do,do,do,do,do,do,do,do,do,do,bg,bg,bg],
            [bg,bg,bg,cl,cl,cl,cl,cl,cl,cl,cl,cl,cl,cl,cl,cl,bg,bg,bg],
            [bg,bg,bg,do,do,lt,lt,lt,lt,gd,lt,lt,lt,lt,do,do,bg,bg,bg],
            [bg,bg,bg,do,do,lt,lt,lt,lt,lt,lt,lt,lt,lt,do,do,bg,bg,bg],
            [bg,bg,bg,do,do,lt,lt,lt,lt,lt,lt,lt,lt,lt,do,do,bg,bg,bg],
            [bg,bg,bg,do,do,lt,lt,lt,lt,lt,lt,lt,lt,lt,do,do,bg,bg,bg]
        ]

        shibe_array = np.array(shibe, dtype=np.uint8)
        shibe_pic = Image.fromarray(shibe_array)
        shibe_pic = shibe_pic.resize((img_w,img_h),resample=Image.NEAREST)
        img_arr.append(shibe_pic)
        counter += 1

    #Generate collage
    result_pic = collage(img_arr)

    #Save image in the same folder where the shibe_generator is saved
    while True:
        try:
            print("What do you want to name your collage?")
            input_name = input("Please enter alphabets with no spaces or symbols: ")
            if(not input_name.isalnum()):
                raise ValueError
            shibe_name = "{}.png".format(input_name)
            break
        except (TypeError, ValueError):
            print("Please enter only alphabets with no spaces or symbols. Try again!")
            
    result_pic.save(shibe_name)
    print("Generation complete!")

    #Continue generation or quit program
    another = input("Do you want to generate another collage? (y/n) ").strip().lower()
    if another == "n":
        print("See you!")
        break
