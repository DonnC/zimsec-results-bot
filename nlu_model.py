#! /usr/local/bin/python3.6
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals
from pprint import pprint

from sys import argv

from rasa_nlu.training_data import load_data
from rasa_nlu import config
from rasa_nlu.model import Trainer, Interpreter
from rasa_core.interpreter import RasaNLUInterpreter
from rasa_core.agent import Agent

def train_nlu(train_data, config_data, model_dir):
    training_data = load_data(train_data)
    trainer = Trainer(config.load(config_data))
    trainer.train(training_data)
    model_directory = trainer.persist(model_dir, fixed_model_name="nlu")

    # return model_directory

def run_nlu():
    parse_query = "22/7/2002"                   # put any of your entity to see some stats, here its candindateBirth

    print("[INFO] Interpreting query: ", parse_query.upper())

    interpreter = Interpreter.load('./models/zimsec_bot/default/nlu')
    pprint(interpreter.parse(parse_query))

if __name__ == '__main__':
    try:
        data = argv[1]
        if data:
            if data == "train":
                print("[INFO] Training..")
                train_nlu('data/train.md', 'config_spacy.yml', './models/zimsec_bot')

            elif data == "run":
                print("[INFO] Running..")
                run_nlu()

            else:
                print("[ERROR] Indicate if u want to `run` or `train` via `sys.argv`")

        else:
            print("[ERROR] Indicate if u want to `run` or `train` via `sys.argv`")

    except Exception as err:
        print("[ERROR] Indicate if u want to `run` or `train` via `sys.argv`")