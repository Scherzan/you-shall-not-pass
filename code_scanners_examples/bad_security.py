import os
import subprocess
import pickle

# Vulnerability: Command injection
def command_injection(user_input):
    os.system("echo " + user_input)

# Vulnerability: Use of eval
def insecure_eval(user_input):
    result = eval(user_input)
    return result

# Vulnerability: Use of dangerous built-in functions
def dangerous_builtin_functions(user_input):
    exec(user_input)

# Vulnerability: Use of insecure deserialization
def insecure_deserialization(serialized_data):
    data = pickle.loads(serialized_data)
    return data

# Vulnerability: Use of os.system
def insecure_os_system(user_input):
    os.system(user_input)

# Vulnerability: Use of subprocess with shell=True
def subprocess_shell_true(user_input):
    subprocess.Popen(user_input, shell=True)

if __name__ == "__main__":

    admin = "admin_user"
    password = "very_secure_1234"
    user_input = "Enter something: "

    # Calling vulnerable functions with user input
    command_injection(user_input)
    insecure_eval(user_input)
    dangerous_builtin_functions(user_input)
    insecure_deserialization(user_input)
    insecure_os_system(user_input)
    subprocess_shell_true(user_input)
