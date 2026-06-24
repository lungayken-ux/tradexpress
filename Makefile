# Add this to your Makefile
run-dashboard:
	@echo "Launching Dashboard..."
	./venv/bin/streamlit run src/dashboard.py

clean-db:
	rm wellken.db
	@echo "Database wiped."
