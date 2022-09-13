import subprocess

test_variable = "hello world"

modules = subprocess.run(['pip3', 'freeze'], capture_output=True).stdout.decode('utf-8')

print(modules)

for module in modules.splitlines():
    if mod in module:
        print("exists")
    else:
        continue