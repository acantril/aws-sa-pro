
# USERDATA TEMPLATE

Apply the Userdata template
Note that when it completes the instance isn't yet in a functional state?
Wait 5 minutes
Try again ...now it works
We simulated a lengthy bootstrapping process with a `Sleep 300` statement in the userdata
An instance reports to CFN that it's `ready` long before lengthy userdata processes complete

# UPDATE STACK

Notice the test on the webpage of the instance ....
Update the stack, same template, change parameters
Change the Message parameter
Apply update
Notice the instance restarts.... `update with disruption`
Does the message change? if not, why ?
Userdata is not reapplied after instance launch by default.

# Two problems
# 1) the disconnect between the bootstrapping process and CREATE_COMPLETE
# 2) Instance configuration not updating when the stack is Updated


# SIGNAL TEMPLATE

Apply the Userdata with Signal Template
Follow the same process
Notice how this time it takes longer for the stack to move into CREATE_COMPLETE ?
the `Instance` logical resource has a creation policy
it expects a signal within 15 minutes
Notice how in the userdata, the last line is `cfn-signal` which references the Stack, Region and Logical resource Name
This explicitly signals CloudFormation when the bootstrapping has been completed
The stack only moves to `CREATE_COMPLETE` when this process has finished

# CFNINIT & SIGNAL TEMPLATE

Apply the CFNINIT Template
Wait for it to complete
Connect to the instance via EC2 Instance Connect
Look at /var/log/cfn-init-* logs
Look at /var/log/cloud-init-* logs

# CFNINIT & SIGNAL & CFNHUP Stack
Apply the CFNHUP Template
Wait for it to complete
Connect to the instance via EC2 Instance Connect
Run `tail -f /var/log/cfn-hup.log`
Update stack, same template, change the message parameter
Apply Update
Monitor the log






