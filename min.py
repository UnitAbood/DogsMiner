import requests
import time

# Define URLs
url_reward = 'https://dogs.triplecloudmining.com/get/advertisement/reward'
url_claim = 'https://dogs.triplecloudmining.com/claim/points/by/watching/ad'

# Define headers for the requests
headers = {
    "authority": "dogs.triplecloudmining.com",
    "method": "GET",
    "path": "/get/advertisement/reward",
    "scheme": "https",
    "accept": "*/*",
    "accept-encoding": "gzip, deflate, br, zstd",
    "accept-language": "en-US,en;q=0.9",
    "priority": "u=1, i",
    "referer": "https://dogs.triplecloudmining.com/",
    "sec-ch-ua": '"Microsoft Edge";v="129", "Not=A?Brand";v="8", "Chromium";v="129", "Microsoft Edge WebView2";v="129"',
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": '"Windows"',
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "same-origin",
    "x-csrf-token": "bqB8V994et7uxg91dRTOdaRcE3uAik67DdMhzBQm",
    "x-requested-with": "XMLHttpRequest",
}

# Define cookies
cookies = {
    "_ga": "GA1.1.146763373.1729098138",
    "_ga_8KRV3XSJBH": "GS1.1.1729098137.1.1.1729101637.0.0.0",
    "XSRF-TOKEN": "eyJpdiI6IjFtYXRSOEp3Z3NIMHNabUdBcFlVRXc9PSIsInZhbHVlIjoidTdSU1l2aTNFNDlkYmxtRDRiQkkxM2NlVlA1NVNSd1ZKRWFLZ2dzTjNhc2lDNURjUUc0WnF3Slc2NEpMajFZMlI1TjdkTUt0MkpvN0VuMkdCYjB5L2tCZEM0eHByV2laOExxTThtbGdFTllMWHp4YmZLQXUwUUl6NzRMUG9FRnUiLCJtYWMiOiJhNWNmNGY5YTM4YTJjYmJiYTI1MGM5OTVmNTBmNjQyOTBmZTg0ZDBkMmY3MTg2ZTUzZjgyZDQ0NDczNGYxOGM4IiwidGFnIjoiIn0%3D",
    "telegrambotdogs_session": "eyJpdiI6IjJoaHVubzZrMmdmWTF2ZkFIeTB5Tnc9PSIsInZhbHVlIjoiZEF5cjNsUHoxbTcvbXRvR3RNRllrVzZONzg4UGRiQ0tuNGRWVjR3SmU4WFlldUdXU1htbS9uTWlpNk1mRE0xR1RWc2d5cXJpRnVqK3VINHVOWW94VFRtK1lzRnEzRFRoai9xR0dxSEdVdkExNXNjVEVMdHdLQmhsVktkSWZ1dUwiLCJtYWMiOiIzZDg1MjllYTg3MjNiYjBlYzYzZWRhNmE5ZjQ2MzI4YWEwMjQzODgzZGZhY2Y2Y2YxOWZjOTdlM2RjZDEzN2FkIiwidGFnIjoiIn0%3D",
}

while True:
    try:
       
        response_reward = requests.get(url_reward, headers=headers, cookies=cookies)
       
        if response_reward.status_code == 200:
            print("1 dogs added")

          
            response_claim = requests.get(url_claim, headers=headers, cookies=cookies)
            
            if response_claim.status_code == 200:
                print("0.25 dogs added")
                
    except requests.exceptions.RequestException as e:
        print(f'Error: {e}. Retrying in 2 seconds...')
    