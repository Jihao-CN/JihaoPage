from PIL import Image
import tkinter.messagebox as messagebox

def convert_images_to_gif(selected_image_files, output_path, frame_interval):
    try:
        images = []
        print(f"开始打开图片，图片数量: {len(selected_image_files)}")
        for file in selected_image_files:
            img = Image.open(file)
            images.append(img)
            print(f"已打开图片: {file}")

        # 确保 frame_interval 为整数
        frame_interval = int(round(frame_interval))
        print(f"最终使用的帧间隔: {frame_interval} ms")

        # 保存为 GIF 文件
        print(f"开始保存 GIF 文件到: {output_path}")
        images[0].save(output_path, save_all=True, append_images=images[1:], duration=frame_interval, loop=0)
        print(f"GIF 文件保存成功: {output_path}")

    except Exception as e:
        messagebox.showerror("错误", f"转换过程中出现错误: {e}")
        print(f"转换过程中出现错误: {e}")