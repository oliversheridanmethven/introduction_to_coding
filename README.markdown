# Introduction to coding
 
### Author

[Oliver Sheridan-Methven](mailto:oliver.sheridan-methven@maths.ox.ac.uk).

#### Date

April 2018.

### Description

Introduction to coding course.

#### Website

[https://github.com/oliversheridanmethven/introduction_to_coding](https://github.com/oliversheridanmethven/introduction_to_coding).

### Questions, issues, bugs, etc.

If you have questions about the course, find bugs in the code,
discover issues running the code, or anything similar, then please
email me at
[oliver.sheridan-methven@maths.ox.ac.uk](mailto:oliver.sheridan-methven@maths.ox.ac.uk).


## Getting started

Prior to getting started on this course I ***strongly recommend*** doing the following:

1. Install Python 2.7 - The latest version is Python 2.7.14 and can be downloaded from 
the [Python downloads webpage](https://www.python.org/downloads/).
2. Install PyCharm - PyCharm is what we will be using to write and edit code. The community
edition is free to use and can be downloaded from the 
[PyCharm downloads webpage](https://www.jetbrains.com/pycharm/download/).

>Don't install these as an administrator, but install them with regular user permissions 
(**default installation**). 



## Course information

### Language

Python 2.7.

>Most of the code will be easily transferable to Python 3, 
and there may be examples from other languages such as C, JavaScript, etc.
Before diving into Python, it is useful to install Python (if using MS Windows). 
If you are running UNIX/LINUX/OSX then you will most likely already have this installed. 
To check, open the terminal and type in `python --version`. 
In this course we will mostly be using Python 2.7 instead of Python 3. 
This is not a major issue, but there will be some small syntactic differences between the two.
([For more information about *getting started* with Python](https://www.python.org/about/gettingstarted/)).
>  
>![Python version](figures/python_version.gif)
>  
> The default python version I am using on my machine is Python 2.7.12. 


> *The joy of coding Python should be in seeing short, concise, readable
classes that express a lot of action in a small amount of clear code \-
not in reams of trivial code that bores the reader to death.*
\- Guido van Rossum.

## Git

This project will use *git large file storage* (`git lfs`) 
for any large files which are not predominantly source code.
(This is easy to install and use on UNIX/LINUX based systems, 
and should also be installable on MS Windows with the 
appropriate application).

### iPython Notebooks

Much of this code will be written using iPython notebooks. These are useful for interactively demonstrating the results
from running different source code. 

> I am generally not a fan of coding notebooks, but occasionally they can be useful. 
However, they can be a pain when using VCS (such as git). To circumvent committing the output
of such notebooks, 
[see the instructions on StackOverflow](https://stackoverflow.com/a/20844506/5134817).

## Course structure

> The syllabus and topics we cover are very flexible, and can be heavily
influenced by the students taking this course. The first few classes will
constitute some of the basic requisites for understanding the building-blocks
of the language, but after that **any suggestions about topics which students
would like me to include (or remove) are encouraged**.

> Currently there is no homework required for this course, although I will
offer various exercises to demonstrate the topics covered. Hopefully you
will find this useful practice and interesting. Feedback on this would be
highly appreciated. Each lesson will have a file named `exercises` in it,
**please have a try at the tasks presented here**.

> *The only way to learn a new programming language is by writing programs
in it.* \- Dennis Ritchie.

> *Programming is a skill best acquired by practice and example rather
than from books.* \- Alan Turing.

#### Lesson 0 - Getting set up

#### Lesson 1 - Hello world

Writing your first program in Python. A comparison of the different programming
languages and how to write hello world in a variety of languages. We also introduce
some of the basics data types, containers, and operators.

#### Lesson 2 - Control flow, I/O, and functions

We introduce control flow tools like `if  else`,  `while`, and `for`. We also
show how to take use input, either from a file or interactively, and to output
this either to a file or the screen. We also introduce how to define functions
and consider variable scope.

#### Lesson 3 - Packages

We introduce the most commonly used packages in Python:
`numpy`, `pandas`, and `matplotlib`. This will introduce the python package
installer `pip`, namespaces, and some nice plotting features.

#### Lesson 4 - More functionality

More advanced functionality and function calls are explained,
introducing variable and keyword arguments. Resetting default
values is shown using `partial`, and we show how to vectorise 
functions with the `vectorize` wrapper. This leads to an 
introduction of some function wrappers and decorators. 

We introduce generators and `yield`, and showcase their use with some examples
of prime number generation. 

 
#### Lesson 5 - Classes

Classes are introduced and we introduce the basic class structure drawing
attention to the notion of class variables and methods. We will show the 
ideas behind class inheritance introducing the notion of the super-class
structure for good practice. 

#### Lesson 6 - Operator overloading

Using classes as an example, we will demonstrate the concept of operator 
overloading.

#### Lesson 7 - Advances classes

We introduce the notion of public and private class variables, and 
demonstrate virtual functions and abstract base classes. 

#### Lesson 8 - Requested topics

The current list of topics which have been requested by students include:
 * Algorithm design and analysis.
 * Overview of hardware and underlying processes.
    - Difference and similarities between OOP and functional programming.
    - Von Neumann architecture:
        + Differences between operation limited and bandwidth limited programms.
        + CPU and GPU structures.
        
#### Lesson 9
#### Lesson 10
#### Lesson 11
#### Lesson 12


## Possible topics

#### The basics

 * `Hello world`.
 * Data types:
    - Integers.
    - Floats.
    - Strings.
    - Booleans.
    - None.
    - NaN.
 * Containers:
    - Lists.
    - Sets.
    - Dictionaries.
    - Tuples.
 * Control flow:
    - If statements.
    - While loops.
    - For loops.
 * Input and output.
 * Functions:
    - Lambda functions.
 * Packages:
    - Numpy.
    - Matplotlib.
    - Pandas.
    - Scipy.
    - Sklearn.
 * `pip`.

#### Intermediate topics

 * Iterators:
    - Generators.
 * Functions:
    - Variable and keyword arguments.
    - Recursive functions.
    - Partial functions.
    - Function wrappers and decorators:
        + Meta decorators
    - Virtual functions.
 * Classes:
    - Public and private variables.
    - Inheritance.
    - Virtual/abstract methods.
    - `super`
 * LaTeX.
 * Storing data:
    - JSON.
    - Pickling.
    - Databases (MongoDB).
 * Data-frames, (`pandas.DataFrame`).
 * Arrays, (`numpy.array`).
 * Changing values by reference or by copying. 
 * Machine learning, (`sklearn`).
 * Symbolic programming, (`sympy`).
 * Garbage collection.
 * Object depth.
    - Deep copy and shallow copy. 
 * System commands.
 * Debugging.



### Advanced topics

 * Interacting with different programming languages.
 * Automatic testing.
 * Executables and compiled python.
 * Cython.
 * Parallel computing:
    - Multicore computing, (`mpi4py`).
    - GPU coding, (PyCuda).
 * Asynchronous programming. 


### Good practices

 * Commenting code:
    - Style guides, e.g. PEP8.
    - Docstrings.
    - Sphinx.
 * Virtual environments.
 * Modular organisation.
 * Project structure.
 * Unit testing.
 * Version control:
    - Git.

### Beyond Python

 * Compiled languages, e.g. C, C++.
 * Creating websites.
 * Algorithm design.
 * Pointers.
 * Memory management.










