import torchvision.transforms as transforms
import PIL.Image as Image
import os
import glob

if __name__ == '__main__':
    input_size = (224, 224)
    inout_ratio = 0.9
    inout_num = 20
    prob = 0.99
    pyramid_ratio = [inout_ratio**(i) for i in range(1, inout_num + 1)]
    pyramid_size = [[int(ratio * input_size[0]), int(ratio * input_size[1])] for ratio in pyramid_ratio]
    pyramid_ls = [transforms.Resize(pyramid_size[i]) for i in range(inout_num)]
    img_paths = glob.glob(os.path.join('sample', '*.jpg'))
    input_size = 224
    for img_path in img_paths:
        img = Image.open(img_path)
        img_name = img_path.split('/')[-1].split('.jpg')[0]
        for idx, resize in enumerate(pyramid_ls, 1):
            transforms.Resize(224)(resize(img)).save(f'output/{img_name}-pyramid-{idx}.jpg')
