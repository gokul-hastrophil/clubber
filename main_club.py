import os
import shutil
import glob

def copy_images_from_selected_folders(source_folder, destination_folder, start_roll_id, end_roll_id,date, file_extensions=[".jpg",".png"]):
    # Create the destination folder if it doesn't exist
    if not os.path.exists(destination_folder):
        os.makedirs(destination_folder)

    # Iterate through the selected roll IDs
    for roll_id in range(start_roll_id, end_roll_id + 1):
        folder_path = os.path.join(source_folder, str(roll_id),date, "voltcam", "alarm", "unbox")
        #print(folder_path)
        condition = os.path.exists(os.path.join(source_folder, str(roll_id)))
        # Check if the folder exists before attempting to copy
        if condition:
            #print(f"{roll_id} Copying..........")
            # Construct the path for each selected folder
            folder_pattern = os.path.join(folder_path, "*", "*")
            #print(folder_pattern)
            # Use glob to find all files with the specified extension in the selected folder
            for extension in file_extensions:
                file_pattern = folder_pattern + extension
                image_files = glob.glob(file_pattern)
                #print(image_files)
                # Copy each image file to the destination folder
                for file_path in image_files:
                    print(file_path)
                    shutil.copy(file_path, destination_folder)
            #print(f"{roll_id} Copying Completed..........")
        else:
            print(f"Skipping roll ID {roll_id}: Folder does not exist")

if __name__ == "__main__":
    # Replace these paths with your actual source and destination paths
    source_directory = "/home/kniti/projects/knit-i/knitting-core/data"
    destination_directory = "/home/kniti/projects/alarm_log"
    
    # Take user input for the range of roll IDs
    start_roll_id = int(input("Enter start roll ID: "))
    end_roll_id = int(input("Enter end roll ID:"))
    date = str(input("Enter the date (yyyy-mm-dd):"))

    # Call the function to copy images from the specified folders
    copy_images_from_selected_folders(source_directory, destination_directory, start_roll_id, end_roll_id,date)

    print("Image copy completed.")
