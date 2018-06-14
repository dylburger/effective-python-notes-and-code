# This goes outside of the try / finally block because
# there's no need to close the file when it's not open
f = open('file.txt')
try:
    data = f.read()
finally:
    f.close()

f = open('file.txt')
try:
    lines = f.readlines()
except UnicodeDecodeError as e:
    print(f"Unicode Decode Error: {e}")
else:
    for line in lines:
        print(f"Line: {line.strip()}")
finally:
    f.close()
