# Makefile
IMAGE_NAME  := python-app
CONTAINER   := python-app-container
REQUIREMENTS := requirements.txt
HOST_PORT   := 5000
APP_PORT    := 5000

.PHONY: help build run serve shell stop clean rebuild install

help:
	@echo "Available targets:"
	@echo "  build    - Build the Docker image"
	@echo "  run      - Run container with \$$(pwd):/app volume (interactive bash)"
	@echo "  serve    - Run container and start the Flask server on port $(HOST_PORT)"
	@echo "  shell    - Open a bash shell inside the container"
	@echo "  stop     - Stop and remove the running container"
	@echo "  rebuild  - Rebuild image from scratch (no cache)"
	@echo "  install  - Install/update requirements inside container"
	@echo "  clean    - Remove image and container"

build:
	docker build -t $(IMAGE_NAME) .

# Interactive shell (no port needed)
run: build
	docker run -it --rm \
		--name $(CONTAINER) \
		-p $(HOST_PORT):$(APP_PORT) \
		-v $(shell pwd):/app \
		-w /app \
		$(IMAGE_NAME) bash

# One-shot server: exits with Ctrl+C
serve: build
	docker run -it --rm \
		--name $(CONTAINER) \
		-p $(HOST_PORT):$(APP_PORT) \
		-v $(shell pwd):/app \
		-w /app \
		$(IMAGE_NAME) \
		python3 manage.py runserver -h 0.0.0.0 -p $(APP_PORT)

shell: run

stop:
	-docker stop $(CONTAINER) 2>/dev/null || true
	-docker rm   $(CONTAINER) 2>/dev/null || true

rebuild:
	docker build --no-cache -t $(IMAGE_NAME) .

install: build
	docker run --rm \
		-v $(shell pwd):/app \
		-w /app \
		$(IMAGE_NAME) \
		pip3 install --break-system-packages -r $(REQUIREMENTS)

clean: stop
	-docker rmi $(IMAGE_NAME) 2>/dev/null || true
