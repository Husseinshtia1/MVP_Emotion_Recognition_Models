
import os

def deploy_to_edge(device_ip, user, app_path):
    """Deploy the application to an edge device via SSH."""
    command = f"ssh {user}@{device_ip} 'mkdir -p ~/emotion_app && exit'"
    os.system(command)
    copy_command = f"scp -r {app_path} {user}@{device_ip}:~/emotion_app/"
    os.system(copy_command)
    print(f"Application deployed to {device_ip}")

if __name__ == "__main__":
    # Replace with actual device details
    deploy_to_edge("192.168.1.100", "pi", "./app")
