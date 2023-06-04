import webbrowser
from msal import ConfidentialClientApplication, PublicClientApplication

client_secret =  '955f7c56-aa69-4972-b602-c26ce41b3e23'
app_id = 'eace41e9-7190-47aa-bcd3-dd3fb5d2bcf5'
SCOPES = ['User.Read']

client = ConfidentialClientApplication(client_id=app_id, client_credential = client_secret)

authorization_url =  client.get_authorization_request_url(SCOPES)
print(authorization_url)
webbrowser.open(authorization_url)