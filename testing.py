import uuid
import base64

# Your UUID as a string
uuid_str = "6f3fa56b-19ea-4e69-aa0f-b2dc180185c3"

# Encode the UUID bytes in base64
uuid_base64 = uuid_str.encode("utf-8")

# The generated user_id
generated_user_id = "NmYzZmE1NmItMTllYS00ZTY5LWFhMGYtYjJkYzE4MDE4NWMz"

# Compare the UUID base64 with the generated user_id
if uuid_base64 == generated_user_id:
    print("The UUID and the generated user_id are the same.")
else:
    print("The UUID and the generated user_id are different.")
