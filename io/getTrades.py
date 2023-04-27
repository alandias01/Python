import io
import re


def reg():
    with open("data.txt", "r") as f:
        for line in f:
            x = re.search("updating", line)
            if x:
                print(line.rstrip())


f = "updating trade: 8645 now"
x = re.search("trade: (.*?) now", f, re.IGNORECASE)
print(x.groups()[0])
