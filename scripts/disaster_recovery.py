
import os
import shutil
import datetime

def backup_data(source_dir, backup_dir):
    """Backup the data from source to backup directory."""
    timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    backup_path = os.path.join(backup_dir, f"backup_{timestamp}")
    shutil.copytree(source_dir, backup_path)
    print(f"Data backed up to: {backup_path}")

def restore_data(backup_path, restore_dir):
    """Restore data from the backup directory."""
    shutil.copytree(backup_path, restore_dir, dirs_exist_ok=True)
    print(f"Data restored from: {backup_path}")

if __name__ == "__main__":
    # Example usage
    backup_data("./data", "./backups")
    restore_data("./backups/backup_20231018_120000", "./data")
