FROM jupyter/pyspark-notebook:31b807ec9e83

ENV JUPYTER_ENABLE_LAB=yes

USER root

ENV DEBIAN_FRONTEND=noninteractive
RUN apt-get update \
    && apt-get -y install --no-install-recommends apt-utils 2>&1

RUN apt-get -y install git procps lsb-release

RUN apt-get install -y libicu[0-9][0-9]

RUN mkdir /workspace
WORKDIR /workspace

COPY ./conda_dependencies.yml /workspace/conda_dependencies.yml

RUN conda env create -f /workspace/conda_dependencies.yml

ENV CONDANAME "aibootcamp"
ENV CONDATYPE "conda"
ENV PYTHONVERSION "3.7"

RUN echo "source activate $CONDANAME" > ~/.bashrc
ENV PATH /opt/$CONDATYPE/envs/$CONDANAME/bin:$PATH

RUN /opt/$CONDATYPE/envs/$CONDANAME/bin/python$PYTHONVERSION -m ipykernel install --name $CONDANAME --display-name "$CONDANAME"