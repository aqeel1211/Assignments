FROM alpine
RUN apk add python3 \
        py3-pip \
    && pip3 install --upgrade pip \
    && pip3 install \
        awscli
 
RUN aws --version
ENTRYPOINT [ "usr/bin/aws","configure" ]

#docker image build -t my-aws-cli .
#docker run -ti my-aws-cli