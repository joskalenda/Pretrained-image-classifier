#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# */AIPND-revision/intropyproject-classify-pet-images/get_pet_labels.py
#                                                                             
# PROGRAMMER: kalenda Ntumba Josue
# DATE CREATED: 04.08.2021                              
# REVISED DATE: 
# PURPOSE: Create the function get_pet_labels that creates the pet labels from 
#          the image's filename. This function inputs: 
#           - The Image Folder as image_dir within get_pet_labels function and 
#             as in_arg.dir for the function call within the main function. 
#          This function creates and returns the results dictionary as results_dic
#          within get_pet_labels function and as results within main. 
#          The results_dic dictionary has a 'key' that's the image filename and
#          a 'value' that's a list. This list will contain the following item
#          at index 0 : pet image label (string).
#
##
# Imports python modules
from os import listdir

# TODO 2: Define get_pet_labels function below please be certain to replace None
#       in the return statement with results_dic dictionary that you create 
#       with this function
# 
def get_pet_labels(image_dir):
    """
    Creates a dictionary of pet labels (results_dic) based upon the filenames 
    of the image files. These pet image labels are used to check the accuracy 
    of the labels that are returned by the classifier function, since the 
    filenames of the images contain the true identity of the pet in the image.
    Be sure to format the pet labels so that they are in all lower case letters
    and with leading and trailing whitespace characters stripped from them.
    (ex. filename = 'Boston_terrier_02259.jpg' Pet label = 'boston terrier')
    Parameters:
     image_dir - The (full) path to the folder of images that are to be
                 classified by the classifier function (string)
    Returns:
      results_dic - Dictionary with 'key' as image filename and 'value' as a 
      List. The list contains for following item:
         index 0 = pet image label (string)
    """
    results_dic = dict()
    
#     # Retrieves the file names from the folder specified as 'image_dir' 
    filenames_list = listdir(image_dir)
        
#     # Processes the filenames to create the pet image labels
#     # Retrieves the filenames from folder pet_images/
    for i in range (0, len(filenames_list), 1):
#         # Skips file if starts with . (like .DS_Store of Mac OSX) because it 
#         # isn't an pet image file
        if filenames_list[i][0] != ".":
#               # Reads respectively indexed element from filenames_list into temporary string variable 'pet_image' 
            pet_image = filenames_list[i]
#             # Sets all characters in 'pet_image' to lower case 
            pet_image_lower = pet_image.lower()
#             # Creates list called 'pet_image_word_list' that contains every element in pet_image_lower seperated by '_'
            pet_image_word_list = pet_image_lower.split("_")
#             # Creates temporary variable 'pet_label' to hold pet label name extracted starting as empty string
            pet_image_alpha = ""
#             # Iterates through every word in 'pet_image_word_list' and appends word to 'pet_label_alpha' only if word consists 
#             # purely of alphabetic characters 
            for word in pet_image_word_list:
                if word.isalpha():
                         pet_image_alpha += word + " "
#             # Removes possible leading or trailing whitespace characters from 'pet_pet_image_alpha' and add stores final label as 'pet_label' 
            pet_label = pet_image_alpha.strip()

#             # Adds the original filename as 'key' and the created pet_label as 'value' to the 'results_dic' dictionary if 'key' does 
#             # not yet exist in 'results_dic', otherwise print Warning message 
            if filenames_list[i] not in results_dic:
                results_dic[filenames_list[i]] = [pet_label]
            else:
                print("** Warning: Key = ", filenames_list[i], " already in 'results_dic' with value = ", results_dic[filenames_list[i]])
            
#     # Iterates through the 'results_dic' dictionary and prints its keys and their associated values
    print("\nPrinting: All 'key' - 'value' pairs in dictionary results_dic: ")
    for key in results_dic:
        print("Filename = ", key, "   Pet Label = ", results_dic[key])
    
#     # Returns results_dic
    return results_dic 