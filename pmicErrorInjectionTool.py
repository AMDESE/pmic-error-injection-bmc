#!/usr/bin/env python3
import paramiko
import sys
import argparse

## @class Client
# @brief class for PMIC Error Injection Tool
##
class Client:

	##
	# @brief function that connects BMC through SSH
	# @param [in] host ---name of the host
	# @param [in] user ---username
	# @param [in] password ---password
	# @param [in] channel ---channel it is running on
	# @return none
	##
	def __init__(self, host, user, password, DIMMS, channel): 
		self.hostname = host
		self.username = user
		self.password = password
		self.DIMMS = DIMMS
		self.channel = channel
		self.command = ""
		self.response = ""
		self.channel_map_P0 = {"A": "0-20400000000", 
				"B": "0-20400000001",
				"C": "0-20400000002",
				"D": "0-20400000003",
				"E": "0-20400000004",
				"F": "0-20400000005",
				"G": "1-20400000000",
				"H": "1-20400000001",
				"I": "1-20400000002",
				"J": "1-20400000003",
				"K": "1-20400000004",
				"L": "1-20400000005"
				}
		self.channel_map_P1 = {"A": "2-20400000000", 
				"B": "2-20400000001",
				"C": "2-20400000002",
				"D": "2-20400000003",
				"E": "2-20400000004",
				"F": "2-20400000005",
				"G": "3-20400000000",
				"H": "3-20400000001",
				"I": "3-20400000002",
				"J": "3-20400000003",
				"K": "3-20400000004",
				"L": "3-20400000005"
				}
		print("\nThe number of DIMMS that are populated: ")
		client = paramiko.SSHClient()
		client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
		client.connect(hostname = self.hostname, port = 22, username = self.username, password = self.password)
		self.command = "/usr/sbin/dimm-info.sh"
		stdin, stdout, stderr = client.exec_command(self.command)
		output = stdout.read()
		output = output.replace(b'\n', b'')
		print(output)
		client.close()
		channel_key_P0  = self.channel.upper() 
		channel_key_P1  = self.channel.upper() 
		if self.DIMMS == "P0": 
			self.command = "i3ctransfer -d/dev/i3c-" + self.channel_map_P0[channel_key_P0] + " -w 0x35," 
		
		elif self.DIMMS == "P1":
			self.command = "i3ctransfer -d/dev/i3c-" + self.channel_map_P1[channel_key_P1] + " -w 0x35," 
		paramiko.SSHClient().set_missing_host_key_policy(paramiko.AutoAddPolicy())

	
	##
	# @brief function that connects BMC through SSH and has commands for the error registers. Calling this method in each other method allows the error registers to be printed
	# @return none
	##	
	def err_reg(self):	
		client = paramiko.SSHClient()
		client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
		client.connect(hostname = self.hostname, port = 22, username = self.username, password = self.password)
		stdin, stdout, stderr = client.exec_command(self.command)
		if ("0-20400000000" in self.command):
			self.response = "/usr/sbin/dimm-pmic-err.sh 0 0"
		elif ("0-20400000001" in self.command):
			self.response = "/usr/sbin/dimm-pmic-err.sh 0 1"
		elif ("0-20400000002" in self.command):
			self.response = "/usr/sbin/dimm-pmic-err.sh 0 2"
		elif ("0-20400000002" in self.command):
			self.response = "/usr/sbin/dimm-pmic-err.sh 0 3"
		elif ("0-20400000004" in self.command):
			self.response = "/usr/sbin/dimm-pmic-err.sh 0 4"
		elif ("0-20400000005" in self.command):
			self.response = "/usr/sbin/dimm-pmic-err.sh 0 5"
		elif ("1-20400000000" in self.command):
			self.response = "/usr/sbin/dimm-pmic-err.sh 1 0"
		elif ("1-20400000001" in self.command):
			self.response = "/usr/sbin/dimm-pmic-err.sh 1 1"
		elif ("1-20400000002" in self.command):
			self.response = "/usr/sbin/dimm-pmic-err.sh 1 2"
		elif ("1-20400000003" in self.command):
			self.response = "/usr/sbin/dimm-pmic-err.sh 1 3"
		elif ("1-20400000004" in self.command):
			self.response = "/usr/sbin/dimm-pmic-err.sh 1 4"
		elif ("1-20400000005" in self.command):
			self.response = "/usr/sbin/dimm-pmic-err.sh 1 5"
		elif ("2-20400000000" in self.command):
			self.response = "/usr/sbin/dimm-pmic-err.sh 2 0"
		elif ("2-20400000001" in self.command):
			self.response = "/usr/sbin/dimm-pmic-err.sh 2 1"
		elif ("2-20400000002" in self.command):
			self.response = "/usr/sbin/dimm-pmic-err.sh 2 2"
		elif ("2-20400000003" in self.command):
			self.response = "/usr/sbin/dimm-pmic-err.sh 2 3"
		elif ("2-20400000004" in self.command):
			self.response = "/usr/sbin/dimm-pmic-err.sh 2 4"
		elif ("2-20400000005" in self.command):
			self.response = "/usr/sbin/dimm-pmic-err.sh 2 5"
		elif ("3-20400000000" in self.command):
			self.response = "/usr/sbin/dimm-pmic-err.sh 3 0"
		elif ("3-20400000001" in self.command):
			self.response = "/usr/sbin/dimm-pmic-err.sh 3 1"
		elif ("3-20400000002" in self.command):
			self.response = "/usr/sbin/dimm-pmic-err.sh 3 2"
		elif ("3-20400000003" in self.command):
			self.response = "/usr/sbin/dimm-pmic-err.sh 3 3"
		elif ("3-20400000004" in self.command):
			self.response = "/usr/sbin/dimm-pmic-err.sh 3 4"
		elif ("3-20400000005" in self.command):
			self.response = "/usr/sbin/dimm-pmic-err.sh 3 5"	
		stdinResponse, stdoutResponse, stderrResponse = client.exec_command(self.response)
		output = stdoutResponse.read()
		output = output.replace(b'\n', b'')
		print(output)
		client.close()
	##
	# @brief function calls the error_registers method to print the error registres along with connecting to BMC to SSH
	# @return none
	##
	def run_swa_over_voltage(self):
		self.command = self.command + "0x90"
		print("\nFatal Error has been injected on SWA...\n")
		print("Over Voltage Command: " + self.command + "\n")
		
		if(self.command =="i3ctransfer -d/dev/i3c-0-20400000000 -w 0x35,0x90"):					
			print("P0: Channel A: Harvesting Channel Error Registers\n")
			self.err_reg()	
			
		elif(self.command =="i3ctransfer -d/dev/i3c-0-20400000001 -w 0x35,0x90"):
			print("P0: Channel B: Harvesting Channel Error Registers\n")	
			self.err_reg()
			
		elif(self.command =="i3ctransfer -d/dev/i3c-0-20400000002 -w 0x35,0x90"):
			print("P0: Channel C: Harvesting Channel Error Registers\n")
			self.err_reg()
			
		elif(self.command =="i3ctransfer -d/dev/i3c-0-20400000003 -w 0x35,0x90"):
			print("P0: Channel D: Harvesting Channel Error Registers\n")	
			self.err_reg()
			
		elif(self.command =="i3ctransfer -d/dev/i3c-0-20400000004 -w 0x35,0x90"):
			print("P0: Channel E: Harvesting Channel Error Registers\n")	
			self.err_reg()
			
		elif(self.command =="i3ctransfer -d/dev/i3c-0-20400000005 -w 0x35,0x90"):
			print("P0: Channel F: Harvesting Channel Error Registers\n")
			self.err_reg()
		elif(self.command =="i3ctransfer -d/dev/i3c-1-20400000000 -w 0x35,0x90"):
			print("P0: Channel G: Harvesting Channel Error Registers\n")	
			self.err_reg()
			
		elif(self.command =="i3ctransfer -d/dev/i3c-1-20400000001 -w 0x35,0x90"):
			print("P0: Channel H: Harvesting Channel Error Registers\n")	
			self.err_reg()
			
		elif(self.command =="i3ctransfer -d/dev/i3c-1-20400000002 -w 0x35,0x90"):
			print("P0: Channel I: Harvesting Channel Error Registers\n")	
			self.err_reg()
			
		elif(self.command =="i3ctransfer -d/dev/i3c-1-20400000003 -w 0x35,0x90"):
			print("P0: Channel J: Harvesting Channel Error Registers\n")	
			self.err_reg()
			
		elif(self.command =="i3ctransfer -d/dev/i3c-1-20400000004 -w 0x35,0x90"):
			print("P0: Channel K: Harvesting Channel Error Registers\n")	
			self.err_reg()
			
		elif(self.command =="i3ctransfer -d/dev/i3c-1-20400000005 -w 0x35,0x90"):
			print("P0: Channel L: Harvesting Channel Error Registers\n")	
			self.err_reg()
			
		elif(self.command =="i3ctransfer -d/dev/i3c-2-20400000000 -w 0x35,0x90"):
			print("P1: Channel A: Harvesting Channel Error Registers\n")	
			self.err_reg()
			
		elif(self.command =="i3ctransfer -d/dev/i3c-2-20400000001 -w 0x35,0x90"):
			print("P1: Channel B: Harvesting Channel Error Registers\n")	
			self.err_reg()
			
		elif(self.command =="i3ctransfer -d/dev/i3c-2-20400000002 -w 0x35,0x90"):
			print("P1: Channel C: Harvesting Channel Error Registers\n")	
			self.err_reg()
			
		elif(self.command =="i3ctransfer -d/dev/i3c-2-20400000003 -w 0x35,0x90"):
			print("P1: Channel D: Harvesting Channel Error Registers\n")	
			self.err_reg()
			
		elif(self.command =="i3ctransfer -d/dev/i3c-2-20400000004 -w 0x35,0x90"):
			print("P1: Channel E: Harvesting Channel Error Registers\n")	
			self.err_reg()
			
		elif(self.command =="i3ctransfer -d/dev/i3c-2-20400000005 -w 0x35,0x90"):
			print("P1: Channel F: Harvesting Channel Error Registers\n")	
			self.err_reg()
			
		elif(self.command =="i3ctransfer -d/dev/i3c-3-20400000000 -w 0x35,0x90"):
			print("P1: Channel G: Harvesting Channel Error Registers\n")	
			self.err_reg()
			
		elif(self.command =="i3ctransfer -d/dev/i3c-3-20400000001 -w 0x35,0x90"):
			print("P1: Channel H: Harvesting Channel Error Registers\n")	
			self.err_reg()
		
		elif(self.command =="i3ctransfer -d/dev/i3c-3-20400000002 -w 0x35,0x90"):
			print("P1: Channel I: Harvesting Channel Error Registers\n")	
			self.err_reg()
		
		elif(self.command =="i3ctransfer -d/dev/i3c-3-20400000003 -w 0x35,0x90"):
			print("P1: Channel J: Harvesting Channel Error Registers\n")	
			self.err_reg()
		
		elif(self.command =="i3ctransfer -d/dev/i3c-3-20400000004 -w 0x35,0x90"):
			print("P1: Channel K: Harvesting Channel Error Registers\n")	
			self.err_reg()
		
		elif(self.command =="i3ctransfer -d/dev/i3c-3-20400000005 -w 0x35,0x90"):
			print("P1: Channel L: Harvesting Channel Error Registers\n")	
			self.err_reg()
	
		print("\nAC Cycle required for system recovery if DIMM is detected and is a fatal error...")

	##
	# @brief function calls the error_registers method to print the error registres along with connecting to BMC to SSH
	# @return none
	##
	def run_swa_under_voltage(self):
		self.command = self.command + "0x98"
		print("\nFatal Error has been injected on SWA...\n")
		print("Under Voltage Command: " + self.command + "\n")
		
		if(self.command =="i3ctransfer -d/dev/i3c-0-20400000000 -w 0x35,0x98"):					
			print("P0: Channel A: Harvesting Channel Error Registers\n")	
			self.err_reg()
		
		elif(self.command =="i3ctransfer -d/dev/i3c-0-20400000001 -w 0x35,0x98"):
			print("P0: Channel B: Harvesting Channel Error Registers\n")	
			self.err_reg()
		
		elif(self.command =="i3ctransfer -d/dev/i3c-0-20400000002 -w 0x35,0x98"):
			print("P0: Channel C: Harvesting Channel Error Registers\n")	
			self.err_reg()
		
		elif(self.command =="i3ctransfer -d/dev/i3c-0-20400000003 -w 0x35,0x98"):
			print("P0: Channel D: Harvesting Channel Error Registers\n")	
			self.err_reg()
		
		elif(self.command =="i3ctransfer -d/dev/i3c-0-20400000004 -w 0x35,0x98"):
			print("P0: Channel E: Harvesting Channel Error Registers\n")	
			self.err_reg()
		
		elif(self.command =="i3ctransfer -d/dev/i3c-0-20400000005 -w 0x35,0x98"):
			print("P0: Channel F: Harvesting Channel Error Registers\n")
			self.err_reg()
		
		elif(self.command =="i3ctransfer -d/dev/i3c-1-20400000000 -w 0x35,0x98"):
			print("P0: Channel G: Harvesting Channel Error Registers\n")	
			self.err_reg()
		
		elif(self.command =="i3ctransfer -d/dev/i3c-1-20400000001 -w 0x35,0x98"):
			print("P0: Channel H: Harvesting Channel Error Registers\n")	
			self.err_reg()

		elif(self.command =="i3ctransfer -d/dev/i3c-1-20400000002 -w 0x35,0x98"):
			print("P0: Channel I: Harvesting Channel Error Registers\n")	
			self.err_reg()
		
		elif(self.command =="i3ctransfer -d/dev/i3c-1-20400000003 -w 0x35,0x98"):
			print("P0: Channel J: Harvesting Channel Error Registers\n")	
			self.err_reg()
		
		elif(self.command =="i3ctransfer -d/dev/i3c-1-20400000004 -w 0x35,0x98"):
			print("P0: Channel K: Harvesting Channel Error Registers\n")	
			self.err_reg()
		
		elif(self.command =="i3ctransfer -d/dev/i3c-1-20400000005 -w 0x35,0x98"):
			print("P0: Channel L: Harvesting Channel Error Registers\n")	
			self.err_reg()
		
		elif(self.command =="i3ctransfer -d/dev/i3c-2-20400000000 -w 0x35,0x98"):
			print("P1: Channel A: Harvesting Channel Error Registers\n")	
			self.err_reg()
			
		elif(self.command =="i3ctransfer -d/dev/i3c-2-20400000001 -w 0x35,0x98"):
			print("P1: Channel B: Harvesting Channel Error Registers\n")	
			self.err_reg()
			
		elif(self.command =="i3ctransfer -d/dev/i3c-2-20400000002 -w 0x35,0x98"):
			print("P1: Channel C: Harvesting Channel Error Registers\n")	
			self.err_reg()
			
		elif(self.command =="i3ctransfer -d/dev/i3c-2-20400000003 -w 0x35,0x98"):
			print("P1: Channel D: Harvesting Channel Error Registers\n")	
			self.err_reg()
			
		elif(self.command =="i3ctransfer -d/dev/i3c-2-20400000004 -w 0x35,0x98"):
			print("P1: Channel E: Harvesting Channel Error Registers\n")	
			self.err_reg()
			
		elif(self.command =="i3ctransfer -d/dev/i3c-2-20400000005 -w 0x35,0x98"):
			print("P1: Channel F: Harvesting Channel Error Registers\n")	
			self.err_reg()
			
		elif(self.command =="i3ctransfer -d/dev/i3c-3-20400000000 -w 0x35,0x98"):
			print("P1: Channel G: Harvesting Channel Error Registers\n")	
			self.err_reg()
			
		elif(self.command =="i3ctransfer -d/dev/i3c-3-20400000001 -w 0x35,0x98"):
			print("P1: Channel H: Harvesting Channel Error Registers\n")	
			self.err_reg()
		
		elif(self.command =="i3ctransfer -d/dev/i3c-3-20400000002 -w 0x35,0x98"):
			print("P1: Channel I: Harvesting Channel Error Registers\n")	
			self.err_reg()
		
		elif(self.command =="i3ctransfer -d/dev/i3c-3-20400000003 -w 0x35,0x98"):
			print("P1: Channel J: Harvesting Channel Error Registers\n")	
			self.err_reg()
		
		elif(self.command =="i3ctransfer -d/dev/i3c-3-20400000004 -w 0x35,0x98"):
			print("P1: Channel K: Harvesting Channel Error Registers\n")	
			self.err_reg()
		
		elif(self.command =="i3ctransfer -d/dev/i3c-3-20400000005 -w 0x35,0x98"):
			print("P1: Channel L: Harvesting Channel Error Registers\n")	
			self.err_reg()
	
		print("\nAC Cycle required for system recovery if DIMM is detected and is a fatal error...")						

	##
	# @brief function calls the error_registers method to print the error registres along with connecting to BMC to SSH
	# @return none
	##
	def run_swb_over_voltage(self): 
		self.command = self.command + "0xA0"
		print("\nVendor Specific Error has been injected on SWB...\n")
		print("Over Voltage Command: " + self.command + "\n")
		
		if(self.command =="i3ctransfer -d/dev/i3c-0-20400000000 -w 0x35,0xA0"):					
			print("P0: Channel A: Harvesting Channel Error Registers\n")	
			self.err_reg()
		
		elif(self.command =="i3ctransfer -d/dev/i3c-0-20400000001 -w 0x35,0xA0"):
			print("P0: Channel B: Harvesting Channel Error Registers\n")	
			self.err_reg()
		
		elif(self.command =="i3ctransfer -d/dev/i3c-0-20400000002 -w 0x35,0xA0"):
			print("P0: Channel C: Harvesting Channel Error Registers\n")	
			self.err_reg()
		
		elif(self.command =="i3ctransfer -d/dev/i3c-0-20400000003 -w 0x35,0xA0"):
			print("P0: Channel D: Harvesting Channel Error Registers\n")	
			self.err_reg()
		
		elif(self.command =="i3ctransfer -d/dev/i3c-0-20400000004 -w 0x35,0xA0"):
			print("P0: Channel E: Harvesting Channel Error Registers\n")	
			self.err_reg()
		
		elif(self.command =="i3ctransfer -d/dev/i3c-0-20400000005 -w 0x35,0xA0"):
			print("P0: Channel F: Harvesting Channel Error Registers\n")
			self.err_reg()
		
		elif(self.command =="i3ctransfer -d/dev/i3c-1-20400000000 -w 0x35,0xA0"):
			print("P0: Channel G: Harvesting Channel Error Registers\n")	
			self.err_reg()
		
		elif(self.command =="i3ctransfer -d/dev/i3c-1-20400000001 -w 0x35,0xA0"):
			print("P0: Channel H: Harvesting Channel Error Registers\n")	
			self.err_reg()

		elif(self.command =="i3ctransfer -d/dev/i3c-1-20400000002 -w 0x35,0xA0"):
			print("P0: Channel I: Harvesting Channel Error Registers\n")	
			self.err_reg()
		
		elif(self.command =="i3ctransfer -d/dev/i3c-1-20400000003 -w 0x35,0xA0"):
			print("P0: Channel J: Harvesting Channel Error Registers\n")	
			self.err_reg()
		
		elif(self.command =="i3ctransfer -d/dev/i3c-1-20400000004 -w 0x35,0xA0"):
			print("P0: Channel K: Harvesting Channel Error Registers\n")	
			self.err_reg()
		
		elif(self.command =="i3ctransfer -d/dev/i3c-1-20400000005 -w 0x35,0xA0"):
			print("P0: Channel L: Harvesting Channel Error Registers\n")	
			self.err_reg()
		
		elif(self.command =="i3ctransfer -d/dev/i3c-2-20400000000 -w 0x35,0xA0"):
			print("P1: Channel A: Harvesting Channel Error Registers\n")	
			self.err_reg()
			
		elif(self.command =="i3ctransfer -d/dev/i3c-2-20400000001 -w 0x35,0xA0"):
			print("P1: Channel B: Harvesting Channel Error Registers\n")	
			self.err_reg()
			
		elif(self.command =="i3ctransfer -d/dev/i3c-2-20400000002 -w 0x35,0xA0"):
			print("P1: Channel C: Harvesting Channel Error Registers\n")	
			self.err_reg()
			
		elif(self.command =="i3ctransfer -d/dev/i3c-2-20400000003 -w 0x35,0xA0"):
			print("P1: Channel D: Harvesting Channel Error Registers\n")	
			self.err_reg()
			
		elif(self.command =="i3ctransfer -d/dev/i3c-2-20400000004 -w 0x35,0xA0"):
			print("P1: Channel E: Harvesting Channel Error Registers\n")	
			self.err_reg()
			
		elif(self.command =="i3ctransfer -d/dev/i3c-2-20400000005 -w 0x35,0xA0"):
			print("P1: Channel F: Harvesting Channel Error Registers\n")	
			self.err_reg()
			
		elif(self.command =="i3ctransfer -d/dev/i3c-3-20400000000 -w 0x35,0xA0"):
			print("P1: Channel G: Harvesting Channel Error Registers\n")	
			self.err_reg()
			
		elif(self.command =="i3ctransfer -d/dev/i3c-3-20400000001 -w 0x35,0xA0"):
			print("P1: Channel H: Harvesting Channel Error Registers\n")	
			self.err_reg()
		
		elif(self.command =="i3ctransfer -d/dev/i3c-3-20400000002 -w 0x35,0xA0"):
			print("P1: Channel I: Harvesting Channel Error Registers\n")	
			self.err_reg()
		
		elif(self.command =="i3ctransfer -d/dev/i3c-3-20400000003 -w 0x35,0xA0"):
			print("P1: Channel J: Harvesting Channel Error Registers\n")	
			self.err_reg()
		
		elif(self.command =="i3ctransfer -d/dev/i3c-3-20400000004 -w 0x35,0xA0"):
			print("P1: Channel K: Harvesting Channel Error Registers\n")	
			self.err_reg()
		
		elif(self.command =="i3ctransfer -d/dev/i3c-3-20400000005 -w 0x35,0xA0"):
			print("P1: Channel L: Harvesting Channel Error Registers\n")	
			self.err_reg()
		
		print("\nNo AC Cycle required for system recovery...")
		
	
	##
	# @brief function calls the error_registers method to print the error registres along with connecting to BMC to SSH
	# @return none
	##
	def run_swb_under_voltage(self): 
		self.command = self.command + "0xA8"
		print("\nVendor Specific Error has been injected on SWB...\n")
		print("Under Voltage Command: " + self.command + "\n")
		
		if(self.command =="i3ctransfer -d/dev/i3c-0-20400000000 -w 0x35,0xA8"):					
			print("P0: Channel A: Harvesting Channel Error Registers\n")	
			self.err_reg()
		
		elif(self.command =="i3ctransfer -d/dev/i3c-0-20400000001 -w 0x35,0xA8"):
			print("P0: Channel B: Harvesting Channel Error Registers\n")	
			self.err_reg()
		
		elif(self.command =="i3ctransfer -d/dev/i3c-0-20400000002 -w 0x35,0xA8"):
			print("P0: Channel C: Harvesting Channel Error Registers\n")	
			self.err_reg()
		
		elif(self.command =="i3ctransfer -d/dev/i3c-0-20400000003 -w 0x35,0xA8"):
			print("P0: Channel D: Harvesting Channel Error Registers\n")	
			self.err_reg()
		
		elif(self.command =="i3ctransfer -d/dev/i3c-0-20400000004 -w 0x35,0xA8"):
			print("P0: Channel E: Harvesting Channel Error Registers\n")	
			self.err_reg()
		
		elif(self.command =="i3ctransfer -d/dev/i3c-0-20400000005 -w 0x35,0xA8"):
			print("P0: Channel F: Harvesting Channel Error Registers\n")
			self.err_reg()
		
		elif(self.command =="i3ctransfer -d/dev/i3c-1-20400000000 -w 0x35,0xA8"):
			print("P0: Channel G: Harvesting Channel Error Registers\n")	
			self.err_reg()
		
		elif(self.command =="i3ctransfer -d/dev/i3c-1-20400000001 -w 0x35,0xA8"):
			print("P0: Channel H: Harvesting Channel Error Registers\n")	
			self.err_reg()

		elif(self.command =="i3ctransfer -d/dev/i3c-1-20400000002 -w 0x35,0xA8"):
			print("P0: Channel I: Harvesting Channel Error Registers\n")	
			self.err_reg()
		
		elif(self.command =="i3ctransfer -d/dev/i3c-1-20400000003 -w 0x35,0xA8"):
			print("P0: Channel J: Harvesting Channel Error Registers\n")	
			self.err_reg()
		
		elif(self.command =="i3ctransfer -d/dev/i3c-1-20400000004 -w 0x35,0xA8"):
			print("P0: Channel K: Harvesting Channel Error Registers\n")	
			self.err_reg()
		
		elif(self.command =="i3ctransfer -d/dev/i3c-1-20400000005 -w 0x35,0xA8"):
			print("P0: Channel L: Harvesting Channel Error Registers\n")	
			self.err_reg()
		
		elif(self.command =="i3ctransfer -d/dev/i3c-2-20400000000 -w 0x35,0xA8"):
			print("P1: Channel A: Harvesting Channel Error Registers\n")	
			self.err_reg()
			
		elif(self.command =="i3ctransfer -d/dev/i3c-2-20400000001 -w 0x35,0xA8"):
			print("P1: Channel B: Harvesting Channel Error Registers\n")	
			self.err_reg()
			
		elif(self.command =="i3ctransfer -d/dev/i3c-2-20400000002 -w 0x35,0xA8"):
			print("P1: Channel C: Harvesting Channel Error Registers\n")	
			self.err_reg()
			
		elif(self.command =="i3ctransfer -d/dev/i3c-2-20400000003 -w 0x35,0xA8"):
			print("P1: Channel D: Harvesting Channel Error Registers\n")	
			self.err_reg()
			
		elif(self.command =="i3ctransfer -d/dev/i3c-2-20400000004 -w 0x35,0xA8"):
			print("P1: Channel E: Harvesting Channel Error Registers\n")	
			self.err_reg()
			
		elif(self.command =="i3ctransfer -d/dev/i3c-2-20400000005 -w 0x35,0xA8"):
			print("P1: Channel F: Harvesting Channel Error Registers\n")	
			self.err_reg()
			
		elif(self.command =="i3ctransfer -d/dev/i3c-3-20400000000 -w 0x35,0xA8"):
			print("P1: Channel G: Harvesting Channel Error Registers\n")	
			self.err_reg()
			
		elif(self.command =="i3ctransfer -d/dev/i3c-3-20400000001 -w 0x35,0xA8"):
			print("P1: Channel H: Harvesting Channel Error Registers\n")	
			self.err_reg()
		
		elif(self.command =="i3ctransfer -d/dev/i3c-3-20400000002 -w 0x35,0xA8"):
			print("P1: Channel I: Harvesting Channel Error Registers\n")	
			self.err_reg()
		
		elif(self.command =="i3ctransfer -d/dev/i3c-3-20400000003 -w 0x35,0xA8"):
			print("P1: Channel J: Harvesting Channel Error Registers\n")	
			self.err_reg()
		
		elif(self.command =="i3ctransfer -d/dev/i3c-3-20400000004 -w 0x35,0xA8"):
			print("P1: Channel K: Harvesting Channel Error Registers\n")	
			self.err_reg()
		
		elif(self.command =="i3ctransfer -d/dev/i3c-3-20400000005 -w 0x35,0xA8"):
			print("P1: Channel L: Harvesting Channel Error Registers\n")	
			self.err_reg()
		
		print("\nAC Cycle required for system recovery...")
	
	##
	# @brief function calls the error_registers method to print the error registres along with connecting to BMC to SSH
	# @return none
	##
	def run_swc_over_voltage(self):
		self.command = self.command + "0xB0"
		print("\nFatal Error Injected into SWC...\n")
		print("Over Voltage Command: " + self.command + "\n")

		if(self.command =="i3ctransfer -d/dev/i3c-0-20400000000 -w 0x35,0xB0"):					
			print("P0: Channel A: Harvesting Channel Error Registers\n")	
			self.err_reg()
		
		elif(self.command =="i3ctransfer -d/dev/i3c-0-20400000001 -w 0x35,0xB0"):
			print("P0: Channel B: Harvesting Channel Error Registers\n")	
			self.err_reg()
		
		elif(self.command =="i3ctransfer -d/dev/i3c-0-20400000002 -w 0x35,0xB0"):
			print("P0: Channel C: Harvesting Channel Error Registers\n")	
			self.err_reg()
		
		elif(self.command =="i3ctransfer -d/dev/i3c-0-20400000003 -w 0x35,0xB0"):
			print("P0: Channel D: Harvesting Channel Error Registers\n")	
			self.err_reg()
		
		elif(self.command =="i3ctransfer -d/dev/i3c-0-20400000004 -w 0x35,0xB0"):
			print("P0: Channel E: Harvesting Channel Error Registers\n")	
			self.err_reg()
		
		elif(self.command =="i3ctransfer -d/dev/i3c-0-20400000005 -w 0x35,0xB0"):
			print("P0: Channel F: Harvesting Channel Error Registers\n")
			self.err_reg()
		
		elif(self.command =="i3ctransfer -d/dev/i3c-1-20400000000 -w 0x35,0xB0"):
			print("P0: Channel G: Harvesting Channel Error Registers\n")	
			self.err_reg()
		
		elif(self.command =="i3ctransfer -d/dev/i3c-1-20400000001 -w 0x35,0xB0"):
			print("P0: Channel H: Harvesting Channel Error Registers\n")	
			self.err_reg()

		
		elif(self.command =="i3ctransfer -d/dev/i3c-1-20400000002 -w 0x35,0xB0"):
			print("P0: Channel I: Harvesting Channel Error Registers\n")	
			self.err_reg()
		
		
		elif(self.command =="i3ctransfer -d/dev/i3c-1-20400000003 -w 0x35,0xB0"):
			print("P0: Channel J: Harvesting Channel Error Registers\n")	
			self.err_reg()
		
		elif(self.command =="i3ctransfer -d/dev/i3c-1-20400000004 -w 0x35,0xB0"):
			print("P0: Channel K: Harvesting Channel Error Registers\n")	
			self.err_reg()
		
		elif(self.command =="i3ctransfer -d/dev/i3c-1-20400000005 -w 0x35,0xB0"):
			print("P0: Channel L: Harvesting Channel Error Registers\n")	
			self.err_reg()
		
		elif(self.command =="i3ctransfer -d/dev/i3c-2-20400000000 -w 0x35,0xB0"):
			print("P1: Channel A: Harvesting Channel Error Registers\n")	
			self.err_reg()
			
		elif(self.command =="i3ctransfer -d/dev/i3c-2-20400000001 -w 0x35,0xB0"):
			print("P1: Channel B: Harvesting Channel Error Registers\n")	
			self.err_reg()
			
		elif(self.command =="i3ctransfer -d/dev/i3c-2-20400000002 -w 0x35,0xB0"):
			print("P1: Channel C: Harvesting Channel Error Registers\n")	
			self.err_reg()
			
		elif(self.command =="i3ctransfer -d/dev/i3c-2-20400000003 -w 0x35,0xB0"):
			print("P1: Channel D: Harvesting Channel Error Registers\n")	
			self.err_reg()
			
		elif(self.command =="i3ctransfer -d/dev/i3c-2-20400000004 -w 0x35,0xB0"):
			print("P1: Channel E: Harvesting Channel Error Registers\n")	
			self.err_reg()
			
		elif(self.command =="i3ctransfer -d/dev/i3c-2-20400000005 -w 0x35,0xB0"):
			print("P1: Channel F: Harvesting Channel Error Registers\n")	
			self.err_reg()
			
		elif(self.command =="i3ctransfer -d/dev/i3c-3-20400000000 -w 0x35,0xB0"):
			print("P1: Channel G: Harvesting Channel Error Registers\n")	
			self.err_reg()
			
		elif(self.command =="i3ctransfer -d/dev/i3c-3-20400000001 -w 0x35,0xB0"):
			print("P1: Channel H: Harvesting Channel Error Registers\n")	
			self.err_reg()
		
		elif(self.command =="i3ctransfer -d/dev/i3c-3-20400000002 -w 0x35,0xB0"):
			print("P1: Channel I: Harvesting Channel Error Registers\n")	
			self.err_reg()
		
		elif(self.command =="i3ctransfer -d/dev/i3c-3-20400000003 -w 0x35,0xB0"):
			print("P1: Channel J: Harvesting Channel Error Registers\n")	
			self.err_reg()
		
		elif(self.command =="i3ctransfer -d/dev/i3c-3-20400000004 -w 0x35,0xB0"):
			print("P1: Channel K: Harvesting Channel Error Registers\n")	
			self.err_reg()
			
		elif(self.command =="i3ctransfer -d/dev/i3c-3-20400000005 -w 0x35,0xB0"):
			print("P1: Channel L: Harvesting Channel Error Registers\n")	
			self.err_reg()
		
		print("\nAC Cycle required for system recovery if DIMM is detected and is a fatal error...")
	
	##
	# @brief function calls the error_registers method to print the error registres along with connecting to BMC to SSH
	# @return none
	##
	def run_swc_under_voltage(self):
		self.command = self.command + "0xB8"
		print("\nFatal Error Injected into SWC...\n")
		print("Under Voltage Command: " + self.command + "\n")

		if(self.command =="i3ctransfer -d/dev/i3c-0-20400000000 -w 0x35,0xB8"):					
			print("P0: Channel A: Harvesting Channel Error Registers\n")	
			self.err_reg()
		
		elif(self.command =="i3ctransfer -d/dev/i3c-0-20400000001 -w 0x35,0xB8"):
			print("P0: Channel B: Harvesting Channel Error Registers\n")	
			self.err_reg()
		
		elif(self.command =="i3ctransfer -d/dev/i3c-0-20400000002 -w 0x35,0xB8"):
			print("P0: Channel C: Harvesting Channel Error Registers\n")	
			self.err_reg()
		
		elif(self.command =="i3ctransfer -d/dev/i3c-0-20400000003 -w 0x35,0xB8"):
			print("P0: Channel D: Harvesting Channel Error Registers\n")	
			self.err_reg()
		
		elif(self.command =="i3ctransfer -d/dev/i3c-0-20400000004 -w 0x35,0xB8"):
			print("P0: Channel E: Harvesting Channel Error Registers\n")	
			self.err_reg()
		
		elif(self.command =="i3ctransfer -d/dev/i3c-0-20400000005 -w 0x35,0xB8"):
			print("P0: Channel F: Harvesting Channel Error Registers\n")
			self.err_reg()
		
		elif(self.command =="i3ctransfer -d/dev/i3c-1-20400000000 -w 0x35,0xB8"):
			print("P0: Channel G: Harvesting Channel Error Registers\n")	
			self.err_reg()
		
		elif(self.command =="i3ctransfer -d/dev/i3c-1-20400000001 -w 0x35,0xB8"):
			print("P0: Channel H: Harvesting Channel Error Registers\n")	
			self.err_reg()

		elif(self.command =="i3ctransfer -d/dev/i3c-1-20400000002 -w 0x35,0xB8"):
			print("P0: Channel I: Harvesting Channel Error Registers\n")	
			self.err_reg()
		
		elif(self.command =="i3ctransfer -d/dev/i3c-1-20400000003 -w 0x35,0xB8"):
			print("P0: Channel J: Harvesting Channel Error Registers\n")	
			self.err_reg()
		
		elif(self.command =="i3ctransfer -d/dev/i3c-1-20400000004 -w 0x35,0xB8"):
			print("P0: Channel K: Harvesting Channel Error Registers\n")	
			self.err_reg()
		
		elif(self.command =="i3ctransfer -d/dev/i3c-1-20400000005 -w 0x35,0xB8"):
			print("P0: Channel L: Harvesting Channel Error Registers\n")	
			self.err_reg()
		
		elif(self.command =="i3ctransfer -d/dev/i3c-2-20400000000 -w 0x35,0xB8"):
			print("P1: Channel A: Harvesting Channel Error Registers\n")	
			self.err_reg()
			
		elif(self.command =="i3ctransfer -d/dev/i3c-2-20400000001 -w 0x35,0xB8"):
			print("P1: Channel B: Harvesting Channel Error Registers\n")	
			self.err_reg()
			
		elif(self.command =="i3ctransfer -d/dev/i3c-2-20400000002 -w 0x35,0xB8"):
			print("P1: Channel C: Harvesting Channel Error Registers\n")	
			self.err_reg()
			
		elif(self.command =="i3ctransfer -d/dev/i3c-2-20400000003 -w 0x35,0xB8"):
			print("P1: Channel D: Harvesting Channel Error Registers\n")	
			self.err_reg()
			
		elif(self.command =="i3ctransfer -d/dev/i3c-2-20400000004 -w 0x35,0xB8"):
			print("P1: Channel E: Harvesting Channel Error Registers\n")	
			self.err_reg()
			
		elif(self.command =="i3ctransfer -d/dev/i3c-2-20400000005 -w 0x35,0xB8"):
			print("P1: Channel F: Harvesting Channel Error Registers\n")	
			self.err_reg()
			
		elif(self.command =="i3ctransfer -d/dev/i3c-3-20400000000 -w 0x35,0xB8"):
			print("P1: Channel G: Harvesting Channel Error Registers\n")	
			self.err_reg()
			
		elif(self.command =="i3ctransfer -d/dev/i3c-3-20400000001 -w 0x35,0xB8"):
			print("P1: Channel H: Harvesting Channel Error Registers\n")	
			self.err_reg()
		
		elif(self.command =="i3ctransfer -d/dev/i3c-3-20400000002 -w 0x35,0xB8"):
			print("P1: Channel I: Harvesting Channel Error Registers\n")	
			self.err_reg()
		
		elif(self.command =="i3ctransfer -d/dev/i3c-3-20400000003 -w 0x35,0xB8"):
			print("P1: Channel J: Harvesting Channel Error Registers\n")	
			self.err_reg()
		
		elif(self.command =="i3ctransfer -d/dev/i3c-3-20400000004 -w 0x35,0xB8"):
			print("P1: Channel K: Harvesting Channel Error Registers\n")	
			self.err_reg()
			
		elif(self.command =="i3ctransfer -d/dev/i3c-3-20400000005 -w 0x35,0xB8"):
			print("P1: Channel L: Harvesting Channel Error Registers\n")	
			self.err_reg()
		
		print("\nAC Cycle required for system recovery if DIMM is detected and is a fatal error...")
	
	##
	# @brief function calls the error_registers method to print the error registres along with connecting to BMC to SSH
	# @return none
	##
	def run_swd_over_voltage(self):
		self.command = self.command + "0xC0"
		print("\nFatal Error Injected into SWD...")
		print("\nOver Voltage Command: " + self.command + "\n")
		
		
		if(self.command =="i3ctransfer -d/dev/i3c-0-20400000000 -w 0x35,0xC0"):					
			print("P0: Channel A: Harvesting Channel Error Registers\n")	
			self.err_reg()
		
		elif(self.command =="i3ctransfer -d/dev/i3c-0-20400000001 -w 0x35,0xC0"):
			print("P0: Channel B: Harvesting Channel Error Registers\n")	
			self.err_reg()
		
		elif(self.command =="i3ctransfer -d/dev/i3c-0-20400000002 -w 0x35,0xC0"):
			print("P0: Channel C: Harvesting Channel Error Registers\n")	
			self.err_reg()
		
		elif(self.command =="i3ctransfer -d/dev/i3c-0-20400000003 -w 0x35,0xC0"):
			print("P0: Channel D: Harvesting Channel Error Registers\n")	
			self.err_reg()
		
		elif(self.command =="i3ctransfer -d/dev/i3c-0-20400000004 -w 0x35,0xC0"):
			print("P0: Channel E: Harvesting Channel Error Registers\n")	
			self.err_reg()
		
		elif(self.command =="i3ctransfer -d/dev/i3c-0-20400000005 -w 0x35,0xC0"):
			print("P0: Channel F: Harvesting Channel Error Registers\n")
			self.err_reg()
		
		elif(self.command =="i3ctransfer -d/dev/i3c-1-20400000000 -w 0x35,0xC0"):
			print("P0: Channel G: Harvesting Channel Error Registers\n")	
			self.err_reg()
		
		elif(self.command =="i3ctransfer -d/dev/i3c-1-20400000001 -w 0x35,0xC0"):
			print("P0: Channel H: Harvesting Channel Error Registers\n")	
			self.err_reg()
		
		elif(self.command =="i3ctransfer -d/dev/i3c-1-20400000002 -w 0x35,0xC0"):
			print("P0: Channel I: Harvesting Channel Error Registers\n")	
			self.err_reg()
		
		elif(self.command =="i3ctransfer -d/dev/i3c-1-20400000003 -w 0x35,0xC0"):
			print("P0: Channel J: Harvesting Channel Error Registers\n")	
			self.err_reg()
		
		elif(self.command =="i3ctransfer -d/dev/i3c-1-20400000004 -w 0x35,0xC0"):
			print("P0: Channel K: Harvesting Channel Error Registers\n")	
			self.err_reg()
		
		elif(self.command =="i3ctransfer -d/dev/i3c-1-20400000005 -w 0x35,0xC0"):
			print("P0: Channel L: Harvesting Channel Error Registers\n")	
			self.err_reg()
		
		elif(self.command =="i3ctransfer -d/dev/i3c-2-20400000000 -w 0x35,0xC0"):
			print("P1: Channel A: Harvesting Channel Error Registers\n")	
			self.err_reg()
			
		elif(self.command =="i3ctransfer -d/dev/i3c-2-20400000001 -w 0x35,0xC0"):
			print("P1: Channel B: Harvesting Channel Error Registers\n")	
			self.err_reg()
			
		elif(self.command =="i3ctransfer -d/dev/i3c-2-20400000002 -w 0x35,0xC0"):
			print("P1: Channel C: Harvesting Channel Error Registers\n")	
			self.err_reg()
			
		elif(self.command =="i3ctransfer -d/dev/i3c-2-20400000003 -w 0x35,0xC0"):
			print("P1: Channel D: Harvesting Channel Error Registers\n")	
			self.err_reg()
			
		elif(self.command =="i3ctransfer -d/dev/i3c-2-20400000004 -w 0x35,0xC0"):
			print("P1: Channel E: Harvesting Channel Error Registers\n")	
			self.err_reg()
			
		elif(self.command =="i3ctransfer -d/dev/i3c-2-20400000005 -w 0x35,0xC0"):
			print("P1: Channel F: Harvesting Channel Error Registers\n")	
			self.err_reg()
			
		elif(self.command =="i3ctransfer -d/dev/i3c-3-20400000000 -w 0x35,0xC0"):
			print("P1: Channel G: Harvesting Channel Error Registers\n")	
			self.err_reg()
			
		elif(self.command =="i3ctransfer -d/dev/i3c-3-20400000001 -w 0x35,0xC0"):
			print("P1: Channel H: Harvesting Channel Error Registers\n")	
			self.err_reg()
		
		elif(self.command =="i3ctransfer -d/dev/i3c-3-20400000002 -w 0x35,0xC0"):
			print("P1: Channel I: Harvesting Channel Error Registers\n")	
			self.err_reg()
		
		elif(self.command =="i3ctransfer -d/dev/i3c-3-20400000003 -w 0x35,0xC0"):
			print("P1: Channel J: Harvesting Channel Error Registers\n")	
			self.err_reg()
		
		elif(self.command =="i3ctransfer -d/dev/i3c-3-20400000004 -w 0x35,0xC0"):
			print("P1: Channel K: Harvesting Channel Error Registers\n")	
			self.err_reg()
		
		elif(self.command =="i3ctransfer -d/dev/i3c-3-20400000005 -w 0x35,0xC0"):
			print("P1: Channel L: Harvesting Channel Error Registers\n")	
			self.err_reg()
		
		print("\nAC Cycle required for system recovery if DIMM is detected and is a fatal error...")
		
	
	##
	# @brief function calls the error_registers method to print the error registres along with connecting to BMC to SSH
	# @return none
	##
	def run_swd_under_voltage(self):
		self.command = self.command + "0xC8"
		print("\nFatal Error Injected into SWD...")
		print("\nUnder Voltage Command: " + self.command + "\n")
		
		
		if(self.command =="i3ctransfer -d/dev/i3c-0-20400000000 -w 0x35,0xC8"):					
			print("P0: Channel A: Harvesting Channel Error Registers\n")	
			self.err_reg()
		
		elif(self.command =="i3ctransfer -d/dev/i3c-0-20400000001 -w 0x35,0xC8"):
			print("P0: Channel B: Harvesting Channel Error Registers\n")	
			self.err_reg()
		
		elif(self.command =="i3ctransfer -d/dev/i3c-0-20400000002 -w 0x35,0xC8"):
			print("P0: Channel C: Harvesting Channel Error Registers\n")	
			self.err_reg()
		
		elif(self.command =="i3ctransfer -d/dev/i3c-0-20400000003 -w 0x35,0xC8"):
			print("P0: Channel D: Harvesting Channel Error Registers\n")	
			self.err_reg()
		
		elif(self.command =="i3ctransfer -d/dev/i3c-0-20400000004 -w 0x35,0xC8"):
			print("P0: Channel E: Harvesting Channel Error Registers\n")	
			self.err_reg()
		
		elif(self.command =="i3ctransfer -d/dev/i3c-0-20400000005 -w 0x35,0xC8"):
			print("P0: Channel F: Harvesting Channel Error Registers\n")
			self.err_reg()
		
		elif(self.command =="i3ctransfer -d/dev/i3c-1-20400000000 -w 0x35,0xC8"):
			print("P0: Channel G: Harvesting Channel Error Registers\n")	
			self.err_reg()
		
		elif(self.command =="i3ctransfer -d/dev/i3c-1-20400000001 -w 0x35,0xC8"):
			print("P0: Channel H: Harvesting Channel Error Registers\n")	
			self.err_reg()

		
		elif(self.command =="i3ctransfer -d/dev/i3c-1-20400000002 -w 0x35,0xC8"):
			print("P0: Channel I: Harvesting Channel Error Registers\n")	
			self.err_reg()
		
		
		elif(self.command =="i3ctransfer -d/dev/i3c-1-20400000003 -w 0x35,0xC8"):
			print("P0: Channel J: Harvesting Channel Error Registers\n")	
			self.err_reg()
		
		elif(self.command =="i3ctransfer -d/dev/i3c-1-20400000004 -w 0x35,0xC8"):
			print("P0: Channel K: Harvesting Channel Error Registers\n")	
			self.err_reg()
		
		elif(self.command =="i3ctransfer -d/dev/i3c-1-20400000005 -w 0x35,0xC8"):
			print("P0: Channel L: Harvesting Channel Error Registers\n")	
			self.err_reg()
		
		elif(self.command =="i3ctransfer -d/dev/i3c-2-20400000000 -w 0x35,0xC8"):
			print("P1: Channel A: Harvesting Channel Error Registers\n")	
			self.err_reg()
			
		elif(self.command =="i3ctransfer -d/dev/i3c-2-20400000001 -w 0x35,0xC8"):
			print("P1: Channel B: Harvesting Channel Error Registers\n")	
			self.err_reg()
			
		elif(self.command =="i3ctransfer -d/dev/i3c-2-20400000002 -w 0x35,0xC8"):
			print("P1: Channel C: Harvesting Channel Error Registers\n")	
			self.err_reg()
			
		elif(self.command =="i3ctransfer -d/dev/i3c-2-20400000003 -w 0x35,0xC8"):
			print("P1: Channel D: Harvesting Channel Error Registers\n")	
			self.err_reg()
			
		elif(self.command =="i3ctransfer -d/dev/i3c-2-20400000004 -w 0x35,0xC8"):
			print("P1: Channel E: Harvesting Channel Error Registers\n")	
			self.err_reg()
			
		elif(self.command =="i3ctransfer -d/dev/i3c-2-20400000005 -w 0x35,0xC8"):
			print("P1: Channel F: Harvesting Channel Error Registers\n")	
			self.err_reg()
			
		elif(self.command =="i3ctransfer -d/dev/i3c-3-20400000000 -w 0x35,0xC8"):
			print("P1: Channel G: Harvesting Channel Error Registers\n")	
			self.err_reg()
			
		elif(self.command =="i3ctransfer -d/dev/i3c-3-20400000001 -w 0x35,0xC8"):
			print("P1: Channel H: Harvesting Channel Error Registers\n")	
			self.err_reg()
		
		elif(self.command =="i3ctransfer -d/dev/i3c-3-20400000002 -w 0x35,0xC8"):
			print("P1: Channel I: Harvesting Channel Error Registers\n")	
			self.err_reg()
		
		elif(self.command =="i3ctransfer -d/dev/i3c-3-20400000003 -w 0x35,0xC8"):
			print("P1: Channel J: Harvesting Channel Error Registers\n")	
			self.err_reg()
		
		elif(self.command =="i3ctransfer -d/dev/i3c-3-20400000004 -w 0x35,0xC8"):
			print("P1: Channel K: Harvesting Channel Error Registers\n")	
			self.err_reg()
		
		elif(self.command =="i3ctransfer -d/dev/i3c-3-20400000005 -w 0x35,0xC8"):
			print("P1: Channel L: Harvesting Channel Error Registers\n")	
			self.err_reg()
		
		print("\nAC Cycle required for system recovery if DIMM is detected and is a fatal error...")
	
	##
	# @brief function calls the error_registers method to print the error registres along with connecting to BMC to SSH
	# @return none
	##
	def run_VINBulk_over_voltage(self):
		self.command = self.command + "0xD0"
		
		print("\nOver Voltage Command: " + self.command)
		
		print("\nFatal Error Injected into VINBULK...\n")
		
		if(self.command =="i3ctransfer -d/dev/i3c-0-20400000000 -w 0x35,0xD0"):					
			print("P0: Channel A: Harvesting Channel Error Registers\n")	
			self.err_reg()
		
		elif(self.command =="i3ctransfer -d/dev/i3c-0-20400000001 -w 0x35,0xD0"):
			print("P0: Channel B: Harvesting Channel Error Registers\n")	
			self.err_reg()
		
		elif(self.command =="i3ctransfer -d/dev/i3c-0-20400000002 -w 0x35,0xD0"):
			print("P0: Channel C: Harvesting Channel Error Registers\n")	
			self.err_reg()
		
		elif(self.command =="i3ctransfer -d/dev/i3c-0-20400000003 -w 0x35,0xD0"):
			print("P0: Channel D: Harvesting Channel Error Registers\n")	
			self.err_reg()
		
		elif(self.command =="i3ctransfer -d/dev/i3c-0-20400000004 -w 0x35,0xD0"):
			print("P0: Channel E: Harvesting Channel Error Registers\n")	
			self.err_reg()
		
		elif(self.command =="i3ctransfer -d/dev/i3c-0-20400000005 -w 0x35,0xD0"):
			print("P0: Channel F: Harvesting Channel Error Registers\n")
			self.err_reg()
		
		elif(self.command =="i3ctransfer -d/dev/i3c-1-20400000000 -w 0x35,0xD0"):
			print("P0: Channel G: Harvesting Channel Error Registers\n")	
			self.err_reg()
		
		elif(self.command =="i3ctransfer -d/dev/i3c-1-20400000001 -w 0x35,0xD0"):
			print("P0: Channel H: Harvesting Channel Error Registers\n")	
			self.err_reg()

		
		elif(self.command =="i3ctransfer -d/dev/i3c-1-20400000002 -w 0x35,0xD0"):
			print("P0: Channel I: Harvesting Channel Error Registers\n")	
			self.err_reg()
		
		
		elif(self.command =="i3ctransfer -d/dev/i3c-1-20400000003 -w 0x35,0xD0"):
			print("P0: Channel J: Harvesting Channel Error Registers\n")	
			self.err_reg()
		
		elif(self.command =="i3ctransfer -d/dev/i3c-1-20400000004 -w 0x35,0xD0"):
			print("P0: Channel K: Harvesting Channel Error Registers\n")	
			self.err_reg()
		
		elif(self.command =="i3ctransfer -d/dev/i3c-1-20400000005 -w 0x35,0xD0"):
			print("P0: Channel L: Harvesting Channel Error Registers\n")	
			self.err_reg()
		
		elif(self.command =="i3ctransfer -d/dev/i3c-2-20400000000 -w 0x35,0xD0"):
			print("P1: Channel A: Harvesting Channel Error Registers\n")	
			self.err_reg()
			
		elif(self.command =="i3ctransfer -d/dev/i3c-2-20400000001 -w 0x35,0xD0"):
			print("P1: Channel B: Harvesting Channel Error Registers\n")	
			self.err_reg()
			
		elif(self.command =="i3ctransfer -d/dev/i3c-2-20400000002 -w 0x35,0xD0"):
			print("P1: Channel C: Harvesting Channel Error Registers\n")	
			self.err_reg()
			
		elif(self.command =="i3ctransfer -d/dev/i3c-2-20400000003 -w 0x35,0xD0"):
			print("P1: Channel D: Harvesting Channel Error Registers\n")	
			self.err_reg()
			
		elif(self.command =="i3ctransfer -d/dev/i3c-2-20400000004 -w 0x35,0xD0"):
			print("P1: Channel E: Harvesting Channel Error Registers\n")	
			self.err_reg()
			
		elif(self.command =="i3ctransfer -d/dev/i3c-2-20400000005 -w 0x35,0xD0"):
			print("P1: Channel F: Harvesting Channel Error Registers\n")	
			self.err_reg()
			
		elif(self.command =="i3ctransfer -d/dev/i3c-3-20400000000 -w 0x35,0xD0"):
			print("P1: Channel G: Harvesting Channel Error Registers\n")	
			self.err_reg()
			
		elif(self.command =="i3ctransfer -d/dev/i3c-3-20400000001 -w 0x35,0xD0"):
			print("P1: Channel H: Harvesting Channel Error Registers\n")	
			self.err_reg()
		
		elif(self.command =="i3ctransfer -d/dev/i3c-3-20400000002 -w 0x35,0xD0"):
			print("P1: Channel I: Harvesting Channel Error Registers\n")	
			self.err_reg()
		
		elif(self.command =="i3ctransfer -d/dev/i3c-3-20400000003 -w 0x35,0xD0"):
			print("P1: Channel J: Harvesting Channel Error Registers\n")	
			self.err_reg()
		
		elif(self.command =="i3ctransfer -d/dev/i3c-3-20400000004 -w 0x35,0xD0"):
			print("P1: Channel K: Harvesting Channel Error Registers\n")	
			self.err_reg()
			
		elif(self.command =="i3ctransfer -d/dev/i3c-3-20400000005 -w 0x35,0xD0"):
			print("P1: Channel L: Harvesting Channel Error Registers\n")	
			self.err_reg()
		
		print("\nAC Cycle required for system recovery if DIMM is detected and is a fatal error...")
			
	
	##
	# @brief function calls the error_registers method to print the error registres along with connecting to BMC to SSH
	# @return none
	##
	def run_VINBulk_under_voltage(self):
		self.command = self.command + "0xD8"
		
		print("\nUnder Voltage Command: " + self.command)
		
		print("\nFatal Error Injected into VINBULK...\n")
		
		if(self.command =="i3ctransfer -d/dev/i3c-0-20400000000 -w 0x35,0xD8"):					
			print("P0: Channel A: Harvesting Channel Error Registers\n")	
			self.err_reg()
		
		elif(self.command =="i3ctransfer -d/dev/i3c-0-20400000001 -w 0x35,0xD8"):
			print("P0: Channel B: Harvesting Channel Error Registers\n")	
			self.err_reg()
		
		elif(self.command =="i3ctransfer -d/dev/i3c-0-20400000002 -w 0x35,0xD8"):
			print("P0: Channel C: Harvesting Channel Error Registers\n")	
			self.err_reg()
		
		elif(self.command =="i3ctransfer -d/dev/i3c-0-20400000003 -w 0x35,0xD8"):
			print("P0: Channel D: Harvesting Channel Error Registers\n")	
			self.err_reg()
		
		elif(self.command =="i3ctransfer -d/dev/i3c-0-20400000004 -w 0x35,0xD8"):
			print("P0: Channel E: Harvesting Channel Error Registers\n")	
			self.err_reg()
		
		elif(self.command =="i3ctransfer -d/dev/i3c-0-20400000005 -w 0x35,0xD8"):
			print("P0: Channel F: Harvesting Channel Error Registers\n")
			self.err_reg()
		
		elif(self.command =="i3ctransfer -d/dev/i3c-1-20400000000 -w 0x35,0xD8"):
			print("P0: Channel G: Harvesting Channel Error Registers\n")	
			self.err_reg()
		
		elif(self.command =="i3ctransfer -d/dev/i3c-1-20400000001 -w 0x35,0xD8"):
			print("P0: Channel H: Harvesting Channel Error Registers\n")	
			self.err_reg()
		
		elif(self.command =="i3ctransfer -d/dev/i3c-1-20400000002 -w 0x35,0xD8"):
			print("P0: Channel I: Harvesting Channel Error Registers\n")	
			self.err_reg()
		
		elif(self.command =="i3ctransfer -d/dev/i3c-0-20400000000 -w 0x35,0xD8"):
			print("P0: Channel J: Harvesting Channel Error Registers\n")	
			self.err_reg()
		
		elif(self.command =="i3ctransfer -d/dev/i3c-1-20400000004 -w 0x35,0xD8"):
			print("P0: Channel K: Harvesting Channel Error Registers\n")	
			self.err_reg()
		
		elif(self.command =="i3ctransfer -d/dev/i3c-1-20400000005 -w 0x35,0xD8"):
			print("P0: Channel L: Harvesting Channel Error Registers\n")	
			self.err_reg()
		
		elif(self.command =="i3ctransfer -d/dev/i3c-2-20400000000 -w 0x35,0xD8"):
			print("P1: Channel A: Harvesting Channel Error Registers\n")	
			self.err_reg()
			
		elif(self.command =="i3ctransfer -d/dev/i3c-2-20400000001 -w 0x35,0xD8"):
			print("P1: Channel B: Harvesting Channel Error Registers\n")	
			self.err_reg()
			
		elif(self.command =="i3ctransfer -d/dev/i3c-2-20400000002 -w 0x35,0xD8"):
			print("P1: Channel C: Harvesting Channel Error Registers\n")	
			self.err_reg()
			
		elif(self.command =="i3ctransfer -d/dev/i3c-2-20400000003 -w 0x35,0xD8"):
			print("P1: Channel D: Harvesting Channel Error Registers\n")	
			self.err_reg()
			
		elif(self.command =="i3ctransfer -d/dev/i3c-2-20400000004 -w 0x35,0xD8"):
			print("P1: Channel E: Harvesting Channel Error Registers\n")	
			self.err_reg()
			
		elif(self.command =="i3ctransfer -d/dev/i3c-2-20400000005 -w 0x35,0xD8"):
			print("P1: Channel F: Harvesting Channel Error Registers\n")	
			self.err_reg()
			
		elif(self.command =="i3ctransfer -d/dev/i3c-3-20400000000 -w 0x35,0xD8"):
			print("P1: Channel G: Harvesting Channel Error Registers\n")	
			self.err_reg()
			
		elif(self.command =="i3ctransfer -d/dev/i3c-3-20400000001 -w 0x35,0xD8"):
			print("P1: Channel H: Harvesting Channel Error Registers\n")	
			self.err_reg()
		
		elif(self.command =="i3ctransfer -d/dev/i3c-3-20400000002 -w 0x35,0xD8"):
			print("P1: Channel I: Harvesting Channel Error Registers\n")	
			self.err_reg()
		
		elif(self.command =="i3ctransfer -d/dev/i3c-3-20400000003 -w 0x35,0xD8"):
			print("P1: Channel J: Harvesting Channel Error Registers\n")	
			self.err_reg()
		
		elif(self.command =="i3ctransfer -d/dev/i3c-3-20400000004 -w 0x35,0xD8"):
			print("P1: Channel K: Harvesting Channel Error Registers\n")	
			self.err_reg()
			
		elif(self.command =="i3ctransfer -d/dev/i3c-3-20400000005 -w 0x35,0xD8"):
			print("P1: Channel L: Harvesting Channel Error Registers\n")	
			self.err_reg()
		
		print("\nAC Cycle required for system recovery if DIMM is detected and is a fatal error...")
	
	##
	# @brief function calls the error_registers method to print the error registres along with connecting to BMC to SSH
	# @return none
	##
	def run_VINMgmt_over_voltage(self):
		self.command = self.command + "0xE0"
		print("\nNon-Fatal Error has been injected into VINMgmt...\n") 
		print("Over Voltage Command: " + self.command + "\n")
		
		if(self.command =="i3ctransfer -d/dev/i3c-0-20400000000 -w 0x35,0xE0"):					
			print("P0: Channel A: Harvesting Channel Error Registers\n")	
			self.err_reg()
		
		elif(self.command =="i3ctransfer -d/dev/i3c-0-20400000001 -w 0x35,0xE0"):
			print("P0: Channel B: Harvesting Channel Error Registers\n")	
			self.err_reg()
		
		elif(self.command =="i3ctransfer -d/dev/i3c-0-20400000002 -w 0x35,0xE0"):
			print("P0: Channel C: Harvesting Channel Error Registers\n")	
			self.err_reg()
		
		elif(self.command =="i3ctransfer -d/dev/i3c-0-20400000003 -w 0x35,0xE0"):
			print("P0: Channel D: Harvesting Channel Error Registers\n")	
			self.err_reg()
		
		elif(self.command =="i3ctransfer -d/dev/i3c-0-20400000004 -w 0x35,0xE0"):
			print("P0: Channel E: Harvesting Channel Error Registers\n")	
			self.err_reg()
		
		elif(self.command =="i3ctransfer -d/dev/i3c-0-20400000005 -w 0x35,0xE0"):
			print("P0: Channel F: Harvesting Channel Error Registers\n")
			self.err_reg()
		
		elif(self.command =="i3ctransfer -d/dev/i3c-1-20400000000 -w 0x35,0xE0"):
			print("P0: Channel G: Harvesting Channel Error Registers\n")	
			self.err_reg()
		
		elif(self.command =="i3ctransfer -d/dev/i3c-1-20400000001 -w 0x35,0xE0"):
			print("P0: Channel H: Harvesting Channel Error Registers\n")	
			self.err_reg()
		
		elif(self.command =="i3ctransfer -d/dev/i3c-1-20400000002 -w 0x35,0xE0"):
			print("P0: Channel I: Harvesting Channel Error Registers\n")	
			self.err_reg()
		
		elif(self.command =="i3ctransfer -d/dev/i3c-1-20400000003 -w 0x35,0xE0"):
			print("P0: Channel J: Harvesting Channel Error Registers\n")	
			self.err_reg()
		
		elif(self.command =="i3ctransfer -d/dev/i3c-1-20400000004 -w 0x35,0xE0"):
			print("P0: Channel K: Harvesting Channel Error Registers\n")	
			self.err_reg()
		
		elif(self.command =="i3ctransfer -d/dev/i3c-1-20400000005 -w 0x35,0xE0"):
			print("P0: Channel L: Harvesting Channel Error Registers\n")	
			self.err_reg()
		
		elif(self.command =="i3ctransfer -d/dev/i3c-2-20400000000 -w 0x35,0xE0"):
			print("P1: Channel A: Harvesting Channel Error Registers\n")	
			self.err_reg()
			
		elif(self.command =="i3ctransfer -d/dev/i3c-2-20400000001 -w 0x35,0xE0"):
			print("P1: Channel B: Harvesting Channel Error Registers\n")	
			self.err_reg()
			
		elif(self.command =="i3ctransfer -d/dev/i3c-2-20400000002 -w 0x35,0xE0"):
			print("P1: Channel C: Harvesting Channel Error Registers\n")	
			self.err_reg()
			
		elif(self.command =="i3ctransfer -d/dev/i3c-2-20400000003 -w 0x35,0xE0"):
			print("P1: Channel D: Harvesting Channel Error Registers\n")	
			self.err_reg()
			
		elif(self.command =="i3ctransfer -d/dev/i3c-2-20400000004 -w 0x35,0xE0"):
			print("P1 Channel E: Harvesting Channel Error Registers\n")	
			self.err_reg()
			
		elif(self.command =="i3ctransfer -d/dev/i3c-2-20400000005 -w 0x35,0xE0"):
			print("P1: Channel F: Harvesting Channel Error Registers\n")	
			self.err_reg()
			
		elif(self.command =="i3ctransfer -d/dev/i3c-3-20400000000 -w 0x35,0xE0"):
			print("P1: Channel G: Harvesting Channel Error Registers\n")	
			self.err_reg()
			
		elif(self.command =="i3ctransfer -d/dev/i3c-3-20400000001 -w 0x35,0xE0"):
			print("P1: Channel H: Harvesting Channel Error Registers\n")	
			self.err_reg()
		
		elif(self.command =="i3ctransfer -d/dev/i3c-3-20400000002 -w 0x35,0xE0"):
			print("P1: Channel I: Harvesting Channel Error Registers\n")	
			self.err_reg()
		
		elif(self.command =="i3ctransfer -d/dev/i3c-3-20400000003 -w 0x35,0xE0"):
			print("P1: Channel J: Harvesting Channel Error Registers\n")	
			self.err_reg()
		
		elif(self.command =="i3ctransfer -d/dev/i3c-3-20400000004 -w 0x35,0xE0"):
			print("P1: Channel K: Harvesting Channel Error Registers\n")	
			self.err_reg()
		
		elif(self.command =="i3ctransfer -d/dev/i3c-3-20400000005 -w 0x35,0xE0"):
			print("P1: Channel L: Harvesting Channel Error Registers\n")	
			self.err_reg()
		
		print("\nNo AC Cycle required for system recovery...")
	
	
	
	##
	# @brief function calls the error_registers method to print the error registres along with connecting to BMC to SSH
	# @return none
	##
	def run_VINMgmt_under_voltage(self):
		self.command = self.command + "0xE8"
		print("\nNon-Fatal Error has been injected into VINMgmt...\n") 
		print("Under Voltage Command: " + self.command + "\n")
		
		if(self.command =="i3ctransfer -d/dev/i3c-0-20400000000 -w 0x35,0xE8"):					
			print("P0: Channel A: Harvesting Channel Error Registers\n")	
			self.err_reg()
		
		elif(self.command =="i3ctransfer -d/dev/i3c-0-20400000001 -w 0x35,0xE8"):
			print("P0: Channel B: Harvesting Channel Error Registers\n")	
			self.err_reg()
		
		elif(self.command =="i3ctransfer -d/dev/i3c-0-20400000002 -w 0x35,0xE8"):
			print("P0: Channel C: Harvesting Channel Error Registers\n")	
			self.err_reg()
		
		elif(self.command =="i3ctransfer -d/dev/i3c-0-20400000003 -w 0x35,0xE8"):
			print("P0: Channel D: Harvesting Channel Error Registers\n")	
			self.err_reg()
		
		elif(self.command =="i3ctransfer -d/dev/i3c-0-20400000004 -w 0x35,0xE8"):
			print("P0: Channel E: Harvesting Channel Error Registers\n")	
			self.err_reg()
		
		elif(self.command =="i3ctransfer -d/dev/i3c-0-20400000005 -w 0x35,0xE8"):
			print("P0: Channel F: Harvesting Channel Error Registers\n")
			self.err_reg()
		
		elif(self.command =="i3ctransfer -d/dev/i3c-1-20400000000 -w 0x35,0xE8"):
			print("P0: Channel G: Harvesting Channel Error Registers\n")	
			self.err_reg()
		
		elif(self.command =="i3ctransfer -d/dev/i3c-1-20400000001 -w 0x35,0xE8"):
			print("P0: Channel H: Harvesting Channel Error Registers\n")	
			self.err_reg()

		elif(self.command =="i3ctransfer -d/dev/i3c-1-20400000002 -w 0x35,0xE8"):
			print("P0: Channel I: Harvesting Channel Error Registers\n")	
			self.err_reg()
		
		
		elif(self.command =="i3ctransfer -d/dev/i3c-1-20400000003 -w 0x35,0xE8"):
			print("P0: Channel J: Harvesting Channel Error Registers\n")	
			self.err_reg()
		
		elif(self.command =="i3ctransfer -d/dev/i3c-1-20400000004 -w 0x35,0xE8"):
			print("P0: Channel K: Harvesting Channel Error Registers\n")	
			self.err_reg()
		
		elif(self.command =="i3ctransfer -d/dev/i3c-1-20400000005 -w 0x35,0xE8"):
			print("P0: Channel L: Harvesting Channel Error Registers\n")	
			self.err_reg()
		
		elif(self.command =="i3ctransfer -d/dev/i3c-2-20400000000 -w 0x35,0xE8"):
			print("P1: Channel A: Harvesting Channel Error Registers\n")	
			self.err_reg()
			
		elif(self.command =="i3ctransfer -d/dev/i3c-2-20400000001 -w 0x35,0xE8"):
			print("P1: Channel B: Harvesting Channel Error Registers\n")	
			self.err_reg()
			
		elif(self.command =="i3ctransfer -d/dev/i3c-2-20400000002 -w 0x35,0xE8"):
			print("P1: Channel C: Harvesting Channel Error Registers\n")	
			self.err_reg()
			
		elif(self.command =="i3ctransfer -d/dev/i3c-2-20400000003 -w 0x35,0xE8"):
			print("P1: Channel D: Harvesting Channel Error Registers\n")	
			self.err_reg()
			
		elif(self.command =="i3ctransfer -d/dev/i3c-2-20400000004 -w 0x35,0xE8"):
			print("P1: Channel E: Harvesting Channel Error Registers\n")	
			self.err_reg()
			
		elif(self.command =="i3ctransfer -d/dev/i3c-2-20400000005 -w 0x35,0xE8"):
			print("P1: Channel F: Harvesting Channel Error Registers\n")	
			self.err_reg()
			
		elif(self.command =="i3ctransfer -d/dev/i3c-3-20400000000 -w 0x35,0xE8"):
			print("P1: Channel G: Harvesting Channel Error Registers\n")	
			self.err_reg()
			
		elif(self.command =="i3ctransfer -d/dev/i3c-3-20400000001 -w 0x35,0xE8"):
			print("P1: Channel H: Harvesting Channel Error Registers\n")	
			self.err_reg()
		
		elif(self.command =="i3ctransfer -d/dev/i3c-3-20400000002 -w 0x35,0xE8"):
			print("P1: Channel I: Harvesting Channel Error Registers\n")	
			self.err_reg()
		
		elif(self.command =="i3ctransfer -d/dev/i3c-3-20400000003 -w 0x35,0xE8"):
			print("P1: Channel J: Harvesting Channel Error Registers\n")	
			self.err_reg()
		
		elif(self.command =="i3ctransfer -d/dev/i3c-3-20400000004 -w 0x35,0xE8"):
			print("P1: Channel K: Harvesting Channel Error Registers\n")	
			self.err_reg()
		
		elif(self.command =="i3ctransfer -d/dev/i3c-3-20400000005 -w 0x35,0xE8"):
			print("P1: Channel L: Harvesting Channel Error Registers\n")	
			self.err_reg()
		
		print("\nNo AC Cycle required for system recovery...")
	 
	
	##
	# @brief function calls the error_registers method to print the error registres along with connecting to BMC to SSH
	# @return none
	##
	def undefined(self):
		self.command = self.command + "0x80"
		print("\nNon-Fatal Error...\n") 
		print("Undefined Command: " + self.command + "\n")
		
		if(self.command =="i3ctransfer -d/dev/i3c-0-20400000000 -w 0x35,0x80"):					
			print("P0: Channel A: Harvesting Channel Error Registers\n")	
			self.err_reg()
		
		elif(self.command =="i3ctransfer -d/dev/i3c-0-20400000001 -w 0x35,0x80"):
			print("P0: Channel B: Harvesting Channel Error Registers\n")	
			self.err_reg()
		
		elif(self.command =="i3ctransfer -d/dev/i3c-0-20400000002 -w 0x35,0x80"):
			print("P0: Channel C: Harvesting Channel Error Registers\n")	
			self.err_reg()
		
		elif(self.command =="i3ctransfer -d/dev/i3c-0-20400000003 -w 0x35,0x80"):
			print("P0: Channel D: Harvesting Channel Error Registers\n")	
			self.err_reg()
		
		elif(self.command =="i3ctransfer -d/dev/i3c-0-20400000004 -w 0x35,0x80"):
			print("P0: Channel E: Harvesting Channel Error Registers\n")	
			self.err_reg()
		
		elif(self.command =="i3ctransfer -d/dev/i3c-0-20400000005 -w 0x35,0x80"):
			print("P0: Channel F: Harvesting Channel Error Registers\n")
			self.err_reg()
		
		elif(self.command =="i3ctransfer -d/dev/i3c-1-20400000000 -w 0x35,0x80"):
			print("P0: Channel G: Harvesting Channel Error Registers\n")	
			self.err_reg()
		
		elif(self.command =="i3ctransfer -d/dev/i3c-1-20400000001 -w 0x35,0x80"):
			print("P0: Channel H: Harvesting Channel Error Registers\n")	
			self.err_reg()
		
		elif(self.command =="i3ctransfer -d/dev/i3c-1-20400000002 -w 0x35,0x80"):
			print("P0: Channel I: Harvesting Channel Error Registers\n")	
			self.err_reg()
		
		
		elif(self.command =="i3ctransfer -d/dev/i3c-1-20400000003 -w 0x35,0x80"):
			print("P0: Channel J: Harvesting Channel Error Registers\n")	
			self.err_reg()
		
		elif(self.command =="i3ctransfer -d/dev/i3c-1-20400000004 -w 0x35,0x80"):
			print("P0: Channel K: Harvesting Channel Error Registers\n")	
			self.err_reg()
		
		elif(self.command =="i3ctransfer -d/dev/i3c-1-20400000005 -w 0x35,0x80"):
			print("P0: Channel L: Harvesting Channel Error Registers\n")	
			self.err_reg()
		
		elif(self.command =="i3ctransfer -d/dev/i3c-2-20400000000 -w 0x35,0x80"):
			print("P1: Channel A: Harvesting Channel Error Registers\n")	
			self.err_reg()
			
		elif(self.command =="i3ctransfer -d/dev/i3c-2-20400000001 -w 0x35,0x80"):
			print("P1: Channel B: Harvesting Channel Error Registers\n")	
			self.err_reg()
			
		elif(self.command =="i3ctransfer -d/dev/i3c-2-20400000002 -w 0x35,0x80"):
			print("P1: Channel C: Harvesting Channel Error Registers\n")	
			self.err_reg()
			
		elif(self.command =="i3ctransfer -d/dev/i3c-2-20400000003 -w 0x35,0x80"):
			print("P1: Channel D: Harvesting Channel Error Registers\n")	
			self.err_reg()
			
		elif(self.command =="i3ctransfer -d/dev/i3c-2-20400000004 -w 0x35,0x80"):
			print("P1: Channel E: Harvesting Channel Error Registers\n")	
			self.err_reg()
			
		elif(self.command =="i3ctransfer -d/dev/i3c-2-20400000005 -w 0x35,0x80"):
			print("P1: Channel F: Harvesting Channel Error Registers\n")	
			self.err_reg()
			
		elif(self.command =="i3ctransfer -d/dev/i3c-3-20400000000 -w 0x35,0x80"):
			print("P1: Channel G: Harvesting Channel Error Registers\n")	
			self.err_reg()
			
		elif(self.command =="i3ctransfer -d/dev/i3c-3-20400000001 -w 0x35,0x80"):
			print("P1: Channel H: Harvesting Channel Error Registers\n")	
			self.err_reg()
		
		elif(self.command =="i3ctransfer -d/dev/i3c-3-20400000002 -w 0x35,0x80"):
			print("P1: Channel I: Harvesting Channel Error Registers\n")	
			self.err_reg()
		
		elif(self.command =="i3ctransfer -d/dev/i3c-3-20400000003 -w 0x35,0x80"):
			print("P1: Channel J: Harvesting Channel Error Registers\n")	
			self.err_reg()
		
		elif(self.command =="i3ctransfer -d/dev/i3c-3-20400000004 -w 0x35,0x80"):
			print("P1: Channel K: Harvesting Channel Error Registers\n")	
			self.err_reg()
		
		elif(self.command =="i3ctransfer -d/dev/i3c-3-20400000005 -w 0x35,0x82"):
			print("P1: Channel L: Harvesting Channel Error Registers\n")	
			self.err_reg()
		
		print("\nNo AC Cycle required for system recovery...")
	
	
	##
	# @brief function calls the error_registers method to print the error registres along with connecting to BMC to SSH
	# @return none
	##
	def VINMgmt_to_VINBulk_switchover(self):
		self.command = self.command + "0x81"
		print("\nNon-Fatal Error has been injected into VINMgmt to VINBulk Switchover...\n") 
		print("VINMgmt to VINBulk Switchover Command: " + self.command + "\n")
		
		if(self.command =="i3ctransfer -d/dev/i3c-0-20400000000 -w 0x35,0x81"):					
			print("P0: Channel A: Harvesting Channel Error Registers\n")	
			self.err_reg()
		
		elif(self.command =="i3ctransfer -d/dev/i3c-0-20400000001 -w 0x35,0x81"):
			print("P0: Channel B: Harvesting Channel Error Registers\n")	
			self.err_reg()
		
		elif(self.command =="i3ctransfer -d/dev/i3c-0-20400000002 -w 0x35,0x81"):
			print("P0: Channel C: Harvesting Channel Error Registers\n")	
			self.err_reg()
		
		elif(self.command =="i3ctransfer -d/dev/i3c-0-20400000003 -w 0x35,0x81"):
			print("P0: Channel D: Harvesting Channel Error Registers\n")	
			self.err_reg()
		
		elif(self.command =="i3ctransfer -d/dev/i3c-0-20400000004 -w 0x35,0x81"):
			print("P0: Channel E: Harvesting Channel Error Registers\n")	
			self.err_reg()
		
		elif(self.command =="i3ctransfer -d/dev/i3c-0-20400000005 -w 0x35,0x81"):
			print("P0: Channel F: Harvesting Channel Error Registers\n")
			self.err_reg()
		
		elif(self.command =="i3ctransfer -d/dev/i3c-1-20400000000 -w 0x35,0x81"):
			print("P0: Channel G: Harvesting Channel Error Registers\n")	
			self.err_reg()
		
		elif(self.command =="i3ctransfer -d/dev/i3c-1-20400000001 -w 0x35,0x81"):
			print("P0: Channel H: Harvesting Channel Error Registers\n")	
			self.err_reg()
		
		elif(self.command =="i3ctransfer -d/dev/i3c-1-20400000002 -w 0x35,0x81"):
			print("P0: Channel I: Harvesting Channel Error Registers\n")	
			self.err_reg()
		
		elif(self.command =="i3ctransfer -d/dev/i3c-1-20400000003 -w 0x35,0x81"):
			print("P0: Channel J: Harvesting Channel Error Registers\n")	
			self.err_reg()
		
		elif(self.command =="i3ctransfer -d/dev/i3c-1-20400000004 -w 0x35,0x81"):
			print("P0: Channel K: Harvesting Channel Error Registers\n")	
			self.err_reg()
		
		elif(self.command =="i3ctransfer -d/dev/i3c-1-20400000005 -w 0x35,0x81"):
			print("P0: Channel L: Harvesting Channel Error Registers\n")	
			self.err_reg()
		
		elif(self.command =="i3ctransfer -d/dev/i3c-2-20400000000 -w 0x35,0x81"):
			print("P1: Channel A: Harvesting Channel Error Registers\n")	
			self.err_reg()
			
		elif(self.command =="i3ctransfer -d/dev/i3c-2-20400000001 -w 0x35,0x81"):
			print("P1: Channel B: Harvesting Channel Error Registers\n")	
			self.err_reg()
			
		elif(self.command =="i3ctransfer -d/dev/i3c-2-20400000002 -w 0x35,0x81"):
			print("P1: Channel C: Harvesting Channel Error Registers\n")	
			self.err_reg()
			
		elif(self.command =="i3ctransfer -d/dev/i3c-2-20400000003 -w 0x35,0x81"):
			print("P1: Channel D: Harvesting Channel Error Registers\n")	
			self.err_reg()
			
		elif(self.command =="i3ctransfer -d/dev/i3c-2-20400000004 -w 0x35,0x81"):
			print("P1: Channel E: Harvesting Channel Error Registers\n")	
			self.err_reg()
			
		elif(self.command =="i3ctransfer -d/dev/i3c-2-20400000005 -w 0x35,0x81"):
			print("P1: Channel F: Harvesting Channel Error Registers\n")	
			self.err_reg()
			
		elif(self.command =="i3ctransfer -d/dev/i3c-3-20400000000 -w 0x35,0x81"):
			print("P1: Channel G: Harvesting Channel Error Registers\n")	
			self.err_reg()
			
		elif(self.command =="i3ctransfer -d/dev/i3c-3-20400000001 -w 0x35,0x81"):
			print("P1: Channel H: Harvesting Channel Error Registers\n")	
			self.err_reg()
		
		elif(self.command =="i3ctransfer -d/dev/i3c-3-20400000002 -w 0x35,0x81"):
			print("P1: Channel I: Harvesting Channel Error Registers\n")	
			self.err_reg()
		
		elif(self.command =="i3ctransfer -d/dev/i3c-3-20400000003 -w 0x35,0x81"):
			print("P1: Channel J: Harvesting Channel Error Registers\n")	
			self.err_reg()
		
		elif(self.command =="i3ctransfer -d/dev/i3c-3-20400000004 -w 0x35,0x81"):
			print("P1: Channel K: Harvesting Channel Error Registers\n")	
			self.err_reg()
		
		elif(self.command =="i3ctransfer -d/dev/i3c-3-20400000005 -w 0x35,0x81"):
			print("P1: Channel L: Harvesting Channel Error Registers\n")	
			self.err_reg()
		
		print("\nNo AC Cycle required for system recovery...")
		
	
	##
	# @brief function calls the error_registers method to print the error registres along with connecting to BMC to SSH
	# @return none
	##
	def critical_temp_shutdown(self):
		self.command = self.command + "0x82"
		print("\nFatal Error has been injected into Critical Temperature Shutdown...\n") 
		print("Critical Temperature Shutdown Command: " + self.command + "\n")
		
		if(self.command =="i3ctransfer -d/dev/i3c-0-20400000000 -w 0x35,0x82"):					
			print("P0: Channel A: Harvesting Channel Error Registers\n")	
			self.err_reg()
		
		elif(self.command =="i3ctransfer -d/dev/i3c-0-20400000001 -w 0x35,0x82"):
			print("P0: Channel B: Harvesting Channel Error Registers\n")	
			self.err_reg()
		
		elif(self.command =="i3ctransfer -d/dev/i3c-0-20400000002 -w 0x35,0x82"):
			print("P0: Channel C: Harvesting Channel Error Registers\n")	
			self.err_reg()
		
		elif(self.command =="i3ctransfer -d/dev/i3c-0-20400000003 -w 0x35,0x82"):
			print("P0: Channel D: Harvesting Channel Error Registers\n")	
			self.err_reg()
		
		elif(self.command =="i3ctransfer -d/dev/i3c-0-20400000004 -w 0x35,0x82"):
			print("P0: Channel E: Harvesting Channel Error Registers\n")	
			self.err_reg()
		
		elif(self.command =="i3ctransfer -d/dev/i3c-0-20400000005 -w 0x35,0x82"):
			print("P0: Channel F: Harvesting Channel Error Registers\n")
			self.err_reg()
		
		elif(self.command =="i3ctransfer -d/dev/i3c-1-20400000000 -w 0x35,0x82"):
			print("P0: Channel G: Harvesting Channel Error Registers\n")	
			self.err_reg()
		
		elif(self.command =="i3ctransfer -d/dev/i3c-1-20400000001 -w 0x35,0x82"):
			print("P0: Channel H: Harvesting Channel Error Registers\n")	
			self.err_reg()

		
		elif(self.command =="i3ctransfer -d/dev/i3c-1-20400000002 -w 0x35,0x82"):
			print("P0: Channel I: Harvesting Channel Error Registers\n")	
			self.err_reg()
		
		elif(self.command =="i3ctransfer -d/dev/i3c-1-20400000003 -w 0x35,0x82"):
			print("P0: Channel J: Harvesting Channel Error Registers\n")	
			self.err_reg()
		
		elif(self.command =="i3ctransfer -d/dev/i3c-1-20400000004 -w 0x35,0x82"):
			print("P0: Channel K: Harvesting Channel Error Registers\n")	
			self.err_reg()
		
		elif(self.command =="i3ctransfer -d/dev/i3c-1-20400000005 -w 0x35,0x82"):
			print("P0: Channel L: Harvesting Channel Error Registers\n")	
			self.err_reg()
		
		elif(self.command =="i3ctransfer -d/dev/i3c-2-20400000000 -w 0x35,0x82"):
			print("P1: Channel A: Harvesting Channel Error Registers\n")	
			self.err_reg()
			
		elif(self.command =="i3ctransfer -d/dev/i3c-2-20400000001 -w 0x35,0x82"):
			print("P1: Channel B: Harvesting Channel Error Registers\n")	
			self.err_reg()
			
		elif(self.command =="i3ctransfer -d/dev/i3c-2-20400000002 -w 0x35,0x82"):
			print("P1: Channel C: Harvesting Channel Error Registers\n")	
			self.err_reg()
			
		elif(self.command =="i3ctransfer -d/dev/i3c-2-20400000003 -w 0x35,0x82"):
			print("P1: Channel D: Harvesting Channel Error Registers\n")	
			self.err_reg()
			
		elif(self.command =="i3ctransfer -d/dev/i3c-2-20400000004 -w 0x35,0x82"):
			print("P1: Channel E: Harvesting Channel Error Registers\n")	
			self.err_reg()
			
		elif(self.command =="i3ctransfer -d/dev/i3c-2-20400000005 -w 0x35,0x82"):
			print("P1: Channel F: Harvesting Channel Error Registers\n")	
			self.err_reg()
			
		elif(self.command =="i3ctransfer -d/dev/i3c-3-20400000000 -w 0x35,0x82"):
			print("P1: Channel G: Harvesting Channel Error Registers\n")	
			self.err_reg()
			
		elif(self.command =="i3ctransfer -d/dev/i3c-3-20400000001 -w 0x35,0x82"):
			print("P1: Channel H: Harvesting Channel Error Registers\n")	
			self.err_reg()
		
		elif(self.command =="i3ctransfer -d/dev/i3c-3-20400000002 -w 0x35,0x82"):
			print("P1: Channel I: Harvesting Channel Error Registers\n")	
			self.err_reg()
		
		elif(self.command =="i3ctransfer -d/dev/i3c-3-20400000003 -w 0x35,0x82"):
			print("P1: Channel J: Harvesting Channel Error Registers\n")	
			self.err_reg()
		
		elif(self.command =="i3ctransfer -d/dev/i3c-3-20400000004 -w 0x35,0x82"):
			print("P1: Channel K: Harvesting Channel Error Registers\n")	
			self.err_reg()
		
		elif(self.command =="i3ctransfer -d/dev/i3c-3-20400000005 -w 0x35,0x82"):
			print("P1: Channel L: Harvesting Channel Error Registers\n")	
			self.err_reg()
		
		print("\nAC Cycle required for system recovery...")
		
	
	##
	# @brief function calls the error_registers method to print the error registres along with connecting to BMC to SSH
	# @return none
	##
	def high_temp_warning_threshold(self):
		self.command = self.command + "0x83"
		print("\nNon Fatal Error has been injected into High Temperature Warning Threshold...\n") 
		print("High Temperature Warning Threshold Command: " + self.command + "\n")
		
		if(self.command =="i3ctransfer -d/dev/i3c-0-20400000000 -w 0x35,0x83"):					
			print("P0: Channel A: Harvesting Channel Error Registers\n")	
			self.err_reg()
		
		elif(self.command =="i3ctransfer -d/dev/i3c-0-20400000001 -w 0x35,0x83"):
			print("P0: Channel B: Harvesting Channel Error Registers\n")	
			self.err_reg()
		
		elif(self.command =="i3ctransfer -d/dev/i3c-0-20400000002 -w 0x35,0x83"):
			print("P0: Channel C: Harvesting Channel Error Registers\n")	
			self.err_reg()
		
		elif(self.command =="i3ctransfer -d/dev/i3c-0-20400000003 -w 0x35,0x83"):
			print("P0: Channel D: Harvesting Channel Error Registers\n")	
			self.err_reg()
		
		elif(self.command =="i3ctransfer -d/dev/i3c-0-20400000004 -w 0x35,0x83"):
			print("P0: Channel E: Harvesting Channel Error Registers\n")	
			self.err_reg()
		
		elif(self.command =="i3ctransfer -d/dev/i3c-0-20400000005 -w 0x35,0x83"):
			print("P0: Channel F: Harvesting Channel Error Registers\n")
			self.err_reg()
		
		elif(self.command =="i3ctransfer -d/dev/i3c-1-20400000000 -w 0x35,0x83"):
			print("P0: Channel G: Harvesting Channel Error Registers\n")	
			self.err_reg()
		
		elif(self.command =="i3ctransfer -d/dev/i3c-1-20400000001 -w 0x35,0x83"):
			print("P0: Channel H: Harvesting Channel Error Registers\n")	
			self.err_reg()
		
		elif(self.command =="i3ctransfer -d/dev/i3c-1-20400000002 -w 0x35,0x83"):
			print("P0: Channel I: Harvesting Channel Error Registers\n")	
			self.err_reg()
		
		elif(self.command =="i3ctransfer -d/dev/i3c-1-20400000003 -w 0x35,0x83"):
			print("P0: Channel J: Harvesting Channel Error Registers\n")	
			self.err_reg()
		
		elif(self.command =="i3ctransfer -d/dev/i3c-1-20400000004 -w 0x35,0x83"):
			print("P0: Channel K: Harvesting Channel Error Registers\n")	
			self.err_reg()
		
		elif(self.command =="i3ctransfer -d/dev/i3c-1-20400000005 -w 0x35,0x83"):
			print("P0: Channel L: Harvesting Channel Error Registers\n")	
			self.err_reg()
		
		elif(self.command =="i3ctransfer -d/dev/i3c-2-20400000000 -w 0x35,0x83"):
			print("P1: Channel A: Harvesting Channel Error Registers\n")	
			self.err_reg()
			
		elif(self.command =="i3ctransfer -d/dev/i3c-2-20400000001 -w 0x35,0x83"):
			print("P1: Channel B: Harvesting Channel Error Registers\n")	
			self.err_reg()
			
		elif(self.command =="i3ctransfer -d/dev/i3c-2-20400000002 -w 0x35,0x83"):
			print("P1: Channel C: Harvesting Channel Error Registers\n")	
			self.err_reg()
			
		elif(self.command =="i3ctransfer -d/dev/i3c-2-20400000003 -w 0x35,0x83"):
			print("P1: Channel D: Harvesting Channel Error Registers\n")	
			self.err_reg()
			
		elif(self.command =="i3ctransfer -d/dev/i3c-2-20400000004 -w 0x35,0x83"):
			print("P1: Channel E: Harvesting Channel Error Registers\n")	
			self.err_reg()
			
		elif(self.command =="i3ctransfer -d/dev/i3c-2-20400000005 -w 0x35,0x83"):
			print("P1: Channel F: Harvesting Channel Error Registers\n")	
			self.err_reg()
			
		elif(self.command =="i3ctransfer -d/dev/i3c-3-20400000000 -w 0x35,0x83"):
			print("P1: Channel G: Harvesting Channel Error Registers\n")	
			self.err_reg()
			
		elif(self.command =="i3ctransfer -d/dev/i3c-3-20400000001 -w 0x35,0x83"):
			print("P1: Channel H: Harvesting Channel Error Registers\n")	
			self.err_reg()
		
		elif(self.command =="i3ctransfer -d/dev/i3c-3-20400000002 -w 0x35,0x83"):
			print("P1: Channel I: Harvesting Channel Error Registers\n")	
			self.err_reg()
		
		elif(self.command =="i3ctransfer -d/dev/i3c-3-20400000003 -w 0x35,0x83"):
			print("P1: Channel J: Harvesting Channel Error Registers\n")	
			self.err_reg()
		
		elif(self.command =="i3ctransfer -d/dev/i3c-3-20400000004 -w 0x35,0x83"):
			print("P1: Channel K: Harvesting Channel Error Registers\n")	
			self.err_reg()
		
		elif(self.command =="i3ctransfer -d/dev/i3c-3-20400000005 -w 0x35,0x83"):
			print("P1: Channel L: Harvesting Channel Error Registers\n")	
			self.err_reg()
		
		print("\nNo AC Cycle required for system recovery...")
		
	
	##
	# @brief function calls the error_registers method to print the error registres along with connecting to BMC to SSH
	# @return none
	##
	def power_good(self):
		self.command = self.command + "0x84"
		print("\nNon Fatal Error has been injected into VOUT 1.8 V LDO Power Good...\n") 
		print("VOUT 1.8 V LDO Power Good Command: " + self.command + "\n")
		
		if(self.command =="i3ctransfer -d/dev/i3c-0-20400000000 -w 0x35,0x84"):					
			print("P0: Channel A: Harvesting Channel Error Registers\n")	
			self.err_reg()
		
		elif(self.command =="i3ctransfer -d/dev/i3c-0-20400000001 -w 0x35,0x84"):
			print("P0: Channel B: Harvesting Channel Error Registers\n")	
			self.err_reg()
		
		elif(self.command =="i3ctransfer -d/dev/i3c-0-20400000002 -w 0x35,0x84"):
			print("P0: Channel C: Harvesting Channel Error Registers\n")	
			self.err_reg()
		
		elif(self.command =="i3ctransfer -d/dev/i3c-0-20400000003 -w 0x35,0x84"):
			print("P0: Channel D: Harvesting Channel Error Registers\n")	
			self.err_reg()
		
		elif(self.command =="i3ctransfer -d/dev/i3c-0-20400000004 -w 0x35,0x84"):
			print("P0: Channel E: Harvesting Channel Error Registers\n")	
			self.err_reg()
		
		elif(self.command =="i3ctransfer -d/dev/i3c-0-20400000005 -w 0x35,0x84"):
			print("P0: Channel F: Harvesting Channel Error Registers\n")
			self.err_reg()
		
		elif(self.command =="i3ctransfer -d/dev/i3c-1-20400000000 -w 0x35,0x84"):
			print("P0: Channel G: Harvesting Channel Error Registers\n")	
			self.err_reg()
		
		elif(self.command =="i3ctransfer -d/dev/i3c-1-20400000001 -w 0x35,0x84"):
			print("P0: Channel H: Harvesting Channel Error Registers\n")	
			self.err_reg()

		
		elif(self.command =="i3ctransfer -d/dev/i3c-1-20400000002 -w 0x35,0x84"):
			print("P0: Channel I: Harvesting Channel Error Registers\n")	
			self.err_reg()
		
		
		elif(self.command =="i3ctransfer -d/dev/i3c-1-20400000003 -w 0x35,0x84"):
			print("P0: Channel J: Harvesting Channel Error Registers\n")	
			self.err_reg()
		
		elif(self.command =="i3ctransfer -d/dev/i3c-1-20400000004 -w 0x35,0x84"):
			print("P0: Channel K: Harvesting Channel Error Registers\n")	
			self.err_reg()
		
		elif(self.command =="i3ctransfer -d/dev/i3c-1-20400000005 -w 0x35,0x84"):
			print("P0: Channel L: Harvesting Channel Error Registers\n")	
			self.err_reg()
		
		elif(self.command =="i3ctransfer -d/dev/i3c-2-20400000000 -w 0x35,0x84"):
			print("P1: Channel A: Harvesting Channel Error Registers\n")	
			self.err_reg()
			
		elif(self.command =="i3ctransfer -d/dev/i3c-2-20400000001 -w 0x35,0x84"):
			print("P1: Channel B: Harvesting Channel Error Registers\n")	
			self.err_reg()
			
		elif(self.command =="i3ctransfer -d/dev/i3c-2-20400000002 -w 0x35,0x84"):
			print("P1: Channel C: Harvesting Channel Error Registers\n")	
			self.err_reg()
			
		elif(self.command =="i3ctransfer -d/dev/i3c-2-20400000003 -w 0x35,0x84"):
			print("P1: Channel D: Harvesting Channel Error Registers\n")	
			self.err_reg()
			
		elif(self.command =="i3ctransfer -d/dev/i3c-2-20400000004 -w 0x35,0x84"):
			print("P1: Channel E: Harvesting Channel Error Registers\n")	
			self.err_reg()
			
		elif(self.command =="i3ctransfer -d/dev/i3c-2-20400000005 -w 0x35,0x84"):
			print("P1: Channel F: Harvesting Channel Error Registers\n")	
			self.err_reg()
			
		elif(self.command =="i3ctransfer -d/dev/i3c-3-20400000000 -w 0x35,0x84"):
			print("P1: Channel G: Harvesting Channel Error Registers\n")	
			self.err_reg()
			
		elif(self.command =="i3ctransfer -d/dev/i3c-3-20400000001 -w 0x35,0x84"):
			print("P1: Channel H: Harvesting Channel Error Registers\n")	
			self.err_reg()
		
		elif(self.command =="i3ctransfer -d/dev/i3c-3-20400000002 -w 0x35,0x84"):
			print("P1: Channel I: Harvesting Channel Error Registers\n")	
			self.err_reg()
		
		elif(self.command =="i3ctransfer -d/dev/i3c-3-20400000003 -w 0x35,0x84"):
			print("P1: Channel J: Harvesting Channel Error Registers\n")	
			self.err_reg()
		
		elif(self.command =="i3ctransfer -d/dev/i3c-3-20400000004 -w 0x35,0x84"):
			print("P1: Channel K: Harvesting Channel Error Registers\n")	
			self.err_reg()
		
		elif(self.command =="i3ctransfer -d/dev/i3c-3-20400000005 -w 0x35,0x84"):
			print("P1: Channel L: Harvesting Channel Error Registers\n")	
			self.err_reg()
		
		print("\nNo AC Cycle required for system recovery...")
	
	
	##
	# @brief function calls the error_registers method to print the error registres along with connecting to BMC to SSH
	# @return none
	##
	def high_current_consumption(self):
		self.command = self.command + "0x85"
		print("\nNon Fatal Error has been injected into High Current Consumption Warning...\n") 
		print("High Current Consumption Warning Command: " + self.command + "\n")
		
		if(self.command =="i3ctransfer -d/dev/i3c-0-20400000000 -w 0x35,0x85"):					
			print("P0: Channel A: Harvesting Channel Error Registers\n")	
			self.err_reg()
		
		elif(self.command =="i3ctransfer -d/dev/i3c-0-20400000001 -w 0x35,0x85"):
			print("P0: Channel B: Harvesting Channel Error Registers\n")	
			self.err_reg()
		
		elif(self.command =="i3ctransfer -d/dev/i3c-0-20400000002 -w 0x35,0x85"):
			print("P0: Channel C: Harvesting Channel Error Registers\n")	
			self.err_reg()
		
		elif(self.command =="i3ctransfer -d/dev/i3c-0-20400000003 -w 0x35,0x85"):
			print("P0: Channel D: Harvesting Channel Error Registers\n")	
			self.err_reg()
		
		elif(self.command =="i3ctransfer -d/dev/i3c-0-20400000004 -w 0x35,0x85"):
			print("P0: Channel E: Harvesting Channel Error Registers\n")	
			self.err_reg()
		
		elif(self.command =="i3ctransfer -d/dev/i3c-0-20400000005 -w 0x35,0x85"):
			print("P0: Channel F: Harvesting Channel Error Registers\n")
			self.err_reg()
		
		elif(self.command =="i3ctransfer -d/dev/i3c-1-20400000000 -w 0x35,0x85"):
			print("P0: Channel G: Harvesting Channel Error Registers\n")	
			self.err_reg()
		
		elif(self.command =="i3ctransfer -d/dev/i3c-1-20400000001 -w 0x35,0x85"):
			print("P0: Channel H: Harvesting Channel Error Registers\n")	
			self.err_reg()

		elif(self.command =="i3ctransfer -d/dev/i3c-1-20400000002 -w 0x35,0x85"):
			print("P0: Channel I: Harvesting Channel Error Registers\n")	
			self.err_reg()
		
		elif(self.command =="i3ctransfer -d/dev/i3c-1-20400000003 -w 0x35,0x85"):
			print("P0: Channel J: Harvesting Channel Error Registers\n")	
			self.err_reg()
		
		elif(self.command =="i3ctransfer -d/dev/i3c-1-20400000004 -w 0x35,0x85"):
			print("P0: Channel K: Harvesting Channel Error Registers\n")	
			self.err_reg()
		
		elif(self.command =="i3ctransfer -d/dev/i3c-1-20400000005 -w 0x35,0x85"):
			print("P0: Channel L: Harvesting Channel Error Registers\n")	
			self.err_reg()
		
		elif(self.command =="i3ctransfer -d/dev/i3c-2-20400000000 -w 0x35,0x85"):
			print("P1: Channel A: Harvesting Channel Error Registers\n")	
			self.err_reg()
			
		elif(self.command =="i3ctransfer -d/dev/i3c-2-20400000001 -w 0x35,0x85"):
			print("P1: Channel B: Harvesting Channel Error Registers\n")	
			self.err_reg()
			
		elif(self.command =="i3ctransfer -d/dev/i3c-2-20400000002 -w 0x35,0x85"):
			print("P1: Channel C: Harvesting Channel Error Registers\n")	
			self.err_reg()
			
		elif(self.command =="i3ctransfer -d/dev/i3c-2-20400000003 -w 0x35,0x85"):
			print("P1: Channel D: Harvesting Channel Error Registers\n")	
			self.err_reg()
			
		elif(self.command =="i3ctransfer -d/dev/i3c-2-20400000004 -w 0x35,0x85"):
			print("P1: Channel E: Harvesting Channel Error Registers\n")	
			self.err_reg()
			
		elif(self.command =="i3ctransfer -d/dev/i3c-2-20400000005 -w 0x35,0x85"):
			print("P1: Channel F: Harvesting Channel Error Registers\n")	
			self.err_reg()
			
		elif(self.command =="i3ctransfer -d/dev/i3c-3-20400000000 -w 0x35,0x85"):
			print("P1: Channel G: Harvesting Channel Error Registers\n")	
			self.err_reg()
			
		elif(self.command =="i3ctransfer -d/dev/i3c-3-20400000001 -w 0x35,0x85"):
			print("P1: Channel H: Harvesting Channel Error Registers\n")	
			self.err_reg()
		
		elif(self.command =="i3ctransfer -d/dev/i3c-3-20400000002 -w 0x35,0x85"):
			print("P1: Channel I: Harvesting Channel Error Registers\n")	
			self.err_reg()
			
		elif(self.command =="i3ctransfer -d/dev/i3c-3-20400000003 -w 0x35,0x85"):
			print("P1: Channel J: Harvesting Channel Error Registers\n")	
			self.err_reg()
		
		elif(self.command =="i3ctransfer -d/dev/i3c-3-20400000004 -w 0x35,0x85"):
			print("P1: Channel K: Harvesting Channel Error Registers\n")	
			self.err_reg()
		
		elif(self.command =="i3ctransfer -d/dev/i3c-3-20400000005 -w 0x35,0x85"):
			print("P1: Channel L: Harvesting Channel Error Registers\n")	
			self.err_reg()
		
		print("\nNo AC Cycle required for system recovery...")
		
	##
	# @brief function calls the error_registers method to print the error registres along with connecting to BMC to SSH
	# @return none
	##	
	def reserved(self):
		self.command = self.command + "0x86"
		print("\nNon Fatal Error has been injected into Reserved...\n") 
		print("Reserved Command: " + self.command + "\n")
		
		if(self.command =="i3ctransfer -d/dev/i3c-0-20400000000 -w 0x35,0x86"):					
			print("P0: Channel A: Harvesting Channel Error Registers\n")	
			self.err_reg()
		
		elif(self.command =="i3ctransfer -d/dev/i3c-0-20400000001 -w 0x35,0x86"):
			print("P0: Channel B: Harvesting Channel Error Registers\n")	
			self.err_reg()
		
		elif(self.command =="i3ctransfer -d/dev/i3c-0-20400000002 -w 0x35,0x86"):
			print("P0: Channel C: Harvesting Channel Error Registers\n")	
			self.err_reg()
		
		elif(self.command =="i3ctransfer -d/dev/i3c-0-20400000003 -w 0x35,0x86"):
			print("P0: Channel D: Harvesting Channel Error Registers\n")	
			self.err_reg()
		
		elif(self.command =="i3ctransfer -d/dev/i3c-0-20400000004 -w 0x35,0x86"):
			print("P0: Channel E: Harvesting Channel Error Registers\n")	
			self.err_reg()
		
		elif(self.command =="i3ctransfer -d/dev/i3c-0-20400000005 -w 0x35,0x86"):
			print("P0: Channel F: Harvesting Channel Error Registers\n")
			self.err_reg()
		
		elif(self.command =="i3ctransfer -d/dev/i3c-1-20400000000 -w 0x35,0x86"):
			print("P0: Channel G: Harvesting Channel Error Registers\n")	
			self.err_reg()
		
		elif(self.command =="i3ctransfer -d/dev/i3c-1-20400000001 -w 0x35,0x86"):
			print("P0: Channel H: Harvesting Channel Error Registers\n")	
			self.err_reg()
		
		elif(self.command =="i3ctransfer -d/dev/i3c-1-20400000002 -w 0x35,0x86"):
			print("P0: Channel I: Harvesting Channel Error Registers\n")	
			self.err_reg()
		
		elif(self.command =="i3ctransfer -d/dev/i3c-1-20400000003 -w 0x35,0x86"):
			print("P0: Channel J: Harvesting Channel Error Registers\n")	
			self.err_reg()
		
		elif(self.command =="i3ctransfer -d/dev/i3c-1-20400000004 -w 0x35,0x86"):
			print("P0: Channel K: Harvesting Channel Error Registers\n")	
			self.err_reg()
		
		elif(self.command =="i3ctransfer -d/dev/i3c-1-20400000005 -w 0x35,0x86"):
			print("P0: Channel L: Harvesting Channel Error Registers\n")	
			self.err_reg()
		
		elif(self.command =="i3ctransfer -d/dev/i3c-2-20400000000 -w 0x35,0x86"):
			print("P1: Channel A: Harvesting Channel Error Registers\n")	
			self.err_reg()
			
		elif(self.command =="i3ctransfer -d/dev/i3c-2-20400000001 -w 0x35,0x86"):
			print("P1: Channel B: Harvesting Channel Error Registers\n")	
			self.err_reg()
			
		elif(self.command =="i3ctransfer -d/dev/i3c-2-20400000002 -w 0x35,0x86"):
			print("P1: Channel C: Harvesting Channel Error Registers\n")	
			self.err_reg()
			
		elif(self.command =="i3ctransfer -d/dev/i3c-2-20400000003 -w 0x35,0x86"):
			print("P1: Channel D: Harvesting Channel Error Registers\n")	
			self.err_reg()
			
		elif(self.command =="i3ctransfer -d/dev/i3c-2-20400000004 -w 0x35,0x86"):
			print("P1: Channel E: Harvesting Channel Error Registers\n")	
			self.err_reg()
			
		elif(self.command =="i3ctransfer -d/dev/i3c-2-20400000005 -w 0x35,0x86"):
			print("P1: Channel F: Harvesting Channel Error Registers\n")	
			self.err_reg()
			
		elif(self.command =="i3ctransfer -d/dev/i3c-3-20400000000 -w 0x35,0x86"):
			print("P1: Channel G: Harvesting Channel Error Registers\n")	
			self.err_reg()
			
		elif(self.command =="i3ctransfer -d/dev/i3c-3-20400000001 -w 0x35,0x86"):
			print("P1: Channel H: Harvesting Channel Error Registers\n")	
			self.err_reg()
		
		elif(self.command =="i3ctransfer -d/dev/i3c-3-20400000002 -w 0x35,0x86"):
			print("P1: Channel I: Harvesting Channel Error Registers\n")	
			self.err_reg()
		
		elif(self.command =="i3ctransfer -d/dev/i3c-3-20400000003 -w 0x35,0x86"):
			print("P1: Channel J: Harvesting Channel Error Registers\n")	
			self.err_reg()
		
		elif(self.command =="i3ctransfer -d/dev/i3c-3-20400000004 -w 0x35,0x86"):
			print("P1: Channel K: Harvesting Channel Error Registers\n")	
			self.err_reg()
		
		elif(self.command =="i3ctransfer -d/dev/i3c-3-20400000005 -w 0x35,0x86"):
			print("P1: Channel L: Harvesting Channel Error Registers\n")	
			self.err_reg()
		
		print("\nNo AC Cycle required for system recovery...")
	
	
	##
	# @brief function calls the error_registers method to print the error registres along with connecting to BMC to SSH
	# @return none
	##	
	def current_limiter_warning(self):
		self.command = self.command + "0x87"
		print("\nNon Fatal Error has been injected into Current Limiter Warning...\n") 
		print("Current Limiter Warning Command: " + self.command + "\n")
		
		if(self.command =="i3ctransfer -d/dev/i3c-0-20400000000 -w 0x35,0x87"):					
			print("P0: Channel A: Harvesting Channel Error Registers\n")	
			self.err_reg()
		
		elif(self.command =="i3ctransfer -d/dev/i3c-0-20400000001 -w 0x35,0x87"):
			print("P0: Channel B: Harvesting Channel Error Registers\n")	
			self.err_reg()
		
		elif(self.command =="i3ctransfer -d/dev/i3c-0-20400000002 -w 0x35,0x87"):
			print("P0: Channel C: Harvesting Channel Error Registers\n")	
			self.err_reg()
		
		elif(self.command =="i3ctransfer -d/dev/i3c-0-20400000003 -w 0x35,0x87"):
			print("P0: Channel D: Harvesting Channel Error Registers\n")	
			self.err_reg()
		
		elif(self.command =="i3ctransfer -d/dev/i3c-0-20400000004 -w 0x35,0x87"):
			print("P0: Channel E: Harvesting Channel Error Registers\n")	
			self.err_reg()
		
		elif(self.command =="i3ctransfer -d/dev/i3c-0-20400000005 -w 0x35,0x87"):
			print("P0: Channel F: Harvesting Channel Error Registers\n")
			self.err_reg()
		
		elif(self.command =="i3ctransfer -d/dev/i3c-1-20400000000 -w 0x35,0x87"):
			print("P0: Channel G: Harvesting Channel Error Registers\n")	
			self.err_reg()
		
		elif(self.command =="i3ctransfer -d/dev/i3c-1-20400000001 -w 0x35,0x87"):
			print("P0: Channel H: Harvesting Channel Error Registers\n")	
			self.err_reg()

		
		elif(self.command =="i3ctransfer -d/dev/i3c-1-20400000002 -w 0x35,0x87"):
			print("P0: Channel I: Harvesting Channel Error Registers\n")	
			self.err_reg()
		
		
		elif(self.command =="i3ctransfer -d/dev/i3c-1-20400000003 -w 0x35,0x87"):
			print("P0: Channel J: Harvesting Channel Error Registers\n")	
			self.err_reg()
		
		elif(self.command =="i3ctransfer -d/dev/i3c-1-20400000004 -w 0x35,0x87"):
			print("P0: Channel K: Harvesting Channel Error Registers\n")	
			self.err_reg()
		
		elif(self.command =="i3ctransfer -d/dev/i3c-1-20400000005 -w 0x35,0x87"):
			print("P0: Channel L: Harvesting Channel Error Registers\n")	
			self.err_reg()
		
		elif(self.command =="i3ctransfer -d/dev/i3c-2-20400000000 -w 0x35,0x87"):
			print("P1: Channel A: Harvesting Channel Error Registers\n")	
			self.err_reg()
			
		elif(self.command =="i3ctransfer -d/dev/i3c-2-20400000001 -w 0x35,0x87"):
			print("P1: Channel B: Harvesting Channel Error Registers\n")	
			self.err_reg()
			
		elif(self.command =="i3ctransfer -d/dev/i3c-2-20400000002 -w 0x35,0x87"):
			print("P1: Channel C: Harvesting Channel Error Registers\n")	
			self.err_reg()
			
		elif(self.command =="i3ctransfer -d/dev/i3c-2-20400000003 -w 0x35,0x87"):
			print("P1: Channel D: Harvesting Channel Error Registers\n")	
			self.err_reg()
			
		elif(self.command =="i3ctransfer -d/dev/i3c-2-20400000004 -w 0x35,0x87"):
			print("P1: Channel E: Harvesting Channel Error Registers\n")	
			self.err_reg()
			
		elif(self.command =="i3ctransfer -d/dev/i3c-2-20400000005 -w 0x35,0x87"):
			print("P1: Channel F: Harvesting Channel Error Registers\n")	
			self.err_reg()
			
		elif(self.command =="i3ctransfer -d/dev/i3c-3-20400000000 -w 0x35,0x87"):
			print("P1: Channel G: Harvesting Channel Error Registers\n")	
			self.err_reg()
			
		elif(self.command =="i3ctransfer -d/dev/i3c-3-20400000001 -w 0x35,0x87"):
			print("P1: Channel H: Harvesting Channel Error Registers\n")	
			self.err_reg()
		
		elif(self.command =="i3ctransfer -d/dev/i3c-3-20400000002 -w 0x35,0x87"):
			print("P1: Channel I: Harvesting Channel Error Registers\n")	
			self.err_reg()
		
		elif(self.command =="i3ctransfer -d/dev/i3c-3-20400000003 -w 0x35,0x87"):
			print("P1: Channel J: Harvesting Channel Error Registers\n")	
			self.err_reg()
		
		elif(self.command =="i3ctransfer -d/dev/i3c-3-20400000004 -w 0x35,0x87"):
			print("P1: Channel K: Harvesting Channel Error Registers\n")	
			self.err_reg()
		
		elif(self.command =="i3ctransfer -d/dev/i3c-3-20400000005 -w 0x35,0x87"):
			print("P1: Channel L: Harvesting Channel Error Registers\n")	
			self.err_reg()
		
		print("\nNo AC Cycle required for system recovery...")
		
	##
	# @brief function prints the menu of options
	# @return none
	##
	def print_menu(self): 
		command = " "
		while command == " ":
			print("\nPMIC ERROR INJECTION TOOL")	
			print("\nChoose from the following options: ")
			print("OVER & UNDER VOLTAGE ERRORS BELOW...")
			print("1. SWA")                            
			print("2. SWB")
			print("3. SWC")
			print("4. SWD")
			print("5. VIN_BULK")
			print("6. VIN_MGMT")
			print("7. EXIT")
			print("MISC ERRORS BELOW...")
			print("1. Undefined")
			print("2. VINMgmt to VINBulk Switchover")
			print("3. Critical Temperature Shutdown")
			print("4. High Temperature Warning Threshold")
			print("5. VOUT_1.8V LDO Power Good")
			print("6. High Current Consumption Warning")
			print("7. Reserved")
			print("8. Current Limiter Warning")
			print("9. EXIT")
			command = input("Enter command: ")
			
			if command.upper() == "SWA":
				print("1. Over Voltage")
				print("2. Under Voltage")
				print("3. EXIT")
				command = input("Enter command: ")
				if command == "Over Voltage":
					print("\nRunning Over Voltage SWA Command...") 
					self.run_swa_over_voltage()
				elif command == "Under Voltage":
					print("\nRunning Under Voltage SWA Command...")
					self.run_swa_under_voltage()
				elif command.upper() == "EXIT":
					print("Exiting...")
					exit()
				else:
					print("Command not Found. Exiting ...")
					exit()
			
			elif command.upper() == "SWB":
				print("1. Over Voltage")
				print("2. Under Voltage")
				print("3. EXIT")
				command = input("Enter command: ")
				if command == "Over Voltage":
					print("\nRunning Over Voltage SWB Command...") 
					self.run_swb_over_voltage()
				elif command == "Under Voltage":
					print("\nRunning Under Voltage SWB Command...")
					self.run_swb_under_voltage()
				elif command.upper() == "EXIT":
					print("Exiting...")
					exit()
				else:
					print("Command not Found. Exiting ...")
					exit()
			elif command.upper() == "SWC":
				print("1. Over Voltage")
				print("2. Under Voltage")
				print("3. EXIT")
				command = input("Enter command: ")
				if command == "Over Voltage":
					print("\nRunning Over Voltage SWC Command...") 
					self.run_swc_over_voltage()
				elif command == "Under Voltage":
					print("\nRunning Under Voltage SWC Command...")
					self.run_swc_under_voltage()
				elif command.upper() == "EXIT":
					print("Exiting...")
					exit()
				else:
					print("Command not Found. Exiting ...")
					exit()
			
			elif command.upper() == "SWD":
				print("1. Over Voltage")
				print("2. Under Voltage")
				print("3. EXIT")
				command = input("Enter command: ")
				if command == "Over Voltage":
					print("\nRunning Over Voltage SWD Command...") 
					self.run_swd_over_voltage()
				elif command == "Under Voltage":
					print("\nRunning Under Voltage SWD Command...")
					self.run_swd_under_voltage()
				elif command.upper() == "EXIT":
					print("Exiting...")
					exit()
				else:
					print("Command not Found. Exiting ...")
					exit()
			
			elif command.upper() == "VIN_BULK":
				print("1. Over Voltage")
				print("2. Under Voltage")
				print("3. EXIT")
				command = input("Enter command: ")
				if command == "Over Voltage":
					print("\nRunning Over Voltage VIN_BULK Command...") 
					self.run_VINBulk_over_voltage()
				elif command == "Under Voltage":
					print("\nRunning Under Voltage VIN_BULK Command...")
					self.run_VINBulk_under_voltage()
				elif command.upper() == "EXIT":
					print("Exiting...")
					exit()
				else:
					print("Command not Found. Exiting ...")
					exit()
			
			elif command.upper() == "VIN_MGMT":
				print("1. Over Voltage")
				print("2. Under Voltage")
				print("3. EXIT")
				command = input("Enter command: ")
				if command == "Over Voltage":
					print("\nRunning Over Voltage VIN_MGMT Command...") 
					self.run_VINMgmt_over_voltage()
				elif command == "Under Voltage":
					print("\nRunning Under Voltage VIN_MGMT Command...")
					self.run_VINMgmt_under_voltage()
				elif command.upper() == "EXIT":
					print("Exiting...")
					exit()
				else:
					print("Command not Found. Exiting ...")
					exit()
			elif command == "Undefined":
				print("Running Undefined Command...")
				self.undefined()
			elif command == "VINMgmt to VINBulk Switchover":
				print("Running VINMgmt to VINBulk Switchover Command...")
				self.VINMgmt_to_VINBulk_switchover()
			elif command == "Critical Temperature Shutdown":
				print("Running Critical Temperature Shutdown Command...")
				self.critical_temp_shutdown()
			elif command == "High Temperature Warning Threshold":
				print("Running High Temperature Warning Threshold Command...")
				self.high_temp_warning_threshold()
			elif command == "VOUT_1.8V LDO Power Good":
				print("Running VOUT_1.8V LDO Power Good Command...")
				self.power_good()
			elif command == "High Current Consumption Warning":
				print("Running High Current Consumption Warning Command...")
				self.high_current_consumption()
			elif command == "Reserved":
				print("Running Reserved Command...")
				self.reserved()
			elif command == "Current Limiter Warning":
				print("Running Current Limiter Warning Command...")
				self.current_limiter_warning()
			elif command.upper() == "EXIT":
				print("Exiting...")
				exit()
			else:
				print("Command not Found. Exiting ...")
				exit()
	##
	# @brief main function
	# @return none
	##
def main():
	parser = argparse.ArgumentParser()
	parser.add_argument("-host", required=True, help="name of the host")
	parser.add_argument("-username", required=True, help="username")
	parser.add_argument("-password", required=True, help="password")
	parser.add_argument("-DIMMS", required=True, help="P0 or P1")
	parser.add_argument("-channel", required=True, help="channel")
	args_list = parser.parse_args()
	hostName = sys.argv[1].split("=")[1]
	userName = sys.argv[2].split("=")[1]
	password = sys.argv[3].split("=")[1]
	DIMMS = sys.argv[4].split("=")[1]
	channel = sys.argv[5].split("=")[1]
	c = Client(hostName, userName, password, DIMMS, channel)
	c.print_menu()
if __name__ == "__main__":
	main()

