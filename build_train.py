# this file automatically creates the train.md
import glob
import os
from os import path

data_dir = path.join(path.dirname(__file__), "data")

def create_vocab():
	output_f = path.join(data_dir, 'train.md')

	with open(output_f, 'w') as outfile:
		print("[*] Writing data to ", output_f)
		write_md("intent", outfile)
		write_md("synonym", outfile)
		write_md("regex", outfile)

def write_md(name, outfile):
	files = glob.glob('vocab/' + name + '/*.md')

	for fname in files:
		print('[*] Writing intent ', fname)
		with open(fname) as infile:
			outfile.write("\n\n## " + name + ":" + os.path.basename(fname)[:-3] + "\n")
			outfile.write(infile.read())

if __name__ == "__main__":
    try:
        print("Creating `train.md` file.. ")
        create_vocab()
        print("`train.md` file ready!")

    except Exception as err:
        print("[ERROR] There was a problem building `train.md`. Error: ", err)