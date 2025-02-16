install:
	sudo apt install imagemagick

test:
	export PYTHONPATH="${PYTHONPATH}:/home/ramon/Projects/spinorama/src"
	pytest -v tests	
