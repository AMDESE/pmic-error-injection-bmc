# pmic-error-injection-bmc

**What the tool does:**

The PMIC Error Injection Tool will shutdown the system you are running the script on if a fatal error is injected into the system. Only certain errors are fatal depending on the type of error injected into the system. The tool connects BMC to SSH to shutdown/hang if the injected error is fatal.

**Paramiko Library:**
This code uses a Python library that makes a connection with a remote device through SSH. Paramiko provides a client server functionality.

**An overview of the code:**

1. The way the code starts is it starts with an initialization constructor which initializes all of the variables and then creates a map/dictionary that contains the bus number and slave addressees for P0 and P1 which then allows in the other methods to call it by calling that certain method. In that same method you can call the dimm-info.sh which also shows which DIMMS are populated so when you run the code you are able to figure out if the system will shutdown and which will not.

2. The next method is the method which connects the BMC to the SSH and prints the error registers of the certain error that you requested to shutdown/hang the system. 
 Most of the other methods except for the last one are all methods are for the errors. They will print out the error and the command and say if a fatal, non-fatal, or a vendor-specific error has been printed and that will determine if an AC cycle is required.

3. The final method is a print menu method which prints out all the options of the errors: the MISC errors, the under voltage and the over voltage errors when you run the program. The print menu will show that the command is running with a print statement

**The Main Function:**

An argparse was written in the main function which allows you to input the correct arguments to run the program. Argparse is a user-friendly command line interface. Argparse is used when you need command-line arguments. There are 5 parser.add() arguments in the main function that are required. Those are described below and detailed in the format. Then the print_menu() is being called. When that is called then the options are able to be printed out
