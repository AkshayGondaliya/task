###Steps to run this Repository.

Requirements

- Docker
- Python3

###  Clone The Repository:

`git clone https://github.com/AkshayGondaliya/task.git`

`cd task` 

### Run Requirement.sh using the command given below

`sh requirements.sh`

After successful execution of this requirement.sh file you will land in docker container(name of the container = wobottask2).

Now, Go inside datadrive folder using command ..

`cd datadrive`

Now, install other Requirements using command ..

`sh requirement2.sh`
### How to execute edge detection Application

Go TO edge_detection folder and run given command to get edge detected image.

`python3 edge_detection.py --image input.png`

you will get output image (edge.png)

### How to execute edge detection Application

Go TO qr_code_scanner folder and run given command to get edge detected image.

`python3 scanner.py --image sc1.jpg`

you will get output in your terminal something like...

``image sc1.jpg is contain I love you .``

-Thank you
