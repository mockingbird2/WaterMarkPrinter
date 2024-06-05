from PIL import Image, ImageDraw, ImageFont
import numpy as np
import os
import argparse


class WaterMarkPrinter:
    def __init__(self, watermark, x_align='start', y_align='start', x_offset=0, y_offset=0, transparency=1, scale=1):
        self.watermark = Image.open(watermark)
        self.x_align = x_align  # start, center, end
        self.y_align = y_align  # start, center, end
        self.x_offset = x_offset  # 取值-100-100 按原图比例
        self.y_offset = y_offset  # 取值-100-100 按原图比例
        self.transparency = int(transparency * 255)  # 0-1
        self.scale = scale
        self.watermark_width = None
        self.watermark_height = None

    def load_main_image(self, img):
        self.img = Image.open(img)

    def load_watermark(self):
        if self.watermark != 'RGBA':
            self.watermark = self.watermark.convert('RGBA')
        array_mark = np.asarray(self.watermark)
        self.watermark_width = array_mark.shape[1]
        self.watermark_height = array_mark.shape[0]
        if 0 <= self.transparency <= 255:
            self.transparency_process()
        else:
            raise Exception('invalid transparency value, range 0.0-1.0')

    def transparency_process(self):
        x, y = self.watermark.size
        for i in range(x):
            for j in range(y):
                color = self.watermark.getpixel((i, j))
                if color[-1] > 100:
                    color = color[:-1] + (self.transparency, )
                    self.watermark.putpixel((i, j), color)

    def add_watermark(self):
        #  获取图片宽度和高度
        array_img = np.asarray(self.img)
        width = array_img.shape[1]
        height = array_img.shape[0]
        scale = self.scale
        if width/height > self.watermark_width/self.watermark_height:
            mark = self.watermark.resize((int(height * scale), int(height * scale)))
            watermark_width = watermark_height = int(height * scale)
        else:
            mark = self.watermark.resize((int(width * scale), int(width * scale)))
            watermark_width = watermark_height = int(width * scale)
        layer = Image.new('RGBA', self.img.size, (0, 0, 0, 0))
        #  调整图片x轴对齐
        if self.x_align == 'center':
            x_point = (width-watermark_width) // 2 + self.x_offset * (width -  watermark_width)// 100
        elif self.x_align == 'end':
            x_point = width-watermark_width + self.x_offset * (width -  watermark_width)// 100
        else:
            x_point = 0 + self.x_offset * (width -  watermark_width)// 100
        #  调整图片y轴对齐
        if self.y_align == 'center':
            y_point = (height-watermark_height) // 2 + self.y_offset * (height - watermark_height) // 100
        elif self.y_align == 'end':
            y_point = height-watermark_height + self.y_offset * (height - watermark_height) // 100
        else:
            y_point = 0 + self.y_offset * (height - watermark_height) // 100
        layer.alpha_composite(mark, (x_point, y_point))
        res = Image.composite(layer, self.img, layer)
        return res


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("path", help="type in your images directory path")
    parser.add_argument("watermark", help="type in your watermark path")
    parser.add_argument("-x", "--alignx", help="x-axis alignment method, default start", choices=['start', 'center', 'end'], default='start')
    parser.add_argument("-y", "--aligny", help="y-axis alignment method, default start", choices=['start', 'center', 'end'], default='start')
    parser.add_argument("-i", "--offsetx", help="offset in x-axis (overlay with alignment), default 0, range -100-100", type=int, default=0)
    parser.add_argument("-j", "--offsety", help="offset in y-axis (overlay with alignment), default 0, range -100-100", type=int, default=0)
    parser.add_argument("-t", "--transparency", help="transparency of the watermark, default 1.0, range 0.0-1.0", type=float, default=1.0)
    parser.add_argument("-s", "--scale", help="scale of the watermark, default 1.0, range 0.0-1.0", type=float, default=1.0)
    args = parser.parse_args()
    fs = os.listdir(args.path)
    if os.path.basename(args.watermark) in fs:
        fs.remove(os.path.basename(args.watermark))
    ls = ['.png', '.jpg', '.jpeg', 'webp']
    printer = WaterMarkPrinter(watermark=args.watermark, x_align=args.alignx, y_align=args.aligny, x_offset=args.offsetx, y_offset=args.offsety, transparency=args.transparency, scale=args.scale)
    printer.load_watermark()
    for f in fs:
        if os.path.splitext(f)[1] in ls:
            printer.load_main_image(os.path.join(args.path, f))
            result = printer.add_watermark()
            if not os.path.exists(os.path.join(args.path, 'images_with_watermark')):
                os.makedirs(os.path.join(args.path, 'images_with_watermark'))
            save_path = os.path.join(args.path, 'images_with_watermark') + '/' + f
            result.save(save_path)
            print(save_path, 'done')
