.PHONY: all install uninstall

install:
	install -D -m 0755 data/xreader.service /etc/systemd/system/xreader.service

uninstall:
	rm -f /etc/systemd/system/xreader.service