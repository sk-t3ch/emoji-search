ARG FUNCTION_DIR="/home/app/"
ARG RUNTIME_VERSION="3.7"
ARG DISTRO_VERSION="3.12"

FROM python:${RUNTIME_VERSION}-slim AS build-image

RUN python${RUNTIME_VERSION} -m pip install numpy scikit-learn 

ARG FUNCTION_DIR
ARG RUNTIME_VERSION
RUN mkdir -p ${FUNCTION_DIR}

COPY ./requirements.txt ${FUNCTION_DIR}
RUN python${RUNTIME_VERSION} -m pip install -r ${FUNCTION_DIR}/requirements.txt --target ${FUNCTION_DIR}
RUN python${RUNTIME_VERSION} -m pip install awslambdaric --target ${FUNCTION_DIR}

ARG FUNCTION_DIR
WORKDIR ${FUNCTION_DIR}
ADD https://github.com/aws/aws-lambda-runtime-interface-emulator/releases/latest/download/aws-lambda-rie /usr/bin/aws-lambda-rie
RUN chmod 755 /usr/bin/aws-lambda-rie

COPY . ${FUNCTION_DIR}

COPY entry.sh /
ENTRYPOINT [ "/entry.sh" ]
CMD [ "main_lambda.handler" ]