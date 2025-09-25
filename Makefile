.PHONY: build run test benchmark logs stop clean deploy

build:
	docker-compose build

run:
	docker-compose up -d

stop:
	docker-compose down

logs:
	docker-compose logs -f gaia-core

test:
	python3 gaia_v67.py --mode test

benchmark:
	python3 gaia_v67.py --mode benchmark --cycles 1000

clean:
	docker-compose down -v
	rm -rf data/*

deploy: build
	docker-compose up -d
	@echo "✅ GAIA déployé - API: http://localhost:8000 - Grafana: http://localhost:3000"