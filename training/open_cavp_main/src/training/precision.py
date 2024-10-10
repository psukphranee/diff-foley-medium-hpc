import torch
from contextlib import suppress


def get_autocast(precision):
    if precision == 'amp':
        # Panya 10.9.24 Change this per warning
        #return torch.cuda.amp.autocast
        return torch.amp.autocast("cuda")
    elif precision == 'amp_bfloat16' or precision == 'amp_bf16':
        # amp_bfloat16 is more stable than amp float16 for clip training
        # Panya (10.9.24) Comment out original : return lambda: torch.cuda.amp.autocast(dtype=torch.bfloat16)
        return lambda: torch.amp.autocast("cuda", dtype=torch.bfloat16)
    else:
        return suppress
