#１枚だけ画像をリサイズ
import os
import glob
from PIL import Image

src = glob.glob('/Users/KT/Documents/photo/016.jpg') # オリジナル画像のパスと拡張子を設定
dst = '/Users/KT/Documents/resize_after/' # リサイズ画像の保存フォルダ

width = 300 # リサイズ後の横幅

for f in src:
    img = Image.open(f)
    original_width, original_height = img.size
    scale = width / original_width
    height = int(original_height * scale)
    img = img.resize((width,height))
    img.save(dst + os.path.basename(f))

#height = 513 #リサイズ後の縦幅

#for f in src:

    #img = Image.open(f)
    #original_width, original_height = img.size
    #scale = height / original_height
    #width = int(original_width * scale)
    #img = img.resize((width,height))
    #img.save(dst + os.path.basename(f))

