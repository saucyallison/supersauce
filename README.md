I created this for maximum convenience for using the Sauce Labs REST API. Commands are designed to be short and memorable - to update the job name of your most recent job:

supersauce.name('latest', name)
supersauce.name('l', name)
supersauce.update(full-job-url, name)
supersauce.update('latest', name="name")

Delete a job:

supersauce.delete(jobid)

Delete the most recent 20 jobs:

supersauce.delete(20)

supersauce.activity('awilbur')
getactivity

tunnels('awilbur')
tunnel('awilbur')
tunnel(tunnelid) (check if input is 32 chars with a-f0-9)

LAZYMODE:

import supersauce as ss
ss.n('l', name) # update latest job's name



A job can be referred to by:
- jobID
- 'latest-N' (Nth latest job)

A group of jobs can be referred to by:
- a number (N most recent jobs)# supersauce
