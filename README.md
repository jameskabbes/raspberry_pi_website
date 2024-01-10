# raspberry_pi_website

Instructions for turning your raspberry pi into a web server

# Reference Materials

## Caddy

[https://caddyserver.com/]() <br>
Open-source web server with automatic https written in Go.

### Usage

Caddy's configuration can be viewed / changed here:

```
sudo nano /etc/caddy/Caddyfile
```

And after you edit it, you need to restart / reload Caddy like. This is the same as any other systemd service.

```
sudo systemctl restart caddy
```

You can view the logs of Caddy like any other systemd service, with the journalctl command

```
sudo journalctl -f -u caddy
```

### Hosting a Static Site

www.website.com {
encode zstd gzip
try_files {path} /
root \* /path/to/app/dist/folder
file_server
}

### Reverse Proxy to Localhost

www.website.com {
encode zstd gzip
reverse_proxy localhost:8080
}

## Raspberry Pi systemd service

### Template

Found in `notes/template.service`

### Restarting Service

sudo systemctl start <service>
sudo systemctl stop <service>

### See Service Logs

sudo journalctl -f -u <service>

### See Service Status

sudo systemctl status <service>

### Adding New Service

sudo ln -s /path/to/<service>.service /etc/systemd/system/<service>.service

### Enabling the Service on bootup

sudo ln -s /path/to/<service>.service /etc/systemd/system/multi-user.target.wants/<service>.service

## Python Web Server

### Make Virtual Environment

`python -m venv venv`
`source venv/bin/activate`
`pip install -r requirements.txt`

### Gunicorn

[https://gunicorn.org]() <br>

`gunicorn -b 0.0.0.0:8080 wsgi:app`

# Author

James Kabbes
