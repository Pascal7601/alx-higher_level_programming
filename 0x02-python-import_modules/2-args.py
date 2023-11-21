import sys

num_args = len(sys.argv) - 1 
print(f"{'s' if num_args != 1 else ''}: {num_args}", end="")
print(":", end="" if num_args == 0 else "\n")

for i, arg in enumerate(sys.argv[1:], start=1):
    print(f"{i}: {arg}")

if num_args == 0:
    print(".")
