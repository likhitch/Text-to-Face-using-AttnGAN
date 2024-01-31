# Define the path
path = "C:\\Users\\likhi\\OneDrive\\Desktop\\text2facegan-master\\Face data\\img_align_celeba\\img_align_celeba"

# Read the existing text file
with open("caps.txt", "r") as file:
    lines = file.readlines()

# Open the file for writing with the same name, which will overwrite the existing file
with open("caps.txt", "w") as file:
    for line in lines:
        if line.strip():  # Check if the line is not empty
            # Add the path and a backslash before the image name
            file.write(f"{path}\\{line}")

print("Paths added to the text file.")
