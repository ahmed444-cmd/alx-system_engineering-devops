Here’s a rewritten version of your README file with a different structure and tone:

---

# 0x1A: Application Server Setup
##### DevOps SysAdmin

![c7d1ed0a2e10d1b4e9b3](https://github.com/samuelselasi/alx-system_engineering-devops/assets/85158665/2c883c9d-24a6-4d34-ac0b-e7fb86af802e)

## Overview
In this project, you'll extend your web infrastructure, initially set up with Nginx to serve static content, by integrating an application server. This step involves connecting Nginx to an application server to handle dynamic content, with a focus on serving your Airbnb clone project.

## Learning Resources
**Essential Readings and Videos**:
- [Application Server vs Web Server](https://www.nginx.com/resources/glossary/application-server-vs-web-server/)
- [Serving Flask with Gunicorn and Nginx on Ubuntu 16.04](https://www.digitalocean.com/community/tutorials/how-to-serve-flask-applications-with-gunicorn-and-nginx-on-ubuntu-16-04) (Note: Install Gunicorn globally, not within a virtualenv)
- [Gunicorn Documentation](https://docs.gunicorn.org/en/latest/run.html)
- [Flask Routing Details](https://werkzeug.palletsprojects.com/en/0.14.x/routing/) and [Flask Route Handling](https://flask.palletsprojects.com/en/1.0.x/api/#flask.Flask.route)
- [Upstart Documentation](https://doc.ubuntu-fr.org/upstart)

## Project Requirements
### General Guidelines
- Include a `README.md` file at the root of your project directory.
- Use Python 3 for all Python-related tasks.
- Ensure all configuration files are well-commented.

### Bash Scripts
- Scripts should be compatible with Ubuntu 16.04 LTS.
- End all files with a newline.
- Make all Bash scripts executable.
- Scripts must pass Shellcheck (version 0.3.7-5~ubuntu16.04.1 via `apt-get`) without errors.
- Start each script with `#!/usr/bin/env bash` and a comment describing its purpose.

## Tasks

### [0. Configure Development Environment](./README.md)
Set up your development environment to serve content from your [AirBnB clone v2 - Web framework](https://github.com/samuelselasi/AirBnB_clone_v2) on `web-01`. This involves:
- Completing [task #3](0x0B-ssh/README.md) of your [SSH project](../0x0B-ssh) for web-01.
- Installing `net-tools` on your server: `sudo apt install -y net-tools`.
- Cloning the AirBnB repository onto your server.
- Configuring `web_flask/0-hello_route.py` to serve content from `/airbnb-onepage/` on port 5000 with a Flask application named `app`.

**Example**:

##### Development Server:

```bash
ubuntu@229-web-01:~/AirBnB_clone_v2$ python3 -m web_flask.0-hello_route
 * Serving Flask app "0-hello_route" (lazy loading)
 * Environment: production
   WARNING: Do not use the development server in a production environment.
   Use a production WSGI server instead.
 * Debug mode: off
 * Running on http://0.0.0.0:5000/ (Press CTRL+C to quit)
35.231.193.217 - - [02/May/2019 22:19:42] "GET /airbnb-onepage/ HTTP/1.1" 200 -
```

##### Verify with Curl:

```bash
ubuntu@229-web-01:~/AirBnB_clone_v2$ curl 127.0.0.1:5000/airbnb-onepage/
Hello HBNB!
```

### [1. Configure Production Environment with Gunicorn](./README.md)
Prepare your production environment by installing Gunicorn and setting it up to serve your Flask application on port 5000. Ensure that:
- Gunicorn and necessary libraries are installed.
- The Flask app object is named `app`.
- Verify that Gunicorn serves content from the same route as the development setup and is bound to port 6000 for the checker.

**Example**:

##### Start Gunicorn:

```bash
ubuntu@229-web-01:~/AirBnB_clone_v2$ gunicorn --bind 0.0.0.0:5000 web_flask.0-hello_route:app
[2019-05-03 20:47:20 +0000] [3595] [INFO] Starting gunicorn 19.9.0
[2019-05-03 20:47:20 +0000] [3595] [INFO] Listening at: http://0.0.0.0:5000 (3595)
```

##### Verify with Curl:

```bash
ubuntu@229-web-01:~$ curl 127.0.0.1:5000/airbnb-onepage/
Hello HBNB!
```

### [2. Configure Nginx to Serve Your Page](./2-app_server-nginx_config)
Set up Nginx to serve the content from `/airbnb-onepage/`:
- Serve locally and on the public IP on port 80.
- Proxy requests to the Gunicorn process on port 5000.
- Include your Nginx configuration in `2-app_server-nginx_config`.

**Example**:

##### Local and Public Access:

```bash
# On server
ubuntu@229-web-01:~/AirBnB_clone_v2$ gunicorn --bind 0.0.0.0:5000 web_flask.0-hello_route:app

# Verify locally
ubuntu@229-web-01:~/AirBnB_clone_v2$ curl 127.0.0.1/airbnb-onepage/
Hello HBNB!

# Verify publicly
vagrant@ubuntu-xenial:~$ curl -sI 35.231.193.217/airbnb-onepage/
HTTP/1.1 200 OK
```

### [3. Add Route with Query Parameters](./3-app_server-nginx_config)
Expand your application by adding a route with query parameters:
- Configure Nginx to proxy requests from `/airbnb-dynamic/number_odd_or_even/<int:n>` to a Gunicorn instance on port 5001.
- Include your Nginx configuration in `3-app_server-nginx_config`.

**Example**:

##### Start Gunicorn Instances:

```bash
ubuntu@229-web-01:~/AirBnB_clone_v2$ tmux new-session -d 'gunicorn --bind 0.0.0.0:5000 web_flask.0-hello_route:app'
ubuntu@229-web-01:~/AirBnB_clone_v2$ tmux new-session -d 'gunicorn --bind 0.0.0.0:5001 web_flask.6-number_odd_or_even:app'
```

##### Verify with Curl:

```bash
ubuntu@229-web-01:~/AirBnB_clone_v2$ curl 127.0.0.1:5001/number_odd_or_even/6
<!DOCTYPE html><HTML lang="en"><HEAD><TITLE>HBNB</TITLE></HEAD><BODY><H1>Number: 6 is even</H1></BODY></HTML>
```

### [4. Configure API Endpoint](./4-app_server-nginx_config)
Serve your [AirBnB clone v3 - RESTful API](https://github.com/samuelselasi/AirBnB_clone_v3):
- Clone the repository and set up Nginx to proxy requests to Gunicorn on port 5002.
- Test the setup with the API endpoint `/api/v1/`.

**Example**:

##### Start Gunicorn for API:

```bash
ubuntu@229-web-01:~/AirBnB_clone_v3$ tmux new-session -d 'gunicorn --bind 0.0.0.0:5002 api.v1.app:app'
```

##### Verify with Curl:

```bash
ubuntu@229-web-01:~/AirBnB_clone_v3$ curl 127.0.0.1:5002/api/v1/states
[{"__class__":"State","created_at":"2019-05-10T00:39:27.032802","id":"7512f664-4951-4231-8de9-b18d940cc912","name":"California","updated_at":"2019-05-10T00:39:27.032965"}]
```

### [5. Serve AirBnB Clone with Nginx](./5-app_server-nginx_config)
Serve your [AirBnB clone - Web dynamic](https://github.com/samuelselasi/alx-system_engineering-devops) with Nginx:
- Clone `AirBnB_clone_v4` and configure Gunicorn to serve content from `web_dynamic/2-hbnb.py` on port 5003.
- Ensure Nginx serves static assets from `web_dynamic/static/` and verify that your site functions correctly.

**Example**:

##### Start Gunicorn for Dynamic Content:

```bash
ubuntu@229-web-01:~/AirBnB_clone_v4$ gunicorn --bind 0.0.0.0:5003 web_dynamic/2-hbnb:app
```

##### Verify with Browser:

- Check that your site loads correctly and that no errors appear

 in the logs.

## Debugging & Troubleshooting
- **Logs**: Check logs in `/var/log/nginx/` and `/var/log/gunicorn/`.
- **Firewall**: Ensure ports 80, 5000, 5001, 5002, and 5003 are open.
- **Nginx Status**: Use `systemctl status nginx` to check Nginx status.

## Contributing
Feel free to submit issues and pull requests to improve this repository. Your contributions help enhance the learning experience for others.

## License
This project is licensed under the MIT License. See `LICENSE` for details.

---
