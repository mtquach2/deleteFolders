import os 
import shutil 
import time

def delete_folder(directory):
	# Get the disk usage of the current directory
	total, used, free = shutil.disk_usage(directory)

	# Calculate the percentage of disk space used 
	used_percentage = (used / total) * 100

	# Check to disk is at 75%+ capacity
	if used_percentage >= 75: 
		# Get the current time 
		current_time = time.time()

		# Iterate over all subdirectories 
		for subdirectory in os.listdir(directory):
			subdirectory_path = os.path.join(directory, subdirectory)

			# Check if it is a directory and older than 2 days 
			if os.path.isdir(subdirectory_path) and current_time - os.path.getctime(subdirectory_path) >= 2 * 24 * 60 * 60:
				# Delete subdirectory folder 
				shutil.rmtree(subdirectory_path)

# Specify the directory to check for disk capacity 
directory_path = "" # TODO: Change directory

# Call the function to delete folders
delete_folder(directory_path)
