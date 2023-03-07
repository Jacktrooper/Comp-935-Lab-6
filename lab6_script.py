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
        expected_sha256 = file_content.split()[0]
        return expected_sha256

    
        #a618d66b2f753343402200ad17d92eb6d4ab10db0dd1a098402e2968aa3114c4 this is the expeceted sha for refeence
    
    

def download_installer():
    # Send GET message to download the file
    file_url = 'http://download.videolan.org/pub/videolan/vlc/3.0.17.4/win64/vlc-3.0.17.4-win64.exe'
    resp_msg = requests.get(file_url)
    
    # Check whether the download was successful
    if resp_msg.status_code == requests.codes.ok:
        # Extract binary file content from response message
        installer_data = resp_msg.content
        return installer_data

    
    

def installer_ok(installer_data, expected_sha256):

    get_expected_sha256()
    download_installer()

    if installer_data == expected_sha256(installer_data).hexdigest():
        save_installer()
        return installer_data


def save_installer(installer_data):
    with open(r'C:\temp\vlc-3.0.17.4-win64.exe') as file:
        file.write(installer_data)
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