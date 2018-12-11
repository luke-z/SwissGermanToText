import os

def export_model(model):
    if not os.path.exists("./models"):
        os.makedirs("./models")
    model.save("./models/model")

def import_model():
    return load_model("./models/model")
