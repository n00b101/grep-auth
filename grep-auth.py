import os
import sys
import shutil
import platform

#Commands to gather SAP credentials from the data dump
#command1 is to scrape all SAP LOB customer accounts from all SAP LOB domains
command1 = "rg -i 'https?://(.+\.|)(ariba\.com|askdata\.com|calliduscloud\.com|cambridgesemantics\.com|concur\.com|concursolutions\.com|emarsys\.com|fieldglass\.com|ondemand\.com|qualtrics\.com|sap\.com|signavio\.com|successfactors\.com|dawex\.com|concurasp\.com|kerschies\.com|cnqr-cn\.com|concur\.concurtech\.org|fieldglass\.net|gusr\.net|eg2pp\.net|fgsap\.net|sapanalytics\.cloud|cnqr\.tech)' * >> SAP-LOB-Customers.txt"
command2 = "rg -i '@(ariba\.com|askdata\.com|calliduscloud\.com|cambridgesemantics\.com|concur\.com|concursolutions\.com|emarsys\.com|fieldglass\.com|ondemand\.com|qualtrics\.com|sap\.com|signavio\.com|successfactors\.com|dawex\.com|concurasp\.com|kerschies\.com|cnqr-cn\.com|concur\.concurtech\.org|fieldglass\.net|gusr\.net|eg2pp\.net|fgsap\.net|sapanalytics\.cloud|cnqr\.tech)' * >> SAP-LOB-User-Domains.txt"
command3 = "grep -E -r accounts.sap.com >> SAP-User-Accounts-SAP >> SAP-Accounts-User.txt"
command4 = "grep -E -r account.sap.com >> SAP-User-Accounts-SAP >> SAP-Account-User.txt"

# Run the commands using subprocess
result1 = subprocess.run(command1, shell=True, stdout=subprocess.PIPE, text=True)
result2 = subprocess.run(command2, shell=True, stdout=subprocess.PIPE, text=True)
result3 = subprocess.run(command3, shell=True, stdout=subprocess.PIPE, text=True)
result4 = subprocess.run(command3, shell=True, stdout=subprocess.PIPE, text=True)

# Print the results
print("Result of command 1:")
print(result1.stdout)

print("\nResult of command 2:")
print(result2.stdout)

print("\nResult of command 3:")
print(result3.stdout)

print("\nResult of command 3:")
print(result4.stdout)

# Check files under the current working directory
current_directory = os.getcwd()
files_in_directory = os.listdir(current_directory)

print("\nFiles under the current working directory:")
print(files_in_directory)
