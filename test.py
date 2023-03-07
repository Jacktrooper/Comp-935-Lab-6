import requests


file_url = 'http://download.videolan.org/pub/videolan/vlc/3.0.17.4/win64/vlc-3.0.17.4-win64.exe.sha256'
resp_msg = requests.get(file_url)
    
    # Check whether the download was successful
if resp_msg.status_code == requests.codes.ok:
    file_content = resp_msg.text
    # Extract text file content from response message so we can comapre it later
    expected_sha = file_content.split()[0]
    print(f'this is yeeters {expected_sha}')