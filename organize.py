import os
import shutil
import time

# =====================================================
# YOUR DOWNLOADS FOLDER
# =====================================================

source_folder = r"C:\Users\Hp EliteBook  850 G3\Downloads"

# =====================================================
# DAYS BEFORE MOVING FILES
# =====================================================

days_old = 7

# Convert days to seconds
age_limit = days_old * 24 * 60 * 60

# =====================================================
# FILE TYPES
# =====================================================

file_types = {
    "Images": [".png", ".jpg", ".jpeg", ".gif"],
    "PDFs": [".pdf"],
    "Videos": [".mp4", ".mkv"],
    "Music": [".mp3"],
    "Archives": [".zip", ".rar"],
    "Word": [".doc", ".docx"],
    "Excel": [".xls", ".xlsx"],
    "PowerPoint": [".ppt", ".pptx"],
    "Code": [".py", ".js", ".html", ".css"]
}

# =====================================================
# ORGANIZE FILES
# =====================================================

print("\nChecking files older than 7 days...\n")

# Current time
current_time = time.time()

for filename in os.listdir(source_folder):

    file_path = os.path.join(source_folder, filename)

    # Skip folders
    if os.path.isdir(file_path):
        continue

    # File creation/modification time
    file_time = os.path.getmtime(file_path)

    # File age
    file_age = current_time - file_time

    # Skip recent files
    if file_age < age_limit:
        print(f"Skipping recent file: {filename}")
        continue

    # File extension
    extension = os.path.splitext(filename)[1].lower()

    moved = False

    # Check categories
    for folder_name, extensions in file_types.items():

        if extension in extensions:

            # Create destination folder
            destination_folder = os.path.join(
                source_folder,
                folder_name
            )

            os.makedirs(destination_folder, exist_ok=True)

            # Destination path
            destination_path = os.path.join(
                destination_folder,
                filename
            )

            # Handle duplicate names
            counter = 1
            base_name, ext = os.path.splitext(filename)

            while os.path.exists(destination_path):

                new_filename = f"{base_name}_{counter}{ext}"

                destination_path = os.path.join(
                    destination_folder,
                    new_filename
                )

                counter += 1

            # Move file
            shutil.move(file_path, destination_path)

            print(f"Moved: {filename} → {folder_name}")

            moved = True
            break

    # Unknown file type
    if not moved:
        print(f"No category for: {filename}")

print("\nDone!\n")