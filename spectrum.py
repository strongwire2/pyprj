# 스펙트럼 이미지를 읽어들여 10등분한 다음 R,G,B성분을 더한 다음 상대도수를 얻어냄.
# PIL 설치하려면, pip install pillow
# 참고: https://www.geeksforgeeks.org/python-pil-getpixel-method/

# Importing Image from PIL package
from PIL import Image

# creating a image object


def analyze(filename):
    block_count = 50
    im = Image.open(filename)
    px = im.load()
    # print(px[4, 4])
    width, height = im.size
    # print(f"image width={width}, height={height}")

    count = []
    w = int(width / block_count)
    n = 0  # block의 번호
    for n in range(block_count):
        intensity = 0
        for dx in range(w):
            x = n*w + dx
            for y in range(height):
                intensity += px[x, y][0] + px[x, y][1] + px[x, y][2]  # R, G, B 를 더함
        # print(f"block={n}, intensity={intensity}")
        count.append(intensity)

    # print(count)
    # 상대도수 구하기
    total = sum(count)
    freq = []  # 상대도수
    for i in count:
        freq.append(i/total)
    # print(freq)
    line = filename + ','
    for item in freq:
        line += str(item) + ','
    print(line)

analyze('images/태양광2.jpg')
analyze('images/조명LED1.jpg')
analyze('images/삼파장1.jpg')
analyze('images/형광등1.jpg')

# 태양광
# [0.0771044510131966, 0.10509779512328529, 0.12611088422623135, 0.1554355941369334, 0.09763247819965065, 0.08236249583733563, 0.12309439535883474, 0.10631051298784222, 0.07786737195914906, 0.04898402115754104]

# LED
# 0.10522852712735369, 0.15323840451152057, 0.10935410722554238, 0.1202303862468014, 0.09030314532376602, 0.08019054231817954, 0.10333698818174848, 0.12386894244801241, 0.07676696159302744, 0.03748199502404808]

# 삼파장

