from PIL import Image
image_path_list = {'matrix01.jpg', 'matrix02.jpg', 'matrix03.jpg'}
image_list = [Image.open(file) for file in image_path_list]
image_list[0].save(
            'animation.gif',
            save_all=True,
            duration=1000,
            append_images=image_list[1:],
            loop=0)