#!/bin/bash
curl http://$WDA_SERVER_IP:$WDA_SERVER_PORT/status
python3 main.py
