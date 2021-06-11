PACKAGE_NAME ?= my-webhook

help:
	@echo "make"
	@echo "    package"
	@echo "        Package python code into a zip file using PACKAGE_NAME environment variable (default: my-webhook)."
	@echo "    deploy"
	@echo "        Deploy packaged python code to IBM cloud functions."

package:
	zip -r $(PACKAGE_NAME).zip .

deploy:
	ibmcloud fn action update $(PACKAGE_NAME) $(PACKAGE_NAME).zip --kind python:3.7 --main main --web yes