# Project 0x00. Shell, Basics

It aims to learn about how to handle basic commands in **Shell**.

## Learning Objectives
At the end of this project, you are expected to be able to explain to anyone, without the help of Google:

##General
  -What does RTFM mean?
  -What is a Shebang
  -What is the Shell
  -What is the shell
  -What is the difference between a terminal and a shell
  -What is the shell prompt
  -How to use the history (the basics)
  
##Navigation
  -What do the commands or built-ins cd, pwd, ls do
  -How to navigate the filesystem
  -What are the . and .. directories
  -What is the working directory, how to print it and how to change it
  -What is the root directory
  -What is the home directory, and how to go there
  -What is the difference between the root directory and the home directory of the user root
  -What are the characteristics of hidden files and how to list them
  -What does the command cd - do
  
##Looking Around
  -What do the commands ls, less, file do
  -How do you use options and arguments with commands
  -Understand the ls long format and how to display it
  
##A Guided Tour
  -What does the ln command do
  -What do you find in the most common/important directories
  -What is a symbolic link
  -What is a hard link
  -What is the difference between a hard link and a symbolic link

##Manipulating Files
  -What do the commands cp, mv, rm, mkdir do
  -What are wildcards and how do they work
  -How to use wildcards
  
##Working with Commands
  -What do type, which, help, man commands do
  -What are the different kinds of commands
  -What is an alias
  -When do you use the command help instead of man

##Reading Man Pages
  -How to read a man page
  -What are man page sections
  -What are the section numbers for User commands, System calls and Library functions
  -Keyboard Shortcuts for Bash
  -Common shortcuts for Bash

##LTS
  -What does LTS mean?

## Technologies
| Technology | Details |
| Bash | 5.0.17(1)-release |
| Ubuntu | 20.04 LTS |

## Scripts
The following describes what each script does when executed:

| Filename | Description |
| -------- | ----------- |
| `0-current_working_directory` | A script that prints the absolute path name of the current working directory. |
| `1-listit` | Display the contents list of your current directory |
| `2-bring_me_home` | A script that changes the working directory to the user’s home directory |
| `3-listfiles` | Displays current directory contents in a long format |
| `4-listmorefiles` | Displays current directory contents, including hidden files (starting with `.`) using long format |
| `5-listfilesdigitonly` | Displays current directory contents in long format with user and group IDs displayed numerically and hidden files (starting with `.`) |
| `6-firstdirectory` | A script that creates a directory named `my_first_directory` in the `/tmp/` directory |
| `7-movethatfile` | Moves the file `betty` from `/tmp/` to `/tmp/my_first_directory` |
| `8-firstdelete` | Deletes the file betty |
| `9-firstdirdeletion` | Delete the directory `my_first_directory` that is in the `/tmp` directory |
| `10-back` | Changes the working directory to the previous one |
| `11-lists` | Lists all files in the current directory and its parent directory and the `/boot` directory |
| `12-file_type` | Prints the type of the file named `iamafile` that is in the `/tmp` directory |
| `13-symbolic_link` | Creates a symbolic link to `/bin/ls`, named `__ls__` |
| `14-copy_html` | Copies all the HTML files from the current working directory to the parent directory, but only copies files that did not exist in the parent directory |
| `100-lets_move` | Moves all files beginning with an uppercase letter to the directory `/tmp/u` |
| `101-clean_emacs` | Deletes all files in the current working directory that end with the character `~` |
| `102-tree` | Creates the directories `welcome/`, `welcome/to/` and `welcome/to/school` in the current directory |
| `103-commas` | Lists all the files and directories of the current directory, separated by commas (`,`) |
| `school.mgc` | Magic file that can be used with the command `file` to detect `School` data files. `School` data files always contain the string `SCHOOL` at offset 0 |
