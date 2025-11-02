import sys
import platform
import os
import subprocess

"""
This script is used to debug the server.
"""

print("Python version:", sys.version)
print("Platform:", platform.platform())
print("Processor:", platform.processor())
print("Environment variables:\n")
for k, v in sorted(os.environ.items()):
    print(f"{k}={v}")

print("\nInstalled packages:")
subprocess.run(["pip", "list"])
