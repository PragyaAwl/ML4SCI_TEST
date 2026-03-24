Due to the presence of interactive widgets in my jupyternb, I was facing issues in uploading the files to github without losing their states.  
Hence, Please visit the following collab links to work about the same.
1. Heart segmentation model (U-Net implementation nb)
https://colab.research.google.com/drive/1RSPRT_brdSZJO2h40jYZOAnsFyD9maKH?usp=sharing
2. CAC segmentation model (ResU-Net implementation nb)
https://colab.research.google.com/drive/1KLvt5I8_UvhT48QWxqNwTxZbUhDJZH8i?usp=sharing


Below are the links to the model weights and dataset in Google drive:(200 epochs):  
https://drive.google.com/file/d/1TAkw4doq8RGOlTskRG3adIcn_7EW_kvQ/view?usp=sharing  

Link to the dataset drive:  
https://drive.google.com/drive/folders/124ZmfsQZld3REH09pTFTk2-RAzzRw0MJ?usp=sharing  

The link contains the following data:  
a. data_resampled: Contains the ground truths(generated using TotalSegmentator)+resampled CT Scans+ segmentation ground truths of CAC. However out of 69 scans only 35 have the heart segmentation ground truths.  
b. hearmask_ids.json: Contains the list of the 35 scans that have the heart masks. It gets updated everytime, I get inference made from totalsegmenatator on some new scan  
c. heartmask_unet_best.pth: Weights and bias file from intital 15 epochs.  
d. heartmask_v2_unet_best.pth: Weights and bias files from the final 200 epochs.  
