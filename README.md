# pytorch-zoomout

Simple code snippet for applying various scale transform. This code can be used for preventing undesirable cropping process in `torchvision.transforms.RandomResizedCrop()` while enjoying scale transform.

## Output Example
|              org              |           scale**5            |          scale ** 10           |          scale ** 15           |           scale**20            |
| :---------------------------: | :---------------------------: | :----------------------------: | :----------------------------: | :----------------------------: |
| ![](./output/1-pyramid-0.jpg) | ![](./output/1-pyramid-5.jpg) | ![](./output/1-pyramid-10.jpg) | ![](./output/1-pyramid-15.jpg) | ![](./output/1-pyramid-20.jpg) |
| ![](./output/2-pyramid-0.jpg) | ![](./output/2-pyramid-5.jpg) | ![](./output/2-pyramid-10.jpg) | ![](./output/2-pyramid-15.jpg) | ![](./output/2-pyramid-20.jpg) |

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
