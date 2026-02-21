# --- Procesamiento por lotes ---
import os
import subprocess

# input_dir = 'data_directory'

for filename in os.listdir('data_directory'):
    if filename.endswith('.csv'):
        # Convert CSV diles to Excel using a shell command
        subprocess.call(['libreoffice', '--convert-to', 'xls', filename])

# --- Try-except ---
import subprocess

try: #Delete a file, raise an error if it fails
    subprocess.run(['rm', 'important_file.txt'], check=True)
except subprocess.CalledProcessError as e:
    print(f"Error deleting file: {e}")