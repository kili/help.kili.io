Title: Preparing an Image for use on the Kili Cloud
Date: 2014-08-24 14:00
Tags: images, how to
Slug: Creating_an_Image 
Author: James Nzomo
Summary: A "how to" on creating or preparing existing images for 

###INTRO
This help article will illustrate how to prepare an existing image for use on Kili.

###Prerequisites

1. A kili account
2. For amd64 images, a cpu with virtualization extensions 
Intel VT or AMD-V. VIA VT may also work.

###Getting an image
An image is a virtual disk file with an operating system pre-installed on it. 
You can either download one from the many image providers out there or 
create one using virtualization software such as virtualbox or lib-virt.

The Kili Cloud uses qemu-KVM as it's hypervisor. This means that you will 
get better compatibility by using qcow2 as your image format.
You may also choose to go with raw disk format if you prefer performance 
over other features such as copy on write.
Using qemu also makes it possible for you to run images created for non-x86 
architectures (PPC, ARM, SPARK, MIPS...etc) on Kili.

If your virtualization app does not support qcow2, you can convert its native
image type to qcow2 using the 
[qemu-img convert command](http://docs.openstack.org/image-guide/content/ch_converting.html) before uploading.

###Cloud init
Before you can import your image to the cloud, it would be a good idea to 
install cloud-init on it. 
From [readthedocs](http://cloudinit.readthedocs.org/en/latest/), "Cloud-init 
is the de-facto multi-distribution package that handles early initialization 
of a cloud instance." Early initialization involves preparing instances during
boot up for use on the cloud.  
From the [Official OpenStack docs](http://docs.openstack.org/image-guide/
content/ch_openstack_images.html), 
some of these preparations involve:-

- Adding your public key (ssh) to the default user's authorized_keys
- Disk Partitioning and resizing
- Handling user-submitted data such as host-names
- Setting repositories

You can configure some of the above by editing `/etc/cloud/cloud.cfg`. 
For an example, with repositories, feel free to use the following 
as your primary mirrors:-

- Ubuntu (http://mirror.internal.ke-nbo-1a.kili.io/ubuntu/), 
- Debian (http://mirror.internal.ke-nbo-1a.kili.io/debian/)
- and CentOS (http://mirror.internal.ke-nbo-1a.kili.io/centos/)

You can set them as shown in the cloud-init 
[apt-repo example](http://cloudinit.readthedocs.org/en/latest/topics/examples.html#add-apt-repositories) 
and the [yum-repo example](http://cloudinit.readthedocs.org/en/latest/topics/examples.html#adding-a-yum-repository) 

###The Boot log 
It will also be a good idea for your instances to boot verbosely 
by writing the boot log to the console. If you are building a Linux 
image, edit your `/boot/grub/grub.cfg` to pass the `console=ttyS0` 
parameter to your kernel and set `GRUB_CMDLINE_LINUX_DEFAULT="console=ttyS0"` 
in your `/etc/default/grub`file.  
Update your grub configuration by running `update-grub` for debian-based distros or `grub2-mkconfig -o /boot/grub2/grub.cfg` for fedora-based distros.

###Uploading your image
To upload your image via the dashboard, visit this url :- 
https://dash.kili.io/project/images/create/ (login if you are prompted to), 
set the appropriate options and submit.   

To upload your image from the command line, see 
[setting up cli tools](setting_up_cli.html) for installing and 
configuring python-glanceclient for use with your account.  

Here is an example of how to add an image from the cli:-

    glance image-create --name "Image name" --disk-format qcow2 --container-format bare --min-disk 30 --min-ram 2048 --file IMAGENAME.qcow2 --is-public False

The above command that adds a qcow2 image for an instance that requires 
a minimum of 2GB for ram and 30 GB for root as a private image 
(no sharing with other kili tenants).  
Specifying these requirements facilitates forcing the right flavors when 
spinning up an instance from the image.

###Further reading

- http://cloudinit.readthedocs.org/en/latest/
- http://docs.openstack.org/image-guide/content/ch_obtaining_images.html
