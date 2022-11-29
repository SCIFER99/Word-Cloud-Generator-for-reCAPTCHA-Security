# By: Tim Tarver also known as CryptoKeyPlayer

# This script is to develop a word cloud generator for possible
# use in CAPTCHA Security using random text files. I chose to use a poem
# and put into a text file.

# Best seen in Jupyter Notebooks; each defined function per cell.
# Perhaps a text file from your operating system will work better than
# a created text file. The more data in a text file, the more complex
# a word cloud gets! 

import wordcloud
import numpy
from matplotlib import pyplot as plt
from IPython.display import display
import fileupload
import io
import sys
import os

# Here is a loop below in a docstring that will go through your operating
# system and generate a list of your files. You can choose any text(.txt)
# file on your system to achieve this goal.

"""
for dirname, _, filenames in os.walk('/'):
    for filename in filenames:
        print(os.path.join(dirname, filename))
"""        

# Another thing you can do is create your own text(.txt) file to
# generate your desired word cloud. Most effective with a text file from
# your current operating system.

with open('Poem - Grammar by Tony Hoagland.txt', 'r') as file:
    file_data = file.read()

# Now, create a custom widget method to upload your chosen text file
# using the fileupload module and FileUploadWidget() function. 

def widget_uploader():

    upload_widget = fileupload.FileUploadWidget()

    # Then, we will display the widget to the screen for text file uploading.

    def data_decoder(change):
        global file_data
        decoded = io.StringIO(change['owner'].data.decode('utf-8'))
        filename = change['owner'].filename
        print('Uploaded `{}` ({:.2f} kb)'.format(
            filename, len(decoded.read()) / 2 ** 10))
        file_data = decoded.getvalue()

    upload_widget.observe(data_decoder, names = 'data')
    display(widget_uploader)

print(widget_uploader())

# Next, we must store the results of our upload in a dictionary 'before'
# passing them into the wordcloud using the generate_from_frequencies() function.

def frequency_calculator(file_data):

    # Lets define some characters we do not want in our word cloud.
    ascii_characters = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
    word_bank = ["the", "a", "to", "if", "is", "it", "of", "and", "or", "an", "as", "i", "me", "my", \
    "we", "our", "ours", "you", "your", "yours", "he", "she", "him", "his", "her", "hers", "its", "they", "them", \
    "their", "what", "which", "who", "whom", "this", "that", "am", "are", "was", "were", "be", "been", "being", \
    "have", "has", "had", "do", "does", "did", "but", "at", "by", "with", "from", "here", "when", "where", "how", \
    "all", "any", "both", "each", "few", "more", "some", "such", "no", "nor", "too", "very", "can", "will", "just"]

    dictionary = {}

    data = file_data.split()
    
    # Iterate through the data to calculate the number of times a specific word shows up.
    
    for word in data:
        if word not in word_bank:
            for letter in word:
                if letter in ascii_characters:
                    letter.replace(ascii_characters, "")
            if word not in dictionary.keys():
                dictionary[word] = 0
            else:
                dictionary[word] += 1

                
    # These lines develop the word cloud using the wordcloud module
    # and WordCloud() and inserts the data into a jpeg file.

    cloud = wordcloud.WordCloud()
    cloud.generate_from_frequencies(dictionary)
    cloud.to_file("myfile.jpg")
    return cloud.to_array()

# print(frequency_calculator(file_data))

# Finally, we create the word cloud image displayer function to print our
# word cloud.

def wordcloud_image_displayer():

    figure1 = plt.figure(figsize = (10,10))
    myimage = frequency_calculator(file_data)
    plt.imshow(myimage, interpolation = 'nearest')
    plt.axis('off')
    plt.show()

print(wordcloud_image_displayer())    
