import requests

def shorten_url(api_key, long_url):
    headers = {
        'Authorization': f'Bearer {api_key}',
        'Content-Type': 'application/json',
    }
    data = {
        "long_url": long_url,
    }
    response = requests.post('https://api-ssl.bitly.com/v4/shorten', json=data, headers=headers)

    if response.status_code == 200:
        return response.json()['link']
    else:
        raise Exception(f"Error shortening URL: {response.status_code}, {response.text}")

if __name__ == "__main__":
    api_key = 'bc3fdc563514a2e7a8652ad0a9a1e547671f6198'
    long_url = 'https://www.youtube.com/watch?v=nK1r_9hPWuI&ab_channel=LittleSoul'
    
    try:
        short_url = shorten_url(api_key, long_url)
        print(f'Shortened URL: {short_url}')
    except Exception as e:
        print(e)
