import random
sentences = []
with open("/u/scr/mhahn/PRETRAINED/GLUE/glue_data/SST-2/dev.tsv", "r") as inFile:
  header = next(inFile) # for the header
  assert header == "sentence\tlabel\n"
#  next(inFile)
  for line in inFile:
     line = line.strip().split("\t")
     if len(line) < 2:
       continue
     assert len(line) == 2
     sentences.append(line[0])
random.shuffle(sentences)

with open("PROCESSED_TEXT/SST2_valid.txt", "w") as outFile:
   for s in sentences:
      print(s+"\n", file=outFile)

