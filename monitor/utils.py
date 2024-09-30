import os
import hashlib

# Directory to monitor
MONITOR_DIR = 'C:/Users/HP/FileMonitor/files_to_monitor'

# Save initial state of files
file_hashes = {}

def initialize_monitor():
    """Initialize file monitoring by hashing all files in the directory."""
    global file_hashes
    file_hashes = {}

    for root, dirs, files in os.walk(MONITOR_DIR):
        for filename in files:
            filepath = os.path.join(root, filename)
            file_hashes[filepath] = hash_file(filepath)

def hash_file(filepath):
    """Return SHA256 hash of a file."""
    hasher = hashlib.sha256()
    with open(filepath, 'rb') as f:
        buf = f.read()
        hasher.update(buf)
    return hasher.hexdigest()

def detect_modifications():
    """Detects file changes in MONITOR_DIR."""
    modifications = []
    current_files = {}

    # Hash current files
    for root, dirs, files in os.walk(MONITOR_DIR):
        for filename in files:
            filepath = os.path.join(root, filename)
            current_files[filepath] = hash_file(filepath)

            if filepath not in file_hashes:
                modifications.append(f"New file detected: {filepath}")
            elif current_files[filepath] != file_hashes[filepath]:
                modifications.append(f"File modified: {filepath}")

    # Detect deleted files
    for filepath in file_hashes:
        if filepath not in current_files:
            modifications.append(f"File deleted: {filepath}")

    # Update the file_hashes with current state
    file_hashes.update(current_files)

    return modifications
