default:
	python src/main.py

package:
	buildid -n
	zip -r upsilon-alerter-$(shell buildid -k timestamp).zip src var

.PHONY: default package
