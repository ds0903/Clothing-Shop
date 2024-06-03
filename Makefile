.PHONY: run
run:
	python Clothing_shop\manage.py runserver
	

.PHONY: check
check:
	python -m ruff . && python -m black --check . && python -m isort --check .

.PHONY: fix
fix:
	python -m black . && python -m isort .