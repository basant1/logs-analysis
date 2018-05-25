# Project 3: Logs Analysis 
### by Basant Singh

Third project of Udacity's [Full Stack Web Developer Nanodegree](https://www.udacity.com/course/full-stack-web-developer-nanodegree--nd004) program

## What it does

A Python program that creates a reporting tool that prints out reports (in plain text) based on the data in the database. This reporting tool is a Python program using the psycopg2 module to connect to the database.

## Required Libraries and Dependencies

1. [Python](https://www.python.org/downloads/) 2.x is required to run this project.

2. [VirtualBox](https://www.virtualbox.org/) to run your virtual machine. Install the platform package for your operating system. You do not need to launch VirtualBox after installing it; Vagrant will do that.

3. [Vagrant](https://www.vagrantup.com/) is the software that configures the VM and lets you share files between your host computer and the VM's filesystem.

4. Download the [project file](https://s3.amazonaws.com/video.udacity-data.com/topher/2018/April/5acfbfa3_fsnd-virtual-machine/fsnd-virtual-machine.zip) and unzip it or clone the [fullstack-nanodegree-vm](https://github.com/udacity/fullstack-nanodegree-vm) repository to your computer.

5. Download the [data](https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip) and unzip the file. Put this file into the vagrant directory, which is shared with your virtual machine.

## Project contents

This project consists of the following files:

* logs-analysis.py -  Will connect to the database, use SQL queries to analyze the log data, and print out the answers to the questions asked.

* output.txt - The output to the three questions asked:

1. What are the most popular three articles of all time?
2. Who are the most popular article authors of all time?
3. On which days did more than 1% of requests lead to errors?

* The project files and data you have to download which can be found [above.](https://github.com/basant1/logs-analysis#required-libraries-and-dependencies)

## How to Run Project
  
### Launching the Virtual Machine

1. Change to project directory in your terminal with cd. Inside, you will find another directory called vagrant. Change directory to the vagrant directory and run the following command:

```
vagrant up
``` 

2. Run the following command to log in to your newly installed Linux VM!

```
vagrant ssh
```

3. Inside the VM, change directory to /vagrant and look around with ls.

### Running the database

In the /vagrant directory, load the data by running command:

```
psql -d news -f newsdata.sql
```

which will connect to the database named news which has been set up for you and run the SQL statements in the file newsdata.sql.

### Running the queries

Open the terminal for your operating system (e.g. terminal window in Mac/Linux, command prompt in Windows)

Navigate to the /vagrant directory in the virtual machine and type the following command:

```
python logs-analysis.py
```

Your terminal should output the query results.
