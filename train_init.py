#! /usr/local/bin/python3.6
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

import logging

from rasa_core.agent import Agent
from rasa_core.policies.keras_policy import KerasPolicy
from rasa_core.policies.memoization import MemoizationPolicy

def train_dialogue(domain_file="domain/domain.yml", model_path="models/dialogue", training_data_file="data/stories.md"):

    agent = Agent(domain_file, policies=[MemoizationPolicy(max_history=3), KerasPolicy()])

    training_data = agent.load_data(training_data_file)

    agent.train(
        training_data,
        epochs = 500,
        batch_size = 100,
        validation_split = 0.2
    )

    agent.persist(model_path)

if __name__ == '__main__':
    try:
        print("[INFO] Running dialogue training..\n")
        logging.basicConfig(level='INFO')
        train_dialogue()

    except Exception as err:
        print("[ERROR] There was a problem training dialogue: ", err)
