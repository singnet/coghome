if [ "$#" -ne 1 ]
then
echo "Usage: run_in_docker.sh <your-python-script>"
exit 1
fi

docker run --name test_coghome -it -v $PWD:/run  singularitynet/opencog-dev:cli bash -c "sudo pip install websockets;cd; cp -r /run ./; cd run ; python3 $1"
docker cp test_coghome:/home/opencog/run/opencog.log .
docker cp test_coghome:/home/opencog/run/known_entity_ids.txt .
docker rm test_coghome

