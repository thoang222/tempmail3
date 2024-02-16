import docker

def build_image_from_dockerfile():
    client = docker.from_env()
    image, build_logs = client.images.build(path="./flask", dockerfile="Dockerfile", tag="flask")

    for log in build_logs:
        if 'stream' in log:
            print(log['stream'], end='')

    return image

def run_container(image, port):
    client = docker.from_env()
    
    # Thiết lập giá trị của biến môi trường PORT để chuyển đến container
    environment = {'PORT': port}
    
    ports = {'{0}/tcp'.format(port): port}
    container = client.containers.run(image, ports=ports, detach=True, environment=environment)
    print(f'Container {container.id} is running on port {port}')

if __name__ == "__main__":
    docker_image = build_image_from_dockerfile()

    if docker_image:
        for port in range(5000, 5006):
            run_container(docker_image.tags[0], port)
    else:
        print("Failed to build Docker image.")