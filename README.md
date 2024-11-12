This repo creates Opensearch Cluster based on folowing documentation
https://opensearch.org/blog/getting-started-with-fluent-bit-and-opensearch/
https://opensearch.org/docs/latest/install-and-configure/install-opensearch/docker/
# Instalation
  1. Change password in .env file and app/fluent-bit.conf
  2. Import .env as environment varialbe
  3. Run ```docker compose up --build```
  4. Connect to http://localhost:5601/
