# compare_packages.py

global_packages = set()
venv_packages = set()

# Read your two package lists
with open('global-packages.txt', 'r') as f:
    for line in f:
        if '==' in line:
            pkg = line.split('==')[0].lower()
            global_packages.add(pkg)

with open('venv-packages.txt', 'r') as f:
    for line in f:
        if '==' in line:
            pkg = line.split('==')[0].lower()
            venv_packages.add(pkg)

# Compare
missing_in_venv = global_packages - venv_packages

print("\n🚨 Packages installed globally but missing in venv:")
for pkg in sorted(missing_in_venv):
    print(f" - {pkg}")

