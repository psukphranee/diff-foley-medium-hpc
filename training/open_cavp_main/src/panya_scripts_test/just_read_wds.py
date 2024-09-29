import webdataset as wds

dataset = wds.WebDataset("/Users/920753844/Diff-Foley/video/goodarchive_1.tar")

sample = next(iter(dataset))

for k, v in sample.items():
    print("%20s = %s"%(k, repr(v)[:60]))