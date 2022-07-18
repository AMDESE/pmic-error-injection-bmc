# pmic-error-injection-bmc

In order to run the code you need to put python3 pmicErrorInjectionTool.py host name, the username, the password, the DIMMS (2 options P0 or P1) and the channel name
Ex: python3 pmicErrorInjectionTool.py -host=hostname -username=username -password=password -DIMMS=P0  -channel=b
Then you will get dimm-info.sh which will give you which dimms are populated
Next you will get a list of options and you enter the command of which options you want.
If you choose an option from over or under voltage errors then you get a sub option of over voltage and under voltage before you get the actual command, but if you pick a MISC error you then will get the command after you pick that option 
Then the system will hang or shutdown depending on the type of error.

