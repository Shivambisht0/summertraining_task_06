import os
def awsservies():
    #To check the version of AWS CLI  
    os.system("aws --version")
    #To launch the instance in Mumbai region in the first av
    os.system("aws ec2 run-instances --image-id ami-0ad704c126371a549  --instance-type t2.micro --count 1 --subnet-id subnet-010be16a  --security-group-ids sg-78777b05 --key-name shivamkey1")
    os.system("aws ec2 create-volume --availability-zone ap-south-1a --size 5")
    os.system("aws ec2 attach-volume --volume-id vol-0d9930f180d23f0f9 --instance-id i-00bb4ac8c7a7c8bbb --device xvdh")
