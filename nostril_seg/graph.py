import csv
import matplotlib.pyplot as plt


print("---------------------------------------")
print("[INFO] Show plot")
print("[INFO] Author: Martin Juricek")
print("[INFO] Supervisor: Ing. Roman Parak")
print("[INFO] IACS FME BUT @2022")
print("---------------------------------------")

# paths = ['Unet-Resnet', 'Unet-Mobilenet', 'Unet-Seresnet']
paths = ["ASPOCRNET-Resnet", "ASPOCRNET-Mobilenet", "ASPOCRNET-Xception"]

for path in paths:

    epochs = []
    data = []
    # opening the CSV file
    with open("result_csv/" + path + "/l.csv", mode="r") as file:
        # reading the CSV file
        csvFile = csv.reader(file)
        t = iter(csvFile)
        t = next(t)
        # displaying the contents of the CSV file
        for lines in csvFile:
            epochs.append(int(lines[0]))
            data.append(float(lines[1]))

    plt.style.use(["science"])
    plt.subplot(2, 2, 1)
    plt.plot(epochs, data, label=path)
    plt.title("Model loss")
    plt.ylabel("Loss")
    plt.xlabel("Epoch")
    plt.legend(loc="upper right")

    epochs = []
    data = []

    with open("result_csv/" + path + "/v_l.csv", mode="r") as file:
        csvFile = csv.reader(file)
        t = iter(csvFile)
        t = next(t)
        for lines in csvFile:
            epochs.append(int(lines[0]))
            data.append(float(lines[1]))

    plt.subplot(2, 2, 2)
    plt.plot(epochs, data, label=path)
    plt.title("Model validation loss")
    plt.ylabel("Validation Loss")
    plt.xlabel("Epoch")
    plt.legend(loc="upper right")

    epochs = []
    data = []

    with open("result_csv/" + path + "/s_c_a.csv", mode="r") as file:
        csvFile = csv.reader(file)
        t = iter(csvFile)
        t = next(t)
        for lines in csvFile:
            epochs.append(int(lines[0]))
            data.append(float(lines[1]))

    plt.subplot(2, 2, 3)
    plt.plot(epochs, data, label=path)
    plt.title("Sparse catecorigal accuracy")
    plt.ylabel("Accuracy")
    plt.xlabel("Epoch")
    plt.legend(loc="lower right")

    epochs = []
    data = []

    with open("result_csv/" + path + "/v_s_c_a.csv", mode="r") as file:
        csvFile = csv.reader(file)
        t = iter(csvFile)
        t = next(t)
        for lines in csvFile:
            epochs.append(int(lines[0]))
            data.append(float(lines[1]))

    plt.subplot(2, 2, 4)
    plt.plot(epochs, data, label=path)
    plt.title("Validation sparse catecorigal accuracy")
    plt.ylabel("Validation Accuracy")
    plt.xlabel("Epoch")
    plt.legend(loc="lower right")

plt.show()
