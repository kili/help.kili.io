Title: Backing up your data (snapshot and download)
Date: 2015-12-03 12:00
Tags: glance, swift, snapshot, backup, how to
Slug: snapshot_and_download
Author: James Nzomo
Summary: A "how to" on retrieving your data in preparation for Kili Cloud suspension.

###INTRO
This is a step by step guide on how to retrieve your data (volume and instance snapshots) for migration to a different cloud provider.  
This is only necessary if you require the entire volume(s). Feel free to be more surgical and [ [mysql](https://dev.mysql.com/doc/refman/5.7/en/mysqldump.html) | [pg_](http://www.postgresql.org/docs/current/static/app-pg-dumpall.html) ]dump then [scp](https://en.wikipedia.org/wiki/Secure_copy) or [rsync](https://en.wikipedia.org/wiki/Rsync) the data out of your instances or mounted volumes.  

###Step 1
Visit <a href="https://dash.kili.io/project/instances/" target="_blank">Instances Dashboard</a> and create a snapshot of the instance you'd like to back up, specify a snapshot name, click "create snapshot". Give it time to complete.

###Step 1.5
Visit <a href="https://dash.kili.io/project/volumes/" target="_blank">Volumes Dashboard</a> and do the same as above for your volume(s). (Snapshot action is in the "more" menu for each row to the far right).

###Step 2
Make sure you have the glance client installed (preferably via [pip](https://pip.pypa.io/en/latest/installing/)):-

    pip install python-glanceclient

###Step 3
[CTRL-Click here to Download Your OpenStack RC Credentials File](https://dash.kili.io/project/access_and_security/api_access/openrc/) and [source](https://en.wikipedia.org/wiki/Source_(command)) it. If you are on windows, look at the env vars therein and set them manually.  


###Step 4
Find the snapshot you need

    glance --os-image-api-version 2 image-list

    +--------------------------------------+-------------------------------+-------------+------------------+------------+--------+
    | ID                                   | Name                          | Disk Format | Container Format | Size       | Status |
    +--------------------------------------+-------------------------------+-------------+------------------+------------+--------+

    ----- Output Truncated -----

    | 0ec56a99-b713-4d4c-b3de-6219890857dc | Your_Snapshot                | qcow2       | bare             | 7591559168 | active |

    ----- Output Truncated -----

    +--------------------------------------+-------------------------------+-------------+------------------+------------+--------+


###Step 5
Download your snapshot. Repeat for all the snapshots you have/need.

    you@your-host:~# glance --os-image-api-version 2 image-download 0ec56a99-b713-4d4c-b3de-6219890857dc --progress --file Your_Snapshot.img
    [=============================>] 100%

##In conclusion
Once you've successfully accomplished the above, you can then upload (and mount) your snapshots on most other cloud providers out there that support [QCOW2](http://www.linux-kvm.org/page/Qcow2) format images.
For swift/object storage backup, see [swift_cli_usage](swift_cli_usage)
