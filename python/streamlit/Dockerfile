FROM python:3.7
LABEL maintainer "pyx7b"

# Install sudo
RUN apt-get update && \
    apt-get install -y sudo && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

#Install python packages
COPY requirements.txt /root/requirements.txt
RUN pip install -r /root/requirements.txt


#Setup app user
RUN useradd -m -u 1000 -s /bin/bash app && \
echo 'app ALL=(ALL) NOPASSWD:ALL' >> /etc/sudoers && \
chown -R app /home/app
ENV HOME /home/app
WORKDIR /home/app
USER app

EXPOSE 8501

#ENTRYPOINT ["python"]
CMD ["/bin/bash"]
