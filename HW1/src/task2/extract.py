import PyPDF2
from os import path, listdir, getcwd
import numpy as np

def read_pdfs(path, files):
	data_size = len(files)
	train_indicies = (np.random.randint(10, size=(data_size))>3)
	while (train_indicies.sum() < data_size*.8):
		train_indicies[np.random.randint(data_size)] = True
	
	
	files_content1 = []
	files_content2 = []
	i=-1
	for the_file in files:
		i+=1
		if the_file[-3:]!='pdf':
	    		continue
		pdfFileObj = open(path+the_file, 'rb')
		pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
		file_content = ""
		for page_ind,page in enumerate(range(pdfReader.numPages)):
			pageObj = pdfReader.getPage(page_ind)
			page_content = pageObj.extractText()
			file_content += page_content
		if  train_indicies[i]==True:
			files_content1.append(file_content)
		else:
			files_content2.append(file_content)
		pdfFileObj.close()
	return files_content1, files_content2, train_indicies



def extract_words():
	dataset_directory = 'data/LinkedIn/'
	files = listdir(dataset_directory)


	train_docs, test_docs, train_indicies = read_pdfs(dataset_directory, files)
	
	sum_out = open("sum_train.txt","w")
	exp_out = open("exp_train.txt","w")
	edu_out = open("edu_train.txt","w")
	
	for document in train_docs:
		sum_b = document.find('\nSummary\n')
		exp_b = document.find('\nExperience\n')
		edu_b = document.find('\nEducation\n')
		
		sum_out.write(document[sum_b:exp_b]+"\n")
		exp_out.write(document[exp_b:edu_b]+"\n")
		edu_out.write(document[edu_b:]+"\n")
	
	sum_out.close()
	exp_out.close()
	edu_out.close()

	sum_out = open("sum_test.txt","w")
	exp_out = open("exp_test.txt","w")
	edu_out = open("edu_test.txt","w")
	
	for document in test_docs:
		sum_b = document.find('\nSummary\n')
		exp_b = document.find('\nExperience\n')
		edu_b = document.find('\nEducation\n')
		
		sum_out.write(document[sum_b:exp_b]+"\n")
		exp_out.write(document[exp_b:edu_b]+"\n")
		edu_out.write(document[edu_b:]+"\n")
	
	sum_out.close()
	exp_out.close()
	edu_out.close()
	return train_indicies
