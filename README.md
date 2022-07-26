# pmic-error-injection-bmc

**What the tool does:**
The PMIC Error Injection Tool will shutdown the system you are running the script on if a fatal error is injected into the system. Only certain errors are fatal depending on the type of error injected into the system. The tool connects BMC to SSH to shutdown/hang if the injected error is fatal.

**Paramiko Library:**
This code uses a Python library called Paramiko that makes a connection with a remote device through SSH. Paramiko provides a client server functionality.

**An overview of the code:**

1. The way the code starts is it starts with an initialization constructor which initializes all of the variables and then creates a map/dictionary that contains the bus number and slave addressees for P0 and P1 which then allows in the other methods to call it by calling that certain method. In that same method you can call the dimm-info.sh which also shows which DIMMS are populated so when you run the code you are able to figure out if the system will shutdown and which will not.

2. The next method is the method which connects the BMC to the SSH and prints the error registers of the certain error that you requested to shutdown/hang the system. 
 Most of the other methods except for the last one are all methods are for the errors. They will print out the error and the command and say if a fatal, non-fatal, or a vendor-specific error has been printed and that will determine if an AC cycle is required.

3. The final method is a print menu method which prints out all the options of the errors: the MISC errors, the under voltage and the over voltage errors when you run the program. The print menu will show that the command is running with a print statement

**The Main Function:**
An argparse was written in the main function which allows you to input the correct arguments to run the program. Argparse is a user-friendly command line interface. Argparse is used when you need command-line arguments. There are 5 parser.add() arguments in the main function that are required. Those are described below and detailed in the format. Then the print_menu() is being called. When that is called then the options are able to be printed out

**Python Type:**
python 3

**File Name:**
pmicErrorInjectionTool.py

**To Run the Program (Generic Form):**
python3 pmicErrorInjectionTool.py -hostname=hostname -username=username -password=password -DIMM=DIMM -channel=channel

Ex: python3 pmicErrorInjectionTool.py -hostname=onyx-738e -username=username -password=password -DIMM=P0 -channel=A

**DIMMS:**

Either P0 or P1 --->(needs to be P0 or P1)

P0 has Bus Number 0 or 1 

P1 has Bus Number 2 or 3

**Channels:**

A-L --->(the channel name can either be uppercase or lowercase)

A-L is the same for both P0 and P1

**Steps to Run the Code:**

1. Run the command
2. Pick the host name 
3. Type the username and password of the hostname
4. Pick the DIMM (which is either P0 or P1)
5. Then choose the channel
6. Once you press enter a list of options will appear: those are the error injections 
7. If it is a fatal error the system needs to be AC cycled

**Other Information:**

If you choose an SWA, SWB, SWC, SWD, VIN_BULK or VIN_MGMT you will get a sub-menu with options of over voltage and under voltage
If you choose a MISC error you will get the command straight away
When you pick the error type it the way it is written it the options
Once you pick the command you will get the output which either depending on the error will shutdown the system or do nothing depending on if it is a fatal error or not

**Confluence Page:**

The confluence page has a very detailed descreption of everything in the ReadMe and has more information
https://confluence.amd.com/display/ES/PMIC+Error+Injection+Tool
