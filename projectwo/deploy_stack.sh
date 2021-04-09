#!/bin/bash
scp -i ~/.ssh/ansible_id_rsa docker-compose.yaml jenkins@manager-node:/home/ayona/prizegenerator/projectwo/docker-compose.yaml
scp -i ~/.ssh/ansible_id_rsa jenkins@manager-node << EOF
    export DATABASE_URI=${DATABASE_URI}
    export SECRET_KEY=${SECRET_KEY}
    docker stack deploy --compose-file /home/ayona/prizegenerator/projectwo/docker-compose.yaml projectwo
EOF
