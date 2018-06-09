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

You can also, like me, set it in a cron on a computer which is always at home, in my case my raspberry (connected to my router).

**Please note that** the used service [ipinfo.io](https://ipinfo.io) supports 1000 requests a day in the free plan. So don't plan your cron every minutes. There's 1440 minutes in a day. That's silly.

At the best, plan it every 2 minutes but I do not advise that. Every five minutes is fine.