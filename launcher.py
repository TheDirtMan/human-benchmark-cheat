#####

scripts = [
    ("Reaction Time", 'modules/reactionTime.py')
]

#####

from pathlib import Path
import subprocess
import sys
import os



os.system("clear")

print(
  "\n  -----------------------\n",
    "   Human Benchmark Cheat \n",
    "       By TheDirtMan     \n",
    "  -----------------------\n"
    )

for i, script in enumerate(scripts, start=1):
    print("  (" + str(i) + ")", script[0])


choice = 0

try:
    choice = int(input("\n\n  Select your Benchmark: "))
except ValueError:
    print("\nERROR: Input is not a number. Please select a real option and try again.\n")
    sys.exit(1)


if choice <= 0 or choice > len(scripts):
    print("\nERROR: Invalid option. Please select a real option and try again.\n")
    sys.exit(1)


launcher_dir = Path(__file__).resolve().parent

path = launcher_dir / scripts[choice-1][1]

if path.is_file():
    subprocess.run([sys.executable, str(path)])
else:
    print("\nERROR: File does not exist. Ensure files exist and try again.\n")