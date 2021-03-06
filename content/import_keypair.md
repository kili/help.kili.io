Title: Importing keypairs
Date: 2014-04-16 14:00
Tags: instances, launching, how to
Slug: import_keypair
Author: James Nzomo
Summary: Uploading your public key is a necessary step to getting ssh access to your instances.  This is a far more secure method of authentication than password-based auth and is the only method enabled by default.

###INTRO
Key-based authentication is the most secure way to gain access to your Kili instance (provided you keep your private key under lock and key).<br>
The others are password based and kerberos based SSH authentication which are disabled by default on the production images we provide for you.<br>
This article will illustrate how to generate SSH Keys and import the resultant public key into your kili account when launching an instance and thereafter, allowing you to gain access to your new VM. 

###Pre-requisites:-

1. Active login session


###Instructions

1. If you do not have a keypair, generate one on:-
    * Posix (Mac/Linux) by :-
        - Running ssh-keygen -t rsa
        - Enter key location (leave blank for bracketed default)
        - Enter a passphrase and confirm
    * Windows using [PuTTY](http://www.chiark.greenend.org.uk/~sgtatham/putty/download.html) by:-
        - Running puttygen.exe
        - Click generate and fill the progress bar by moving the cursor over the blank area to generate random characters.
        - Enter a passphrase in the Key passphrase field and confirm the same in the respective field.
        - Save the public and private keys in a safe location.

2. On the dashboard, open the launch Instance modal from either:-
    * The <a href="https://dash.kili.io/project/access_and_security/" target="_blank">access and security panel</a> (`Project` &rarr; `Compute` &rarr; `Access & Security`) by clicking "Import keypair" button at the top right of the panel.
    * The Access & Security tab in the [launch instance](launch_an_instance.html) modal form.<br>
        <br><img src="img/Select_Access_Security.png" alt="Access & Security Panel" height="2500" width="673"></img><br><br>
        + Click on Import Keypair button.<br>
            <br><img src="img/Import_Keypair.png" alt="Import Keypair" height="500" width="462"></img><br><br>
        + Keypair Details will be displayed as shown in the image below.<br>
            <br><img src="img/Import_Successful.png" alt="Confirm Keypair Import" height="2500" width="675"></img><br>
3. Once your have your Import Keypair modal, provide a name you will recognise for the key and paste the contents of your public key file into the public key text field.<br>
    <br><img src="img/instance_access_n_security.png" alt="Import/Select Keypair" height="1500" width="658"></img><br>
