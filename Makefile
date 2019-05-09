

build:
	docker build -t opcua-challenge .

run:
	docker run -d -p 6666:22 -p "6100-6300":"6100-6300" --name savethefactory opcua-challenge

stop:
	docker stop savethefactory
	docker rm savethefactory


