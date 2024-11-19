import os

# Full path of shared directory, with templates, log, and screenshots directory
shared_dir = os.path.dirname(os.path.abspath(__file__))
templates_dir = os.path.join(shared_dir, 'templates')
log_dir = os.path.join(shared_dir, 'logs')
screenshot_dir = os.path.join(log_dir, 'screenshots')

# Base file name for Activity Description (json) from ChatGPT and resulting VM Interaction Script
script_base_file_name = "catherine" # TODO: enter base file name here for files in shared dir

# VM Interaction
qcow2_file_name = 'windows10_catherine.qcow2' # TODO: enter file name of qcow2 file (in shared dir) 
qmp_port = 4444 # localhost port for qmp



