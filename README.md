# raspberry_pi_website
Instructions for turning your raspberry pi into a web server

[Documentation](https://jameskabbes.github.io/raspberry_pi_website)


# Reference

## Service Location
`sudo nano /etc/systemd/system/<service_name>.service`

## Reverse Proxy

Caddy
https://caddyserver.com/

Is a reverse proxy that can dispatch http request inbound to port 80 and 443 to other servers running on your pi.

The configuration for it can be viewed / changed here:
```
sudo vim /etc/caddy/Caddyfile
```

And after you edit it, you need to restart / reload Caddy like. This is the same as any other systemd service.
```
sudo systemctl reload caddy
# OR
sudo systemctl restart caddy
```

You can view the logs of Caddy like any other systemd service, with the journalctl command
```
sudo journalctl -f -u caddy
```

## Adding New Service

sudo nano /etc/systemd/system/<filename>.service
sudo systemctl enable personal_blog.service

sudo nano /etc/systemd/system/personal_blog.service

chmod a+x run_live_server.sh

## Service Template

Found in `notes/template.service`

## Restarting Service
sudo systemctl start <service>
sudo systemctl stop <service>

## See Service Logs
sudo journalctl -f -u <service>

## See Service Status
sudo systemctl status <service>


# Author
James Kabbes