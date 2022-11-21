# Python-Generator-Python-Mini-Project
 Mini Python project for generating text based captcha using tkinter
###

CONTENTS

### 1.	Introduction

#### 1.1.	 Purpose
#### 1.2.	 Captcha Overview
#### 1.3.	 Problem Statement
#### 1.4.	 System Overview
#### 1.5.	 Goal and Vision

### 2.	 Requirements Specification

### 3.	Procedure

### 4.	Constraints and Assumptions

### 5.	GUI Design 

### 6.	Coding

### 7.	Work done by each member

### 8.	Result/Conclusion

### 9.	References
#
## FlowChart
![image](https://user-images.githubusercontent.com/84535788/202147963-2ecead00-40d0-4b33-af36-8cdf61928cee.png)


## 1.	Introduction

This section will tell us about the project and give us an overview of what’s inside this project, the outcome of the project, the goal, and the vision of the project.


### 1.	Purpose

The purpose of this document tells us about a detailed description of the text-based captcha project. It will also explain the working of the project and the constraints and assumptions of the project. Also tells us about the GUI interface of the program. This basically helps anyone who wants to know how the captcha works and it’s possible usage in the future.


### 2.	Captcha Overview

A CAPTCHA (Completely Automated Public Turing Test to tell Computer and Humans Apart) is a type of test/challenge-response test used in determining whether the user is human or not.

Basically, the captcha is fully automated code requiring little human attention that benefits its user. It is a text-based image code with lines or blurry background or distorted background. The user is asked to enter the code, if he/she fails, then the access is denied.

So, if the test is passed by the user, then he/she is considered human otherwise it is considered a “Web Bot”.

### 3.	Problem Statement

As we know that nowadays computer bots are everywhere even on the Web. “Bot” generally refers to a computer program that is assigned a particular task automatically without any help.



Bots are generally used for fair means like testing some things. But nowadays people are using them for unfair means like spreading hate comments on Twitter and spamming someone resulting in huge traffic. So, to stop this one can use Captcha authentication as anyone can guess from its motto also “Easy for people, hard for bots”.


### 4.	System Overview

According to the topic, we have created a text-based captcha generator for university students and teachers. In this system, the user is first asked to enter his/her registration number and then the captcha.
Upon submission, the data is verified through the constraints in the program, and then they are taken to the next screen or presented with an error.

### 5.	Goal and Vision

The main goal of this project is to put a system that creates a test for the human beings but almost impossible for the computers to crack. The CAPTCHAs can be used by various website like IRCTC that have huge amount of data and can be halted with a small amount of error. They can also be used in mailing service to avoid the user to create fake emails.

## 2.	 Requirements Specifications

Firstly, to access this program you should have a PC/Laptop with working python compiler and GUI working on it.

Secondly, you should have all the necessary libraries like tkinter and random to use this program.


## 3.	 Procedure

1.	Open the python compiler.

2.	After opening the python compiler, type the code and attach all the images required by the program.

3.	After typing all the code, execute it.

4.	Then type your registration number and type the correct captcha.

5.	If the captcha and registration number will be correct, you will be forwarded to the next screen.


## 4.	 Constraints and Assumptions


Constraints for the registration number

1.	The registration number should be in numeric form.

2.	Registration number should be 5 digits for the faculty number and 8 digits for the students.
Constraints for the CAPTCHA
1.	It should be correct.


The assumption for this project is that it is designed for the university purpose and the users should know whether they have to type faculty/student registration number.


 ## 5. GUI Designs
![image](https://user-images.githubusercontent.com/84535788/203107457-5cba35b4-4b14-4bd3-9cdd-8c2749c5f02c.png)
  
### FIGURE 1
![image](https://user-images.githubusercontent.com/84535788/203107585-44017c27-ca45-42ba-be5b-14e36a429c60.png)

 
### FIGURE 2

 ![image](https://user-images.githubusercontent.com/84535788/203107600-552f3b57-ceb8-43a8-ac8e-34b77ac33a7c.png)

### FIGURE 3


![image](https://user-images.githubusercontent.com/84535788/203107635-0aceff69-1989-4e5d-af6a-ade019b8c316.png)


 
#### FIGURE 3.1

 ![image](https://user-images.githubusercontent.com/84535788/203107653-a645218e-d853-4b98-a5a0-8fcbf5e8ef68.png)

#### Figure 3.2

As we can see that in fig 3.1 and fig 3.2, the captchas are different. This is because the captcha is refreshed using the refresh button beside the captcha.

![image](https://user-images.githubusercontent.com/84535788/203107687-68817d4c-f120-459b-8cad-35eb619ac891.png)

 
#### FIGURE 4.1

As we can see in fig 4.1 that user has entered 123 as registration number which is against the constraints of the program, so the error message is prompted.

![image](https://user-images.githubusercontent.com/84535788/203107702-f2662771-8883-46fa-b45d-1ac39203db19.png)

 
#### FIGURE 4.2
As we can see in fig 4.2, user has entered wrong captcha this time, so for this also error message is prompted.

## RESULT/CONCLUSION

The captcha helps us to avoid both spam and bot present on different platform. It helps different platform to avoid fake accounts or post. The experience of developing this project also helped us learning lot about python and python GUI. It also simplifies the problem of redundant accounts on any platform.

It helps us to learn how to code in python and we can learn more about different module present in python. It also proved beneficial for us because we were able to design GUI in python


