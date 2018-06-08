# updateSecurityGroup

So, this is a simple python script to update your favorite AWS security group with your new IP. 

You need the followings :

* An up-to-date ~/.aws/config file with your credentials
* Boto3 installed, ideally latest version


Then, from your terminal, just do:

~~~
  kharec@macbee ~/Desktop % path/to/updateSecurityGroup.py --id <YOUR_SECURITY_GROUP_ID>
~~~

And it's on.

You can also, like me, set it in a cron on a computer witch is always at home, in my case my raspberry (connected to my router). 
