import subprocess, os

file_names = []
file_dirs = []

COMPILER = "g++"
COMPILE_FLAGS = "-c"
OUTPUT_FLAGS = "-o"
LIBRARIES = "-l example -l one_more_example"
OUTPUT_NAME = "output.out"
OUTPUT_FORMAT = ".out"
BUILD_DIRECTORY = "build"
SOURCE_DIRECTORY = "src"

for _, dirs, files in os.walk("."):
  for file in files:
    if file.endswith('.cpp'):
      file_dirs.append(dirs)
      file_names.append(file)

file_dirs.reverse()

for index in range(len(file_names)):
  path = f"{SOURCE_DIRECTORY}/"
  for dirs_index in range(len(file_dirs[index])):
    path += f"{file_dirs[index][dirs_index]}/"
  path += file_names[index]
  subprocess_instance = subprocess.Popen(f"{COMPILER} {COMPILE_FLAGS} {path} {OUTPUT_FLAGS} {BUILD_DIRECTORY}/{file_names[index].rstrip('.cpp')}{OUTPUT_FORMAT}", shell=True, stdout=subprocess.PIPE)
  subprocess_instance.stdout.read()

compiled_files_string = ""

for _, _, files in os.walk(BUILD_DIRECTORY):
  for file in files:
    compiled_files_string += f"{BUILD_DIRECTORY}/{file} "

subprocess_instance = subprocess.Popen(f"{COMPILER} {compiled_files_string} {LIBRARIES} {OUTPUT_FLAGS} {OUTPUT_NAME}", shell=True, stdout=subprocess.PIPE)
subprocess_instance.stdout.read()
subprocess.Popen(f"./{OUTPUT_NAME}", shell=True)
