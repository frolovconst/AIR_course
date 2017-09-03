import xml.etree.ElementTree as ET
import re

def get_topics(doc,pos):
    topic_start = doc.find("<TOPICS>",pos)
    topics_end = doc.find("</TOPICS>",pos)
    topics = doc[topic_start+8:topics_end]
    topics = topics.replace("</D><D>"," ")
    topics = topics.replace("<D>","")
    topics = topics.replace("</D>","")
    return topics.split()

def get_terms_with_counts(doc,pos):
    def get_document_words(document):
        return list(filter(lambda x: x!= '', re.split(r"[^A-Z,a-z,0-9]", document.lower().replace(","," "))))

    text_start = doc.find("<BODY>",pos)
    text_end = doc.find("</BODY>",pos)
    text = doc[text_start+6:text_end]
    tokens = get_document_words(text)
    return tokens

def add_to_voc(voc,tokens):
    for token in tokens:
        if token in voc:
            voc[token] += 1
        else:
            voc[token] = 1
    return voc


def read_data():

    dataset = {}
    voc = dict()

    files = ['reut2-000.sgm']

    for i,flnm in enumerate(files):
        with open(flnm, 'r') as content_file:
            inf = content_file.read()
            seek_pos = 0

            while seek_pos != -1:
                doc_end = inf.find("</REUTERS>",seek_pos)
                topics = get_topics(inf,seek_pos)
                tokens = get_terms_with_counts(inf,seek_pos)

                add_to_voc(voc,tokens)

                for topic in topics:
                    if topic in dataset:
                        dataset[topic] = add_to_voc(dataset[topic],tokens)
                    else:
                        dataset[topic] = add_to_voc(dict(),tokens)

                seek_pos = inf.find("<REUTERS TOPICS=\"YES\"",doc_end)
    return dataset,voc

def get_vocabulary(dataset):
    voc = {}
    print (len(dataset))
    for topic in dataset:
        print(len(voc))
        unique = set(dataset[topic])
        for token in unique:
            if token in voc:
                voc[token] += dataset[topic].count(token)
            else:
                voc[token] = dataset[topic].count(token)
    return voc
