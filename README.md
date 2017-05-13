## Synopsis
This program is written to generate random list of groups of employees at Apartment List. Each group is minimum of 3 employees and maximum of 5 employees. 

## Project
This project has been implemented in python using a basic CLI. A menu is presented to the user to add new employee, generate groups or exit out of the menu. In order to keep the employee list persistent, the records are stored in a database.

## Scenarios
The application checks for basic requirements like making sure groups are between three(3) and five(5), the group size is a random between
3-5 to keep the surprise factor in picking the group size. All employees are picked randomly in the groups. However, this application
doesn't keep track of previous groups so eventhough random, it's possible that two employees get selected into the same group in the 
following week. However, with increasing number of employees, this is an unlikely scenario.



