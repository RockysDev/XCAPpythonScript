import subprocess
import os
import glob
import shutil # Used for deleting folders
import pandas as pd # you're gonna need to run 'python -m pip install pandas', because it's not part of the standard python installation
import matplotlib.pyplot as plt

# --- Define Your Variables ---
XCAP_M_EXE = r"C:\Program Files (x86)\Accuver\XCAP-M\XCAP-M.exe"
LOG_INPUT_PATH = r"C:\Users\Wireless\Documents\11-21inOfficeStationary\Mobile1"
BASE_PROJECT_PATH = r"C:\Users\Wireless\Desktop\Project"
BATCH_FOLDER = os.path.join(BASE_PROJECT_PATH, "Batch1")
FAV_TEMPLATE = r"C:\Users\Wireless\Desktop\Project\DLThroughput.fav" 
SAMPLING_RATE = "-500ms"

# --- 1. PREP: Ensure Batch1 is Empty/Fresh ---
if os.path.exists(BATCH_FOLDER):
    try:
        shutil.rmtree(BATCH_FOLDER) # Delete it if it exists to remove old data
    except OSError as e:
        print(f"Error: {BATCH_FOLDER} : {e.strerror}")

os.makedirs(BATCH_FOLDER) # Create a fresh, empty folder
print(f"📁 Created fresh temporary folder: {BATCH_FOLDER}")

# --- 2. EXECUTE: Run XCAP Command ---
command = [
    XCAP_M_EXE,
    "-CM", LOG_INPUT_PATH, BATCH_FOLDER,
    "-FEP", FAV_TEMPLATE,
    "-MG",
    SAMPLING_RATE
]

try:
    print("⏳ Running XCAP-M (Please wait)...")
    subprocess.run(command, check=True, capture_output=True, text=True)
    print("✅ XCAP Export complete.")

    # --- 3. IDENTIFY: Find the 'Crazy Name' CSV ---
    # We use *.csv to find ANY csv file in that folder, regardless of the name
    csv_files = glob.glob(os.path.join(BATCH_FOLDER, "*.csv"))

    if not csv_files:
        print("❌ Error: XCAP finished, but no CSV file was found in Batch1.")
        exit()

    # Grab the first one found (since you said there is only one)
    target_file = csv_files[0]
    print(f"👀 Found data file: {os.path.basename(target_file)}")

    # --- 4. VISUALIZE: Plot the Data ---
    # Note: The script will PAUSE here until you close the graph window.
    print("📊 generating graph... (Close the graph window to finish and clean up)")
    
    df = pd.read_csv(target_file)
    
    # Basic plotting (Assumes Col 0 is Time, Col 1 is Data - Adjust if needed)
    plt.figure(figsize=(12, 6))
    plt.plot(df.iloc[:, 0], df.iloc[:, 1], label='Data Trace')
    plt.title(f"Trace: {os.path.basename(target_file)}")
    plt.grid(True)
    plt.legend()
    
    # This command halts the script. The cleanup code below won't run until you close the popup.
    plt.show() 

    print("📉 Graph closed.")

except subprocess.CalledProcessError as e:
    print(f"❌ XCAP Failed. Code: {e.returncode}")
    
except Exception as e:
    print(f"❌ An error occurred: {e}")

finally:
    # --- 5. CLEANUP: Delete the Batch1 Folder ---
    # This block runs whether the script succeeded or failed (as long as python didn't crash hard)
    if os.path.exists(BATCH_FOLDER):
        print("🧹 Cleaning up...")
        try:
            shutil.rmtree(BATCH_FOLDER)
            print("✨ Batch1 folder deleted. Workspace is clean.")
        except Exception as e:
            print(f"⚠️ Could not delete folder: {e}")