build
	sudo docker buildx build --platform linux/amd64,linux/arm64 -t my-project --push .