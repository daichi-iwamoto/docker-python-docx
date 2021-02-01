FROM centos:8

RUN yum update -y && yum clean all

# Apache install
RUN yum install -y httpd

# Python install
RUN yum install -y python3
RUN yum install -y epel-release
RUN yum install -y python3-pip --enablerepo=epel
RUN pip3 install --upgrade pip

# python-dox install
RUN pip3 install mammoth
RUN pip3 install beautifulsoup4
RUN pip3 install html5lib

EXPOSE 80

# Apache start
CMD ["/usr/sbin/httpd","-D","FOREGROUND"]