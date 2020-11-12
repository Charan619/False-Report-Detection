from os import listdir
from os.path import isfile, join
fout = open('data_opspam_neg_truthful_fold5.txt','w')
mypath='F:/DataScience/NLP/op_spam_v1.4/negative_polarity/truthful_from_Web/fold5/'
onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]
for i in onlyfiles:
  # location = 'F:/DataScience/NLP/deception_dataset/restaurant/deceptive_MTurk/'+str(i)+'.txt'
  # print(i)
  file = open(mypath+i,'r')
  for each in file:
    fout.write(each)
  file.close()
fout.close()