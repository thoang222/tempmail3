import docker, time

def build_image_from_dockerfile():
    client = docker.from_env()
    image, build_logs = client.images.build(path="./flask", dockerfile="Dockerfile", tag="flask")

    for log in build_logs:
        if 'stream' in log:
            print(log['stream'], end='')

    return image

def run_container(image, port, container_name):
    client = docker.from_env()
    
    # Thiết lập giá trị của biến môi trường PORT để chuyển đến container
    environment = {'PORT': port}
    
    ports = {'{0}/tcp'.format(port): port}
    
    # Thiết lập chính sách restart cho container
    restart_policy = {'Name': 'always'}

    container = client.containers.run(
        image,
        name=container_name,  # Đặt tên cho container
        ports=ports,
        detach=True,
        environment=environment,
        restart_policy=restart_policy
    )
    print(f'Container {container.name} is running on port {port} with restart policy set to "always"')

if __name__ == "__main__":
    docker_image = build_image_from_dockerfile()

    if docker_image:
        for i, port in enumerate(range(5000, 5006)):
            container_name = f"flask{i}"
            run_container(docker_image.tags[0], port, container_name)
    else:
        print("Failed to build Docker image.")
