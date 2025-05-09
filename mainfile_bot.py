import Spotify_Bot as sb
import requests
from requests.auth import HTTPProxyAuth
#sb.check()
from multiprocessing import Process
import time



global i,invalid
invalid=[]


def count_lines(filename):
    file= None
    try:
        with open(filename, 'r') as file:
            return sum(1 for _ in file)
    except FileNotFoundError:
        return "File not found."
    finally:
        if file:
            file.close()


def read_line_from_file(filename, line_number):
    file= None
    try:
        with open(filename, 'r') as file:
            lines = file.readlines()
            if 1 <= line_number <= len(lines):
                return lines[line_number - 1].strip()  # line_number is 1-based
            else:
                return f"Line number {line_number} is out of range (1 to {len(lines)})"
    except FileNotFoundError:
        return f"File '{filename}' not found."
    except Exception as e:
        return f"Error: {e}"
    finally:
        if file:
            file.close()




def check_proxy(proxy_host, proxy_port, username, password):
    global i,invalid
    proxy_url = f"http://{username}:{password}@{proxy_host}:{proxy_port}"
    proxies = {
        "http": proxy_url,
        "https": proxy_url,
    }

    test_url = "https://api.open-meteo.com/v1/forecast?latitude=35&longitude=139&current_weather=true"

    try:
        response = requests.get(test_url, proxies=proxies, timeout=10)
        if response.status_code == 200:
            print("✅ Proxy is alive and working.")
            return True
        else:
            print(f"⚠️ Proxy responded with status code: {response.status_code}")
            invalid.append(i)
            return False
    except requests.RequestException as e:
        print(f"❌ Proxy check failed: {e}")
        invalid.append(i)
        return False

# Example usage:

def remove_line_by_number(filename, line_number):
    with open(filename, "r") as file:
        lines = file.readlines()

    with open(filename, "w") as file:
        for i, line in enumerate(lines):
            if i != line_number:  # line_number is 0-based
                file.write(line)

# Example usage: remove the 3rd line (index 2)



with open("proxies.txt", "r") as file:
    i=0
    for line in file:
        gg=(line.strip()).split(':')  # .strip() removes the newline character
        print(i)
        check_proxy(gg[0], gg[1], gg[2], gg[3])
        i+=1
        
print(invalid)
for k in invalid:
    remove_line_by_number("proxies.txt", k)


processes = []



if __name__ == "__main__":

    for g in range(1,count_lines('credentials.txt')+1):  # Start 4 identical processes
        serial, SPOTIFY_USERNAME, SPOTIFY_PASSWORD = read_line_from_file('credentials.txt',g).split(',,')   
        proxy_host, proxy_port, proxy_user, proxy_pass=read_line_from_file('proxies.txt',g).split(':')
        print(SPOTIFY_USERNAME, SPOTIFY_PASSWORD, proxy_host, proxy_port, proxy_pass, proxy_user, serial)
        
        p1 = Process(target=sb.check, args=(SPOTIFY_USERNAME, SPOTIFY_PASSWORD, proxy_host, proxy_port, proxy_pass, proxy_user, serial,))
        #sb.check(SPOTIFY_USERNAME, SPOTIFY_PASSWORD, proxy_host, proxy_port, proxy_pass, proxy_user, serial)
        
        #p2 = Process(target=run_browser_instance, args=('https://httpbin.org',))

    # Start the processes
        p1.start()
        processes.append(p1)
        #p2.start()

    # Wait for both to finish
    for p1 in processes:
        p1.join()
        #p2.join()
