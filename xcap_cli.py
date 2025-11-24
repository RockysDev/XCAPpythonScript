import subprocess
import os
import shutil

# --- Define Your Variables ---
XCAP_M_EXE = r"C:\Program Files (x86)\Accuver\XCAP-M\XCAP-M.exe"
LOG_INPUT_PATH = r"C:\Users\Wireless\Documents\11-21inOfficeStationary\Mobile1" 
OUTPUT_PATH = r"C:\Users\Wireless\Desktop\Project" 
FAV_TEMPLATE = r"C:\Users\Wireless\Desktop\Project\DLThroughput.fav" 
SAMPLING_RATE = "-500ms" 

# --- PRE-RUN CLEANUP: Delete 'batch1' if it exists ---
# We join paths safely to get: C:\Users\Wireless\Desktop\Project\batch1
batch_folder = r"C:\Users\Wireless\Desktop\Project\Batch01"

if os.path.exists(batch_folder):
    print(f"📂 Found existing folder: {batch_folder}")
    try:
        shutil.rmtree(batch_folder)
        print("🗑️  Old 'batch1' folder deleted successfully.")
    except OSError as e:
        print(f"❌ Error deleting folder: {e}")
        # Optional: Exit script if we can't delete the old data
        # exit(1) 
else:
    print("✨ No old 'batch1' folder found. Proceeding...")


# --- Construct the Command ---
# The app will now automatically recreate 'batch1' inside OUTPUT_PATH
command = [
    XCAP_M_EXE,
    "-CM", LOG_INPUT_PATH, OUTPUT_PATH,
    "-FEP", FAV_TEMPLATE,
    "-MG",
    SAMPLING_RATE
]

# --- Execute the Command ---
print("🚀 Starting XCAP-M CLI...")
try:
    # capture_output=True gets stdout/stderr, check=True raises error on non-zero exit
    result = subprocess.run(command, check=True, capture_output=True, text=True)

    print("✅ XCAP-M command executed successfully.")
    
    # Optional debug info
    # print("STDOUT:\n", result.stdout)

except subprocess.CalledProcessError as e:
    print(f"❌ XCAP-M command failed with error code {e.returncode}")
    print("Command:", e.cmd)
    print("STDERR:", e.stderr)