# Makefile
.PHONY: sync-db build-docs deploy

sync-db:
	@echo "Syncing Database Schema..."
	python3 scripts/generate_schema.py > docs/schema.md

build-docs:
	mkdocs build --clean

deploy: sync-db build-docs
	@echo "Pipeline complete: Database synced and documentation built."
