import tkinter as tk
from tkinter import filedialog, ttk, messagebox
import os
import ctypes
from gifconvert import convert_images_to_gif
import random
from playsound import playsound

# 全局变量用于存储选择的图片文件路径
image_files = []

# 获取用户桌面路径
def get_desktop_path():
    CSIDL_DESKTOP = 0x0000
    buf = ctypes.create_unicode_buffer(1024)
    ctypes.windll.shell32.SHGetFolderPathW(None, CSIDL_DESKTOP, None, 0, buf)
    return buf.value

def select_file():
    global image_files
    file_paths = filedialog.askopenfilenames()
    image_files = list(file_paths)
    print(f"选择的图片文件数量: {len(image_files)}")
    print(f"选择的图片文件路径: {image_files}")

def select_export_path():
    path = filedialog.askdirectory(initialdir=get_desktop_path())
    if path:
        export_path_entry.delete(0, tk.END)
        export_path_entry.insert(0, path)
        print(f"选择的导出路径: {path}")

def images_to_gif():
    num_images = len(image_files)
    if num_images == 0:
        messagebox.showwarning("警告", "请选择至少一张图片")
        return
    try:
        frame_interval = float(frame_interval_entry.get())
        if frame_interval < 1:
            raise ValueError
    except ValueError:
        messagebox.showwarning("警告", "请输入大于等于 1 的有效帧间隔数值")
        return
    export_path = export_path_entry.get()
    if not export_path:
        messagebox.showwarning("警告", "请选择导出路径")
        return

    print(f"将使用的图片数量: {num_images}")
    print(f"设置的帧间隔: {frame_interval} ms")
    print(f"导出路径: {export_path}")

    # 弹出提示框
    messagebox.showinfo("提示", "不要点击\n 正在转换，在此期间会卡死几分钟，取决于你的电脑和图片数量\n 提示音响起即为完成。")

    # 生成四位数随机数
    random_num = random.randint(1000, 9999)
    output_filename = f"rc-{random_num}.gif"
    output_path = os.path.join(export_path, output_filename)
    print(f"生成的随机文件名: {output_filename}")
    print(f"最终输出路径: {output_path}")

    convert_images_to_gif(image_files, output_path, frame_interval)

    # 获取当前脚本所在目录
    current_dir = os.path.dirname(os.path.abspath(__file__))
    # 构建end.mp3的相对路径
    sound_path = os.path.join(current_dir, 'end.mp3')
    try:
        playsound(sound_path)
        print("提示音播放")
    except Exception as e:
        messagebox.showerror("错误", f"播放提示音时出现错误: {e}")
        print(f"播放提示音时出现错误: {e}")

root = tk.Tk()
root.title("表情包转换器")
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

select_button = ttk.Button(root, text="+选择文件", command=select_file)
select_button.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")

frame_interval_label = ttk.Label(root, text="帧间隔 (ms):")
frame_interval_label.grid(row=1, column=0, padx=10, pady=10, sticky="nsew")

frame_interval_entry = ttk.Entry(root)
frame_interval_entry.insert(0, "100")  # 默认帧间隔为 100ms
frame_interval_entry.grid(row=2, column=0, padx=10, pady=10, sticky="nsew")

export_path_label = ttk.Label(root, text="导出路径:")
export_path_label.grid(row=3, column=0, padx=10, pady=10, sticky="nsew")

export_path_entry = ttk.Entry(root)
export_path_entry.insert(0, get_desktop_path())
export_path_entry.grid(row=4, column=0, padx=10, pady=10, sticky="nsew")

export_path_button = ttk.Button(root, text="选择导出路径", command=select_export_path)
export_path_button.grid(row=5, column=0, padx=10, pady=10, sticky="nsew")

convert_button = ttk.Button(root, text="转换为GIF", command=images_to_gif)
convert_button.grid(row=6, column=0, padx=10, pady=10, sticky="nsew")

root.mainloop()