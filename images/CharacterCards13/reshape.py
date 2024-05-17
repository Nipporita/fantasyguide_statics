from PIL import Image
import os

def crop_and_resize_images(directory):
    for filename in os.listdir(directory):
        if filename.endswith(".png"):
            image_path = os.path.join(directory, filename)
            image = Image.open(image_path)
            
            # 计算裁剪后的尺寸
            width, height = image.size
            target_ratio = 2 / 3
            scale = 0.995
            current_ratio = width / height
            if current_ratio > target_ratio:
                new_width = int(height * target_ratio * scale)
                new_height = int(height * scale)
            else:
                new_width = int(width * scale)
                new_height = int(width / target_ratio * scale)
            
            # 裁剪并重设尺寸
            left = (width - new_width) // 2
            top = (height - new_height) // 2
            right = left + new_width
            bottom = top + new_height
            cropped_image = image.crop((left, top, right, bottom))
            resized_image = cropped_image.resize((400, 600))
            
            # 保存重设尺寸后的图片
            resized_image.save(image_path)

# 调用函数来处理目录中的所有图片
crop_and_resize_images(r"D:\fantasyguide\frontend\statics\images\CharacterCards13")