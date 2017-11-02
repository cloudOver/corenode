all:
	echo Nothing to compile

install:
	mkdir -p $(DESTDIR)/etc/corenode/
	cp -r config/* $(DESTDIR)/etc/corenode/

	mkdir -p $(DESTDIR)/usr/sbin/
	cp -r sbin/* $(DESTDIR)/usr/sbin

	mkdir -p $(DESTDIR)/var/lib/cloudOver/node/
	mkdir -p $(DESTDIR)/var/log/cloudOver/node/

	mkdir -p $(DESTDIR)/etc/libvirt/hooks/
	cp cloudover_hook.py $(DESTDIR)/etc/libvirt/hooks/cloudOver
	cp qemu_hook.sh $(DESTDIR)/etc/libvirt/hooks/qemu
	cp lxc_hook.sh $(DESTDIR)/etc/libvirt/hooks/lxc
	cp network_hook.sh $(DESTDIR)/etc/libvirt/hooks/network
	echo -n "version='" > $(DESTDIR)/etc/corenode/version.py
	cat debian/changelog | head -n 1 | cut -d ' ' -f 2 | sed -e 's/(//g' -e 's/)//g' | tr -d '\n' >> $(DESTDIR)/etc/corenode/version.py
	echo "'" >> $(DESTDIR)/etc/corenode/version.py

	chmod a+x $(DESTDIR)/etc/libvirt/hooks/lxc
	chmod a+x $(DESTDIR)/etc/libvirt/hooks/qemu
	chmod a+x $(DESTDIR)/etc/libvirt/hooks/network
	chmod a+x $(DESTDIR)/etc/libvirt/hooks/cloudOver

	mkdir -p $(DESTDIR)/etc/sudoers.d/
	echo "cloudover ALL=NOPASSWD: /etc/libvirt/hooks/cloudOver" >> $(DESTDIR)/etc/sudoers.d/corenode
	mkdir -p $(DESTDIR)/etc/nginx/sites-enabled/
	ln -s /etc/corenode/nginx/cloudinit $(DESTDIR)/etc/nginx/sites-enabled/cloudinit

	python setup.py install --root=$(DESTDIR)

egg:
	python setup.py sdist bdist_egg

egg_install:
	python setup.py install

egg_upload:
	# python setup.py sdist bdist_egg upload
	python setup.py sdist upload
egg_clean:
	rm -rf build/ dist/ corenode.egg-info/ corenode.egg-info/
