# Project 0x03 Shell, init files, variables and expansions
Learnt about alias builtin, help builtin, local, global and reserved variables (`PATH`, `HOME` and `PS1`), special parameters `$?` and single an double quotes in **Shell**.

## Learning Objectives
At the end of this project, you are expected to be able to explain to anyone, without the help of Google:

## General
 - What happens when you type `$ ls -l *.txt`

## Shell Initialization Files
 - What are the `/etc/profile` file and the `/etc/profile.d` directory
 - What is the `~/.bashrc` file

## Variables
 - What is the difference between a local and a global variable
 - What is a reserved variable
 - How to create, update and delete shell variables
 - What are the roles of the following reserved variables: `HOME`, `PATH`, `PS1`
 - What are special parameters
 - What is the special parameter `$?`?
 
## Expansions
 - What is expansion and how to use them
 - What is the difference between single and double quotes and how to use them properly
 - How to do command substitution with `$()` and backticks

## Shell Arithmetic
 - How to perform arithmetic operations with the shell
 - The `alias` Command
 - How to create an alias
 - How to list aliases
 - How to temporarily disable an alias

## Other help pages
 - How to execute commands from a file in the current shell
 
## Requirements
### General
 - Allowed editors: `vi`, `vim`, `emacs`
 - All your scripts will be tested on `Ubuntu 20.04 LTS`
 - All your scripts should be exactly two lines long (`$ wc -l file` should print 2)
 - All your files should end with a new line (why?)
 - The first line of all your files should be exactly `#!/bin/bash`
 - A README.md file, at the root of the folder of the project, describing what each script is doing
 - You are not allowed to use `&&`, `||` or `;`
 - You are not allowed to use `bc`, `sed` or `awk`
 - All your files must be executable
 
## Technologies
| Technology | Details |
| -------- | ----------- |
| `Bash` | 5.0.17(1)-release |
| `Ubuntu` | 20.04 LTS |

## Scripts
The following describes what each script does when executed:

| Filename | Description |
| -------- | ----------- |
| `0-alias` | Creates an alias |
| `1-hello_you` | Prints `hello user`, where user is the current Linux user |
| `2-path` | Add `/action` to the `PATH`. `/action` should be the last directory the shell looks into when looking for a program |
| `3-paths` | Counts the number of the directories in the `PATH` |
| `4-global_variables` | Lists environment variables |
| `5-local_variables` | Lists all local variables and environment variables, and functions |
| `6-create_local_variable` | Creates a new local variable named `BETTY` |
| `7-create_global_variable` | Creates a new global variable named `HOLBERTON` |
| `8-true_knowledge` | Prints the result of the addition of 128 with the value stored in the environment variable `TRUEKNOWLEDGE`, followed by a new line |
| `9-divide_and_rule` | Prints the result of `POWER` divided by `DIVIDE`, followed by a new line |
| `10-love_exponent_breath` | Displays the result of `BREATH` to the power `LOVE` |
| `11-binary_to_decimal` | Converts a number from base 2 to base 10 |
| `12-combinations` | Prints all possible combinations of two letters, except `oo` |
| `13-print_float` | Prints a number with two decimal places. The number is stored in the environment variable `NUM` |
| `100-decimal_to_hexadecimal` | Converts a number from base 10 to base 16 |
| `101-rot13` | Encodes and decodes text using the rot13 encryption |
| `102-odd` | Prints every other line from the input, starting with the first line |
| `103-water_and_stir` | Adds the two numbers stored in the environment variables `WATER` and `STIR` and prints the result |
