"""This program is mean tot give you practice using dictionaries.
Write a program that first reads from a user a set of usernames and passwords, and then enters a
program that simulates a user typing in passwords.
In the first part of the program, you are to read in a single integer that states the number of
username/password pairs that you will read in. Following this, there will be a set of that many user
names, one per line. Then there will be a set of that many passwords, one per line. You only need to
prompt one time at the beginning of the program. 
For example, input might be:
3
John
Jim
Joe
SecreT_passWorD
12345
G$a-4(ztY
Once that is read in, you should then repeatedly ask the person to type in a username and then
password. If they have a valid username and password combination, then print a message that they are
allowed into the system. If they have an incorrect username/password, then tell them (and allow them)
to try again (repeatedly).
Note: in practice, although this is the basic way passwords are handled, they should not be stored in
unencrypted format even in the program. Instead, passwords are encrypted when they are typed in,
they are stored in an encrypted format, and the comparisons are always between encrypted passwords.
There are also more extreme security measures."""

"""
By submitting this assignment, I agree to the following:
“Aggies do not lie, cheat, or steal, or tolerate those who do”
“I have not given or received any unauthorized aid on this assignment”

Name : Dathan Johnson
Section : 409
Assignment : lab 7b - 3
Date : 2-28-19
"""
k = 0
guess1 =''
guess2 = ''
passlist = []
userlist = []
Num = int(input('Number of usernames/passwords: '))
for i in range(0,Num):
    username = input('username: ')
    userlist.append(username)

for i in range(0,Num):
    password = input('password: ')
    passlist.append(password)
i = 1
while i > 0:
    guess1 = input('What is your username? ')
    guess2 = input('what is your password? ')
    if guess1 in userlist[k] and guess2 in passlist[k]:
        break
    else:
        k += 1
        continue
    break

print('You are allowd into the system')



print(userlist)
print(passlist) 


