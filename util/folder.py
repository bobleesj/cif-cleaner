import os

def choose_CIF_directory(script_directory):
    """
    Allows the user to select a directory from the given path.
    """
    directories = [d for d in os.listdir(script_directory) 
                   if os.path.isdir(os.path.join(script_directory, d)) 
                   and any(file.endswith('.cif') for file in os.listdir(os.path.join(script_directory, d)))]
    
    if not directories:
        print("No directories found in the current path containing .cif files!")
        return None
    print("\nAvailable folders containing CIF files:")
    for idx, dir_name in enumerate(directories, start=1):
        print(f"{idx}. {dir_name}")
    while True:
        try:
            choice = int(input("\nEnter the number corresponding to the folder containing .cif files: "))
            if 1 <= choice <= len(directories):
                return os.path.join(script_directory, directories[choice-1])
            else:
                print(f"Please enter a number between 1 and {len(directories)}.")
        except ValueError:
            print("Invalid input. Please enter a number.")



def save_to_csv_directory(folder_info, df, base_filename):
    """
    Saves the dataframe as a CSV inside a 'csv' sub-directory of the provided folder.

    :param folder_info: The parent directory where 'csv' sub-directory should be created.
    :param df: The dataframe to be saved.
    :param base_filename: The base name for the CSV file.
    :return: None
    """
    # Create the sub-directory for CSVs if it doesn't exist
    csv_directory = os.path.join(folder_info, "csv")
    if not os.path.exists(csv_directory):
        os.mkdir(csv_directory)

    # Extract the name of the chosen folder
    folder_name = os.path.basename(folder_info)

    # Set the name for the CSV file based on the chosen folder
    csv_filename = f"{folder_name}_{base_filename}.csv"

    # Save the DataFrame to the desired location (within the 'csv' sub-directory)
    df.to_csv(os.path.join(csv_directory, csv_filename), index=False)

    print(csv_filename, "saved")

