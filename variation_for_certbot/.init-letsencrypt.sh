#!/bin/bash

domains=(juhoyoun.com www.juhoyoun.com)
data_path="/home/certbot/"
email="juho.youn.work@gmail.com" 


docker run --rm \
  -p 443:443 -p 80:80 --name letsencrypt \
  -v "$data_path/conf:/etc/letsencrypt" \
  -v "$data_path/lib/var:/var/lib/letsencrypt" \
  certbot/certbot certonly -n \
  -m $email \
  -d $domains  \
  --standalone --agree-tos