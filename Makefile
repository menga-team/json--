all:
	@echo "run \'make install' to install menga-lang tools"

install:
	cp jcc /usr/local/bin
	cp jcc_interpreter.py /usr/local/bin

uninstall:
	-rm -f /usr/local/bin/jcc
	-rm -f /usr/local/bin/jcc_interpreter.py