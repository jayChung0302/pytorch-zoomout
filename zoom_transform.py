import torchvision.transforms as transforms
import PIL.Image as Image
import os
import glob


def zoomout_transform(input_size=(224, 224), inout_ratio=0.9, inout_num=20, prob=0.99):
    pyramid_ratio = [inout_ratio**(i) for i in range(1, inout_num + 1)]
    pyramid_size = [[int(ratio * input_size[0]), int(ratio * input_size[1])] for ratio in pyramid_ratio]
    pyramid_ls = [transforms.Resize(pyramid_size[i]) for i in range(inout_num)]
    return transforms.RandomApply([transforms.RandomChoice(pyramid_ls)], p=prob)


if __name__ == '__main__':
    img_path = glob.glob(os.path.join('sample', '*.jpg'))
    input_size = 224
    transform = transforms.Compose([
        zoomout_transform(),
        transforms.Resize(input_size),
        transforms.RandomHorizontalFlip(p=0.5),
    ])
    transform(Image.open(img_path[0])).show()
    # transform(Image.open(img_path[1])).show()
