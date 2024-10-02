# SkySizeTest for MYSTARSKY by LEYN1092

import os

# Settings
defaultWidth: int = 60
consoleClearCommand: str = "cls" # Change if using not windows

# Width test
while True:
    print("WIDTH TEST\n")
    print(f"Current width: {defaultWidth}")
    print("|" * defaultWidth)
    print("Change width by number, positive or negative (leave empty to save):")
    change = input()
    if change == "":
        break
    else:
        defaultWidth += int(change)
        os.system(consoleClearCommand)

os.system(consoleClearCommand)

# Height test:
print("-1 HEIGHT TEST")
print("0 Press Enter until the \"-1 HEIGHT TEST\"")
print("1 line is no longer visible")
print("2 The last number will be your sky height")
print("3 Leave NOT empty to stop")
i = 4
while True:
    if input(f"{i} ") != "":
        break
    else:
        i += 1

os.system(consoleClearCommand)

# Results
print("RESULTS")
print(f"Width: {defaultWidth}")
print(f"Height: {i}")