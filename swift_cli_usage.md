Title: Working with object storage (swift) from the CLI
Date: 2014-08-24 14:00
Tags: swift, how to
Slug: swift_cli_usage 
Author: James Nzomo
Summary: A "how to" on working with the Kili Cloud object storage service (swift) from the CLI

###INTRO
This help article will illustrate how to work with the Kili Cloud object storage service (swift) from the CLI.

###Prerequisites

1. A kili account
2. Basic knowledge of unix terminal 


###Installation
We recommend installing the swift client (and all other python packages) via 
[pip](http://en.wikipedia.org/wiki/Pip_(package_manager)). You can also install 
the swift client from your distro's software repositories but chances are 
that it will be out of date.  

    pip install python-swiftclient

###Authentication
We use Keystone - The official OpenStack Identity Service - for 
authentication. For swift client to authenticate to your account, you have to 
install the keystone client.  

    pip install python-keystoneclient

To facilitate authentication, we provide you with an rc script that the swift 
client will use to access your account. 
[Click here](https://dash.kili.io/project/access_and_security/api_access/openrc/) 
to save it (login if prompted).  
Once saved, run `source XXX-openrc.sh` and enter your kili password when prompted.  

Test if it works by running `swift stat` which will print your account summary, that looks like what we have below.
  

           Account: AUTH_XXXXXXXXXXXXXXXXXXXXXXXX
        Containers: 0
           Objects: 0
             Bytes: 0
     Accept-Ranges: bytes
            Server: nginx/1.4.7
        Connection: keep-alive
       X-Timestamp: 123456789123.123456
        X-Trans-Id: XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
      ContenType: text/plain; charset=utf-8

###Commands
Swift client provides 6 sub-commands that you you use to manage your data. 
From the [official swift client documentation](http://docs.openstack.org/user-guide/content/swift_commands.html), they are:-

- `stat` - Displays information for the account, container, or object.
- `list` - Lists the containers for the account or the objects for a container.
- `post` - Updates meta information for the account, container, or object.
- `upload` - Uploads files or directories to the given container.
- `download` - Download objects from containers.
- `delete` - Delete a container or objects within a container.

You can also run `swift help` for more. 

###Working with containers
Containers are name spaces used to group objects in an account. You can choose to 
create them as private, for 'internal' use, or as public, to share content over
network or the INTERNET.  

Usage examples:-   
`swift post CONTAINER_NAME` creates a container with the name `CONTAINER_NAME`.  
`swift list` prints out a list of your containers.  
`swift stat CONTAINER_NAME` prints out a summary of an existing container called `CONTAINER_NAME`.  
`swift delete CONTAINER_NAME` deletes an existing container called `CONTAINER_NAME`.  


###Working with objects
Objects are the actual data stored in swift. You can think of them as files on a 
conventional file system. These could be your documents, photos, videos, music, 
disk image snapshots, log files.....the list goes on.  

Usage examples:-   
`swift upload CONTAINER_NAME foo.jpg` uploads a file `foo.jpg` to an existing container. 
For larger files such as disk images, you may want to upload in chunks by passing an 
extra parameter `-S CHUNK_SIZE`.  
`swift stat CONTAINER_NAME foo.jpg` prints out info on a previously uploaded object 
`foo.jpg` inside an existing container.  
`swift list CONTAINER_NAME` prints a list of objects in the named container.  


###Further reading

- https://wiki.openstack.org/wiki/Swift
- http://docs.openstack.org/user-guide/content/swift_commands.html
- http://docs.openstack.org/developer/swift/
- http://nairobilug.or.ke/2014/07/swiftclient-openstack.html
