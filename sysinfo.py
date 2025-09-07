import os
import platform
import getpass

print("=== system information ===")
print(f"User: {getpass.getuser()}")
print(f"Hostname: {platform.node()}")
print(f"OS: {platform.system()} {platform.release()}")

print("\nfiles in current directory:")
print(os.listdir("."))
