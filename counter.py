filePath = "counterfile.bin"

try:
    fh = open(filePath, 'rb')
    count = int.from_bytes(fh.read()) + 1
    fh.close()
    with open(filePath, 'wb') as fh:
        fh.write(count.to_bytes())

except FileNotFoundError:
    fh = open(filePath, 'wb')
    count = 1
    fh.write(count.to_bytes())
    fh.close()

print('This script counts how many times it has been run.')
if count<=1:
    print("This script has been run", count, "time")
else:
    print("This script has been run", count, "times")