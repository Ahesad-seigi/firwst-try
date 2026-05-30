import os
import shutil
from pathlib import Path

print(f'当前工作目录是',os.getcwd())

# ===================== 核心配置区 =====================
# 1. 获取当前用户的桌面路径（自动适配不同电脑的用户名）
desktop_path = Path.home() / 'Desktop'

# 2. 你指定的目标文件夹路径（请在这里修改为你想要存放的位置）
# 例如：target_folder_path = r'D:\MyWPSFiles' 或 desktop_path / 'WPS文档汇总'
target_folder_path = desktop_path / 'WPS文档汇总' 

# 3. 定义 WPS 相关的文件后缀名（涵盖了 WPS 和微软 Office 的常见格式）
wps_extensions = ['.wps', '.wpt', '.et', '.ett', '.dps', '.dpt',  # WPS 专属格式
                  '.doc', '.docx', '.xls', '.xlsx', '.ppt', '.pptx', '.pdf'] # 通用办公格式
# ================================================

def organize_wps_files():
    # 检查桌面路径是否存在
    if not desktop_path.exists():
        print("错误：找不到桌面路径！")
        return

    # 如果目标文件夹不存在，就自动创建它（exist_ok=True 防止已存在时报错）
    target_folder_path.mkdir(parents=True, exist_ok=True)
    print(f"目标文件夹已就绪：{target_folder_path}")

    moved_count = 0

    # 遍历桌面上的所有文件
    for item in os.listdir(desktop_path):
        item_path = desktop_path / item
        
        # 跳过文件夹和以 . 开头的隐藏/系统文件（比如 .DS_Store 或快捷方式缓存）
        if item_path.is_dir() or item.startswith('.'):
            continue

        # 获取文件后缀并转为小写（防止 .DOCX 和 .docx 漏网）
        file_ext = item_path.suffix.lower()

        # 判断该文件是否属于 WPS 相关文件
        if file_ext in wps_extensions:
            destination = target_folder_path / item
            
            # 处理重名文件：如果目标文件夹里已经有同名文件，自动加个数字后缀防止覆盖
            count = 1
            while destination.exists():
                destination = target_folder_path / f"{item_path.stem}_{count}{file_ext}"
                count += 1

            # 执行移动操作
            try:
                shutil.move(str(item_path), str(destination))
                print(f"✅ 已移动：{item} -> {destination.name}")
                moved_count += 1
            except Exception as e:
                print(f"❌ 移动失败 {item}：{str(e)}")

    print(f"\n整理完成！共移动了 {moved_count} 个 WPS 相关文件到指定文件夹。")

if __name__ == "__main__":
    print("开始扫描桌面上的 WPS 文件...")
    organize_wps_files()