# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
#Question 1:
#Assuming that we have some email addresses in the "username@companyname.com" format, please write program
#to print the company name of a given email address. Both user names and company names are composed of letters
#only.
#Input Format:
#The first line of the input contains an email address.
#Output Format:
#Print the company name in single line.
#Example;
#Input:
#john@google.com
#Output:
#google

inputvalue=input("Enter the Company email id:");
#print(inputvalue);
spStr=inputvalue.split("@");
#print(spStr[0]);
company=spStr[1].split(".");
print(company[0])
############################################
############################################

#Question 2:
#Write a program that accepts a comma-separated sequence of words as input and prints the words in a comma
#separated sequence after sorting them alphabetically.
#Input Format:
#The first line of input contains words separated by the comma.
#Output Format:
#Print the sorted words separated by the comma.
#Example:
#Input:
#without,hello,bag,world
#Output:
#bag,hello,without,world
inputvalue=input("Enter comma-separated sequence of words:");
print(inputvalue);
spStr=inputvalue.split(",");
spStr.sort(reverse = True)
str1=""
for st in spStr:  
    str1 =st+","+str1
le=len(str1)
print(str1[:le-1])
############################################
############################################

#Question 3:
#Create your own Jupyter Notebook for Sets.
#Reference link: https://www.w3schools.com/python/python_sets.asp
##done


############################################
############################################

#Question 4:
#Given a list of n-1 numbers ranging from 1 to n, your task is to find the missing number. There are no duplicates.
#Input Format:
#The first line contains n-1 numbers with each number separated by a space.
#Output Format:
#Print the missing number
#Example:
#Input:1 2 4 6 3 7 8
#Output:5
#Explanation:
#In the above list of numbers 5 is missing and hence 5 is the input

# 1 2 4 6 3 7 8

inputvalues=input("Enter list of numbers 1 to 10, each number separated by a space:")
inputvalues="   "+inputvalues
spstr=inputvalues.split(" ")
spint=[]
for l in spstr:
  if len(l)>0:
    spint.append(int(l))

spint.sort()
maxint=max(spint)
missingNumber=[]
for i in range(1,int(maxint)+1):
    if (inputvalues.find(" "+str(i))>0):
      None
    else:
      missingNumber.append(i);

print("Missing nubmers:",missingNumber)
############################################
############################################

#Question 5:
#With a given list L, write a program to print this list L after removing all duplicate values with original order reserved.
#Example:
#If the input list is
#12 24 35 24 88 120 155 88 120 155
#Then the output should be
#12 24 35 88 120 155
#Explanation:
#Third, seventh and ninth element of the list L has been removed because it was already present.
#Input Format:
#In one line take the elements of the list L with each element separated by a space.
#Output Format:
#Print the elements of the modified list in one line with each element separated by a space.
#Example:
#Input: 12 24 35 24
#Output:
#12 24 35
inputvalues=input("Enter list of numbers 1 to 10, each number separated by a space:")
# print(inputvalues)
inputvalues="   "+inputvalues
# print(inputvalues)
spstr=inputvalues.split(" ")
spint=[]
for l in spstr:
  if len(l)>0:
    spint.append(int(l))
spint = list(dict.fromkeys(spint))
spint.sort()

print(spint)
############################################
############################################