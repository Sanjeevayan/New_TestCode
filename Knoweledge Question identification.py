
from nltk import word_tokenize,sent_tokenize,pos_tag
def tagText(str):

    tokens = word_tokenize(str)
    lowercase_tokens= [word.lower()for word in tokens]
    taggedsents = [pos_tag(t)for t in lowercase_tokens]

    return taggedsents


print (tagText("How to install required software in my laptop?"))


************************

import nltk
from nltk import word_tokenize,sent_tokenize
# knowledge_question = "How to raise a service ticket"

#non_knowledge question = "What is status of my service ticket no: 123"
#failed_case= "How to know the status of my ticket"
#failed_case= "How to raise a ticket for an incident"
q_words = ["who","what","where"]
q_symbols = ["?"]
non_knowledge_words = ["service request","incident","status update"]
input = "How to raise an incident?"
tokens = nltk.word_tokenize(input)
token_list =[]
for token in tokens:
   token_list.append(token)
print (token_list)
Flag = False
for item in tokens:
    if tokens[0]=="where" and tokens[-1]=="?":
        Flag = True
        if (Flag == False):
            print (" Knowledge Question")
    else:
        print ("Not  a Knowledge Question")