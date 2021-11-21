# Various helper functions

import json

with open("/Users/michaelgoff/Desktop/Urban Cruise Ship/Energy Model/Model/references.json") as json_file:
    references = json.load(json_file)

def save_image(image_data):
    # Processing on image_data
    if "references" in image_data:
        for i in range(len(image_data["references"])):
            image_data["references"][i] = references[image_data["references"][i]]
    
    # Find the spot for the image data and save it
    with open("/Users/michaelgoff/Desktop/Urban Cruise Ship/Energy Model/Model/image_list.json") as json_file:
        images = json.load(json_file)
        have_found = False
        for i in range(len(images)):
            if images[i]["filename"] == image_data["filename"]:
                have_found = True
                images[i] = image_data
        if not have_found:
            images.append(image_data)
        with open('/Users/michaelgoff/Desktop/Urban Cruise Ship/Energy Model/Model/image_list.json', 'w') as outfile:
            json.dump(images, outfile)