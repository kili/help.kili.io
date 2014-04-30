Title: Importing keypairs
Date: 2014-04-16 14:00
Tags: instances, launching, how to
Slug: import_keypair
Author: James Nzomo
Summary: A "how to" on Importing a keypair

####INTRO

Keypairs are how you login to your instance after it is launched.

####Pre-requisites:-

1. Active login session


####Instructions

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
    * The Access & Security tab in the [launch instance](launch_an_instance.html) modal form.
    ![Access & Security Panel](https://raw.githubusercontent.com/dguitarbite/help.kili.io/master/content/img/Select_Access_Security.png "Access & Security Panel")
        + Click on Import Keypair button.
            ![Import Keypair](https://raw.githubusercontent.com/dguitarbite/help.kili.io/master/content/img/Import_Keypair.png "Import Keypair")
        + Keypair Details will be displayed as shown in the image below.
            ![Confirm Keypair Import](https://raw.githubusercontent.com/dguitarbite/help.kili.io/master/content/img/Import_Successful.png "Confirm Keypair Import")
3. Once your have your Import Keypair modal, provide a name you will recognise for the key and paste the contents of your public key file into the public key text field.
    ![Import Keypair while Launching Instance](https://raw.githubusercontent.com/dguitarbite/help.kili.io/master/content/img/instance_access_n_security.png)