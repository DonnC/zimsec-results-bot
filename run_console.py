from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

import logging

from rasa_core.agent import Agent
from rasa_core.channels.console import ConsoleInputChannel
from rasa_core.interpreter import RegexInterpreter
from rasa_core.policies.keras_policy import KerasPolicy
from rasa_core.policies.memoization import MemoizationPolicy
from rasa_core.interpreter import RasaNLUInterpreter
import warnings

warnings.filterwarnings(action='ignore', category=DeprecationWarning)

logger = logging.getLogger(__name__)


def train_dialogue(domain_file = 'domain/domain.yml',
					model_path = './models/dialogue',
					training_data_file = './data/stories.md'):

	agent = Agent(domain_file, policies = [MemoizationPolicy(), KerasPolicy()])

	agent.train(
				training_data_file,
				epochs = 300,
				batch_size = 50,
				validation_split = 0.2)

	agent.persist(model_path)
	return agent

def run_bot(serve_forever=True):
	interpreter = RasaNLUInterpreter('./models/zimsec_bot/default/nlu')
	agent = Agent.load('./models/dialogue', interpreter = interpreter)

	if serve_forever:
		agent.handle_channel(ConsoleInputChannel())

	return agent

if __name__ == '__main__':
	try:
		print("[INFO] Running bot on CMD channel..\n")
		print("-" * 20 + " running pre-training " + "-" * 20 + "\n")
		train_dialogue()
		print("\n")
		print("-" * 20 + " running bot " + "-" * 20 + "\n")
		run_bot()

	except Exception as err:
		print("[ERROR] There was a problem: ", err)
