import os
import wandb
import time

WORKSPACE = os.path.dirname(os.path.abspath(__file__))
if __name__=="__main__":
    wandb.init(project='TEST',name=time.strftime("%m%d_%H%M%S", time.localtime()))
    wandb.log({'seed':2222})
    wandb.finish()
    print(WORKSPACE)