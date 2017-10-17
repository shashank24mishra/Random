# Random Number Generation
Algo to generate random number which should be 73% biased to the higher number.

## Getting Started
### Prerequisites
Python (2.X or 3.X) required.

### Installing 
Create a directory.
```
$ mkdir Random_number
```
Clone Project from remote.
```
$ git clone git@github.com:shashank24mishra/Random.git
```

## Running code
Change current directory to Random 
```
$ cd Random
```
Open Python shell
```
$ ipython
```
Importing Random_Number Class
```
In [1]: from bais_random import Random_Number
```
Create Instance for Random_Number
```
In [2]: random_obj = Random_Number()
```
Calling first generated random number by Random generator
```
In [3]: random_obj.random_no(start=5,end=39,total=10).next()    #random number between 5 to 39 10times
```
