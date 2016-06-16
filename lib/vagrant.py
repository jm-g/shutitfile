CONFIG vagrant_version 1.8.1
CONFIG_SECRET your_sudo_password

STORE_RUN processor uname -p
INSTALL wget

IF INSTALL_TYPE apt
	RUN wget -qO- https://releases.hashicorp.com/vagrant/{{ shutit.vagrant_version }}/vagrant_{{ shutit.vagrant_version }}_{{ shutit.processor }}.deb > /tmp/vagrant.deb
	RUN sudo dpkg -i /tmp/vagrant.deb
	EXPECT_MULTI ['assword={{ shutit.your_sudo_password }}']
	RUN rm -f /tmp/vagrant.deb
ELIF INSTALL_TYPE yum
	RUN wget -qO- https://releases.hashicorp.com/vagrant/{{ shutit.vagrant_version }}/vagrant_{{ shutit.vagrant_version }}_{{ shutit.processor }}.rpm > /tmp/vagrant.rpm
	RUN sudo rpm -i /tmp/vagrant.rpm
	EXPECT_MULTI ['assword={{ shutit.your_sudo_password }}']
	RUN rm -f /tmp/vagrant.rpm
ELSE
	INSTALL vagrant


# Is it installed already?
ISINSTALLED_BEGIN
	RUN vagrant
ISINSTALLED_END

