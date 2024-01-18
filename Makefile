install:
	pip install --upgrade pip &&\
	pip install -r requirements.txt

lint:
	pylint --disable=R,C *.py

test:
	python -m pytest -vv --cov=hello Practical_MLOps\Ch1\test_hello.py
