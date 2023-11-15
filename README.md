# test_wandb_launch_job
test launching job from git


# reproduce

reproduce the problem discussed in https://github.com/wandb/server/issues/132

1. create a new repository on github
 
2. git clone xxx.git

3. create a new python script `main.py`:
```python
import os
import wandb
import time

WORKSPACE = os.path.dirname(os.path.abspath(__file__))
if __name__=="__main__":
    wandb.init(project='TEST',name=time.strftime("%m%d_%H%M%S", time.localtime()))
    wandb.log({'seed':1111})
    wandb.finish()
    print(WORKSPACE)

```

4. create the requirements.txt:
```txt
wandb
```

5. push to the remote repo
```bash
git add -A && git commit -m "1111" && git push
```
6. check the commits
```bash
$ git log --pretty=oneline -10                         
eac27903bdcbb0afd7dd5a25e414adb3ff7feb30 (HEAD -> main, origin/main, origin/HEAD) 1111
68e8f2223b42ced01e6fe484803fcb67fd3d30d2 Initial commit
```
7. modified the main.py
```git
 WORKSPACE = os.path.dirname(os.path.abspath(__file__))
 if __name__=="__main__":
     wandb.init(project='TEST',name=time.strftime("%m%d_%H%M%S", time.localtime()))
-    wandb.log({'seed':1111})
+    wandb.log({'seed':2222})
     wandb.finish()
     print(WORKSPACE)
```
8. push to the remote repo
```bash
git add -A && git commit -m "2222" && git push
```

```bash
$ git log --pretty=oneline -10
8eb8f0482f538f8802138771ed27c4c078ba918e (HEAD -> main, origin/main, origin/HEAD) 2222
eac27903bdcbb0afd7dd5a25e414adb3ff7feb30 1111
68e8f2223b42ced01e6fe484803fcb67fd3d30d2 Initial commit
```
9. login wandb on my Macbook:
```bash
wandb login
```

10. run the command to start an agent for the existed GPU0 queue:
```bash
wandb launch-agent -e czm -q GPU0 --max-jobs=1
```

11. create a job from xxx.git and give the commit hash `eac27903bdcbb0afd7dd5a25e414adb3ff7feb30`:
```bash
$ wandb job create git https://github.com/zfhxi/test_wandb_launch_job --project="TEST"  \
    --entity="czm" --entry-point="main.py" --name="test_job1" --runtime=3 \
    --git-hash="eac27903bdcbb0afd7dd5a25e414adb3ff7feb30"

wandb: Creating launch job of type: git...
wandb: Using requirements.txt in /
wandb:                                                                                
wandb: Created job: czm/TEST/test_job1:v0, with alias: latest
wandb: View all jobs in project 'TEST' here: https://wandb.ai/czm/TEST/jobs
wandb: 
```
12. launch the job:

![06_01_52-1700028111598.png](https://img.idzc.top/picgoimg/2023/11/15/06_01_52-1700028111598.png)

13. checking the log from `wandb launch-agent -e czm -q GPU0`:
```log
wandb: Starting launch agent ✨                                                                                                                                                                          
wandb: launch: agent fsml111c polling on queues GPU0, running 0 out of a maximum of 1 jobs                                                                                                               
wandb: launch: agent fsml111c polling on queues GPU0, running 0 out of a maximum of 1 jobs                                                                                                               
wandb: launch: agent fsml111c polling on queues GPU0, running 0 out of a maximum of 1 jobs                                                                                                               
wandb: launch: Launch agent received job:                                                                                                                                                                
wandb: {'runQueueItemId': 'UnVuUXVldWVJdGVtOjQ3ODUwOTAzNg==',                                                                                                                                            
wandb:  'runSpec': {'_wandb_job_collection_id': 'QXJ0aWZhY3RDb2xsZWN0aW9uOjExNTg5Njc0OQ==',                                                                                                              
wandb:              'author': 'czm',                                                                                                                                                                     
wandb:              'entity': 'czm',                                                                                                                                                                     
wandb:              'job': 'czm/TEST/test_job1:latest',                                                                                                                                                  
wandb:              'overrides': {'args': [], 'entry_point': [], 'run_config': {}},                                                                                                                      
wandb:              'project': 'TEST',                                                              
wandb:              'resource': 'local-container',                                                  
wandb:              'resource_args': {'local-container': {}}}}                                      
wandb:                                            
wandb: launch: Launching job: czm/TEST/test_job1:latest                                             
wandb: launch: agent fsml111c running 1 out of a maximum of 1 jobs                                  
wandb:   2 of 2 files downloaded.                 
wandb: launch: Launching run in docker with command: docker run --rm -e WANDB_BASE_URL=https://api.wandb.ai -e WANDB_API_KEY -e WANDB_PROJECT=test -e WANDB_ENTITY=czm -e WANDB_LAUNCH=True -e WANDB_RUN_ID=xyq2rvbl -e WANDB_USERNAME=czm -e WANDB_LAUNCH_QUEUE_NAME=GPU0 -e WANDB_LAUNCH_QUEUE_ENTITY=czm -e WANDB_LAUNCH_TRACE_ID=UnVuUXVldWVJdGVtOjQ3ODUwOTAzNg== -e WANDB_CONFIG='{}' -e WANDB_ARTIFACTS='{"_wandb_job": "czm/TEST/test_job1:latest"}' czm__test__test_job1:bdca255b
wandb: Currently logged in as: czm. Use `wandb login --relogin` to force relogin                                                                                                                         
wandb: WARNING Project is ignored when running from wandb launch context. Ignored wandb.init() arg project when running running from launch.                                                             
wandb: Tracking run with wandb version 0.16.0                                                       
wandb: Run data is saved locally in /home/julian/wandb/run-20231115_060215-xyq2rvbl                                                                                                                      
wandb: Run `wandb offline` to turn off syncing.                                                     
wandb: Syncing run 1115_060214                    
wandb: ⭐️ View project at https://wandb.ai/czm/TEST                                                 
wandb: 🚀 View run at https://wandb.ai/czm/TEST/runs/xyq2rvbl                                       
wandb: launch: agent fsml111c running 1 out of a maximum of 1 jobs                                  
wandb:                                                                                                                                                                                                   
wandb:                                            
wandb: Run history:                               
wandb: seed ▁                                     
wandb:                                            
wandb: Run summary:                               
wandb: seed 2222                                  
wandb:                                            
wandb: 🚀 View run 1115_060214 at: https://wandb.ai/czm/TEST/runs/xyq2rvbl                          
wandb: ️⚡ View job at https://wandb.ai/czm/TEST/jobs/QXJ0aWZhY3RDb2xsZWN0aW9uOjExNTg5Njc0OQ==/version_details/v1 
wandb: Synced 4 W&B file(s), 0 media file(s), 2 artifact file(s) and 0 other file(s)                                                                                                                     
wandb: Find logs at: ./wandb/run-20231115_060215-xyq2rvbl/logs                                      
/home/julian                                      
wandb: launch: Job finished with ID: 80742                                                          
wandb: launch: agent fsml111c polling on queues GPU0, running 0 out of a maximum of 1 jobs                                                              
```

the L35 shows that the output seed is 2222. However, the expected output is 1111 for I passed the commit hash.