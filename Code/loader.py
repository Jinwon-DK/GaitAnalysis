import pandas as pd
import os
import numpy as np
import datetime
import csv


def path_loader(target):
    path_collector = dict()
    directories = sorted([folder for folder in os.listdir(target)
                          if os.path.isdir(os.path.join(target, folder))])
    keymap_dir = os.path.join(target, 'keymap.txt')
    if os.path.exists(keymap_dir) is not True:
        pass
    else:
        with open(keymap_dir, "r") as f:
            reader = csv.reader(f, delimiter=":")
            lines = list(reader)[0]

    for dataset_name in directories:
        label_dir = os.path.join(target, dataset_name)
        file_name = [os.path.join(label_dir, file)
                     for file in os.listdir(label_dir)
                     if file.endswith(".npy")]

        if not dataset_name in path_collector.keys():
            path_collector[dataset_name] = file_name

    return path_collector


def data_loader(param, target=1):
    path_collector = path_loader(f'../Datasets/{param.folder}')

    collected_dataset = dict()
    datasets = list()
    for sample_folder, pathlist in path_collector.items():

        _, nb_combine = sample_folder.split('_')
        if int(nb_combine) != target:
            continue

        for datapath in sorted(pathlist):
            filename = datapath.split('/')[-1]
            if param.datatype == "disease":
                stype, datatype = filename.split('_')
                total_dataset = np.load(datapath)
                collected_dataset[stype] = total_dataset
            elif param.datatype == "type":
                stype, datatype = filename.split('_')
                total_dataset = np.load(datapath)
                collected_dataset[stype] = total_dataset

        for sensor in param.sensor_type:
            datasets.append(collected_dataset[sensor])

    return datasets


def viz_loader(param):
    data_dir = f'../Raw/{param.datatype}'

    directories = [folder for folder in os.listdir(data_dir) if os.path.isdir(os.path.join(data_dir, folder))]
    # directories = sorted(directories)

    dataset = dict()
    for folder_name in directories:
        dataset[folder_name] = list()

    for key in dataset.keys():
        folder_dir = os.path.join(data_dir, key)
        files_collecter = [file for file in os.listdir(folder_dir) if file.endswith(".csv")]
        for files in files_collecter:
            file_names = os.path.join(folder_dir, files)
            dataset[key].append(file_names)

    return dataset


def create_loader(param):
    data_dir = f"../Raw/{param.datatype}"

    # data_dir = f"../Raw/{datetime.datetime.today().strftime('%y%m%d')}"
    if os.path.exists(data_dir) is not True:
        os.mkdir(data_dir)

    rsub = param.collect["remover"]
    directories = [folder for folder in os.listdir(data_dir) if os.path.isdir(os.path.join(data_dir, folder))]
    if param.datatype == "type":
        directories = sorted(directories)
    dataset = dict()

    for folder_name in directories:
        dataset[folder_name] = list()

    for key in dataset.keys():
        folder_dir = os.path.join(data_dir, key)
        files_collecter = [file for file in os.listdir(folder_dir) if file.endswith(".csv")]
        for files in files_collecter:
            if files in rsub:
                continue
            else:
                file_names = os.path.join(folder_dir, files)
                dataset[key].append(file_names)

    return dataset
