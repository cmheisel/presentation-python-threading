.venv:
	virtualenv ./venv
	./venv/bin/pip install -r requirements.txt

run: .venv
	./venv/bin/python sequential.py
	./venv/bin/python threaded-naive.py
	./venv/bin/python threaded.py
	./venv/bin/python async.py
