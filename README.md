TASK-1

Instruction to run playbook, in creating Ec2 instance and to list the instance using python script
Step 1: In AWS management console

Step 2: Go to IAM. 
-	Create a new role and provide the Ec2 Access
-	Create a new user and download the credentials file

Step 3: Go to Ec2
-	Create a new Ec2 instance 
-	Login into the putty using ssh keys

Step 4: In the Linux server,
-	Write YAML playbook and save it as Filename.YAML
-	Write python script and save it as Filename.py

Prerequisites to run the above playbook and the filename 
  In the server,
-	 Run the below commands to run above files

      o	sudo yum update
      o	sudo yum install python-pip
      o	pip –version
      o	pip list
      o	sudo pip install boto3
      o	sudo pip install boto
      o	sudo pip install ansible

-	Configure the IAM credential details and check the same in .aws folder

      o	aws configure	

           	Please access key ID and secret access key	
-	Configure the below files to run playbook

      o	Create a static host file or use dynamic inventory to get connect with slave machine
      o	Get the ansible.cfg  file from the below path

           	sudo wget https://raw.githubusercontent.com/ansible/ansible/devel/examples/ansible.cfg

      o	Run the playbook with below command

          	ansible-playbook -i host.txt -m filename.yaml

-	Run the python script as per the below command to list the instance running in AWS console

      o	python filename.py


 
