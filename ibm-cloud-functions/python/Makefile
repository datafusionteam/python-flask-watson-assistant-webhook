PACKAGE_NAME ?= my-webhook

package:
	zip -r $(PACKAGE_NAME).zip .

deploy:
	ibmcloud fn action update $(PACKAGE_NAME) $(PACKAGE_NAME).zip --kind python:3.7 --main main --web yes