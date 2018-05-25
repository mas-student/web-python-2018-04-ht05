default:
# 	echo hello.py:1 1>&2
	pgrep flask && pkill flask || echo NOT
# 	FLASK_APP=hello.py flask run &
	FLASK_APP=hello.py ~/.virtualenvs/web-python-2018-04-ht01/bin/flask run &
#	epiphany http://127.0.0.1:5000/products
	firefox http://127.0.0.1:5000/products
