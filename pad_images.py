import cv2
import numpy as np

p1 = r'C:\Users\javie\.gemini\antigravity\brain\c9ec0ac8-4815-489f-9b21-27f0abb5bb9c\.user_uploaded\media_1792499989781_31f42130.jpg'
p2 = r'C:\Users\javie\.gemini\antigravity\brain\c9ec0ac8-4815-489f-9b21-27f0abb5bb9c\.user_uploaded\media_1792499989795_a6c66a16.jpg'

im1 = cv2.imread(p1)
im2 = cv2.imread(p2)
im2 = im2[:-8, :]

def clean_watermark(img):
    h, w = img.shape[:2]
    gray_roi = cv2.cvtColor(img[h-50:h-5, w-55:w-5], cv2.COLOR_BGR2GRAY)
    _, mask_roi = cv2.threshold(gray_roi, 200, 255, cv2.THRESH_BINARY)
    kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (3, 3))
    mask_roi = cv2.dilate(mask_roi, kernel, iterations=1)
    mask = np.zeros((h, w), dtype=np.uint8)
    mask[h-50:h-5, w-55:w-5] = mask_roi
    return cv2.inpaint(img, mask, 3, cv2.INPAINT_TELEA)

im1_clean = clean_watermark(im1)
im2_clean = clean_watermark(im2)

# For tennis (im1: 1024x640), let's pad top and bottom with natural clay texture to give more room around the keychains
# Target: 1024x768 (4:3 aspect ratio!) so when displayed in 4:3 or 16:10, NO keychains are cut off at all!
h1, w1 = im1_clean.shape[:2]
target_h1 = 768
pad_top = (target_h1 - h1) // 2
pad_bottom = target_h1 - h1 - pad_top

# We can replicate the clay texture on top and bottom seamlessly using reflect or border
im1_padded = cv2.copyMakeBorder(im1_clean, pad_top, pad_bottom, 0, 0, cv2.BORDER_REFLECT_101)

# For padel (im2: 1024x739), target: 1024x768 (pad top: 15px, bottom: 14px)
h2, w2 = im2_clean.shape[:2]
pad_top2 = (768 - h2) // 2
pad_bottom2 = 768 - h2 - pad_top2
im2_padded = cv2.copyMakeBorder(im2_clean, pad_top2, pad_bottom2, 0, 0, cv2.BORDER_REFLECT_101)

# Also let's add a slight lateral pad of 40px so the outer edges of keychains have plenty of margin
margin_x = 40
im1_padded = cv2.copyMakeBorder(im1_padded, 0, 0, margin_x, margin_x, cv2.BORDER_REFLECT_101)
im2_padded = cv2.copyMakeBorder(im2_padded, 0, 0, margin_x, margin_x, cv2.BORDER_REFLECT_101)

# Save high-res
cv2.imwrite('coolpadel-web/assets/images/llaveros-tenis-personalizados-clubs.jpg', im1_padded, [cv2.IMWRITE_JPEG_QUALITY, 94])
cv2.imwrite('coolpadel-web/assets/images/llaveros-tenis-personalizados-clubs.webp', im1_padded, [cv2.IMWRITE_WEBP_QUALITY, 92])

cv2.imwrite('coolpadel-web/assets/images/llaveros-padel-personalizados-clubs.jpg', im2_padded, [cv2.IMWRITE_JPEG_QUALITY, 94])
cv2.imwrite('coolpadel-web/assets/images/llaveros-padel-personalizados-clubs.webp', im2_padded, [cv2.IMWRITE_WEBP_QUALITY, 92])

cv2.imwrite('coolpadel-web/assets/images/llaveros-padel-personalizados-3d.jpg', im2_padded, [cv2.IMWRITE_JPEG_QUALITY, 94])
cv2.imwrite('coolpadel-web/assets/images/llaveros-padel-personalizados-3d.webp', im2_padded, [cv2.IMWRITE_WEBP_QUALITY, 92])

print("Padded and saved images with 4:3 ratio and generous margins!")
