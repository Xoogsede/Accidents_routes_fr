function rech_ip {
    # votre code ici
    result=docker inspect -f '{{.NetworkSettings.IPAddress}}' $*
}

rech_ip "app-neo4j_db-1"
export VARIABLE_ENV="$result"