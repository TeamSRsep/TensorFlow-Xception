""" This code helps to generate the .ini file needed for training xception net"""
""" Example values are taken from https://github.com/kwotsin/TensorFlow-Xception """
import os
import argparse
import configparser


parser = argparse.ArgumentParser()
parser.add_argument('config_path', help='path to and name of config file')
parser.add_argument('--section_name', default='TRAIN')
parser.add_argument('--dataset_dir', default='./dataset', help='path to folder that contains tfrecords')
parser.add_argument('--log_dir', default='./log')
parser.add_argument('--image_size', default='299')
parser.add_argument('--labels_file', default='./dataset/labels.txt')
parser.add_argument('--file_pattern', default='flowers_%s_*.tfrecord')
parser.add_argument('--im_info', default='A 3-channel RGB coloured flower image that is either tulips, sunflowers, roses, dandelion, or daisy.')
parser.add_argument('--label_info', default='A label that is as such -- 0:daisy, 1:dandelion, 2:roses, 3:sunflowers, 4:tulips')
#TRAINING PARAMETERS
parser.add_argument('--num_epochs', default=64)
parser.add_argument('--batch_size', default=10)
parser.add_argument('--initial_learning_rate', default=0.001)
parser.add_argument('--learning_rate_decay_factor', default=0.1)
parser.add_argument('--num_epochs_before_decay', default=2)


parser.add_argument('--num_classes', default='5')
args = parser.parse_args()
config = configparser.RawConfigParser()
config[args.section_name] = {'dataset_dir' : args.dataset_dir,
                             'file_pattern' : args.file_pattern,
                             'log_dir' : args.log_dir,
                             'image_size' : args.image_size,
                             'num_classes' : args.num_classes,
                             'labels_file' : args.labels_file,
                             'num_epochs' : args.num_epochs,
                             'batch_size' : args.batch_size,
                             'initial_learning_rate' : args.initial_learning_rate,
                             'learning_rate_decay_factor' : args.learning_rate_decay_factor,
                             'num_epochs_before_decay' : args.num_epochs_before_decay,
                             'item_description': {
                               'image':args.im_info,
                               'label':args.label_info
                              }
                            }
# ensures file path ends with .ini
cfg_filename = os.path.splitext(args.config_path)[0] +'.ini'
with open(cfg_filename,'w') as configfile:
    config.write(configfile)
