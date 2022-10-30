from pathlib import Path

path = Path("Packages_example/ecommerce")
print(path.exists())
for file in path.glob('*'):
    print(file)
