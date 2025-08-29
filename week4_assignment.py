

def modify_content(content):
    """
    Simple example modification function:
    Converts all text to uppercase.
    You can replace this with any custom logic.
    """
    return content.upper()

# Ask user for input file
filename = input("Enter the filename to read: ")

try:
    # Try opening and reading the file
    with open(filename, "r") as infile:
        content = infile.read()
    
    # Modify the content
    modified_content = modify_content(content)
    
    # Write the modified content to a new file
    new_filename = "modified_" + filename
    with open(new_filename, "w") as outfile:
        outfile.write(modified_content)
    
    print("Successfully created {new_filename} with modified content.")

except FileNotFoundError:
    print(" Error: The file does not exist. Please check the filename and try again.")
except PermissionError:
    print(" Error: Permission denied. Cannot read the file.")
except Exception as e:
    print(" An unexpected error occurred: {e}")
