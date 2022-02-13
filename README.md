# pytorch-zoomout

Simple code snippet for applying various scale transform. This code can be used for preventing undesirable cropping process in `torchvision.transforms.RandomResizedCrop()` while enjoying scale transform.

## Output Example
|            org            |              scale**5               |             scale ** 10              |             scale ** 15              |              scale**20               |
| :-----------------------: | :---------------------------------: | :----------------------------------: | :----------------------------------: | :----------------------------------: |
| ![](./sample/1.jpg =100x) | ![](./output/1-pyramid-5.jpg =100x) | ![](./output/1-pyramid-10.jpg =100x) | ![](./output/1-pyramid-15.jpg =100x) | ![](./output/1-pyramid-20.jpg =100x) |
| ![](./sample/2.jpg =100x) | ![](./output/2-pyramid-5.jpg =100x) | ![](./output/2-pyramid-10.jpg =100x) | ![](./output/2-pyramid-15.jpg =100x) | ![](./output/2-pyramid-20.jpg =100x) |

## Usage

```python
from torchvision.transforms import transforms
from zoom_transform import zoomout_transform

transform_train = transforms.Compose([
    zoomout_transform(),
    transforms.Resize(224),
    transforms.RandomHorizontalFlip(),
    transforms.ToTensor(),
    transforms.Normalize(_IMGNET_MEAN, _IMGNET_STD),
])

```

## References

- `torchvision.transforms.RandomResizeCrop` : [Code](http://pytorch.org/vision/main/_modules/torchvision/transforms/transforms.html#RandomResizedCrop)
