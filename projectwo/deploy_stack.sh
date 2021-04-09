#!/bin/bash
scp -i ~/.ssh/ansible_id_rsa docker-compose.yaml jenkins@manager-node:docker-compose.yaml
ssh -i ~/.ssh/ansible_id_rsa jenkins@manager-node << EOF
    export DATABASE_URI=${DATABASE_URI}
    export SECRET_KEY=${SECRET_KEY}
    python3 create.py
    docker stack deploy --compose-file docker-compose.yaml projectwo
EOF
