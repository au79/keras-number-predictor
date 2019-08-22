# keras-number-predictor
Basic Python Flask app in Docker which uses Keras to load a neural network model and predict handwritten numbers with it.

### Build application
Build the Docker image manually by cloning the Git repo.  Dependencies must be in a file at the project root, named `requirements.txt`.
```
$ git clone https://github.com/au79/keras-number-predictor.git
$ cd keras-number-predictor
$ docker build -t au79/keras-number-predictor .
```

### Run the container
Create a container from the image.  Bind mount your `app` directory t `/app` on the server.
```
$ docker run --name keras-number-predictor -d -p 5000:5000 -v "$(pwd)/app":/app au79/keras-number-predictor
```

Now visit http://localhost:5000
```
 The hostname of the container is 6095273a4e9b and its IP is 172.17.0.2. 
```

### Verify the running container
Verify by checking the container ip and hostname (ID):
```
$ docker inspect -f '{{range .NetworkSettings.Networks}}{{.IPAddress}}{{end}}' my-container
172.17.0.2
$ docker inspect -f '{{ .Config.Hostname }}' my-container
6095273a4e9b
```

### Live updates
Flask runs in development mode, any changes to files in the bind mount directory will trigger a server restart.

Note that the container must be rebuilt to pick up changes to dependencies in `requirements.txt`.
