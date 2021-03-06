from train import train_start,train_endgame
from tournament import round_robin_split
from durak_models import VEmbed_full
import sys
sys.setrecursionlimit(10000)

#train and then tournament and repeat
#also for hyperparameter training
#also for training vs previous model iterations
#To do threshold update, update threshold value and recall train_start?

#training params
iterations = 20
model_checkpoint = 12500
threshold = 50
model_names = [VEmbed_full]
load_tree = True
verbosity = 0
initialize_models = True
attacking_model_path = '/Users/Shuza/Code/Durak/attack_models/attack_model500'
defending_model_path = '/Users/Shuza/Code/Durak/defend_models/defend_model500'
model_paths = [attacking_model_path,defending_model_path]
#instantiate dictionary
initialization_params = {
    'iterations':iterations,
    'model_checkpoint':model_checkpoint,
    'threshold':threshold,
    'model_names':model_names,
    'load_tree':load_tree,
    'verbosity':verbosity,
    'model_paths':model_paths,
    'initialize_models':initialize_models
}

train_start(initialization_params)
#round_robin_split()
