
"""1. Create 50 zip-archives, with 100 xml files to each. Xml file structure:

<root>

<var name=’id’ value=’<случайное уникальное строковое значение>’/>

<var name=’level’ value=’<случайное число от 1 до 100>’/>

<objects>

<object name=’<случайное строковое значение>’/>

<object name=’<случайное строковое значение>’/>

…

</objects>

</root>


In the objects tag, a random number (from 1 to 10) of nested object tags.


2. Processes a directory with the received zip archives and create 2 csv files:

First: id, level

Second: id, object_name"""


import os
import string
import random
import shutil
import zipfile
import xml.etree.cElementTree as ET
from multiprocessing import Pool


#-------------------------task 1------------------------------------------
class Root(object):
    def __init__(self, used_id=[]):
        self.root = None
        self.used_id = used_id

    def create_str(self, size=4, unique=False, only_digits=False):
        if only_digits:
            chars = string.digits
        else:
            chars = string.ascii_letters + string.digits
        while True:
            gen_str = ''.join(random.choice(chars) for _ in range(size))
            if not unique or id not in self.used_id:
                break
        return gen_str

    def generate_root(self):
        if self.root != None:
            return self.root
        root = ET.Element("root")
        id = self.create_str(unique=True)
        ET.SubElement(root, "var", name='id',  value=id)
        self.used_id.append(id)
        ET.SubElement(root, "var",  name="level", value=str(random.randint(1, 100)))
        objects = ET.SubElement(root, "objects")
        for _ in range(random.randint(1, 10)):
            ET.SubElement(objects, "object", name=self.create_str())
        self.root = ET.ElementTree(root)
        return self.root

    def write_root(self, file_name):
        self.root.write(file_name)


def create_xmls_zip(dir_path, zip_quantity=50, files_quantity=100, file_name='filename', zip_name='dirname'):
    used_id = []
    if os.path.isdir(dir_path):
        raise FileExistsError('Такая папка уже существует')
        return
    else:
        os.mkdir(dir_path)
    for j in range(zip_quantity):
        zip_path = os.path.join(dir_path, f'{zip_name}{j}')
        os.mkdir(zip_path)
        for i in range(files_quantity):
            root = Root(used_id)
            root.generate_root()
            used_id = root.used_id
            path = os.path.join(zip_path, f'{file_name}{str(i)}.xml')
            root.write_root(path)
        shutil.make_archive(zip_path, 'zip', zip_path)
        shutil.rmtree(zip_path)
#-------------------------task 1------------------------------------------

#-------------------------task 2------------------------------------------
def _write_to_csv(save_path, zip_info):
    level_text = ''
    objects_text = ''
    for info in zip_info:
        level_text += f'{info[0]},{info[1]}\n'
        for xml_object in info[2]:
            objects_text += f'{info[0]},{xml_object}\n'
    with open(f'{save_path}_level.csv', 'w') as csvfile:
        csvfile.write(level_text)
    with open(f'{save_path}_objects.csv', 'w') as csvfile:
        csvfile.write(objects_text)

def write_xml_zip_to_csv(dir_path, zip_name):
    zip_path = os.path.join(dir_path, zip_name)
    if zipfile.is_zipfile(zip_path):
        zip_archive = zipfile.ZipFile(zip_path)
        zip_info = []
        for zip_file in zip_archive.namelist():
            xml_str = zip_archive.read(zip_file)
            root = ET.fromstring(xml_str)
            id, level, objects = '', '', []
            for child in root:
                if child.tag == 'var':
                    if child.attrib['name'] == 'id':
                        id = child.attrib['value']
                    elif child.attrib['name'] == 'level':
                        level = child.attrib['value']
                if child.tag == 'objects':
                    for xml_object in child:
                        objects.append(xml_object.attrib['name'])
            zip_info.append((id, level, objects))
    save_path = os.path.join(dir_path, zip_name.replace('.zip', ''))
    _write_to_csv(save_path, zip_info)


def write_xml_zips_to_csv(dir_path, processes=5):
    if not os.path.isdir(dir_path):
        raise FileNotFoundError(dir_path)
    with Pool(processes) as p:
        results = [p.apply(write_xml_zip_to_csv, args=(dir_path, zip_name)) for zip_name in os.listdir(dir_path)]
#-------------------------task 2------------------------------------------


if __name__ == '__main__':
    create_xmls_zip('test_dir')
    write_xml_zips_to_csv('test_dir')
