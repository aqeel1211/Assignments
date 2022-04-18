# Description
Docker containers can be interesting to look around in.
You can save containers to a tar archive and then extract the layers and metadata files from them.
Note that exported containers look a little different from images that have been saved to an archive.

## Run instructions

Run an alpine container with an environment variable called tmpvar set to test.
//docker run -it -e tmpvar=test alpine sh
Export that alpine container to an archive, extract the contents of the archive.
//docker export -o alpine.tar <containerID>
// mkdir temp
//cd temp
//tar xvf ../alpine.tar
Do you see the same metadata files from the previous exercise?
//No
