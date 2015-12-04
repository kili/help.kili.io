Title: Setting up Command Line Tools
Date: 2014-04-26 18:00
Tags: instances, launching, CLI
Slug: setting_up_cli
Author: Pranav Salunke (dguitarbite)
Summary: Set up the command line tools in order to really leverage Kili to the max.

###INTRO
OpenStack command-line interface (CLI) tools and the OpenStack dashboard are two ways to access and use various services provided by OpenStack.

The command-line clients for OpenStack can be installed directly from the Python Package Index (PyPI) (https://pypi.python.org/). Using PyPI is recommended over distro specific versions as the clients are under heavy development. It is very likely at any given time that the version of the packages distributed by your operating-system vendor are out of date.

The "pip" utility is used to manage package installation from the PyPI archive and is available in the "python-pip" package in most Linux distributions. Each OpenStack project has its own client, so depending on which services your site runs, install some or all of the following packages:

    * python-novaclient (nova CLI)

    * python-glanceclient (glance CLI)

    * python-keystoneclient (keystone CLI)

    * python-cinderclient (cinder CLI)

    * python-swiftclient (swift CLI)

    * python-neutronclient (neutron CLI)


###Pre-requisites

1. Login Credentials
    * Username/Password
    * Endpoint URLs (RC/Credentials File)
2. Access to Terminal.
    * It is provided by default for Linux and Mac. For windows you may have to install PowerShell.


###Instructions

1.  Installing the Tools
    * To install (or upgrade) a package from the PyPI archive with pip, as root:

        `# pip install [--upgrade] <package-name>`

    * To remove a packages:

        `# pip uninstall <package-name>`

2. To get the Credentials:

    * Login to the OpenStack dashboard.
    * Select <a href="https://dash.kili.io/project/access_and_security/?tab=access_security_tabs__api_access_tab">Access and Security</a> tab by clicking on (`Project` &rarr; `Compute` &rarr; `Access & Security` &rarr; `API Access`)
    * Click on Download OpenStack RC File.

**Note:** OpenStack RC file will let you generate files that you can source in your shell to populate the environment variables the command-line tools require to know where your service endpoints and your authentication information are. The user you logged in to the dashboard dictates the filename for the openrc file, such as demo-openrc.sh.

This is how a typical RC file will look like.


    #!/bin/bash

    # With the addition of Keystone, to use an openstack cloud you should
    # authenticate against keystone, which returns a **Token** and **Service
    # Catalog**.  The catalog contains the endpoint for all services the
    # user/tenant has access to - including nova, glance, keystone, swift.
    #
    # *NOTE*: Using the 2.0 *auth api* does not mean that compute api is 2.0.  We
    # will use the 1.1 *compute api*
    export OS_AUTH_URL=https://api.kili.io/keystone/v2.0

    # With the addition of Keystone we have standardized on the term **tenant**
    # as the entity that owns the resources.
    export OS_TENANT_ID=66c2cf39ddd943ccba4f2dda0f6fdf1d
    export OS_TENANT_NAME="DemoProject"

    # In addition to the owning entity (tenant), openstack stores the entity
    # performing the action as the **user**.
    export OS_USERNAME="user@email.com"

    # With Keystone you pass the keystone password.
    echo "Please enter your OpenStack Password: "
    read -sr OS_PASSWORD_INPUT
    export OS_PASSWORD=$OS_PASSWORD_INPUT

**Note:** Password is not saved in plain text for security reasons. You will be prompted for password which will be stored in the environment variable OS_PASSWORD.

###Access Kili Cloud via. Terminal/Programs

Now you are ready to use OpenStack via. API. You should test it out using simple commands using your terminal. For more sophisticated usage, you can write a program in your favourite language and leverage the awesomeness of Kili cloud.

1. Test Run
Launch your terminal and follow the steps:
    * Install required OpenStack Python Clients
        `# pip install python-keystoneclient`
    * Source the Credentials file (<project-name>.sh) which was downloaded via Kili Dashboard.
        `$ source demo.sh`
    * Enter your password. Now you are ready to use Kili Cloud from your terminal.
    * Type the following command to ask Keystone for Catalog
        `$ keystone catalog`

**Note:** Keystone will reply to your query with list of Services and Endpoints offered by Kili Cloud. The Catalog returned by Keystone should look like this:

        Service: orchestration
        +-------------+--------------------------------------------------------------+
        |   Property  |                            Value                             |
        +-------------+--------------------------------------------------------------+
        |   adminURL  |   http://10.1.0.2:8004/v1/66c2cf39ddd943ccba4f2dda0f6fdf1d   |
        |      id     |               98e800b8fe3044da992b43cc7d561193               |
        | internalURL |   http://10.1.0.2:8004/v1/66c2cf39ddd943ccba4f2dda0f6fdf1d   |
        |  publicURL  | https://api.kili.io/heat/v1/66c2cf39ddd943ccba4f2dda0f6fdf1d |
        |    region   |                          RegionOne                           |
        +-------------+--------------------------------------------------------------+
        Service: metering
        +-------------+----------------------------------+
        |   Property  |              Value               |
        +-------------+----------------------------------+
        |   adminURL  |       http://10.1.0.2:8777       |
        |      id     | 3a15208c5a934457af084caa1a84274c |
        | internalURL |       http://10.1.0.2:8777       |
        |  publicURL  |  https://api.kili.io/ceilometer  |
        |    region   |            RegionOne             |
        +-------------+----------------------------------+
        Service: compute
        +-------------+--------------------------------------------------------------+
        |   Property  |                            Value                             |
        +-------------+--------------------------------------------------------------+
        |   adminURL  |   http://10.1.0.2:8774/v2/66c2cf39ddd943ccba4f2dda0f6fdf1d   |
        |      id     |               0c29b844bbad44ec9f83503312c705ad               |
        | internalURL |   http://10.1.0.2:8774/v2/66c2cf39ddd943ccba4f2dda0f6fdf1d   |
        |  publicURL  | https://api.kili.io/nova/v2/66c2cf39ddd943ccba4f2dda0f6fdf1d |
        |    region   |                          RegionOne                           |
        +-------------+--------------------------------------------------------------+
        Service: ec2
        +-------------+----------------------------------------+
        |   Property  |                 Value                  |
        +-------------+----------------------------------------+
        |   adminURL  |  http://10.1.0.2:8773/services/Admin   |
        |      id     |    08c8baa865aa4461a30cfb64e117bc98    |
        | internalURL |  http://10.1.0.2:8773/services/Cloud   |
        |  publicURL  | https://api.kili.io/ec2/services/Cloud |
        |    region   |               RegionOne                |
        +-------------+----------------------------------------+
        Service: image
        +-------------+----------------------------------+
        |   Property  |              Value               |
        +-------------+----------------------------------+
        |   adminURL  |       http://10.1.0.2:9292       |
        |      id     | 127fb3452f1d434e90fbe9cade523d02 |
        | internalURL |       http://10.1.0.2:9292       |
        |  publicURL  |    https://api.kili.io/glance    |
        |    region   |            RegionOne             |
        +-------------+----------------------------------+
        Service: network
        +-------------+----------------------------------+
        |   Property  |              Value               |
        +-------------+----------------------------------+
        |   adminURL  |       http://10.1.0.2:9696       |
        |      id     | 695672bb97104eea89f6b044a0ba3f5a |
        | internalURL |       http://10.1.0.2:9696       |
        |  publicURL  |   https://api.kili.io/neutron    |
        |    region   |            RegionOne             |
        +-------------+----------------------------------+
        Service: volumev2
        +-------------+----------------------------------------------------------------+
        |   Property  |                             Value                              |
        +-------------+----------------------------------------------------------------+
        |   adminURL  |    http://10.1.0.2:8776/v2/66c2cf39ddd943ccba4f2dda0f6fdf1d    |
        |      id     |                0a4d93aba2ef4051b265f9057ae86079                |
        | internalURL |    http://10.1.0.2:8776/v2/66c2cf39ddd943ccba4f2dda0f6fdf1d    |
        |  publicURL  | https://api.kili.io/v2/cinder/66c2cf39ddd943ccba4f2dda0f6fdf1d |
        |    region   |                           RegionOne                            |
        +-------------+----------------------------------------------------------------+
        Service: object-store
        +-------------+--------------------------------------------------------------------+
        |   Property  |                               Value                                |
        +-------------+--------------------------------------------------------------------+
        |   adminURL  |                      http://10.1.0.2:8888/v1                       |
        |      id     |                  4fd801c437d4454a9e96e7ad3b0a9bb7                  |
        | internalURL |   http://10.1.0.2:8888/v1/AUTH_66c2cf39ddd943ccba4f2dda0f6fdf1d    |
        |  publicURL  | https://api.kili.io/swift/v1/AUTH_66c2cf39ddd943ccba4f2dda0f6fdf1d |
        |    region   |                             RegionOne                              |
        +-------------+--------------------------------------------------------------------+
        Service: identity
        +-------------+-----------------------------------+
        |   Property  |               Value               |
        +-------------+-----------------------------------+
        |   adminURL  |     http://10.1.0.2:35357/v2.0    |
        |      id     |  0c1bed5e18504d03962c26d6af7a4871 |
        | internalURL |     http://10.1.0.2:5000/v2.0     |
        |  publicURL  | https://api.kili.io/keystone/v2.0 |
        |    region   |             RegionOne             |
        +-------------+-----------------------------------+
        Service: cloudformation
        +-------------+----------------------------------------------------------+
        |   Property  |                          Value                           |
        +-------------+----------------------------------------------------------+
        |   adminURL  | http://10.1.0.2:8004/v1/66c2cf39ddd943ccba4f2dda0f6fdf1d |
        |      id     |             117916db73cc477c9233976cb476aead             |
        | internalURL |                 http://10.1.0.2:8000/v1/                 |
        |  publicURL  |                https://api.kili.io/cfn/v1                |
        |    region   |                        RegionOne                         |
        +-------------+----------------------------------------------------------+
        Service: volume
        +-------------+----------------------------------------------------------------+
        |   Property  |                             Value                              |
        +-------------+----------------------------------------------------------------+
        |   adminURL  |    http://10.1.0.2:8776/v1/66c2cf39ddd943ccba4f2dda0f6fdf1d    |
        |      id     |                4fa25feb6b7643beb60ce721c857de34                |
        | internalURL |    http://10.1.0.2:8776/v1/66c2cf39ddd943ccba4f2dda0f6fdf1d    |
        |  publicURL  | https://api.kili.io/v1/cinder/66c2cf39ddd943ccba4f2dda0f6fdf1d |
        |    region   |                           RegionOne                            |
        +-------------+----------------------------------------------------------------+


Now you are ready to leverage the power of Open Source Cloud Kili which runs on OpenStack. You can import these client libraries inside your python modules to use them without any human interaction.
