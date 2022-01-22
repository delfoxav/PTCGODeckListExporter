import os
import parseDecklist

if __name__ == "__main__":
    if not os.path.isdir("Import"):
        print("Please Create the Import folder")
    else:
        for file in os.listdir("Import"):
            parseDecklist.parseTCGODecklist(file).exportToTCGO()
        