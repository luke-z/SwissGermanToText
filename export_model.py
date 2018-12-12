import os
from keras.models import load_model
from datetime import datetime


def export_model(model, settings):
    foldername = datetime.now().strftime('%Y%m%d_%H-%M-%S')
    if not os.path.exists("./models/" + foldername):
        os.makedirs("./models/" + foldername)

    settings_file = open("./models/" + foldername + "/model_settings.txt", "w+")
    for key,val in settings.items():
        settings_file.write(str(key) + ": " + str(val) + "\n")
    settings_file.close()

    model.save("./models/" + foldername + "/SwissGermanToText.model")


def import_model(path):
    return load_model(path)
