import subprocess

# --- Define Your Variables ---
XCAP_M_EXE = r"C:\Program Files (x86)\Accuver\XCAP-M\XCAP-M.exe"
LOG_INPUT_PATH = r"C:\Users\Wireless\Documents\NightTesting All Ports\Mobile1"  # Folder containing the log files
OUTPUT_PATH = r"C:\Users\Wireless\Desktop\Project"    # Folder where the CSV will be saved
FAV_TEMPLATE = r"C:\Users\Wireless\Desktop\Project\DLThroughput.fav" # Your pre-created *.fav file
SAMPLING_RATE = "-500ms"      # Example: Sampling rate option

# --- Construct the Command ---
# Example: Exporting Favorite KPIs (similar to the example in the file)
command = [
    XCAP_M_EXE,
    "-CM", LOG_INPUT_PATH, OUTPUT_PATH,
    "-FEP", FAV_TEMPLATE,
    "-MG",
    SAMPLING_RATE
]

# --- Execute the Command ---
try:
    # 'capture_output=True' to get stdout/stderr, 'check=True' to raise error on non-zero exit code
    result = subprocess.run(command, check=True, capture_output=True, text=True)

    print("✅ XCAP-M command executed successfully.")
    # Optional: Print the output/error if you need to debug or log it
    # print("STDOUT:\n", result.stdout)
    # print("STDERR:\n", result.stderr)

except subprocess.CalledProcessError as e:
    print(f"❌ XCAP-M command failed with error code {e.returncode}")
    print("Command:", e.cmd)
    # print("STDOUT:", e.stdout)
    # print("STDERR:", e.stderr)