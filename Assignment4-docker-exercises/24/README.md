# Description
What is the smallest data only container you can make?


## Solution

Create hello.c file and write a simple program to output hello world

compile the program using 

    gcc -static hello.c -o helloworld

Build image by 

    docker build -t helloworld .

Run container using 

    docker run helloworld
