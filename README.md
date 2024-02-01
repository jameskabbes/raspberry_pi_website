# raspberry_pi_website

Instructions for turning your raspberry pi into a web server. This guide is enough to get started, but not each step is completely detailed.

# Setup

## Caddy

[https://caddyserver.com/]() <br>
Open-source web server with automatic https written in Go.

1. Make a new `caddy.service` file, like the template shown in the repo.
2. Add the `caddy.service` file as a system service.
3. Enable the service to run on startup

### Edit Caddyfile

```
sudo nano /etc/caddy/Caddyfile
```

Use `Caddyfile` template in repo to edit `etc/caddy/Caddyfile`

## ufw

Uncomplicated Firewall

Make sure the ports that your websites are running on are allowed

### install

`sudo apt-get install --reinstall ufw`

### edit ufw ports

`sudo nano /etc/default/ufw`

```
# Allow incoming traffic on specific ports
sudo ufw allow 80     # HTTP
sudo ufw allow 443    # HTTPS
sudo ufw allow 8083   # Custom application on port 8083

# Optionally, if you're using SSH, allow SSH traffic
sudo ufw allow 22     # SSH
```

## Flask Web Server

### Make Virtual Environment

`python -m venv venv`
`source venv/bin/activate`
`pip install -r requirements.txt`

### Gunicorn

[https://gunicorn.org]() <br>

`gunicorn -b 0.0.0.0:{PORT} wsgi:app`

### Service

1. Use `flask_app.service` template in the repo to make a service for the application
2. Change `WorkingDirectory` to repository directory
3. Change `Environment` to be the location of the virtual environment bin: `./venv/bin`
4. Change path and port found in the `ExecStart`
5. Add service, enable the service on startup

# Handy Commands

```
sudo systemctl stop <service>
```

```
sudo systemctl start <service>
```

```
sudo systemctl restart <service>
```

```
sudo journalctl -f -u <service>
```

## Adding New Service

`sudo ln -s /path/to/<service>.service /etc/systemd/system/<service>.service`

## Enabling the Service on bootup

`sudo ln -s /path/to/<service>.service /etc/systemd/system/multi-user.target.wants/<service>.service`
