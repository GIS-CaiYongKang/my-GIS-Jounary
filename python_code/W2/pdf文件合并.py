from pypdf import PdfWriter
import os

# 1. 定义要合并的PDF文件名列表（按你需要的顺序排列）
pdf_files = [
    "0.pdf",
    "1.pdf",  # 注意文件名要和实际一致 
]

# 2. 初始化合并器
merger = PdfWriter()

# 3. 逐个添加PDF文件
for pdf in pdf_files:
    # 检查文件是否存在，避免报错
    if os.path.exists(pdf):
        merger.append(pdf)  # 把PDF添加到合并队列
        print(f"已添加：{pdf}")
    else:
        print(f"警告：文件不存在 → {pdf}")

# 4. 保存合并后的PDF
merger.write("目标输出文件名.pdf")  # 自定义输出文件名
merger.close()  # 关闭合并器，释放资源

print("PDF合并结束！")