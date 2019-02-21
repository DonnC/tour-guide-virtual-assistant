.PHONY: clean train-nlu train-core cmdline server

TEST_PATH=./

clean:
	find . -name '*.pyc' -exec rm -f {} +
	find . -name '*.pyo' -exec rm -f {} +
	find . -name '*~' -exec rm -f  {} +
	rm -rf build/
	rm -rf dist/
	rm -rf *.egg-info
	rm -rf docs/_build

train-nlu:
	python3.6 nlu_model.py

train-init:
	python3.6 train_init.py

train-online:
    python3.6 train_online.py

cmdline:
	python3.6 -m rasa_core.run -d models/dialogue -u models/tour_guide/default/nlu
