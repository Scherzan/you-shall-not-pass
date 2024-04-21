import os
import subprocess

# Hardcoded credentials
username = "admin"
password = "password"

def execute_command(command):
    subprocess.Popen(command, shell=True)

def insecure_crypto():
    key = "my_secret_key"
    # Insecure use of cryptography
    encrypted_data = os.urandom(16)
    return encrypted_data

def unsafe_deserialization(data):
    # Unsafe deserialization
    import pickle
    obj = pickle.loads(data)
    return obj

def command_injection(user_input):
    # Command injection vulnerability
    os.system("echo " + user_input)

def insecure_temp_file():
    # Insecure use of temporary file
    tempfile = "/tmp/tempfile.txt"
    with open(tempfile, "w") as f:
        f.write("Sensitive data")

def use_of_eval(code):
    # Use of eval
    result = eval(code)
    return result

if __name__ == "__main__":
    # Unsafely using user input
    user_input = input("Enter your name: ")
    print("Hello, " + user_input)

    # Calling functions with known security vulnerabilities
    command_injection(user_input)
    insecure_temp_file()

    # Using eval with user input
    code = input("Enter Python code to evaluate: ")
    use_of_eval(code)