import json

# Function to organise the gloss data
def convert(instance):
    Translate_data = ["10:00:00:00", ""]
    Translate_data.append(instance['en-GB'])
    Translate_data += instance['bsl']
    return Translate_data

# Gathers the raw data
def Vcl_TO_Gls(data):

    gloss = {}
    count = 0
    # loop to get data perform function on it then iterate
    for instance in data:
        gloss[str(count)+".0"] = convert(instance)
        count += 1
    return gloss