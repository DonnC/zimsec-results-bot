#! /usr/local/bin/python3.6

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

import logging

from rasa_core.channels.console import ConsoleInputChannel
from rasa_core.agent import Agent
from rasa_core.policies.keras_policy import KerasPolicy
from rasa_core.policies.memoization import MemoizationPolicy
from rasa_core.interpreter import RasaNLUInterpreter
import warnings

# ignore warnings
warnings.filterwarnings(action='ignore', category=DeprecationWarning)
warnings.filterwarnings(action='ignore', category=FutureWarning)

logger = logging.getLogger(__name__)

def run_online(input_channel,
                    interpreter,
                    domain_def_file='domain/domain.yml',
                    training_data_file='data/stories.md',
                    ):

    agent = Agent(domain_def_file,
                  policies=[MemoizationPolicy(max_history=3), KerasPolicy()],
                  interpreter=interpreter)
    
    training_data = agent.load_data(training_data_file)
    agent.train_online(training_data,
                    input_channel=input_channel,
                    batch_size=50,
                    epochs=200,
                    max_training_samples=300)
    return agent

if __name__ == '__main__':
    try:
        print("[INFO] Running interactive training..\n")
        logging.basicConfig(level='INFO')
        nlu_interpreter = RasaNLUInterpreter('models/zimsec_bot/default/nlu')
        run_online(ConsoleInputChannel(), nlu_interpreter)

    except Exception as err:
        print("[ERROR] There was a problem: ", err)
