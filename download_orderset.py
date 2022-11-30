import csv
import gzip
import pickle
import shutil

import requests
from tqdm.auto import tqdm

link = 'https://market.fuzzwork.co.uk/orderbooks/latest.csv.gz'
archive = 'latest.csv.gz'
filecsv = 'orderset.csv'
filepickle = 'orderset.pickle'


def download():
    response = requests.get(link, stream=True)
    with open(archive, "wb") as fout:
        with tqdm(
                # all optional kwargs
                unit='B', unit_scale=True, unit_divisor=1024, miniters=1,
                desc=archive, total=int(response.headers.get('content-length', 0))
        ) as pbar:
            for chunk in response.iter_content(chunk_size=4096):
                fout.write(chunk)
                pbar.update(len(chunk))


def unpacking():
    with gzip.open(archive, 'r') as f_in, open(filecsv, 'wb') as f_out:
        shutil.copyfileobj(f_in, f_out)


def load_pickle(file):
    with open(file, "rb") as read_file:
        return pickle.load(read_file)


def write_pickle(file, data):
    with open(file, 'wb') as f:
        pickle.dump(data, f, protocol=5)
        # pickle.dump(data, f, protocol=pickle.HIGHEST_PROTOCOL)


def load_csv(file):
    with open(file, newline='') as f:
        # with open('tst.csv', newline='') as f:
        reader = csv.reader(f, delimiter='\t')
        datacsv = list(reader)
        print(f'{len(datacsv)=}')
    return datacsv

    # with tqdm.wrapattr(
    #     open(eg_out, "wb"), "write",
    #     unit='B', unit_scale=True, unit_divisor=1024, miniters=1,
    #     desc=eg_file, total=int(response.headers.get('content-length', 0))
    # ) as fout:
    #     for chunk in response.iter_content(chunk_size=4096):
    #         fout.write(chunk)


def wtf():
    import fleep

    with open(archive, "rb") as file:
        info = fleep.get(file.read(128))

    print(info.type)  # prints ['raster-image']
    print(info.extension)  # prints ['png']
    print(info.mime)  # prints ['image/png']

    print(info.type_matches("raster-image"))  # prints True
    print(info.extension_matches("gif"))  # prints False
    print(info.mime_matches("image/png"))  # prints True


def timer_load():
    from codetiming import Timer

    timer = Timer(text=f"Task elapsed time: {{:.4f}} ms")
    timer.start()
    data = load_pickle(filepickle)
    # data = load_csv(filecsv)
    timer.stop()
    print(type(data))
    print(len(data))

    # 5 Task elapsed time: 3.4232 ms
    #  4   Task elapsed time: 3.5137 ms
    # 3 Task elapsed time: 3.9987 ms
    # 2 3.9713 ms


# timer_load()

def main():
    download()
    print('download done')
    unpacking()
    print('unpacking done')
    data = load_csv(filecsv)
    print('load_csv done')
    write_pickle(filepickle, data)
    print('write_pickle done')


main()
