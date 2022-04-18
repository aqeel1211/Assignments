# Description
How can you tell whether or not the ubuntu:16.4 image is signed for content trust?

#Answer

//Run docker trust inspect ubuntu:16.4
//if the image is signed for content trust,signed tags will appear in the //JSON
//if the image tag is unsigned or unavailable,there will be no signed tags