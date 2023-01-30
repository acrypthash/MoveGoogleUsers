from google.oauth2 import service_account
from googleapiclient.discovery import build

# Replace with the path to your service account key file
KEY_FILE_LOCATION = '/path/to/service_account.json'

# Replace with the name of the user you want to move
USER_EMAIL = 'user@example.com'

# Replace with the name of the target Organizational Unit
TARGET_OU = '/new_ou'

# Build the credentials object
credentials = service_account.Credentials.from_json_keyfile_name(
    KEY_FILE_LOCATION,
    ['https://www.googleapis.com/auth/admin.directory.user']
)

# Build the Admin SDK API client
service = build('admin', 'directory_v1', credentials=credentials)

# Get the current parent Organizational Unit of the user
user = service.users().get(userKey=USER_EMAIL).execute()
current_ou = user.get('orgUnitPath')

# Update the user with the new parent Organizational Unit
user['orgUnitPath'] = TARGET_OU
service.users().update(userKey=USER_EMAIL, body=user).execute()

print(f'User {USER_EMAIL} was moved from {current_ou} to {TARGET_OU}')

