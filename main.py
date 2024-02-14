import sys, os
VERSION = "v0.0.01A"

def arun(filepath):
    with open(filepath, "r") as f:
        for line in f.read().split("\n"):
            if line.startswith("println(") and line.endswith(")"):
                toprint = line.removeprefix("println(").removesuffix(")")
                if toprint.startswith("'") and toprint.endswith("'"):
                    print(toprint.removeprefix("'").removesuffix("'"))
                elif toprint.startswith('"') and toprint.endswith('"'):
                    print(toprint.removeprefix('"').removesuffix('"'))
                elif toprint.startswith('"') and toprint.endswith("'"):
                    print("Error: What the hell, do you really create strings like that: \"'? You disgust me.")
                elif toprint.startswith("'") and toprint.endswith('"'):
                    print("Error: What the hell, do you really create strings like that: '\"? You disgust me.")

def run(filepath):
    if os.path.exists("settings.lnst"):
        RunOnlyLNFiles = None
        for line in open("settings.lnst", "r").read().split("\n"):
            if line.startswith("RunOnlyLNFiles"):
                if line.removeprefix("RunOnlyLNFiles: ") == "Y":
                    RunOnlyLNFiles = True
                else:
                    RunOnlyLNFiles = False
        if os.path.exists(filepath):
            if (filepath.endswith(".ln") or filepath.endswith(".ln'") or filepath.endswith('.ln"')) and RunOnlyLNFiles:
                arun(filepath)
            elif not RunOnlyLNFiles:
                arun(filepath)
            else:
                print("Error: File isn't a .ln file.")
        else:
            print("Error: File doesn't exist.")
    else:
        print("Error: settings.lnst file doesn't exist, did you run the setup.py script before using Lunara ?")

def main():
    # totally not generated by ai
    if len(sys.argv) < 3:
        print("Usage: lunara <command> <filepath>")
        return
    
    command = sys.argv[1]
    filename = sys.argv[2]

    if command == "run":
        run(filename)
    else:
        print(f"Invalid command. Use 'run' or 'help'.")

if __name__ == "__main__":
    main()