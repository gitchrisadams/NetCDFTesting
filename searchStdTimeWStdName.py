""" Christopher Adams
    4/18/17 
    Search through netcdf file and match items with 
    time and standard name. 
"""
# Import NetCDF4 library and Dataset module:
import netCDF4
from netCDF4 import Dataset

# Function 
def findStandardTimeVars(url):
	# Get the dataset:
	# nc = netCDF4.Dataset(url, mode='r')

	# With opens the file, then automatically will be closed if error and/or when exits:
	with netCDF4.Dataset(url, mode='r') as nc:

		for key in nc.variables:
			# print("Key: ")
			# print key

			# print("")

			# print("key: variables:")
			# print(nc.variables[key].ncattrs())
			# print("Len:")
			# print(len(nc.variables[key].ncattrs()))
			# print("")


			# Determine if there is a standard_name in this key:
			print("Standard Name testing All:")
			if("standard_name" in nc.variables[key].ncattrs()):
				print(key)
				print("Yes, it does have a standard name but time not check yet. ")
				print("")
			else:
				print(key)
				print("No, it does not have a standard name.")
				print("")

			dimOfKey = nc.variables[key].dimensions


			# Determine if there is a time dimension:
			# Ignore the actual 'time' key itself.
			if('time' in dimOfKey):
				if(key == 'time'):
					print(key)
					print("Yes, " + key + " contains time but ignorning since equal.")
					print("")
				else:
					print(key)
					print("Yes, " + key + " contains time.")
					print("")

					# Determine if there is a standard_name in this key:
					if("standard_name" in nc.variables[key].ncattrs()):
						print(key)
						print("Yes, it does have a standard name and time checked. ")
						print("")

					# Determine if there is an instrument in this key:
					if("instrument" in nc.variables[key].ncattrs()):
						print(key)
						print("Yes, it does have an instrument and time checked. ")
						print("")

						# TODO: It has an instument and time checked so now we have to
						# see if there is a variable named w/ the same name as the 
						# value of instrument.
						print("Instrument name:")
						print(nc.variables[key].ncattrs())


					else:
						print(key)
						print("No, it does not have an instrument and time checked.")
						print("")
			else:
				print("No, " + key + " does not contain time.")
				print("")




# Store URL of remote data:
url = 'http://sos.maracoos.org/stable/dodsC/hrecos/stationHRLCK8H-agg.ncml'

# Call function to search url.
# param: The url to search.
findStandardTimeVars(url)

