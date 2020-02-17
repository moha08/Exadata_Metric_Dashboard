FROM centos:7
RUN yum update -y
RUN yum install -y wget
RUN mkdir /etc/prometheus
RUN cd /etc/prometheus
RUN wget https://github.com/prometheus/prometheus/releases/download/v2.16.0/prometheus-2.16.0.linux-amd64.tar.gz
RUN tar -xvzf prometheus-2.16.0.linux-amd64.tar.gz
RUN mv prometheus-2.16.0.linux-amd64 prometheus
ADD   prometheus.yaml /etc/prometheus/
ADD grafana.repo /etc/yum.repos.d/
RUN yum install grafana -y
EXPOSE 9090
EXPOSE 3000
CMD ["/prometheus/prometheus", "--config.file=/etc/prometheus/prometheus.yaml"]
