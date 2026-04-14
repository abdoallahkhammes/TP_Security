import requests
import hashlib


# API from: Have I Been Pwned (https://api.pwnedpasswords.com)

def check_breached(password: str) -> dict:
    """Check if password has been breached using HIBP API (k-Anonymity)"""
    sha1_hash = hashlib.sha1(password.encode()).hexdigest().upper()
    prefix, suffix = sha1_hash[:5], sha1_hash[5:]

    url = f"https://api.pwnedpasswords.com/range/{prefix}"
    response = requests.get(url)

    if response.status_code != 200:
        raise Exception("API request failed")

    for line in response.text.splitlines():
        hash_suffix, count = line.split(':')
        if hash_suffix == suffix:
            return {
                "breached": True,
                "count": int(count),
                "message": f"Password found {count} times in breaches"
            }

    return {
        "breached": False,
        "count": 0,
        "message": "Password not found in known breaches"
    }


# Example
if __name__ == "__main__":
    result = check_breached("password123")
    print(result)