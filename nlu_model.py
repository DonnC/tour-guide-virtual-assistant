#! /usr/local/bin/python3.6
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

from rasa_nlu.training_data import load_data
from rasa_nlu import config
from rasa_nlu.model import Trainer, Interpreter
from rasa_core.interpreter import RasaNLUInterpreter
from rasa_core.agent import Agent
from os import path

root_dir = path.dirname(__file__)

def train_nlu(train_data, config_data, model_dir):
    training_data = load_data(train_data)
    trainer = Trainer(config.load(config_data))
    trainer.train(training_data)
    model_directory = trainer.persist(model_dir, fixed_model_name="nlu")

    # return model_directory

def run_nlu():
    interpreter = Interpreter.load('./models/tour_guide/default/nlu')
    print(interpreter.parse("How can i get to the Admnistration building?"))

if __name__ == '__main__':
    train_nlu('data/train.md', 'config_spacy.yml', './models/tour_guide')
    #run_nlu()