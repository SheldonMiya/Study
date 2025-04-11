import tkinter as tk
from tkinter import filedialog, messagebox
from pdf2image import convert_from_path
import os

# poppler のパス（Windowsの場合）
POPPLER_PATH = r"C:\1sb3g\Study\poppler-24.08.0\Library\bin"  # ← 環境に合わせて変更！

def convert_multiple_pdfs(pdf_paths, output_folder):
    total_converted = 0

    try:
        for pdf_path in pdf_paths:
            images = convert_from_path(pdf_path, dpi=200, poppler_path=POPPLER_PATH)
            base_name = os.path.splitext(os.path.basename(pdf_path))[0]

            for i, image in enumerate(images):
                page_num = i + 1
                filename = f"{base_name}_page_{page_num}.png"
                full_path = os.path.join(output_folder, filename)
                image.save(full_path, 'PNG')

            total_converted += len(images)

        messagebox.showinfo("完了", f"{len(pdf_paths)} 個のPDFから {total_converted} 枚のPNGを生成しました！")
    except Exception as e:
        messagebox.showerror("エラー", f"変換エラー:\n{e}")

def select_multiple_pdfs():
    pdf_paths = filedialog.askopenfilenames(
        filetypes=[("PDFファイル", "*.pdf")],
        title="複数のPDFファイルを選択"
    )
    if not pdf_paths:
        return

    output_folder = filedialog.askdirectory(title="PNGの保存先フォルダを選択")
    if not output_folder:
        return

    convert_multiple_pdfs(pdf_paths, output_folder)

# GUI
root = tk.Tk()
root.title("複数PDF → PNG一括変換")
root.geometry("360x180")

label = tk.Label(root, text="複数のPDFを一括でPNGに変換", font=("Arial", 12))
label.pack(pady=20)

button = tk.Button(root, text="PDFを選択（複数可）", command=select_multiple_pdfs, height=2, width=25)
button.pack()

root.mainloop()
