FROM centos:7

RUN yum install epel-release -y
ADD http://repos.upsilon-project.co.uk/upsilon-rpm-el7/upsilon-rpm-el7.repo /etc/yum.repos.d/
ADD RPMS/noarch/upsilon-reactor.rpm /opt/
RUN yum localinstall /opt/upsilon-reactor.rpm -y

ENTRYPOINT /usr/share/upsilon-reactor/main.py
