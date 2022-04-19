# Description
How can you tell whether or not the ubuntu:16.4 image is signed for content trust?

# Solution

Run the following command

    docker trust inspect ubuntu:16.4
If the image is signed for content trust,signed tags will appear in the JSON

If the image tag is unsigned or unavailable,there will be no signed tags
