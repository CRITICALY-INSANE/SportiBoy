#working on it phase wise
#use opencv to rectify is it play or pause
#if its pause press
#from WindowCapture import WindowCapture
#if not then check for number
import os
import re
import random
import pickle
import os.path
import zipfile
import threading
import time as tt
import numpy as np
import tkinter as tk
import firebase_admin
from time import time
import git_guy as gg
import pyautogui as pyg
from threading import Thread
from tkinter import messagebox
from seleniumwire import webdriver
#import undetected_chromedriver as UC
from firebase_admin import credentials, db
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service as ChromeService


loop_time=time()
pyg.FAILSAFE= False
#wincap=WindowCapture('Spotify - Web Player: Music for everyone - Google Chrome ')
loop_time=time()
time_space=None
global SPOTIFY_USERNAME,SPOTIFY_PASSWORD,proxy_host,proxy_port,proxy_pass,proxy_user,plugin_file,serial
SPOTIFY_USERNAME = None
SPOTIFY_PASSWORD=None
SONG_URI = "https://open.spotify.com/playlist/5OVLNBfbD8TVEpIR9Y2tGF?si=Z_DVMPpfSKmF8GFSDkv-lQ"
every_link=[]
proxy_host = "your.proxy.host"      # e.g., 123.45.67.89
proxy_port = 8080                   # e.g., 8000
proxy_user = "yourUsername"
proxy_pass = "yourPassword"
plugin_file = "proxy_auth_plugin.zip"

# Initialize Firebase with your credentials
cred = credentials.Certificate("sporty-33cc0-firebase-adminsdk-v9b4v-7a9a3c806d.json")
firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://sporty-33cc0-default-rtdb.firebaseio.com/'
})

# Initialize Firestore database
ref = db.reference()

def check_4_input(typo,element_id):
    global driver
    try:
        element_present = EC.presence_of_element_located((typo, str(element_id)))
        WebDriverWait(driver,2).until(element_present)
        
    except Exception as e:
        check_4_input(typo,element_id)

def page_is_loading():
    global driver
    while True:
        x = driver.execute_script("return document.readyState")
        if x == "complete":
            return True
        else:
            yield False

def wait():
    global driver
    while not page_is_loading():
        tt.sleep(2)
        continue
    




# Path to cookie file
COOKIE_FILE = "cookies.pkl"
# Target website

def cook(driver):
    """Perform login manually or via script."""
    #driver.get(TARGET_URL)
    # --- Automate your login process here ---
    #input("Log in manually and press Enter to continue...")  # For manual login
    # time.sleep(10)  # or wait for login to complete
    pickle.dump(driver.get_cookies(), open(COOKIE_FILE, "wb"))
    print("Cookies saved.")

def start_browser_with_cookies():
    global driver,log
    """Start browser, use cookies if available, else login and save them."""
    

    if os.path.exists(COOKIE_FILE):
        try:
            cookies = pickle.load(open(COOKIE_FILE, "rb"))
            driver.delete_all_cookies()
            for cookie in cookies:
                driver.add_cookie(cookie)
            driver.refresh()
            print("Loaded cookies and refreshed.")
        except Exception as e:
            print(f"Failed to load cookies: {e}. Logging in again.")
            cook(driver)
    else:
        print("No cookie file found. Logging in...")
        cook(driver)

    return driver

# --- Usage ---
#driver = start_browser_with_cookies()
# Continue with your Selenium tasks...




def cookies_thing():
    global driver,log
    #start_browser_with_cookies()
    return


def link():
    thread = Thread(target=verify_did_we_login())
    # Start the thread's activity
    thread.start()
    # The main thread continues its execution while the new thread runs
    print("Main thread continuing...")
    # Wait for the thread to complete
    # This line will block the main thread until 'thread' finishes
    thread.join()

def verify_did_we_login():
    global driver,every_link
    current_url = driver.current_url
    current_url = driver.current_url
    every_link.append(current_url)
    every_link= list(set(every_link))
    print(every_link)

def link():
    thread = threading.Thread(target=verify_did_we_login())
    # Start the thread's activity
    thread.start()
    # The main thread continues its execution while the new thread runs
    print("Main thread continuing...")
    # Wait for the thread to complete
    # This line will block the main thread until 'thread' finishes
    thread.join()

def press_play():
    global driver,t_sta
    wait()
    t_sta='//*[@id="main"]/div/div[2]/div[4]/footer/div/div[2]/div/div[2]/div[1]'
    t_sto='//*[@id="main"]/div/div[2]/div[4]/footer/div/div[2]/div/div[2]/div[3]'
    song_name='//*[@id="main"]/div/div[2]/div[4]/footer/div/div[1]/div/div[2]/div[1]/div/span/span/div/span/a'
    
    check_4_input(By.XPATH,t_sta)
    check_4_input(By.XPATH,t_sto)
    check_4_input(By.XPATH,song_name)

    t_sta=driver.find_element(By.XPATH,t_sta ).text
    t_sto=driver.find_element(By.XPATH,t_sto ).text
    song_name=driver.find_element(By.XPATH,song_name ).text
    print('Start ->'+t_sta+' Stop-> '+t_sto)
    print('song_name ->'+song_name)
    tt.sleep(4)
    def parse(s):
        s=s.replace(':', '.', 1)
        return float(s)
    
    def run_or_not():
        global driver
        t_sta='//*[@id="main"]/div/div[2]/div[4]/footer/div/div[2]/div/div[2]/div[1]'
        check_4_input(By.XPATH,t_sta)
        t_sta=driver.find_element(By.XPATH,t_sta ).text
        cu_time=parse(t_sta)
        tt.sleep(5)



        t_sta='//*[@id="main"]/div/div[2]/div[4]/footer/div/div[2]/div/div[2]/div[1]'
        check_4_input(By.XPATH,t_sta)        
        gg=driver.find_element(By.XPATH,t_sta ).text
        new_time=parse(gg)
        if cu_time==new_time:
            driver.find_element(By.XPATH, "//body").send_keys(Keys.SPACE)  # Adjust as needed
            
    run_or_not()
    tt.sleep(2)
    wait()
    w=(t_sta)
    cook(driver)
    k=parse(w)
    if (k) >= 0.35:
        clr()
        print('one stream completeted')
        temp=song_name
        #print(nme.text)
        nx='//*[@id="main"]/div/div[2]/div[4]/footer/div/div[2]/div/div[1]/div[2]/button[1]'
        check_4_input(By.XPATH,nx)
        driver.find_element(By.XPATH,nx).click()
        save(temp)
        clicked=True   
    else:
        pass
                
    press_play()
    

    
def play():
    global driver,log,SONG_URI
    wait()
    tt.sleep(3)
    driver.get(SONG_URI)
    wait()
    tt.sleep(3)
    wait()
##    get_username()
##    save_cookies()
    press_play()
##    track_time()
##    change_every35to45sec()
    
    
def login():
    global driver,log,SPOTIFY_PASSWORD,SPOTIFY_USERNAME
    print('Enter code for login')
    wait()
    tt.sleep(4)
    wait()
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    cookies_thing()
    usr='login-username'
    passw='login-password'
    submit='login-button'
    continuee='//*[@id="login-button"]/span[1]/span'
    log_with_password='//*[@id="encore-web-main-content"]/div/div/div/div/form/div[2]/section/button'
    check_4_input(By.ID,usr)
    username_input = driver.find_element(By.ID,usr)

    for key1 in SPOTIFY_USERNAME:
        tt.sleep(.02)
        #keyboard.press(key)
        username_input.send_keys(key1)
    tt.sleep(3)
    try:
        driver.find_element(By.XPATH,continuee).click()
        tt.sleep(3)
        wait()
        driver.find_element(By.XPATH,log_with_password).click()
        tt.sleep(3)
        wait()
        
    except Exception as e:
        print(e)
        print('page 1')
        
    check_4_input(By.ID,submit)
    check_4_input(By.ID,passw)
    
    password_input = driver.find_element(By.ID, passw)

    for key in SPOTIFY_PASSWORD:
        tt.sleep(.05)
        password_input.send_keys(key)
            
        #check if the login button is enabled or not
    
    k2=int(random.randint(0, 9))
    tt.sleep(k2)
    wait()
    tt.sleep(5)
    log=driver.find_element(By.ID,'login-button')
    def enab():
        global log, driver
        if log.is_enabled():
            log.click()
            password_input.send_keys(Keys.ENTER)
            wait()
        else:
            tt.sleep(3)
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            enab()
    enab()
    tt.sleep(4)
    wait()
    #cookies_thing()
    

    print('Did We login')
    link()
    play()


def add_second_value():
    global strm
    
    file_name='spotify_report.txt'
    
    try:
        with open(file_name, 'r') as file:
            total = 0
            for line in file:
                values = line.split(',')
                if len(values) >= 2:
                    try:
                        total += float(values[1])
                    except ValueError:
                        print(f"Skipping line {line.strip()}: Second value is not a valid number")
                else:
                    print(f"Skipping line {line.strip()}: Not enough values in the line")

            print("Total sum of Stream values: -->", total)
            strm=total
            
    except FileNotFoundError:
        print("File not found")


def update_file(input_text, file_path):
    try:
        # Open the file in read mode
        with open(file_path, 'r') as file:
            lines = file.readlines()  # Read all lines into a list
            found = False

            # Iterate over each line and check if input text is present
            for index, line in enumerate(lines):
                if input_text in line:
                    found = True
                    # Split the line with ',' as delimiter
                    parts = line.strip().split(',')
                    count = int(parts[1]) + 1  # Increase the count by 1
                    lines[index] = f"{input_text},{count}\n"  # Rewrite the line
                    break
            
            # If input text is not found, add it to the beginning of the file
            if not found:
                lines.insert(0, f"{input_text},1\n")

        # Write the modified lines back to the file
        with open(file_path, 'w') as file:
            file.writelines(lines)
            print("File updated successfully.")
            return

    except FileNotFoundError:
        # If the file doesn't exist, create it and add the input text
        with open(file_path, 'w') as file:
            file.write(f"{input_text},1\n")
            print("File created and text added successfully.")
            return
    
def online():
    with open('spotify_report.txt', 'r', encoding='utf-8') as file:
        content = file.read()
        gg.new_con(content)
    



def save(sng_nme):
        file_name='spotify_report.txt'
        
        #update_file(sng_nme,file_name)
        thread = Thread(target = update_file, args = (sng_nme,file_name ))
        thread.start()
        thread.join()

        thread1 = Thread(target = add_second_value,)
        thread1.start()
        thread1.join()
        

        thread2 = Thread(target = online)
        thread2.start()
        thread2.join()
        
        return
        

def chop_string(string, start_substring, end_substring):
    print(string)
    start_index = string.find(start_substring)
    if start_index == -1:
        return "Start substring not found"
    
    end_index = string.find(end_substring, start_index + len(start_substring))
    if end_index == -1:
        return "End substring not found"
    
    chopped_string = string[start_index + len(start_substring):end_index]
    return chopped_string

# Example usage:



def see(alpha):
    global driver
    dri=driver
    strt='aria-label="'
    end='" data-encore-id='
    sta=chop_string(alpha, strt, end)
    print(sta)
    if sta=='Play':
        dri.find_element(By.XPATH,'//*[@id="main"]/div/div[2]/div[3]/div[1]/div[2]/div[2]/div[2]/main/section/div/div[2]/div[2]/div[2]/div/div/div/button').click()
    return

def clr():
    os.system('cls')  # For Windows
    #os.system('clear')  # For Linux/OS X
def check_status(st):
    print(st)
def search():
    tt.sleep(16)
    global driver
    clicked=True
    wait()
#     pl=driver.find_element('//*[@id="main"]/div/div[2]/div[3]/div[1]/div[2]/div[2]/div[2]/main/section/div/div[2]/div[2]/div[2]/div/div')
    while clicked:
#         check_status(pl.get_attribute("innerHTML"))
        try:
            r=pyg.locateOnScreen('assets/pause_or_play.jpeg',grayscale=True)
        except Exception as es:
            r='monk'
            print('Bhai seleniumm use kr ')
            print(es)
        if (str(r) != 'None' or r != None):
            #r=pyg.center(r)
            #pyg.moveTo(r)
            #print(r)
            #print('found waiting over ..finish')
            g=driver.find_element(By.XPATH,'//*[@id="main"]/div/div[2]/div[3]/div[1]/div[2]/div[2]/div[2]/main/section/div/div[2]/div[2]/div[2]/div/div/div/button').text
            see(g)
            tt.sleep(0.05)
            tt.sleep(2)
            k=driver.find_element(By.XPATH,'//*[@id="main"]/div/div[2]/div[2]/footer/div/div[2]/div/div[2]/div[1]')
            #print(k.text)
            k=(k.text).replace(':', '.', 1)
            if float(k) >= 0.35:
                clr()
                print('one stream completeted')
                nme=driver.find_element(By.XPATH,'//*[@id="main"]/div/div[2]/div[2]/footer/div/div[1]/div/div[2]/div[1]/div/div/div/div/span/a')            
                temp=nme.text
                #print(nme.text)
                driver.find_element(By.XPATH,'//*[@id="main"]/div/div[2]/div[2]/footer/div/div[2]/div/div[1]/div[2]/button[1]').click()
                save(temp)
                clicked=True
                
            else:
                print(str(k))
                
                
        else:
            #print('Still Searching on screen....')
            #print('Not found')
            tt.sleep(2)
            g=driver.find_element(By.XPATH,'//*[@id="main"]/div/div[2]/div[3]/div[1]/div[2]/div[2]/div[2]/main/section/div/div[2]/div[2]/div[2]/div/div/div/button').text
            see(g)
            k=driver.find_element(By.XPATH,'//*[@id="main"]/div/div[2]/div[2]/footer/div/div[2]/div/div[2]/div[1]')
            #print(k.text)
            k=(k.text).replace(':', '.', 1)
            if float(k) >= 0.35:
                clr()
                print('one stream completeted')
                nme=driver.find_element(By.XPATH,'//*[@id="main"]/div/div[2]/div[2]/footer/div/div[1]/div/div[2]/div[1]/div/div/div/div/span/a')
                temp=nme.text
                #print(nme.text)
                driver.find_element(By.XPATH,'//*[@id="main"]/div/div[2]/div[2]/footer/div/div[2]/div/div[1]/div[2]/button[1]').click()
                save(temp)
                clicked=True
                
                
            else:
                print(str(k))
                         
    return

def ch():
    for i in range(1,10):
        wait()
        #through check
        
def archive():
    global SPOTIFY_USERNAME,SPOTIFY_PASSWORD,proxy_host,proxy_port,proxy_pass,proxy_user,plugin_file,serial
    plugin_file = "proxy_auth_plugin"+serial+".zip"
    manifest_json = """
    {
      "version": "1.0.0",
      "manifest_version": 2,
      "name": "Chrome Proxy",
      "permissions": [
        "proxy",
        "tabs",
        "unlimitedStorage",
        "storage",
        "<all_urls>",
        "webRequest",
        "webRequestBlocking"
      ],
      "background": {
        "scripts": ["background.js"]
      }
    }
    """

    background_js = f"""
    var config = {{
      mode: "fixed_servers",
      rules: {{
        singleProxy: {{
          scheme: "http",
          host: "{proxy_host}",
          port: parseInt({proxy_port})
        }},
        bypassList: ["localhost"]
      }}
    }};

    chrome.proxy.settings.set({{value: config, scope: "regular"}}, function() {{}});

    chrome.webRequest.onAuthRequired.addListener(
      function(details) {{
        return {{
          authCredentials: {{
            username: "{proxy_user}",
            password: "{proxy_pass}"
          }}
        }};
      }},
      {{urls: ["<all_urls>"]}},
      ["blocking"]
    );
    """

    # === Write the extension files into a zip ===
    with zipfile.ZipFile(plugin_file, 'w') as zp:
        zp.writestr("manifest.json", manifest_json)
        zp.writestr("background.js", background_js)
    return plugin_file


def initial():
    global driver
    global SPOTIFY_USERNAME,SPOTIFY_PASSWORD,proxy_host,proxy_port,proxy_pass,proxy_user,serial
    plugin_file=archive()
    proxy_url = f"http://{proxy_user}:{proxy_pass}@{proxy_host}:{proxy_port}"
    print(proxy_url)
    seleniumwire_options = {
    "proxy": {
        "http": proxy_url,
        "https": proxy_url
    },
    }

    #for the future       driver = UC.Chrome()

    #service = webdriver.ChromeService(executable_path = 'chromedriver.exe',option=option)
    #driver = webdriver.Chrome(service=service)


    chrome_options = Options()
    a = "proxy_host:proxy_port:proxy_user:proxy_pass"
    chrome_options.add_argument('--proxy-server=:{}'.format(a))
    chrome_options.add_experimental_option("useAutomationExtension", False)
    chrome_options.add_experimental_option("excludeSwitches",["enable-automation"])
    
    
    service_obj = Service("chromedriver.exe")

    driver = webdriver.Chrome(options=chrome_options,service=service_obj)

    #driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()),seleniumwire_options=seleniumwire_options,options=chrome_options)
    
    tt.sleep(3)
    driver.maximize_window()


    driver.get('https://www.google.com/')
    wait()
    driver.get("https://httpbin.org/ip")
    wait()
    print("ip is     "+driver.find_element(By.XPATH, "//body").text)
    ch()
    
    link()
    driver.get('https://www.spotify.com/')
    for i in range(1,10):
        wait()
        tt.sleep(2)
        wait()
    check_4_input(By.XPATH,'//*[@id="onetrust-close-btn-container"]/button')
    driver.find_element(By.XPATH,'//*[@id="onetrust-close-btn-container"]/button').click()
    tt.sleep(2)
    check_4_input(By.XPATH,'//*[@id="global-nav-bar"]/div[3]/div/div/button[2]/span')
    driver.find_element(By.XPATH,'//*[@id="global-nav-bar"]/div[3]/div/div/button[2]/span').click()
    ch()
    login()
    driver.get(SONG_URI)
    tt.sleep(5)
    wait()
    return




def init():
    global SPOTIFY_USERNAME,SPOTIFY_PASSWORD
    # Checking if credentials were read successfully
    if SPOTIFY_USERNAME is not None and SPOTIFY_PASSWORD is not None:
        print("Spotify Username:", SPOTIFY_USERNAME)
        print("Spotify Password:", SPOTIFY_PASSWORD)
    else:
        print("Error: Unable to read Spotify credentials from file.")
    
    
def check(sp_us,sp_pa,pr_h,pr_p,pr_pa,pr_us,se):
    
    global SPOTIFY_USERNAME,SPOTIFY_PASSWORD,proxy_host,proxy_port,proxy_pass,proxy_user,plugin_file,serial    
    proxy_host = pr_h    # e.g., 123.45.67.89
    proxy_port = pr_p                   # e.g., 8000
    proxy_user = pr_us
    proxy_pass = pr_pa
    serial=se
    plugin_file = "proxy_auth_plugin"+serial+".zip"
    SPOTIFY_USERNAME=sp_us
    SPOTIFY_PASSWORD=sp_pa
    
    
    
    def file_check(file_path):
        if os.path.exists(file_path):
            file_present_action()
        else:
            file_not_present_action()

    def file_present_action():
        init()
        initial()
        try:
            search()
        except Exception as es:
            print(str(es))
            search()
        print("File is present. Calling function_a...")

    def file_not_present_action():
        
        print("File is not present. Calling function_b...")
        cred()  # Call your function if the file is not present

    # Example usage:
    file_path = "credentials.txt"
    file_check(file_path)

#check(a,b,c,d,e,f,g)


'''
check loop is on or off
a thread to check internet connection
method to check weather login or not
click play button
if page got stuck refresh
previous song
'''
