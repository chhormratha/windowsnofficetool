from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import pyperclip
import os
import time

os.system('cls & color e & title Windows Downloader')

# Set the download directory
download_directory = "/"  # Replace with your desired download directory

# Set up Chrome options to specify the download directory
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--user-agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36")
chrome_options.add_argument("--headless")
chrome_options.add_experimental_option("prefs", {
    "download.default_directory": download_directory,
    "download.prompt_for_download": False,
    "download.directory_upgrade": True,
    "safebrowsing.enabled": True
})

#options.add_argument('--headless')  # Run in headless mode (without opening a browser window)
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)

def download_win11():
    # Open the Microsoft Windows 11 download page
    driver.get("https://www.microsoft.com/software-download/windows11")
    time.sleep(1)
    select_version = driver.find_element(By.XPATH, "/html/body/main/div/div/div/div[2]/div[1]/div[1]/div/div[5]/div/div/div/div/div/div/div/div[1]/div/div[2]/div/div/select")
    select_version.click()
    os.system('cls')
    print('\n   Select Version')
    time.sleep(1)
    multi_edi = driver.find_element(By.XPATH, "/html/body/main/div/div/div/div[2]/div[1]/div[1]/div/div[5]/div/div/div/div/div/div/div/div[1]/div/div[2]/div/div/select/option[2]")
    multi_edi.click()
    os.system('cls')
    print('\n   Choose Muliple Language')
    time.sleep(1)
    download_now = driver.find_element(By.ID, "submit-product-edition")
    download_now.click()
    os.system('cls')
    print('\n   Next Download')
    time.sleep(5)
    choose_lang = driver.find_element(By.XPATH, "/html/body/main/div/div/div/div[2]/div[1]/div[2]/div/div/div/div/div/div/div/div[2]/div/div[2]/div/div/select")
    choose_lang.click()
    os.system('cls')
    print('\n   Choose Language')
    Eng_US = driver.find_element(By.XPATH, "/html/body/main/div/div/div/div[2]/div[1]/div[2]/div/div/div/div/div/div/div/div[2]/div/div[2]/div/div/select/option[11]")
    Eng_US.click()
    os.system('cls')
    print('\n   Select English United State')
    confirm_button = driver.find_element(By.ID, "submit-sku")
    confirm_button.click()
    os.system('cls')
    print('\n   Get Link Download')
    time.sleep(5)
    link_download = driver.find_element(By.XPATH, "/html/body/main/div/div/div/div[2]/div[1]/div[3]/div/div/div/div/div/div/div/div[2]/div/div/div/div/div/a")
    # Get the value of the href attribute
    link_download = link_download.get_attribute("href")
    pyperclip.copy(link_download)
    try: # Download
        response = requests.get(link_download)
        if response.status_code == 200:
            # Set the file path where you want to save the downloaded file
            file_path = ""  # Replace with your desired file path
            with open(file_path, 'wb') as f:
                f.write(response.content)
            print("Download completed successfully.")
        else:
            print(f"Failed to download the file. HTTP Status Code: {response.status_code}")
    except: pass
    driver.quit()
    os.system('del /q/f/s %TEMP%/*')
    os.system('cls & color e')
    print("\n   Download Link :\n")
    print(link_download)
    print('\n   Link Download was copied already ... !!!')
    start_download = input('\n   Download Now (y/n) : ')
    if start_download in ['y', 'Y', 'yes', 'Yes']:
        import requests
        from urllib.parse import urlparse

        print('')
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

        url = link_download
        file_path = download_file_with_progress_and_speed(url)
        print("File saved as:", file_path)
    else: 
        with open ('Download Windows 11.url', 'w') as file:
            file.write('[InternetShortcut]\n')
            file.write(f'URL={link_download}')


def download_win10():
    # Open the Microsoft Windows 11 download page
    driver.get("https://www.microsoft.com/en-us/software-download/windows10ISO")
    time.sleep(1)
    select_version = driver.find_element(By.XPATH, "/html/body/main/div/div/div/div[2]/div[1]/div[3]/div/div/div/div/div/div[2]/div/div[2]/div/select")
    select_version.click()
    os.system('cls')
    print('\n   Select Version')
    time.sleep(1)
    multi_edi = driver.find_element(By.XPATH, "/html/body/main/div/div/div/div[2]/div[1]/div[3]/div/div/div/div/div/div[2]/div/div[2]/div/select/option[2]")
    multi_edi.click()
    os.system('cls')
    print('\n   Choose Muliple Language')
    time.sleep(1)
    download_now = driver.find_element(By.ID, "submit-product-edition")
    download_now.click()
    os.system('cls')
    print('\n   Next Download')
    time.sleep(5)
    choose_lang = driver.find_element(By.ID, "product-languages")
    choose_lang.click()
    os.system('cls')
    print('\n   Choose Language')
    Eng_US = driver.find_element(By.XPATH, "/html/body/main/div/div/div/div[2]/div[1]/div[4]/div/div/div/div/div/div/div/div[2]/div/div[2]/div/div/select/option[11]")
    Eng_US.click()
    os.system('cls')
    print('\n   Select English United State')
    confirm_button = driver.find_element(By.ID, "submit-sku")
    confirm_button.click()
    time.sleep(5)
    os.system('cls')
    operate_sys = input('\n   Choose Operating System (x86 or x64) : ')
    if operate_sys in ['x86', '86', '32']:
        os.system('cls')
        print('\n   Get Link Download for x86')
        time.sleep(1)
        link_download = driver.find_element(By.XPATH, "/html/body/main/div/div/div/div[2]/div[1]/div[5]/div/div/div/div/div/div/div/div[2]/div/div/div/div[1]/div/a")
    else:
        os.system('cls')
        print('\n   Get Link Download for x64')
        time.sleep(1)
        link_download = driver.find_element(By.XPATH, "/html/body/main/div/div/div/div[2]/div[1]/div[5]/div/div/div/div/div/div/div/div[2]/div/div/div/div[2]/div/a")
    # Get the value of the href attribute
    link_download = link_download.get_attribute("href")
    pyperclip.copy(link_download)
    try: # Download
        response = requests.get(link_download)
        if response.status_code == 200:
            # Set the file path where you want to save the downloaded file
            file_path = ""  # Replace with your desired file path
            with open(file_path, 'wb') as f:
                f.write(response.content)
            print("Download completed successfully.")
        else:
            print(f"Failed to download the file. HTTP Status Code: {response.status_code}")
    except: pass
    driver.quit()
    os.system('del /q/f/s %TEMP%/*')
    os.system('cls & color e')
    print("\n   Download Link :\n")
    print(link_download)
    print('\n   Link Download was copied already ... !!!')
    start_download = input('\n   Download Now (y/n) : ')
    if start_download in ['y', 'Y', 'yes', 'Yes']:
        import requests
        from urllib.parse import urlparse

        print('')
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

        url = link_download
        file_path = download_file_with_progress_and_speed(url)
        print("File saved as:", file_path)
    else: 
        if operate_sys in ['x86', '86', '32']:
            with open ('Download Windows 10 x32.url', 'w') as file:
                file.write('[InternetShortcut]\n')
                file.write(f'URL={link_download}')
        else:
            with open ('Download Windows 10 x64.url', 'w') as file:
                file.write('[InternetShortcut]\n')
                file.write(f'URL={link_download}')

    
os.system('cls')
print('\n   1. Windows 10')
print('\n   2. Windows 11')
windows = input('\n   Choose Windows : ')
if windows in ['1', '10', 'windows 10']:
    download_win10()
else:
    download_win11()

time.sleep(555)

