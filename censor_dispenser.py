# These are the emails you will be censoring. The open() function is opening the text file that the emails are contained in and the .read() method is allowing us to save their contexts to the following variables:
email_one = open("email_one.txt", "r").read()
email_two = open("email_two.txt", "r").read()
email_three = open("email_three.txt", "r").read()
email_four = open("email_four.txt", "r").read()

def censor_word(words , text):
    censored_email = text.replace(words , 'REDACTED')
    return censored_email

#print(email_one)
#print(censor_word('learning algorithms' , email_one))

censor_these = ['herself' , 'Herself' , 'she' , 'She' , 'personality matrix' , 'sense of self' , 'self-preservation' , 'learning algorithms' , 'her' , 'Her']

def censor_list(word_list , text):
    for i in word_list:
        censored_email = text.replace(i , 'REDACTED')
        text = censored_email
    return censored_email


#print(email_two)
#print(censor_list(censor_these , email_two))

negative_words = ["dangerous", "alarming", "alarmed", "out of control", "help", "unhappy", "bad", "upset", "awful", "broken", "damage", "damaging", "dismal", "distressed", "distressed", "concerning", "horrible", "horribly", "questionable"]

def neg_remove(negative_words , text):
    censored = censor_list(censor_these , text)
    counter_list = censored.split()
    counter = 0
    doubles = []
    for i in range(len(negative_words)):
        for n in range(len(counter_list)):
            if negative_words[i] == counter_list[n]:
                counter += 1
                if counter == 2:
                    doubles.append(negative_words[i])
                    counter = 0
    print(doubles)
    for x in doubles:
        negs_gone = censored.replace(x , 'REDACTED - N')
        censored = negs_gone
    return censored
                
        
   
print(email_three)
print(neg_remove(negative_words , email_three))