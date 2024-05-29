import requests
import os
import time
from urllib.parse import urlparse
os.system('cls & color e & title Office Downloader - By CHHORM  RATHA')

def format_time(seconds):
    hours, remainder = divmod(seconds, 3600)
    minutes, seconds = divmod(remainder, 60)
    return f"{int(hours):02d}:{int(minutes):02d}:{int(seconds):02d}"
def download_file_with_progress_and_speed(url):
    response = requests.get(url, stream=True)
    total_size = int(response.headers.get('content-length', 0))
    # Extract file name from URL
    file_name = os.path.basename(urlparse(url).path)
    file_path = os.path.join(os.getcwd(), file_name)
    start_time = time.time()
    downloaded_size = 0
    block_size = 1024
    with open(file_path, 'wb') as file:
        for data in response.iter_content(block_size):
            file.write(data)
            downloaded_size += len(data)
            file_size_completed = f"{downloaded_size / (1024*1024):.2f}MB/{total_size / (1024*1024):.2f}MB"
            progress = downloaded_size / total_size
            elapsed_time = time.time() - start_time
            if elapsed_time > 0:
                download_speed = downloaded_size / elapsed_time
                download_speed_MB = download_speed / (1024*1024)
                remaining_time = (total_size - downloaded_size) / download_speed
                print(f"\rDownloading: {file_size_completed} | {progress:.2%} complete | Speed: {download_speed_MB:.2f} MB/s | Estimated Time: {format_time(remaining_time)}", end='', flush=True)
        print("\nDownload complete!")
    return file_path
office_type = input('\n   Input Office to Download (365, 21, 19, 16, 13, 10) : \n')
if office_type == '365':
    url = 'https://officecdn.microsoft.com/db/492350F6-3A01-4F97-B9C0-C7C6DDF67D60/media/en-US/O365ProPlusRetail.img'
elif office_type == '21':
    url = 'http://officecdn.microsoft.com/db/492350f6-3a01-4f97-b9c0-c7c6ddf67d60/media/en-US/ProPlus2021Retail.img'
elif office_type == '19':
    url = 'http://officecdn.microsoft.com/PR/492350f6-3a01-4f97-b9c0-c7c6ddf67d60/media/en-us/ProPlus2019Retail.img'
elif office_type == '16':
    url = 'https://officecdn.microsoft.com/db/492350F6-3A01-4F97-B9C0-C7C6DDF67D60/media/en-us/ProPlusRetail.img'
elif office_type == '13':
    url = 'http://officecdn.microsoft.com/pr/39168D7E-077B-48E7-872C-B232C3E72675/media/en-US/ProfessionalRetail.img'
elif office_type == '10':
    office_system = input('\n   32bit or 64bit (32, 64) : \n')
    if office_system == '64':
        url = 'https://web.archive.org/web/20160117182355/http://download.microsoft.com/download/1/A/8/1A879A5A-EE48-49E7-8831-449A71582173/officesuite2010sp1-kb2460049-x64-fullfile-en-us.exe'
    else:
        url = 'https://prod.downloadnow.com/faa/6e4/d481e8ae534cbf47afc46c22dc4f43ee3c/officesp2010-kb2687455-fullfile-x86-en-us.exe?Expires=1716759497&Signature=7bf3da2540c521eed6951687efb269d85e2f8c4f&url=https://download.cnet.com/microsoft-office-2010-service-pack-2-32-bit/3000-18513_4-75452813.html&Filename=officesp2010-kb2687455-fullfile-x86-en-us.exe'

file_path = download_file_with_progress_and_speed(url)
print("File saved as:", file_path)