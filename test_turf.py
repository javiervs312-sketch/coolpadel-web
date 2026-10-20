import cv2
import numpy as np

def generate_turf_texture(width, height, base_color=(120, 168, 105)): # soft subtle green
    """Generates an elegant, soft realistic padel turf background with fine fiber texture and soft studio vignette."""
    np.random.seed(42)
    b, g, r = base_color
    
    # Base gradient: slightly lighter in the center, subtly deeper at the edges
    y, x = np.ogrid[:height, :width]
    cx, cy = width / 2.0, height / 2.0
    dist = np.sqrt((x - cx)**2 + (y - cy)**2) / np.sqrt(cx**2 + cy**2)
    vignette = 1.0 - 0.12 * (dist ** 1.5)
    
    # Fine grass/turf fiber noise
    noise = np.random.normal(0, 7, (height, width, 3))
    
    # High frequency turf grain
    turf = np.zeros((height, width, 3), dtype=np.float32)
    turf[:, :, 0] = b * vignette
    turf[:, :, 1] = g * vignette
    turf[:, :, 2] = r * vignette
    
    turf = turf + noise
    
    # Add subtle vertical fiber streaks
    fiber_noise = np.random.normal(0, 4, (height, width))
    fiber_blur = cv2.GaussianBlur(fiber_noise, (1, 5), 0)
    for c in range(3):
        turf[:, :, c] += fiber_blur * 0.8
        
    turf = np.clip(turf, 0, 255).astype(np.uint8)
    return turf

def process_image(img_path):
    img = cv2.imread(img_path)
    h, w = img.shape[:2]
    
    # Convert to color spaces
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    lab = cv2.cvtColor(img, cv2.COLOR_BGR2LAB)
    
    # In wood background:
    # Hue is around 10-25 (warm wood orange/brown/yellow), Saturation is low-moderate 40-140, Value is high
    # Wood color in HSV: H in [8, 30], S in [30, 160], V in [80, 240]
    
    # Sample background color from border margins (top 30px, bottom 30px, left 30px, right 30px)
    border_pixels = np.concatenate([
        lab[:25, :].reshape(-1, 3),
        lab[-25:, :].reshape(-1, 3),
        lab[:, :25].reshape(-1, 3),
        lab[:, -25:].reshape(-1, 3)
    ], axis=0)
    
    mean_bg = np.median(border_pixels, axis=0)
    std_bg = np.std(border_pixels, axis=0)
    
    # Distance in LAB space from wood background
    diff = np.sqrt(np.sum(((lab.astype(np.float32) - mean_bg) / (std_bg + 5.0))**2, axis=2))
    
    # Foregrounds: keychains (white, red, blue, cyan, orange, metal rings)
    # The metal ring is silver/grey or dark reflections, and llaveros are bright saturated or pure white/black
    # Mask of foreground
    mask = (diff > 2.8).astype(np.uint8) * 255
    
    # Clean up mask
    kernel_small = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (3, 3))
    kernel_medium = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (5, 5))
    
    mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel_small)
    mask = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernel_medium)
    
    # Find connected components and remove tiny stray noise
    num_labels, labels, stats, centroids = cv2.connectedComponentsWithStats(mask)
    clean_mask = np.zeros_like(mask)
    for i in range(1, num_labels):
        area = stats[i, cv2.CC_STAT_AREA]
        if area > 150: # keep valid object parts
            clean_mask[labels == i] = 255
            
    # Soft alpha feathering
    feathered = cv2.GaussianBlur(clean_mask, (5, 5), 0)
    alpha = (feathered.astype(np.float32) / 255.0)[:, :, np.newaxis]
    
    # Soft drop shadow for realism on the turf
    shadow_mask = cv2.GaussianBlur(clean_mask, (21, 21), 0)
    # Shift shadow slightly down and right
    M = np.float32([[1, 0, 6], [0, 1, 10]])
    shadow_shifted = cv2.warpAffine(shadow_mask, M, (w, h))
    shadow_alpha = (shadow_shifted.astype(np.float32) / 255.0 * 0.35)[:, :, np.newaxis]
    
    # New turf background (soft light green padel turf: BGR around (115, 175, 120))
    turf = generate_turf_texture(w, h, base_color=(105, 165, 110))
    
    # Apply shadow to turf
    turf_with_shadow = turf.astype(np.float32) * (1.0 - shadow_alpha)
    
    # Composite foreground onto turf
    composed = (img.astype(np.float32) * alpha + turf_with_shadow * (1.0 - alpha))
    composed = np.clip(composed, 0, 255).astype(np.uint8)
    
    return composed

print("Testing script logic...")
padel_res = process_image('coolpadel-web/assets/images/llaveros-padel-personalizados-clubs.jpg')
cv2.imwrite('coolpadel-web/assets/images/test_padel_green.jpg', padel_res)
print("Saved test_padel_green.jpg!")
