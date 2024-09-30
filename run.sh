docker stop promptfoo_container
docker rm promptfoo_container
docker run  --name promptfoo_container -p 3000:3000 -v ./local_promptfoo:/root/.promptfoo ghcr.io/promptfoo/promptfoo:main


