import requests
import hashlib
import subprocess
import os
from sys import exit
def main():

    # Get the expected SHA-256 hash value of the VLC installer
    expected_sha256 = get_expected_sha256()
    

    # Download (but don't save) the VLC installer from the VLC website
    installer_data = download_installer()

    # Verify the integrity of the downloaded VLC installer by comparing the
    # expected and computed SHA-256 hash values
    if installer_ok(installer_data, expected_sha256):

        # Save the downloaded VLC installer to disk
        installer_path = save_installer(installer_data)

        # Silently run the VLC installer
        run_installer(installer_path)

        # Delete the VLC installer from disk
        delete_installer(installer_path)

def get_expected_sha256():
    # Send GET message to download the file
    file_url = 'http://download.videolan.org/pub/videolan/vlc/3.0.17.4/win64/vlc-3.0.17.4-win64.exe.sha256'
    resp_msg = requests.get(file_url)
    
    # Check whether the download was successful
    if resp_msg.status_code == requests.codes.ok:
        file_content = resp_msg.text
        # Extract text file content from response message so we can comapre it later
        expected_sha = file_content.split()[0]
        return expected_sha

    
        #fda8cbf2ee876be4eb14d7affca3a0746ef4ae78341dbb589cbdddcf912db85c this is the expeceted sha for refeence
    
    

def download_installer():
    # Send GET message to download the file
    file_url = 'http://download.videolan.org/pub/videolan/vlc/3.0.17.4/win64/vlc-3.0.17.4-win64.exe'
    resp_msg = requests.get(file_url)
    
    # Check whether the download was successful
    if resp_msg.status_code == requests.codes.ok:
        # Extract binary file content from response message
        data = resp_msg.content
        return data

    
    

def installer_ok(installer_data, expected_sha256):
        installer_data = hashlib.sha256(installer_data).hexdigest()
        if installer_data == expected_sha256:
            return installer_data
        else:
            SystemExit(1)


def save_installer(installer_data):
    file_content = installer_data.content
    with open(r'C:\temp\vlc-3.0.17.4-win64.exe', 'w') as file:
        file.write(file_content)
    return

def run_installer(installer_path):
    installer_path = r'C:\temp\vlc-3.0.17.4-win64.exe'
    subprocess.run([installer_path, '/L=1033', '/S'])
    return
    
def delete_installer(installer_path):
    installer_path = r'C:\temp\vlc-3.0.17.4-win64.exe'
    os.remove(installer_path)
    return

if __name__ == '__main__':
    main()