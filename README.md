# pmic-error-injection-bmc

**An overview of the code:**

The way the code starts is it starts with an initialization constructor which initializes all of the variables and then creates a map/dictionary that contains the bus number and slave addressees for P0 and P1 which then allows in the other methods to call it by calling that certain method. In that same method you can call the dimm-info.sh which also shows which DIMMS are populated so when you run the code you are able to figure out if the system will shutdown and which will not.
The next method is the method which connects the BMC to the SSH and prints the error registers of the certain error that you requested to shutdown/hang the system. 
 Most of the other methods except for the last one are all methods are for the errors. They will print out the error and the command and say if a fatal, non-fatal, or a vendor-specific error has been printed and that will determine if an AC cycle is required.
The final method is a print menu method which prints out all the options of the errors: the MISC errors, the under voltage and the over voltage errors when you run the program. The print menu will show that the command is running with a print statement


**The Main Function:**

An argparse was written in the main function which allows you to input the correct arguments to run the program. Argparse is a user-friendly command line interface. Argparse is used when you need command-line arguments. There are 5 parser.add() arguments in the main function that are required. Those are described below and detailed in the format. Then the print_menu() is being called. When that is called then the options are able to be printed out

In order to run the code you need to 

1. put python3 pmicErrorInjectionTool.py host name, the username, the password, the DIMMS (2 options P0 or P1) and the channel name

Ex: python3 pmicErrorInjectionTool.py -host=hostname -username=username -password=password -DIMMS=P0  -channel=b

2. Then you will get dimm-info.sh which will give you which dimms are populated

3. Next you will get a list of options and you enter the command of which options you want.
If you choose an option from over or under voltage errors then you get a sub option of over voltage and under voltage before you get the actual command, but if you pick a MISC error you then will get the command after you pick that option 

Then the system will hang or shutdown if it is a fatal error or neither if it is not unless it is a vendor specific error then it will only shutdown depending on a certain DIMM. When you run the command it will let you know. 

4. AC Cycle Required to recover the system if a fatal error is injected 

**Confluence Page:**

https://confluence.amd.com/display/ES/PMIC+Error+Injection+Tool
