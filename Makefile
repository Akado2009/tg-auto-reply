NAME = 'tg-auto-reply'
DOCKERFILE = 'Dockerfile'
DOCKER=docker

PYTHON=python

build:
	$(DOCKER) build -f $(DOCKERFILE) -t $(NAME) . 

run:
	$(PYTHON) main.py