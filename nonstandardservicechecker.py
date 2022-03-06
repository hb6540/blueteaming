import os

standardServices = []

with open ('services.txt') as f:
	standardServices = f.read().splitlines()

#print(standardServices)

installedServices = os.listdir('/usr/lib/systemd/system')


#print("***********************")
#print(installedServices)
nonStandardServices = []
nonStandardServicesFile = open("non_standard_services.txt", "w")

for service in installedServices:
	if service not in standardServices:
		nonStandardServices.append(service)

for service in nonStandardServicesFile:
    nonStandardServicesFile.write(service + '\n')

