# 🐶 Random Shiba Inu Collage Generator
![shibe](https://user-images.githubusercontent.com/66938562/149577509-51ddfc9d-9f51-435d-98bf-474a9e8a6091.png)

## Table of Contents
* [Introduction](#introduction)
  *  [Summary](#summary)
  *  [Motivation](#motivation)
  *  [Technologies](#technologies)
* [Instructions](#instructions)
  *  [Installation](#installation)
  *  [Using the Program](#using-the-program)
* [Development Process](#development-process)
  *  [Drafting the Pattern](#drafting-the-pattern)
  *  [Learnings](#learnings)
* [Credits](#credits)

## Introduction
### Summary
`Random Shiba Inu Collage Generator` allows users to generate a collage of randomly colored shiba inus. Users can specify the number of shiba inus they want on the collage and name the collage before the program saves the image. 
### Motivation
I have been making digital art for a couple of years but it mostly involved drawing on a tablet. However, after browsing through some generative art online, I thought it would be cool to give generative art a try too, starting from simple pixel patterns.

Since I have recently started using Python, I think this would be a fun exercise for me to familiarize myself with some basic programming concepts in Python such as using the NumPy and Pillow libraries, lists, and writing methods. Publishing a repo is also a way to familiarize myself with GitHub and document any learnings throughout the development process.

### Technologies
![python](https://img.shields.io/badge/Python-3.10.1-blue) ![pillow](https://img.shields.io/badge/Pillow-9.0.0-blue) ![numpy](https://img.shields.io/badge/NumPy-1.22.0-blue)

## Instructions
### Installation
`Python`, `Pillow` and `NumPy` should be installed before running the script.
* Python installation: [Install](https://www.python.org/downloads/)
* Pillow installation: [Install](https://pillow.readthedocs.io/en/stable/installation.html)
* NumPy installation: [Install](https://numpy.org/install/)

This is a great guide on how to run Python scripts from GitHub:
[How to Run Scripts from Github](https://projectdestroyer.com/2018/01/run-scripts-github/).

For reference, the following steps can be taken to clone the repo and run the script in Windows Command Prompt:

<img src="https://user-images.githubusercontent.com/66938562/149648081-fc20e898-3d62-4c78-a109-a78546fe321e.png" width="650" height="249">

### Using the Program
After running the script in a terminal with:
```
python shibe_generator.py
```
The user will see the following messages:
```
This program generates a collage of randomized shiba inu pixel art.
Do you want to continue? (y/n)
```
Selecting "y" will prompt the user to input the number of shiba inu patterns they want per row and per column. Selecting "n" will prompt the program to exit after a `See you!` message. If the input is something other than a positive integer, the program will display `Please enter a positive integer. Try again!` until it receives a valid input.
```
How many shiba inus do you want per row? 
How many shiba inus do you want per column? 
```
After receiving the row and column inputs, the program will ask the user to name the collage.The user is only allowed to enter a name with no spaces or symbols and will be asked to re-enter a valid name if otherwise.
```
What do you want to name your collage?
Please enter alphabets with no spaces or symbols: 
```
The program will display `Generation complete!` after the collage is saved in the same folder as the local git repo clone. After the collage is generated and saved, the program will ask whether the user wants to generate another collage. 

### Examples
![shibe](https://user-images.githubusercontent.com/66938562/149647277-f9ab8489-d4d0-4d91-b39f-191a4063b06b.png)

*Result of a 1 x 2 collage*

![dog](https://user-images.githubusercontent.com/66938562/149647282-76695f87-ec3b-44a5-9b51-ae1c822ec963.png)

*Result of a 2 x 2 collage*

![shibe3by3](https://user-images.githubusercontent.com/66938562/149647269-23611ebd-ea90-496c-a50c-ba19a4f922c7.png)

*Result of a 3 x 3 collage*

## Development Process
### Drafting the Pattern
The pattern is created through placing different RGB tuples in a 2D list, then converting that list into an Image object through NumPy and Pillow. For more details, "Create Your Unique "Pixel Art Avatar" in Python" by Tommaso De Ponti in the [Credits](#credits) section does a great job explaining the process. 

Essentially, all pixels that share the same color should be represented by the same RGB tuples. For instance, in `shibe_generator.py`, I have placed a RGB tuple named "bg" at every index in the 2D array that is intended to be the background. Generating an image from a list is not intuitive since it is difficult to determine what the final image would look like. On top of that, the process of typing out the array is very tedious. I spoke with Brett Palatiello who launched the Columbia Lion NFT and he suggested to plan out the pattern in Excel.

![image](https://user-images.githubusercontent.com/66938562/149677972-780c6132-f8db-4d50-94cf-6ffb8fd040e6.png)
*A draft of the shiba inu pattern in Excel*

I created this pattern with Conditional Formatting, which changes the color of the cell based on certain keywords such as "bg". I then used the `CONCAT()` function to concatenate the contents in the individual cells in the format of a Python list so I can copy and paste the resulting string directly into Python.

### Learnings
This section documents the concepts I learned via developing this project. Some references are made to Java because I've mostly programmed in Java.

#### Python Functions (def)

Like Java methods, Python functions support reusability and keep the script more concise. For instance, I made `input_value()` a function because the processes of assigning values to rows and columns are essentially the same.

#### Lambda Functions

Lambda function is a function with a more concise syntax similar to a lambda function in Java or an anonymous function in JavaScript. It makes the code look cleaner especially when the code block is short. I've used a lambda function for random color generation for this reason.

#### Try-Except Statement

This is similar to Java's try-catch statement. I have included a try-except statement nested in a while loop for all user inputs. That way I can ensure the user enters a valid input. Instead of throwing an exception, the script will remain in the while loop until the user enters a valid input. Similar to Java, you can also throw an exception when the input fits a certain set of conditions. For instance, the script will throw a `ValueError` when `not input_name.isalnum()`. In other words, the `except` statement will run if a user inputs anything that is not an alphanumeric string.

#### Image module

Through this exercise, I've learned to use some of the functions in the `Image` module. These include creating a new Image object, pasting and resizing, and converting an array into an Image object.
* **Resampling**: Resampling is an option in `resize()`. Since I am increasing the size of each image after they're being generated, interpolation occurs to make up for the missing pixels. I am using the `NEAREST` filter, which means the missing pixels are interpolated through assigning the value of the nearest pixel. The disadvantage of this is the output may have jagged edges, which is exactly what we want for pixel art. `NEAREST` is also the default option if no filter is being specified in the `resize()` function and it has the best performance due to simplicity. There are 5 other options: `BICUBIC`, `BILINEAR`, `BOX`, `HAMMING`, and `LANCZOS`. `BOX` would also work in this case, because it makes up for the missing pixels with identical weights. In upscaling, it is equivalent to `NEAREST`. Meanwhile all other methods survey from more than 1 neighboring pixels. For instance, the `BILINEAR` filter surveys from the 4 closest pixels (2x2) and fills in the missing pixels with a weighted average output. It makes sense that the output would be blurry and smooth because of anti-aliasing. For more information, check out: [Pillow Handbook](https://pillow.readthedocs.io/en/stable/handbook/concepts.html#filters) and [Interpolation Methods](https://climserv.ipsl.polytechnique.fr/documentation/idl_help/Interpolation_Methods.html).
![image](https://user-images.githubusercontent.com/66938562/149853634-5449e4aa-de59-48a2-b1c7-278880f643ef.png)

* **Image.fromArray (NumPy array)**: The Pillow `fromArray()` function only takes an array with uint8 values. Hence it will not accept a Python list because it is not type-safe or fixed in size. This makes sense because an RGB pixel is represented by 3 unsigned bytes (0-255, 0-255, 0-255). The NumPy array function helps us convert a regular Python list into an array of unsigned 1-byte integers. That way we can feed the array to the `fromArray()` function and generate an image.
For more information, check out: [Image Processing with NumPy](https://www.pythoninformer.com/python-libraries/numpy/numpy-and-images/).

## Credits
I used the following resources to develop this project:
* [Create Your Unique “Pixel Art Avatar” in Python](https://betterprogramming.pub/create-your-unique-pixel-art-avatar-in-python-c176d9596bda)
* [How to Create Generative Art In Less Than 100 Lines Of Code](https://www.freecodecamp.org/news/how-to-create-generative-art-in-less-than-100-lines-of-code-d37f379859f/)
* [Concatenate images with Python, Pillow](https://note.nkmk.me/en/python-pillow-concat-images/)
* [The Python Tutorial](https://docs.python.org/3/tutorial/)
* [Pillow Handbook](https://pillow.readthedocs.io/en/stable/handbook/tutorial.html)
