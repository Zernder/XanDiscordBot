import sys

# List of packages that are considered part of the base Python installation
base_packages = sys.builtin_module_names

# List of packages you provided
all_packages = [
    "absl-py", "accelerate", "aiohttp", "aiosignal", "anyascii", "appdirs", "async-timeout", 
    # ... (add all the packages you listed)
]

# Filter out packages that are not in the base Python installation
non_base_packages = [pkg for pkg in all_packages if pkg not in base_packages]

# Print the non-base packages
for pkg in non_base_packages:
    print(pkg)
