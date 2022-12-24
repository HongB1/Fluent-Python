import sys

original_write = sys.stdout.write
def reverse_write(text):
    original_write(text[::-1])
try:
    print("start")
    sys.exit(0)
finally:
    sys.stdout.write = reverse_write
    print("end")