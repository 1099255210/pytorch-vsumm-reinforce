'''
This is used to check what is inside those h5 dataset and result.h5.
'''

'''
result.h5
'''
# import h5py
# f = h5py.File('./log/summe-split0/result.h5', 'r')
# lst = list(f.keys())
# print(lst)

# vid1 = f['video_16']
# print(vid1.keys())
# sum1 = vid1['machine_summary']
# print(sum1)

# for it in list(vid1.keys()):
#   ds = vid1[it]
#   print(it)
#   print(ds.value)



'''
raw datasets.
'''
import h5py
f = h5py.File('./datasets/eccv16_dataset_summe_google_pool5.h5', 'r')
lst = list(f.keys())
print(lst)

vid1 = f['video_16']
print(vid1.keys())

for it in list(vid1.keys()):
  ds = vid1[it]
  print(it)
  print(ds.value)