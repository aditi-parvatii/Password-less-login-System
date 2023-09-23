#to test whether the uuid which is being sent is the same as the displayed user id in the generated options. 
import base64
import uuid

# Your standard UUID
standard_uuid = uuid.UUID("16f4519a-3975-4bca-9f04-6c09603d27c2")

# Convert the UUID to a string
uuid_str = str(standard_uuid)

# Encode the string as a Base64 string
base64_uuid = base64.urlsafe_b64encode(uuid_str.encode('utf-8')).decode('utf-8').rstrip('=')

print(f"Standard UUID: {standard_uuid}")
print(f"Base64 UUID: {base64_uuid}")
