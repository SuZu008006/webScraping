start:
	python main.py

test:
	pip freeze > requirements.txt && pytest ./
