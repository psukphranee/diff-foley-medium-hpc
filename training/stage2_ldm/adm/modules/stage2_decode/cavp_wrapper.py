import torch
import torch.nn as nn



import pytorch_lightning as pl


import importlib

from torch.optim.lr_scheduler import LambdaLR


def disabled_train(self, mode=True):
    """Overwrite model.train with this function to make sure train/eval mode
    does not change anymore."""
    return self

def get_obj_from_str(string, reload=False):
    module, cls = string.rsplit(".", 1)
    if reload:
        module_imp = importlib.import_module(module)
        importlib.reload(module_imp)
    return getattr(importlib.import_module(module, package=None), cls)


def instantiate_from_config(config):
    if not "target" in config:
        if config == '__is_first_stage__':
            return None
        elif config == "__is_unconditional__":
            return None
        raise KeyError("Expected key `target` to instantiate.")
    return get_obj_from_str(config["target"])(**config.get("params", dict()))


class Encoder_Wrapper(pl.LightningModule):

    def __init__(self,
                 first_stage_config,
                 decoder_config,
                 scheduler_config,
                 monitor,
                 first_stage_ckpt=None,
                 first_stage_key="spec",
                 normalize = True,
                 avg = False,
                 pool = False,
                 lossconfig = None,
                 *args, **kwargs):
    
        super().__init__()

        self.instantiate_first_stage(first_stage_config)
        self.first_stage_ckpt = first_stage_ckpt
        if self.first_stage_ckpt is not None:
            self.init_first_from_ckpt(self.first_stage_ckpt)

        # self.model = instantiate_from_config(decoder_config)

        self.mse_loss = torch.nn.MSELoss()
        self.first_stage_key = first_stage_key
        self.monitor = monitor
        self.normalize = normalize
        self.avg = avg
        self.pool = pool

        self.use_scheduler = scheduler_config is not None
        if self.use_scheduler:
            self.scheduler_config = scheduler_config
        
        if lossconfig:
            self.loss = instantiate_from_config(lossconfig)


    def instantiate_first_stage(self, config):
        model = instantiate_from_config(config)
        self.first_stage_model = model.eval()
        self.first_stage_model.train = disabled_train
        for param in self.first_stage_model.parameters():
            param.requires_grad = False
    
    def init_first_from_ckpt(self, path):
        model = torch.load(path, map_location="cpu")
        # 12.1.24 Panya: Loaded model from checkpoint in decode_wrapper.py
        print("Panya: Loaded model from checkpoint in decode_wrapper.py")
        if "state_dict" in list(model.keys()):
            model = model["state_dict"]
        # Remove: module prefix
        new_model = {}
        for key in model.keys():
            new_key = key.replace("module.","")
            new_model[new_key] = model[key]
        missing, unexpected = self.first_stage_model.load_state_dict(new_model, strict=False)
        print(f"Restored from {path} with {len(missing)} missing and {len(unexpected)} unexpected keys")
        if len(missing) > 0:
            print(f"Missing Keys: {missing}")
        if len(unexpected) > 0:
            print(f"Unexpected Keys: {unexpected}")

    def forward(self, x):
         
        x_rec = self.model(x)
        
        return x_rec
    