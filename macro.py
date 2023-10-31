import os

images = os.listdir('./images')

for folder in images:
    elements = os.listdir(f'./images/{folder}')
    length = elements.__len__()

    # if length > 1000:
    #     for e in elements[1000:]:
    #         os.remove(f'./images/{folder}/{e}')
    #     elements = elements[:1000]
    # length = elements.__len__()
    # for i in range(length):
    #     os.rename(
    #         f'./images/{folder}/{elements[i]}',
    #         f'./images/{folder}/{folder}({i}).png',
    #     )

    print(f"{folder:20s} {length:4d}")
