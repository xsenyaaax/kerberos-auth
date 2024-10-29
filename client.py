import requests
from requests_kerberos import HTTPKerberosAuth, REQUIRED

kerberos_auth = HTTPKerberosAuth(mutual_authentication=REQUIRED)

base_url = 'http://127.0.0.1:5000'

# Public endpoint (no authentication)
def access_public_page():
    public_url = f'{base_url}/'
    response = requests.get(public_url)
    print(f"Public Page Response: {response.status_code}")
    print(response.json())

# Protected endpoint (Kerberos authentication required)
def access_protected_page():
    protected_url = f'{base_url}/protected'
    response = requests.get(protected_url, auth=kerberos_auth)
    if response.status_code == 200:
        print(f"Protected Page Response: {response.status_code}")
        print(response.json())
    else:
        print(f"Failed to authenticate with Kerberos. Status code: {response.status_code}")

if __name__ == '__main__':
    # Access public page
    access_public_page()

    # Access protected page
    access_protected_page()
