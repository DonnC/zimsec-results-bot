# automatically build the domain.yml file
import glob
import os
import ast
from os import path
from os.path import join

root_dir = path.dirname(__file__)
domain   = join(root_dir, "domain")
utters   = join(domain, "utterances")
action   = join(domain, "actions")

def writeSubFile(outfile, subfileName, spacer):
    with open(subfileName) as infile:
        for line in infile.readlines():
            outfile.write(spacer + line)

def intents(outfile):
    outfile.write("\n\nintents:\n")
    print("[INFO] Writing intents")
    writeSubFile(outfile, join(domain, "intents.yml"), "  ")

def entities(outfile):
    outfile.write("\n\nentities:\n")
    print("[INFO] Writing entities")
    writeSubFile(outfile, join(domain, "entities.yml"), "  ")

def slots(outfile):
    outfile.write("\n\nslots:\n")
    print("[INFO] Writing slots")
    writeSubFile(outfile, join(domain, "slots.yml"), "  ")

def templates(outfile):
    outfile.write("\n\ntemplates:")
    utterance_files = glob.glob(join(utters, "*.yml"))
    for fname in utterance_files:
        print("[INFO] Writing utterance: {}".format(fname))
        outfile.write("\n  utter_" + os.path.basename(fname)[:-4] + ":\n")
        writeSubFile(outfile, fname, "    ")

def actions(outfile):
    outfile.write("\n\nactions:")
    files = glob.glob(join(utters, "*.yml"))
    for fname in files:
        outfile.write("\n  - utter_" + os.path.basename(fname)[:-4])

    files = glob.glob(join(action, "*.py"))
    for fname in files:
        str = ""
        with open(fname) as infile:
            str = infile.read()

        p = ast.parse(str)
        classes = [node for node in ast.walk(p) if isinstance(node, ast.ClassDef)]
        for item in classes:
            if (item.bases[0].id == "Action") or (item.bases[0].id == "FormAction"):
                print("[INFO] Writing action: ", item.name)
                outfile.write("\n  - domain.actions."+ os.path.basename(fname)[:-3] + "." + item.name)

def build_domain():
    with open(join(domain, "domain.yml"), "w") as outfile:
        intents(outfile)
        entities(outfile)
        slots(outfile)
        templates(outfile)
        actions(outfile)

if __name__ == "__main__":
    try:
        print("[INFO] Creating `domain.yml` file...")
        build_domain()
        print("[INFO] `domain.yml` file ready!")

    except Exception as err:
        print("[ERROR] Failed to create `domain.yml`. Error: ", err)