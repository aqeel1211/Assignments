# Description
How can you quickly and succinctly determine the image id and created date for an Alpine image?

## Run instructions
//docker inspect -f '{{ .Created }}: {{ .ID }}'  alpine
