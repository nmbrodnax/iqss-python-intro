## Introduction to Python
[NaLette Brodnax](www.nalettebrodnax.com)<br>
[The Institute for Quantitative Social Science](http://iq.harvard.edu)<br>
Harvard University<br>

**Date:** Friday, October 6, 2017<br>
**Location:** CGIS Knafel Room K018, 1737 Cambridge St, Cambridge, MA 02138

## Workshop Exercises

### Part 1: Introduction

 1. Complete the one-minute poll at [bit.ly/iqss106](http://bit.ly/iqss106)


### Part 2: Getting the Tools

 1. After installing Python, open the Python IDE (such as Spyder or IDLE) on your machine.  Type the following into the interpreter:
    ```python
    print('Hello, world.')
    ```

 2. Create a file named *hello.py*.  You will add code to this script throughout Parts 2 and 3 of the workshop. On the first two lines, type the following:
    ```
    # My first Python script
    print('Hello, world.')
    ```
    Save the script and run it from the IDE.

### Part 3: Programming Basics
 1. The following code uses operators that have special meanings in Python.  Add the following statements to your *hello.py* script.  Predict what the output will be before running the script.

    |Statement| Prediction|
    |:---|:---|
    |`movie = 'Rogue One'`|N/A|
    |`print(movie)`||
    |`i = 1`||
    |`i += 1`||
    |`print(i)`||
    |`print('A' + 'B')`||
    |`print('me'*3)`||
    |`print('a' == 'a')`||
    |`print('a' == 1)`||
    |`print(5 != 25/5)`||

 2. The following code demonstrates some of the different ways to reference the elements of a sequence.  Add the following statements to your *hello.py* script. Predict what the output will be before running the script.

    |Statement| Prediction|
    |:---|:---|
    |`mystring = 'happy'`|N/A|
    |`print(mystring[0])`||
    |`print(mystring[2:4])`||
    |`mylist = ['Leia', 'Rey', 'Maz']`|N/A|
    |`print(mylist[-1])`||
    |`mydict = {'name': 'Kylo', 'side': 'dark'}`|N/A|
    |`print(mydict['name'])`||

 3. Add the following code to your *hello.py* script, giving special attention to indentation.  Experiment with modifying the code.  For example, what happens if you indent the print statement on the last line?
    ```python
    name = 'Grace Hopper'

    if len(name) < 20:
        print('Yes')
    else:
        print('No')

    i = 0
    for letter in name:
        if letter in ['a', 'e', 'i', 'o', 'u']:
            i = i + 1
    print(name + ' has ' + str(i) + ' vowels.')

    i = 0
    vowel_count = 0
    while i < len(name):
        if name[i] in ['a', 'e', 'i', 'o', 'u']:
            vowel_count = vowel_count + 1
        i = i + 1
    print(name + ' has ' + str(vowel_count) + ' vowels.')
    ```

 4. Add the following code to your *hello.py* script.  Predict how `my_string` will be displayed before running the script.  Using triple quotes, add an informative documentation string to the `say_hello()` function.  Try entering different types of data (text, numbers, etc.) as the argument for the function.  How does Python respond?

    ```python
    my_string = 'aBcDe'
    print(my_string)
    print(my_string.lower())


    def say_hello(name_string):
        print('Hello, ' + str(name_string) + '!')
        return None

    say_hello('NaLette')
    ```

[Click here](https://raw.githubusercontent.com/nmbrodnax/iqss-python-intro/master/hello.py) to download the code for all exercises.