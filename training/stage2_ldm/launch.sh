python main.py \
--base ./configs/ldm_training/diff_foley_train.yaml \
-t --name diff_foley_experiment  \
--gpus 0,1,2,3,4,5,6,7 \
--stage 2 \
--epoch 250 \
--wandb_project diff_foley \
--scale_lr False